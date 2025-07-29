import sys
from antlr4 import InputStream, FileStream, StdinStream, CommonTokenStream
from parser.VerboseLexer import VerboseLexer
from parser.VerboseParser import VerboseParser
from vast.scope import Scope
from compiler.transformer import Transformer
from compiler.resolve_stage import register_module
from compiler.contexts import CompileContext
from compiler.intrinsics import intrinsic_scope
from compiler.generators import llvm as llvm_generator

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = VerboseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VerboseParser(stream)
    tree = parser.module()
    print(tree.toStringTree(recog=parser))
    transformer = Transformer()
    module = transformer.visit(tree)
    print("Parsing stage end")

    print("Resolve stage begin")
    module.scope.parent = intrinsic_scope
    ctx = CompileContext()
    register_module(module, ctx)
    print("Resolve stage end")

    print("Generate stage start")
    llvm_module = llvm_generator.generate(module, llvm_generator.LLVMGeneratorContext())
    print(f"{llvm_module}")
    print("Generate stage end")


if __name__ == '__main__':
    main(sys.argv)