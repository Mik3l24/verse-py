from antlr4 import InputStream, FileStream, StdinStream, CommonTokenStream
from parser.VerboseLexer import VerboseLexer
from parser.VerboseParser import VerboseParser
from compiler.transformer import Transformer
from vast.module import VModule


def parse(input_stream: InputStream | FileStream | StdinStream) -> VModule:
    """
    Parses the input stream and returns the root of the parsed module as VAST.

    :param input_stream: The input stream to parse.
    :return: The root the parsed module.
    """
    lexer = VerboseLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = VerboseParser(stream)
    tree = parser.module()

    transformer = Transformer()
    module: VModule = transformer.visit(tree)

    return module
