#!/bin/bash
if [ -e ./venv/bin/antlr4 ] && [ -e ./venv/bin/activate ]; then 
    source ./venv/bin/activate
fi

antlr4 parser/Verbose.g4 -Dlanguage=Python3 -visitor -listener
