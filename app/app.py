import os
import subprocess
from enum import Enum
from docopt import docopt
from antlr4 import FileStream
from vast import VModule
from compiler.resolve_stage import register_module, CompileContext
from compiler.intrinsics import intrinsic_scope
from .parse import parse
from .emit_ir import emit_ir

class EmitType(Enum):
    EXECUTABLE = "exec"
    IR = "ir"
    ASSEMBLY = "asm" # Not implemented yet

class BackendType(Enum):
    LLVM = "llvm"


verbose: bool = False


def main(args: docopt) -> int:
    global verbose
    verbose = args["--verbose"]
    file_paths: list[str] = args["<file>"]
    if len(file_paths) != 1:
        print("Currently only 1 file supported.")
        return 1
    file_path: str = file_paths[0]
    file_module_name: str = file_path.split("/")[-1].split(".")[0]
    emit_type: EmitType = EmitType(args["--emit"])
    backend_type: BackendType = BackendType(args["--backend"])
    out_path: str = args["--output"]
    preserve_temp: bool = args["--preserve-temp"]

    vmodule: VModule = parse(FileStream(file_path))

    register_module(vmodule, CompileContext(intrinsic_scope))

    match backend_type:
        case BackendType.LLVM:
            from compiler.generators import llvm
            generator = llvm.generate
            gen_ctx = llvm.LLVMGeneratorContext()
        case _:
            raise NotImplementedError(f"Backend {backend_type} is not implemented.")

    ir_path = out_path if emit_type == EmitType.IR else None
    ir_path = emit_ir(vmodule, generator, gen_ctx, ir_path)
    if emit_type == EmitType.IR:
        return 0

    if emit_type == EmitType.EXECUTABLE:
        assert ir_path is not None
        ret = subprocess.run(["clang", ir_path, "-o", out_path])
        if not preserve_temp:
            os.unlink(ir_path)


    return 0

