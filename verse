#!/usr/bin/env python3
"""Verse - The Verbose language compiler

Usage:
    verse <file>... [options]
    verse (-v | --version)
    verse (-h | --help)

Options:
    -h --help               Show this help message
    -v --version            Show version information
    -e --emit=<filetype>    Select what file the compiler should produce [default: exec], supported: "exec", "ir"
    -b --backend=<backend>  Select the backend to use [default: llvm], supported: "llvm"
    -L --library=<dir>      Add a directory to the library search path.
    -o --output=<file>      Specify output file.
    --preserve-temp         Preserve temporary files created during compilation
    --verbose               Enable verbose output

Dependencies:
    - Python 3.13 or higher
    - clang (for LLVM backend)
    - docopt, antlr4-python3-runtime, llvmlite

"""
from docopt import docopt
from app import main

VERSION = "experimental0.0.0"

if __name__ == "__main__":
    args = docopt(__doc__, version=VERSION)
    if args.get("-v"):
        print(VERSION)
        exit(0)
    return_code = main(args)
    exit(return_code)

