from typing import Optional
from vast import VModule


def emit_ir(vmodule: VModule, generator: callable, ctx, out_path: Optional[str] = None) -> str:
    if out_path is None:
        out_path = ctx.default_file_name(vmodule)
    ir_module = generator(vmodule, ctx)
    with open(out_path, "wt") as out:
        out.write(str(ir_module))
    return out_path