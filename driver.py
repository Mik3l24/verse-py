import sys
from antlr4 import InputStream, FileStream, StdinStream, CommonTokenStream
from parser.VerboseLexer import VerboseLexer
from parser.VerboseParser import VerboseParser
from compiler.transformer import Transformer

def main(argv):
    input_stream = FileStream(argv[1])
    lexer = VerboseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VerboseParser(stream)
    tree = parser.module()
    print(tree.toStringTree(recog=parser))
    transformer = Transformer()
    module = transformer.visit(tree)

    print("Transformed module:")
    print(module)


if __name__ == '__main__':
    main(sys.argv)