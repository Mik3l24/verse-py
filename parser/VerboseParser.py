# Generated from parser/Verbose.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,65,370,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,1,0,5,0,74,8,0,10,0,12,0,77,9,0,1,0,1,0,
        1,1,1,1,1,2,3,2,84,8,2,1,2,1,2,3,2,88,8,2,1,3,1,3,1,3,1,3,3,3,94,
        8,3,3,3,96,8,3,1,4,3,4,99,8,4,1,4,1,4,1,4,3,4,104,8,4,1,4,1,4,1,
        5,1,5,1,5,1,5,3,5,112,8,5,3,5,114,8,5,1,5,1,5,1,5,5,5,119,8,5,10,
        5,12,5,122,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,131,8,6,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,161,8,8,1,8,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,5,8,175,8,8,10,8,12,8,178,9,8,
        1,9,1,9,3,9,182,8,9,1,10,1,10,1,10,1,11,1,11,3,11,189,8,11,1,12,
        1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,3,13,201,8,13,1,13,
        1,13,1,14,1,14,1,14,1,14,1,14,1,15,1,15,1,16,1,16,1,16,5,16,215,
        8,16,10,16,12,16,218,9,16,1,16,1,16,3,16,222,8,16,1,17,1,17,1,18,
        1,18,3,18,228,8,18,1,18,1,18,3,18,232,8,18,1,18,3,18,235,8,18,1,
        19,1,19,1,19,1,19,1,19,3,19,242,8,19,1,20,1,20,3,20,246,8,20,1,21,
        1,21,3,21,250,8,21,1,22,1,22,3,22,254,8,22,1,23,1,23,1,23,1,23,1,
        23,3,23,261,8,23,1,24,1,24,3,24,265,8,24,1,24,5,24,268,8,24,10,24,
        12,24,271,9,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,25,3,25,281,
        8,25,3,25,283,8,25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,
        1,28,1,28,1,28,1,29,1,29,1,29,1,30,1,30,1,30,1,30,5,30,304,8,30,
        10,30,12,30,307,9,30,1,30,3,30,310,8,30,1,30,3,30,313,8,30,1,31,
        1,31,1,31,1,31,5,31,319,8,31,10,31,12,31,322,9,31,1,31,3,31,325,
        8,31,1,31,3,31,328,8,31,1,32,1,32,1,32,3,32,333,8,32,1,32,3,32,336,
        8,32,1,32,3,32,339,8,32,1,32,3,32,342,8,32,1,32,1,32,1,33,1,33,1,
        33,1,33,1,33,3,33,351,8,33,1,34,1,34,1,35,5,35,356,8,35,10,35,12,
        35,359,9,35,1,35,1,35,5,35,363,8,35,10,35,12,35,366,9,35,1,35,1,
        35,1,35,0,2,10,16,36,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,0,9,
        1,0,4,6,1,0,20,21,1,0,18,19,1,0,28,30,1,0,22,27,1,0,54,55,1,0,50,
        51,2,0,10,10,53,53,1,0,38,39,398,0,75,1,0,0,0,2,80,1,0,0,0,4,87,
        1,0,0,0,6,95,1,0,0,0,8,98,1,0,0,0,10,113,1,0,0,0,12,130,1,0,0,0,
        14,132,1,0,0,0,16,160,1,0,0,0,18,181,1,0,0,0,20,183,1,0,0,0,22,188,
        1,0,0,0,24,190,1,0,0,0,26,200,1,0,0,0,28,204,1,0,0,0,30,209,1,0,
        0,0,32,216,1,0,0,0,34,223,1,0,0,0,36,225,1,0,0,0,38,236,1,0,0,0,
        40,243,1,0,0,0,42,247,1,0,0,0,44,251,1,0,0,0,46,260,1,0,0,0,48,262,
        1,0,0,0,50,274,1,0,0,0,52,284,1,0,0,0,54,288,1,0,0,0,56,293,1,0,
        0,0,58,296,1,0,0,0,60,299,1,0,0,0,62,314,1,0,0,0,64,329,1,0,0,0,
        66,350,1,0,0,0,68,352,1,0,0,0,70,357,1,0,0,0,72,74,3,66,33,0,73,
        72,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,
        0,77,75,1,0,0,0,78,79,5,0,0,1,79,1,1,0,0,0,80,81,5,65,0,0,81,3,1,
        0,0,0,82,84,5,46,0,0,83,82,1,0,0,0,83,84,1,0,0,0,84,85,1,0,0,0,85,
        88,5,44,0,0,86,88,1,0,0,0,87,83,1,0,0,0,87,86,1,0,0,0,88,5,1,0,0,
        0,89,90,5,63,0,0,90,96,3,2,1,0,91,93,3,8,4,0,92,94,5,10,0,0,93,92,
        1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,89,1,0,0,0,95,91,1,0,0,0,
        96,7,1,0,0,0,97,99,5,63,0,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,
        0,0,0,100,101,3,2,1,0,101,103,5,34,0,0,102,104,5,37,0,0,103,102,
        1,0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,3,32,16,0,106,9,
        1,0,0,0,107,108,6,5,-1,0,108,114,5,65,0,0,109,111,3,12,6,0,110,112,
        5,10,0,0,111,110,1,0,0,0,111,112,1,0,0,0,112,114,1,0,0,0,113,107,
        1,0,0,0,113,109,1,0,0,0,114,120,1,0,0,0,115,116,10,1,0,0,116,117,
        5,11,0,0,117,119,5,65,0,0,118,115,1,0,0,0,119,122,1,0,0,0,120,118,
        1,0,0,0,120,121,1,0,0,0,121,11,1,0,0,0,122,120,1,0,0,0,123,124,5,
        61,0,0,124,131,3,16,8,0,125,126,5,60,0,0,126,127,3,10,5,0,127,128,
        5,61,0,0,128,129,3,16,8,0,129,131,1,0,0,0,130,123,1,0,0,0,130,125,
        1,0,0,0,131,13,1,0,0,0,132,133,5,64,0,0,133,134,3,18,9,0,134,15,
        1,0,0,0,135,136,6,8,-1,0,136,161,7,0,0,0,137,161,5,3,0,0,138,161,
        5,7,0,0,139,161,3,14,7,0,140,141,5,12,0,0,141,142,3,16,8,0,142,143,
        5,13,0,0,143,161,1,0,0,0,144,145,5,14,0,0,145,146,3,16,8,0,146,147,
        5,15,0,0,147,161,1,0,0,0,148,149,5,16,0,0,149,150,3,16,8,0,150,151,
        5,17,0,0,151,161,1,0,0,0,152,161,3,6,3,0,153,161,3,10,5,0,154,155,
        5,19,0,0,155,161,3,16,8,7,156,157,5,31,0,0,157,161,3,16,8,6,158,
        159,5,62,0,0,159,161,3,16,8,5,160,135,1,0,0,0,160,137,1,0,0,0,160,
        138,1,0,0,0,160,139,1,0,0,0,160,140,1,0,0,0,160,144,1,0,0,0,160,
        148,1,0,0,0,160,152,1,0,0,0,160,153,1,0,0,0,160,154,1,0,0,0,160,
        156,1,0,0,0,160,158,1,0,0,0,161,176,1,0,0,0,162,163,10,4,0,0,163,
        164,7,1,0,0,164,175,3,16,8,5,165,166,10,3,0,0,166,167,7,2,0,0,167,
        175,3,16,8,4,168,169,10,2,0,0,169,170,7,3,0,0,170,175,3,16,8,3,171,
        172,10,1,0,0,172,173,7,4,0,0,173,175,3,16,8,2,174,162,1,0,0,0,174,
        165,1,0,0,0,174,168,1,0,0,0,174,171,1,0,0,0,175,178,1,0,0,0,176,
        174,1,0,0,0,176,177,1,0,0,0,177,17,1,0,0,0,178,176,1,0,0,0,179,182,
        3,20,10,0,180,182,3,22,11,0,181,179,1,0,0,0,181,180,1,0,0,0,182,
        19,1,0,0,0,183,184,7,5,0,0,184,185,3,22,11,0,185,21,1,0,0,0,186,
        189,5,65,0,0,187,189,3,24,12,0,188,186,1,0,0,0,188,187,1,0,0,0,189,
        23,1,0,0,0,190,191,5,56,0,0,191,192,5,35,0,0,192,193,3,18,9,0,193,
        25,1,0,0,0,194,201,3,36,18,0,195,201,3,38,19,0,196,201,3,28,14,0,
        197,201,3,40,20,0,198,201,3,42,21,0,199,201,3,44,22,0,200,194,1,
        0,0,0,200,195,1,0,0,0,200,196,1,0,0,0,200,197,1,0,0,0,200,198,1,
        0,0,0,200,199,1,0,0,0,200,201,1,0,0,0,201,202,1,0,0,0,202,203,5,
        8,0,0,203,27,1,0,0,0,204,205,5,58,0,0,205,206,3,10,5,0,206,207,5,
        59,0,0,207,208,3,16,8,0,208,29,1,0,0,0,209,210,3,16,8,0,210,31,1,
        0,0,0,211,212,3,30,15,0,212,213,5,9,0,0,213,215,1,0,0,0,214,211,
        1,0,0,0,215,218,1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,219,
        1,0,0,0,218,216,1,0,0,0,219,221,3,30,15,0,220,222,5,9,0,0,221,220,
        1,0,0,0,221,222,1,0,0,0,222,33,1,0,0,0,223,224,3,10,5,0,224,35,1,
        0,0,0,225,227,3,2,1,0,226,228,3,34,17,0,227,226,1,0,0,0,227,228,
        1,0,0,0,228,234,1,0,0,0,229,231,5,34,0,0,230,232,5,37,0,0,231,230,
        1,0,0,0,231,232,1,0,0,0,232,233,1,0,0,0,233,235,3,32,16,0,234,229,
        1,0,0,0,234,235,1,0,0,0,235,37,1,0,0,0,236,237,3,4,2,0,237,238,3,
        18,9,0,238,241,3,58,29,0,239,240,5,57,0,0,240,242,3,16,8,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,39,1,0,0,0,243,245,5,48,0,0,244,246,
        5,65,0,0,245,244,1,0,0,0,245,246,1,0,0,0,246,41,1,0,0,0,247,249,
        5,49,0,0,248,250,5,65,0,0,249,248,1,0,0,0,249,250,1,0,0,0,250,43,
        1,0,0,0,251,253,5,47,0,0,252,254,3,16,8,0,253,252,1,0,0,0,253,254,
        1,0,0,0,254,45,1,0,0,0,255,261,3,26,13,0,256,261,3,48,24,0,257,261,
        3,50,25,0,258,261,3,52,26,0,259,261,3,54,27,0,260,255,1,0,0,0,260,
        256,1,0,0,0,260,257,1,0,0,0,260,258,1,0,0,0,260,259,1,0,0,0,261,
        47,1,0,0,0,262,264,7,6,0,0,263,265,3,58,29,0,264,263,1,0,0,0,264,
        265,1,0,0,0,265,269,1,0,0,0,266,268,3,46,23,0,267,266,1,0,0,0,268,
        271,1,0,0,0,269,267,1,0,0,0,269,270,1,0,0,0,270,272,1,0,0,0,271,
        269,1,0,0,0,272,273,7,7,0,0,273,49,1,0,0,0,274,275,5,41,0,0,275,
        276,3,16,8,0,276,282,3,48,24,0,277,280,5,42,0,0,278,281,3,48,24,
        0,279,281,3,50,25,0,280,278,1,0,0,0,280,279,1,0,0,0,281,283,1,0,
        0,0,282,277,1,0,0,0,282,283,1,0,0,0,283,51,1,0,0,0,284,285,5,40,
        0,0,285,286,3,16,8,0,286,287,3,48,24,0,287,53,1,0,0,0,288,289,3,
        48,24,0,289,290,5,40,0,0,290,291,3,16,8,0,291,292,5,8,0,0,292,55,
        1,0,0,0,293,294,5,43,0,0,294,295,3,18,9,0,295,57,1,0,0,0,296,297,
        5,32,0,0,297,298,5,65,0,0,298,59,1,0,0,0,299,300,7,8,0,0,300,305,
        3,38,19,0,301,302,5,9,0,0,302,304,3,18,9,0,303,301,1,0,0,0,304,307,
        1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,309,1,0,0,0,307,305,
        1,0,0,0,308,310,5,9,0,0,309,308,1,0,0,0,309,310,1,0,0,0,310,312,
        1,0,0,0,311,313,5,53,0,0,312,311,1,0,0,0,312,313,1,0,0,0,313,61,
        1,0,0,0,314,315,5,37,0,0,315,320,3,38,19,0,316,317,5,9,0,0,317,319,
        3,18,9,0,318,316,1,0,0,0,319,322,1,0,0,0,320,318,1,0,0,0,320,321,
        1,0,0,0,321,324,1,0,0,0,322,320,1,0,0,0,323,325,5,9,0,0,324,323,
        1,0,0,0,324,325,1,0,0,0,325,327,1,0,0,0,326,328,5,53,0,0,327,326,
        1,0,0,0,327,328,1,0,0,0,328,63,1,0,0,0,329,330,3,4,2,0,330,332,5,
        36,0,0,331,333,3,56,28,0,332,331,1,0,0,0,332,333,1,0,0,0,333,335,
        1,0,0,0,334,336,3,58,29,0,335,334,1,0,0,0,335,336,1,0,0,0,336,338,
        1,0,0,0,337,339,3,60,30,0,338,337,1,0,0,0,338,339,1,0,0,0,339,341,
        1,0,0,0,340,342,3,62,31,0,341,340,1,0,0,0,341,342,1,0,0,0,342,343,
        1,0,0,0,343,344,3,48,24,0,344,65,1,0,0,0,345,351,3,70,35,0,346,351,
        3,64,32,0,347,348,3,38,19,0,348,349,5,8,0,0,349,351,1,0,0,0,350,
        345,1,0,0,0,350,346,1,0,0,0,350,347,1,0,0,0,351,67,1,0,0,0,352,353,
        3,60,30,0,353,69,1,0,0,0,354,356,3,68,34,0,355,354,1,0,0,0,356,359,
        1,0,0,0,357,355,1,0,0,0,357,358,1,0,0,0,358,360,1,0,0,0,359,357,
        1,0,0,0,360,364,5,52,0,0,361,363,3,66,33,0,362,361,1,0,0,0,363,366,
        1,0,0,0,364,362,1,0,0,0,364,365,1,0,0,0,365,367,1,0,0,0,366,364,
        1,0,0,0,367,368,5,53,0,0,368,71,1,0,0,0,44,75,83,87,93,95,98,103,
        111,113,120,130,160,174,176,181,188,200,216,221,227,231,234,241,
        245,249,253,260,264,269,280,282,305,309,312,320,324,327,332,335,
        338,341,350,357,364
    ]

class VerboseParser ( Parser ):

    grammarFileName = "Verbose.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'.'", "','", "';'", "<INVALID>", "'('", "')'", "'['", 
                     "']'", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "<INVALID>", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'&'", "'|'", 
                     "'^'", "<INVALID>", "'named'", "'from'", "'with'", 
                     "'to'", "'function'", "'arguments'", "'targets'", "'target'", 
                     "'while'", "'if'", "'else'", "'returning'", "'inline'", 
                     "'forced'", "'optional'", "'return'", "'break'", "'continue'", 
                     "'procedure'", "'do'", "'begin'", "'end'", "'variable'", 
                     "'constant'", "'pointer'", "'assigned'", "'assign'", 
                     "'value'", "'index'", "'at'", "'not'", "'call'" ]

    symbolicNames = [ "<INVALID>", "WS", "INLINE_COMMENT", "V_FLOAT", "V_INTEGER", 
                      "V_INTEGER_HEX", "V_INTEGER_BIN", "V_STRING", "P_PERIOD", 
                      "P_COMMA", "P_SEMIC", "P_ACCESSOR", "L_PARENTHESIS", 
                      "R_PARENTHESIS", "L_BRACKET", "R_BRACKET", "L_BRACE", 
                      "R_BRACE", "O_PLUS", "O_MINUS", "O_TIMES", "O_DIVIDE", 
                      "O_EQUAL", "O_NOT_EQUAL", "O_LESS", "O_GREATER", "O_LESS_EQUAL", 
                      "O_GREATER_EQUAL", "O_BIT_AND", "O_BIT_OR", "O_BIT_XOR", 
                      "O_BIT_NOT", "NAMED", "FROM", "WITH", "TO", "FUNCTION", 
                      "ARGUMENTS", "TARGETS", "TARGET", "WHILE", "IF", "ELSE", 
                      "RETURNING", "INLINE", "FORCED", "OPTIONAL", "RETURN", 
                      "BREAK", "CONTINUE", "PROCEDURE", "DO", "BEGIN", "END", 
                      "VARIABLE", "CONSTANT", "POINTER", "ASSIGNED", "ASSIGN", 
                      "VALUE", "INDEX", "AT", "NOT", "CALL", "SIZEOF", "V_IDENTIFIER" ]

    RULE_module = 0
    RULE_function_access = 1
    RULE_inline_part = 2
    RULE_expr_call = 3
    RULE_expr_call_nonterm = 4
    RULE_access_expr = 5
    RULE_access_expr_nonterm = 6
    RULE_sizeof_expr = 7
    RULE_expression = 8
    RULE_type_expr = 9
    RULE_mutability_node = 10
    RULE_simple_type_expr = 11
    RULE_pointer_node = 12
    RULE_statement = 13
    RULE_assignment = 14
    RULE_call_argument = 15
    RULE_call_arguments = 16
    RULE_call_target = 17
    RULE_call_statement = 18
    RULE_var_decl = 19
    RULE_break_statement = 20
    RULE_continue_statement = 21
    RULE_return_statement = 22
    RULE_block_item = 23
    RULE_block = 24
    RULE_if = 25
    RULE_while = 26
    RULE_do_while = 27
    RULE_return_type_decl_part = 28
    RULE_name_decl_part = 29
    RULE_target_decl_part = 30
    RULE_arguments_decl_part = 31
    RULE_function = 32
    RULE_module_item = 33
    RULE_section_header = 34
    RULE_section = 35

    ruleNames =  [ "module", "function_access", "inline_part", "expr_call", 
                   "expr_call_nonterm", "access_expr", "access_expr_nonterm", 
                   "sizeof_expr", "expression", "type_expr", "mutability_node", 
                   "simple_type_expr", "pointer_node", "statement", "assignment", 
                   "call_argument", "call_arguments", "call_target", "call_statement", 
                   "var_decl", "break_statement", "continue_statement", 
                   "return_statement", "block_item", "block", "if", "while", 
                   "do_while", "return_type_decl_part", "name_decl_part", 
                   "target_decl_part", "arguments_decl_part", "function", 
                   "module_item", "section_header", "section" ]

    EOF = Token.EOF
    WS=1
    INLINE_COMMENT=2
    V_FLOAT=3
    V_INTEGER=4
    V_INTEGER_HEX=5
    V_INTEGER_BIN=6
    V_STRING=7
    P_PERIOD=8
    P_COMMA=9
    P_SEMIC=10
    P_ACCESSOR=11
    L_PARENTHESIS=12
    R_PARENTHESIS=13
    L_BRACKET=14
    R_BRACKET=15
    L_BRACE=16
    R_BRACE=17
    O_PLUS=18
    O_MINUS=19
    O_TIMES=20
    O_DIVIDE=21
    O_EQUAL=22
    O_NOT_EQUAL=23
    O_LESS=24
    O_GREATER=25
    O_LESS_EQUAL=26
    O_GREATER_EQUAL=27
    O_BIT_AND=28
    O_BIT_OR=29
    O_BIT_XOR=30
    O_BIT_NOT=31
    NAMED=32
    FROM=33
    WITH=34
    TO=35
    FUNCTION=36
    ARGUMENTS=37
    TARGETS=38
    TARGET=39
    WHILE=40
    IF=41
    ELSE=42
    RETURNING=43
    INLINE=44
    FORCED=45
    OPTIONAL=46
    RETURN=47
    BREAK=48
    CONTINUE=49
    PROCEDURE=50
    DO=51
    BEGIN=52
    END=53
    VARIABLE=54
    CONSTANT=55
    POINTER=56
    ASSIGNED=57
    ASSIGN=58
    VALUE=59
    INDEX=60
    AT=61
    NOT=62
    CALL=63
    SIZEOF=64
    V_IDENTIFIER=65

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ModuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(VerboseParser.EOF, 0)

        def module_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.Module_itemContext)
            else:
                return self.getTypedRuleContext(VerboseParser.Module_itemContext,i)


        def getRuleIndex(self):
            return VerboseParser.RULE_module

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule" ):
                listener.enterModule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule" ):
                listener.exitModule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule" ):
                return visitor.visitModule(self)
            else:
                return visitor.visitChildren(self)




    def module(self):

        localctx = VerboseParser.ModuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 538772749) != 0):
                self.state = 72
                self.module_item()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(VerboseParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def V_IDENTIFIER(self):
            return self.getToken(VerboseParser.V_IDENTIFIER, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_function_access

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_access" ):
                listener.enterFunction_access(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_access" ):
                listener.exitFunction_access(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_access" ):
                return visitor.visitFunction_access(self)
            else:
                return visitor.visitChildren(self)




    def function_access(self):

        localctx = VerboseParser.Function_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(VerboseParser.V_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inline_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INLINE(self):
            return self.getToken(VerboseParser.INLINE, 0)

        def OPTIONAL(self):
            return self.getToken(VerboseParser.OPTIONAL, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_inline_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInline_part" ):
                listener.enterInline_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInline_part" ):
                listener.exitInline_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInline_part" ):
                return visitor.visitInline_part(self)
            else:
                return visitor.visitChildren(self)




    def inline_part(self):

        localctx = VerboseParser.Inline_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_inline_part)
        self._la = 0 # Token type
        try:
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==46:
                    self.state = 82
                    self.match(VerboseParser.OPTIONAL)


                self.state = 85
                self.match(VerboseParser.INLINE)
                pass
            elif token in [36, 54, 55, 56, 65]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CALL(self):
            return self.getToken(VerboseParser.CALL, 0)

        def function_access(self):
            return self.getTypedRuleContext(VerboseParser.Function_accessContext,0)


        def expr_call_nonterm(self):
            return self.getTypedRuleContext(VerboseParser.Expr_call_nontermContext,0)


        def P_SEMIC(self):
            return self.getToken(VerboseParser.P_SEMIC, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_expr_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_call" ):
                listener.enterExpr_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_call" ):
                listener.exitExpr_call(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_call" ):
                return visitor.visitExpr_call(self)
            else:
                return visitor.visitChildren(self)




    def expr_call(self):

        localctx = VerboseParser.Expr_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr_call)
        try:
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(VerboseParser.CALL)
                self.state = 90
                self.function_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.expr_call_nonterm()
                self.state = 93
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 92
                    self.match(VerboseParser.P_SEMIC)


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr_call_nontermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_access(self):
            return self.getTypedRuleContext(VerboseParser.Function_accessContext,0)


        def WITH(self):
            return self.getToken(VerboseParser.WITH, 0)

        def call_arguments(self):
            return self.getTypedRuleContext(VerboseParser.Call_argumentsContext,0)


        def CALL(self):
            return self.getToken(VerboseParser.CALL, 0)

        def ARGUMENTS(self):
            return self.getToken(VerboseParser.ARGUMENTS, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_expr_call_nonterm

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr_call_nonterm" ):
                listener.enterExpr_call_nonterm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr_call_nonterm" ):
                listener.exitExpr_call_nonterm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr_call_nonterm" ):
                return visitor.visitExpr_call_nonterm(self)
            else:
                return visitor.visitChildren(self)




    def expr_call_nonterm(self):

        localctx = VerboseParser.Expr_call_nontermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr_call_nonterm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==63:
                self.state = 97
                self.match(VerboseParser.CALL)


            self.state = 100
            self.function_access()
            self.state = 101
            self.match(VerboseParser.WITH)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 102
                self.match(VerboseParser.ARGUMENTS)


            self.state = 105
            self.call_arguments()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Access_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VerboseParser.RULE_access_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(Access_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.Access_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def V_IDENTIFIER(self):
            return self.getToken(VerboseParser.V_IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class MemberAccessContext(Access_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.Access_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def access_expr(self):
            return self.getTypedRuleContext(VerboseParser.Access_exprContext,0)

        def P_ACCESSOR(self):
            return self.getToken(VerboseParser.P_ACCESSOR, 0)
        def V_IDENTIFIER(self):
            return self.getToken(VerboseParser.V_IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMemberAccess" ):
                listener.enterMemberAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMemberAccess" ):
                listener.exitMemberAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMemberAccess" ):
                return visitor.visitMemberAccess(self)
            else:
                return visitor.visitChildren(self)


    class NontermContext(Access_exprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.Access_exprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def access_expr_nonterm(self):
            return self.getTypedRuleContext(VerboseParser.Access_expr_nontermContext,0)

        def P_SEMIC(self):
            return self.getToken(VerboseParser.P_SEMIC, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNonterm" ):
                listener.enterNonterm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNonterm" ):
                listener.exitNonterm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNonterm" ):
                return visitor.visitNonterm(self)
            else:
                return visitor.visitChildren(self)



    def access_expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VerboseParser.Access_exprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_access_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                localctx = VerboseParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 108
                self.match(VerboseParser.V_IDENTIFIER)
                pass
            elif token in [60, 61]:
                localctx = VerboseParser.NontermContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 109
                self.access_expr_nonterm()
                self.state = 111
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 110
                    self.match(VerboseParser.P_SEMIC)


                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VerboseParser.MemberAccessContext(self, VerboseParser.Access_exprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_access_expr)
                    self.state = 115
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 116
                    self.match(VerboseParser.P_ACCESSOR)
                    self.state = 117
                    self.match(VerboseParser.V_IDENTIFIER) 
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Access_expr_nontermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VerboseParser.RULE_access_expr_nonterm

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ArrayAccessContext(Access_expr_nontermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.Access_expr_nontermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INDEX(self):
            return self.getToken(VerboseParser.INDEX, 0)
        def access_expr(self):
            return self.getTypedRuleContext(VerboseParser.Access_exprContext,0)

        def AT(self):
            return self.getToken(VerboseParser.AT, 0)
        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess" ):
                listener.enterArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess" ):
                listener.exitArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)


    class DereferenceContext(Access_expr_nontermContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.Access_expr_nontermContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def AT(self):
            return self.getToken(VerboseParser.AT, 0)
        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDereference" ):
                listener.enterDereference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDereference" ):
                listener.exitDereference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDereference" ):
                return visitor.visitDereference(self)
            else:
                return visitor.visitChildren(self)



    def access_expr_nonterm(self):

        localctx = VerboseParser.Access_expr_nontermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_access_expr_nonterm)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [61]:
                localctx = VerboseParser.DereferenceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.match(VerboseParser.AT)
                self.state = 124
                self.expression(0)
                pass
            elif token in [60]:
                localctx = VerboseParser.ArrayAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(VerboseParser.INDEX)
                self.state = 126
                self.access_expr(0)
                self.state = 127
                self.match(VerboseParser.AT)
                self.state = 128
                self.expression(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sizeof_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIZEOF(self):
            return self.getToken(VerboseParser.SIZEOF, 0)

        def type_expr(self):
            return self.getTypedRuleContext(VerboseParser.Type_exprContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_sizeof_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeof_expr" ):
                listener.enterSizeof_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeof_expr" ):
                listener.exitSizeof_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeof_expr" ):
                return visitor.visitSizeof_expr(self)
            else:
                return visitor.visitChildren(self)




    def sizeof_expr(self):

        localctx = VerboseParser.Sizeof_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_sizeof_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(VerboseParser.SIZEOF)
            self.state = 133
            self.type_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VerboseParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class CallContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr_call(self):
            return self.getTypedRuleContext(VerboseParser.Expr_callContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)


    class UnaryOpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def O_MINUS(self):
            return self.getToken(VerboseParser.O_MINUS, 0)
        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)

        def O_BIT_NOT(self):
            return self.getToken(VerboseParser.O_BIT_NOT, 0)
        def NOT(self):
            return self.getToken(VerboseParser.NOT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOp" ):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)


    class LiteralContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def V_INTEGER(self):
            return self.getToken(VerboseParser.V_INTEGER, 0)
        def V_INTEGER_HEX(self):
            return self.getToken(VerboseParser.V_INTEGER_HEX, 0)
        def V_INTEGER_BIN(self):
            return self.getToken(VerboseParser.V_INTEGER_BIN, 0)
        def V_FLOAT(self):
            return self.getToken(VerboseParser.V_FLOAT, 0)
        def V_STRING(self):
            return self.getToken(VerboseParser.V_STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)


    class AccessContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def access_expr(self):
            return self.getTypedRuleContext(VerboseParser.Access_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccess" ):
                listener.enterAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccess" ):
                listener.exitAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccess" ):
                return visitor.visitAccess(self)
            else:
                return visitor.visitChildren(self)


    class MolecContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def L_PARENTHESIS(self):
            return self.getToken(VerboseParser.L_PARENTHESIS, 0)
        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)

        def R_PARENTHESIS(self):
            return self.getToken(VerboseParser.R_PARENTHESIS, 0)
        def L_BRACKET(self):
            return self.getToken(VerboseParser.L_BRACKET, 0)
        def R_BRACKET(self):
            return self.getToken(VerboseParser.R_BRACKET, 0)
        def L_BRACE(self):
            return self.getToken(VerboseParser.L_BRACE, 0)
        def R_BRACE(self):
            return self.getToken(VerboseParser.R_BRACE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMolec" ):
                listener.enterMolec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMolec" ):
                listener.exitMolec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMolec" ):
                return visitor.visitMolec(self)
            else:
                return visitor.visitChildren(self)


    class SizeofContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def sizeof_expr(self):
            return self.getTypedRuleContext(VerboseParser.Sizeof_exprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeof" ):
                listener.enterSizeof(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeof" ):
                listener.exitSizeof(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeof" ):
                return visitor.visitSizeof(self)
            else:
                return visitor.visitChildren(self)


    class BinaryOpContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.ExpressionContext
            super().__init__(parser)
            self.operator = None # Token
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(VerboseParser.ExpressionContext,i)

        def O_TIMES(self):
            return self.getToken(VerboseParser.O_TIMES, 0)
        def O_DIVIDE(self):
            return self.getToken(VerboseParser.O_DIVIDE, 0)
        def O_PLUS(self):
            return self.getToken(VerboseParser.O_PLUS, 0)
        def O_MINUS(self):
            return self.getToken(VerboseParser.O_MINUS, 0)
        def O_BIT_AND(self):
            return self.getToken(VerboseParser.O_BIT_AND, 0)
        def O_BIT_XOR(self):
            return self.getToken(VerboseParser.O_BIT_XOR, 0)
        def O_BIT_OR(self):
            return self.getToken(VerboseParser.O_BIT_OR, 0)
        def O_EQUAL(self):
            return self.getToken(VerboseParser.O_EQUAL, 0)
        def O_NOT_EQUAL(self):
            return self.getToken(VerboseParser.O_NOT_EQUAL, 0)
        def O_LESS(self):
            return self.getToken(VerboseParser.O_LESS, 0)
        def O_GREATER(self):
            return self.getToken(VerboseParser.O_GREATER, 0)
        def O_LESS_EQUAL(self):
            return self.getToken(VerboseParser.O_LESS_EQUAL, 0)
        def O_GREATER_EQUAL(self):
            return self.getToken(VerboseParser.O_GREATER_EQUAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = VerboseParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = VerboseParser.LiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 136
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 112) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                localctx = VerboseParser.LiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(VerboseParser.V_FLOAT)
                pass

            elif la_ == 3:
                localctx = VerboseParser.LiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(VerboseParser.V_STRING)
                pass

            elif la_ == 4:
                localctx = VerboseParser.SizeofContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 139
                self.sizeof_expr()
                pass

            elif la_ == 5:
                localctx = VerboseParser.MolecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(VerboseParser.L_PARENTHESIS)
                self.state = 141
                self.expression(0)
                self.state = 142
                self.match(VerboseParser.R_PARENTHESIS)
                pass

            elif la_ == 6:
                localctx = VerboseParser.MolecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.match(VerboseParser.L_BRACKET)
                self.state = 145
                self.expression(0)
                self.state = 146
                self.match(VerboseParser.R_BRACKET)
                pass

            elif la_ == 7:
                localctx = VerboseParser.MolecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(VerboseParser.L_BRACE)
                self.state = 149
                self.expression(0)
                self.state = 150
                self.match(VerboseParser.R_BRACE)
                pass

            elif la_ == 8:
                localctx = VerboseParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 152
                self.expr_call()
                pass

            elif la_ == 9:
                localctx = VerboseParser.AccessContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 153
                self.access_expr(0)
                pass

            elif la_ == 10:
                localctx = VerboseParser.UnaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.match(VerboseParser.O_MINUS)
                self.state = 155
                self.expression(7)
                pass

            elif la_ == 11:
                localctx = VerboseParser.UnaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 156
                self.match(VerboseParser.O_BIT_NOT)
                self.state = 157
                self.expression(6)
                pass

            elif la_ == 12:
                localctx = VerboseParser.UnaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 158
                self.match(VerboseParser.NOT)
                self.state = 159
                self.expression(5)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 176
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 174
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = VerboseParser.BinaryOpContext(self, VerboseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 162
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 163
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==20 or _la==21):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 164
                        self.expression(5)
                        pass

                    elif la_ == 2:
                        localctx = VerboseParser.BinaryOpContext(self, VerboseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 165
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 166
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 167
                        self.expression(4)
                        pass

                    elif la_ == 3:
                        localctx = VerboseParser.BinaryOpContext(self, VerboseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 168
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 169
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1879048192) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 170
                        self.expression(3)
                        pass

                    elif la_ == 4:
                        localctx = VerboseParser.BinaryOpContext(self, VerboseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 171
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 172
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 264241152) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 173
                        self.expression(2)
                        pass

             
                self.state = 178
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Type_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mutability_node(self):
            return self.getTypedRuleContext(VerboseParser.Mutability_nodeContext,0)


        def simple_type_expr(self):
            return self.getTypedRuleContext(VerboseParser.Simple_type_exprContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_type_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType_expr" ):
                listener.enterType_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType_expr" ):
                listener.exitType_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_expr" ):
                return visitor.visitType_expr(self)
            else:
                return visitor.visitChildren(self)




    def type_expr(self):

        localctx = VerboseParser.Type_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_type_expr)
        try:
            self.state = 181
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [54, 55]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self.mutability_node()
                pass
            elif token in [56, 65]:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self.simple_type_expr()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mutability_nodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.mut = None # Token

        def simple_type_expr(self):
            return self.getTypedRuleContext(VerboseParser.Simple_type_exprContext,0)


        def CONSTANT(self):
            return self.getToken(VerboseParser.CONSTANT, 0)

        def VARIABLE(self):
            return self.getToken(VerboseParser.VARIABLE, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_mutability_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMutability_node" ):
                listener.enterMutability_node(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMutability_node" ):
                listener.exitMutability_node(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMutability_node" ):
                return visitor.visitMutability_node(self)
            else:
                return visitor.visitChildren(self)




    def mutability_node(self):

        localctx = VerboseParser.Mutability_nodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_mutability_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            localctx.mut = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==54 or _la==55):
                localctx.mut = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 184
            self.simple_type_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_type_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def V_IDENTIFIER(self):
            return self.getToken(VerboseParser.V_IDENTIFIER, 0)

        def pointer_node(self):
            return self.getTypedRuleContext(VerboseParser.Pointer_nodeContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_simple_type_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_type_expr" ):
                listener.enterSimple_type_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_type_expr" ):
                listener.exitSimple_type_expr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSimple_type_expr" ):
                return visitor.visitSimple_type_expr(self)
            else:
                return visitor.visitChildren(self)




    def simple_type_expr(self):

        localctx = VerboseParser.Simple_type_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_simple_type_expr)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [65]:
                self.enterOuterAlt(localctx, 1)
                self.state = 186
                self.match(VerboseParser.V_IDENTIFIER)
                pass
            elif token in [56]:
                self.enterOuterAlt(localctx, 2)
                self.state = 187
                self.pointer_node()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Pointer_nodeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POINTER(self):
            return self.getToken(VerboseParser.POINTER, 0)

        def TO(self):
            return self.getToken(VerboseParser.TO, 0)

        def type_expr(self):
            return self.getTypedRuleContext(VerboseParser.Type_exprContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_pointer_node

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPointer_node" ):
                listener.enterPointer_node(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPointer_node" ):
                listener.exitPointer_node(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPointer_node" ):
                return visitor.visitPointer_node(self)
            else:
                return visitor.visitChildren(self)




    def pointer_node(self):

        localctx = VerboseParser.Pointer_nodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_pointer_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(VerboseParser.POINTER)
            self.state = 191
            self.match(VerboseParser.TO)
            self.state = 192
            self.type_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def P_PERIOD(self):
            return self.getToken(VerboseParser.P_PERIOD, 0)

        def call_statement(self):
            return self.getTypedRuleContext(VerboseParser.Call_statementContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(VerboseParser.Var_declContext,0)


        def assignment(self):
            return self.getTypedRuleContext(VerboseParser.AssignmentContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(VerboseParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(VerboseParser.Continue_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(VerboseParser.Return_statementContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = VerboseParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 194
                self.call_statement()

            elif la_ == 2:
                self.state = 195
                self.var_decl()

            elif la_ == 3:
                self.state = 196
                self.assignment()

            elif la_ == 4:
                self.state = 197
                self.break_statement()

            elif la_ == 5:
                self.state = 198
                self.continue_statement()

            elif la_ == 6:
                self.state = 199
                self.return_statement()


            self.state = 202
            self.match(VerboseParser.P_PERIOD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN(self):
            return self.getToken(VerboseParser.ASSIGN, 0)

        def access_expr(self):
            return self.getTypedRuleContext(VerboseParser.Access_exprContext,0)


        def VALUE(self):
            return self.getToken(VerboseParser.VALUE, 0)

        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = VerboseParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(VerboseParser.ASSIGN)
            self.state = 205
            self.access_expr(0)
            self.state = 206
            self.match(VerboseParser.VALUE)
            self.state = 207
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_argumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_call_argument

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_argument" ):
                listener.enterCall_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_argument" ):
                listener.exitCall_argument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_argument" ):
                return visitor.visitCall_argument(self)
            else:
                return visitor.visitChildren(self)




    def call_argument(self):

        localctx = VerboseParser.Call_argumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_call_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_argumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def call_argument(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.Call_argumentContext)
            else:
                return self.getTypedRuleContext(VerboseParser.Call_argumentContext,i)


        def P_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(VerboseParser.P_COMMA)
            else:
                return self.getToken(VerboseParser.P_COMMA, i)

        def getRuleIndex(self):
            return VerboseParser.RULE_call_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_arguments" ):
                listener.enterCall_arguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_arguments" ):
                listener.exitCall_arguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_arguments" ):
                return visitor.visitCall_arguments(self)
            else:
                return visitor.visitChildren(self)




    def call_arguments(self):

        localctx = VerboseParser.Call_argumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_call_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 211
                    self.call_argument()
                    self.state = 212
                    self.match(VerboseParser.P_COMMA) 
                self.state = 218
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 219
            self.call_argument()
            self.state = 221
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 220
                self.match(VerboseParser.P_COMMA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_targetContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def access_expr(self):
            return self.getTypedRuleContext(VerboseParser.Access_exprContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_call_target

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_target" ):
                listener.enterCall_target(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_target" ):
                listener.exitCall_target(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_target" ):
                return visitor.visitCall_target(self)
            else:
                return visitor.visitChildren(self)




    def call_target(self):

        localctx = VerboseParser.Call_targetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_call_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.access_expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_access(self):
            return self.getTypedRuleContext(VerboseParser.Function_accessContext,0)


        def call_target(self):
            return self.getTypedRuleContext(VerboseParser.Call_targetContext,0)


        def WITH(self):
            return self.getToken(VerboseParser.WITH, 0)

        def call_arguments(self):
            return self.getTypedRuleContext(VerboseParser.Call_argumentsContext,0)


        def ARGUMENTS(self):
            return self.getToken(VerboseParser.ARGUMENTS, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_call_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall_statement" ):
                listener.enterCall_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall_statement" ):
                listener.exitCall_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall_statement" ):
                return visitor.visitCall_statement(self)
            else:
                return visitor.visitChildren(self)




    def call_statement(self):

        localctx = VerboseParser.Call_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.function_access()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 60)) & ~0x3f) == 0 and ((1 << (_la - 60)) & 35) != 0):
                self.state = 226
                self.call_target()


            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 229
                self.match(VerboseParser.WITH)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==37:
                    self.state = 230
                    self.match(VerboseParser.ARGUMENTS)


                self.state = 233
                self.call_arguments()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inline_part(self):
            return self.getTypedRuleContext(VerboseParser.Inline_partContext,0)


        def type_expr(self):
            return self.getTypedRuleContext(VerboseParser.Type_exprContext,0)


        def name_decl_part(self):
            return self.getTypedRuleContext(VerboseParser.Name_decl_partContext,0)


        def ASSIGNED(self):
            return self.getToken(VerboseParser.ASSIGNED, 0)

        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = VerboseParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.inline_part()
            self.state = 237
            self.type_expr()
            self.state = 238
            self.name_decl_part()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 239
                self.match(VerboseParser.ASSIGNED)
                self.state = 240
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(VerboseParser.BREAK, 0)

        def V_IDENTIFIER(self):
            return self.getToken(VerboseParser.V_IDENTIFIER, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_break_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak_statement" ):
                listener.enterBreak_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak_statement" ):
                listener.exitBreak_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = VerboseParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(VerboseParser.BREAK)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 244
                self.match(VerboseParser.V_IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(VerboseParser.CONTINUE, 0)

        def V_IDENTIFIER(self):
            return self.getToken(VerboseParser.V_IDENTIFIER, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_continue_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinue_statement" ):
                listener.enterContinue_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinue_statement" ):
                listener.exitContinue_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = VerboseParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(VerboseParser.CONTINUE)
            self.state = 249
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 248
                self.match(VerboseParser.V_IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(VerboseParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_return_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_statement" ):
                listener.enterReturn_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_statement" ):
                listener.exitReturn_statement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = VerboseParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(VerboseParser.RETURN)
            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 3)) & ~0x3f) == 0 and ((1 << (_la - 3)) & 9079256849047431711) != 0):
                self.state = 252
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(VerboseParser.StatementContext,0)


        def block(self):
            return self.getTypedRuleContext(VerboseParser.BlockContext,0)


        def if_(self):
            return self.getTypedRuleContext(VerboseParser.IfContext,0)


        def while_(self):
            return self.getTypedRuleContext(VerboseParser.WhileContext,0)


        def do_while(self):
            return self.getTypedRuleContext(VerboseParser.Do_whileContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_block_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock_item" ):
                listener.enterBlock_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock_item" ):
                listener.exitBlock_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_item" ):
                return visitor.visitBlock_item(self)
            else:
                return visitor.visitChildren(self)




    def block_item(self):

        localctx = VerboseParser.Block_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_block_item)
        try:
            self.state = 260
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 255
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 256
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 257
                self.if_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 258
                self.while_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 259
                self.do_while()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROCEDURE(self):
            return self.getToken(VerboseParser.PROCEDURE, 0)

        def DO(self):
            return self.getToken(VerboseParser.DO, 0)

        def END(self):
            return self.getToken(VerboseParser.END, 0)

        def P_SEMIC(self):
            return self.getToken(VerboseParser.P_SEMIC, 0)

        def name_decl_part(self):
            return self.getTypedRuleContext(VerboseParser.Name_decl_partContext,0)


        def block_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.Block_itemContext)
            else:
                return self.getTypedRuleContext(VerboseParser.Block_itemContext,i)


        def getRuleIndex(self):
            return VerboseParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = VerboseParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            _la = self._input.LA(1)
            if not(_la==50 or _la==51):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 264
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 263
                self.name_decl_part()


            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 8)) & ~0x3f) == 0 and ((1 << (_la - 8)) & 145751068104458241) != 0):
                self.state = 266
                self.block_item()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 272
            _la = self._input.LA(1)
            if not(_la==10 or _la==53):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(VerboseParser.IF, 0)

        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.BlockContext)
            else:
                return self.getTypedRuleContext(VerboseParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(VerboseParser.ELSE, 0)

        def if_(self):
            return self.getTypedRuleContext(VerboseParser.IfContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = VerboseParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.match(VerboseParser.IF)
            self.state = 275
            self.expression(0)
            self.state = 276
            self.block()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==42:
                self.state = 277
                self.match(VerboseParser.ELSE)
                self.state = 280
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [50, 51]:
                    self.state = 278
                    self.block()
                    pass
                elif token in [41]:
                    self.state = 279
                    self.if_()
                    pass
                else:
                    raise NoViableAltException(self)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(VerboseParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)


        def block(self):
            return self.getTypedRuleContext(VerboseParser.BlockContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile" ):
                listener.enterWhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile" ):
                listener.exitWhile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile" ):
                return visitor.visitWhile(self)
            else:
                return visitor.visitChildren(self)




    def while_(self):

        localctx = VerboseParser.WhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(VerboseParser.WHILE)
            self.state = 285
            self.expression(0)
            self.state = 286
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Do_whileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(VerboseParser.BlockContext,0)


        def WHILE(self):
            return self.getToken(VerboseParser.WHILE, 0)

        def expression(self):
            return self.getTypedRuleContext(VerboseParser.ExpressionContext,0)


        def P_PERIOD(self):
            return self.getToken(VerboseParser.P_PERIOD, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_do_while

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDo_while" ):
                listener.enterDo_while(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDo_while" ):
                listener.exitDo_while(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDo_while" ):
                return visitor.visitDo_while(self)
            else:
                return visitor.visitChildren(self)




    def do_while(self):

        localctx = VerboseParser.Do_whileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_do_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 288
            self.block()
            self.state = 289
            self.match(VerboseParser.WHILE)
            self.state = 290
            self.expression(0)
            self.state = 291
            self.match(VerboseParser.P_PERIOD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_type_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURNING(self):
            return self.getToken(VerboseParser.RETURNING, 0)

        def type_expr(self):
            return self.getTypedRuleContext(VerboseParser.Type_exprContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_return_type_decl_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_type_decl_part" ):
                listener.enterReturn_type_decl_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_type_decl_part" ):
                listener.exitReturn_type_decl_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_type_decl_part" ):
                return visitor.visitReturn_type_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def return_type_decl_part(self):

        localctx = VerboseParser.Return_type_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_return_type_decl_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.match(VerboseParser.RETURNING)
            self.state = 294
            self.type_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Name_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAMED(self):
            return self.getToken(VerboseParser.NAMED, 0)

        def V_IDENTIFIER(self):
            return self.getToken(VerboseParser.V_IDENTIFIER, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_name_decl_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName_decl_part" ):
                listener.enterName_decl_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName_decl_part" ):
                listener.exitName_decl_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitName_decl_part" ):
                return visitor.visitName_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def name_decl_part(self):

        localctx = VerboseParser.Name_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_name_decl_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(VerboseParser.NAMED)
            self.state = 297
            self.match(VerboseParser.V_IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Target_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self):
            return self.getTypedRuleContext(VerboseParser.Var_declContext,0)


        def TARGET(self):
            return self.getToken(VerboseParser.TARGET, 0)

        def TARGETS(self):
            return self.getToken(VerboseParser.TARGETS, 0)

        def P_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(VerboseParser.P_COMMA)
            else:
                return self.getToken(VerboseParser.P_COMMA, i)

        def type_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.Type_exprContext)
            else:
                return self.getTypedRuleContext(VerboseParser.Type_exprContext,i)


        def END(self):
            return self.getToken(VerboseParser.END, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_target_decl_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarget_decl_part" ):
                listener.enterTarget_decl_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarget_decl_part" ):
                listener.exitTarget_decl_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget_decl_part" ):
                return visitor.visitTarget_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def target_decl_part(self):

        localctx = VerboseParser.Target_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_target_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not(_la==38 or _la==39):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 300
            self.var_decl()
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 301
                    self.match(VerboseParser.P_COMMA)
                    self.state = 302
                    self.type_expr() 
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

            self.state = 309
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 308
                self.match(VerboseParser.P_COMMA)


            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 311
                self.match(VerboseParser.END)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arguments_decl_partContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARGUMENTS(self):
            return self.getToken(VerboseParser.ARGUMENTS, 0)

        def var_decl(self):
            return self.getTypedRuleContext(VerboseParser.Var_declContext,0)


        def P_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(VerboseParser.P_COMMA)
            else:
                return self.getToken(VerboseParser.P_COMMA, i)

        def type_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.Type_exprContext)
            else:
                return self.getTypedRuleContext(VerboseParser.Type_exprContext,i)


        def END(self):
            return self.getToken(VerboseParser.END, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_arguments_decl_part

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments_decl_part" ):
                listener.enterArguments_decl_part(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments_decl_part" ):
                listener.exitArguments_decl_part(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments_decl_part" ):
                return visitor.visitArguments_decl_part(self)
            else:
                return visitor.visitChildren(self)




    def arguments_decl_part(self):

        localctx = VerboseParser.Arguments_decl_partContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_arguments_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.match(VerboseParser.ARGUMENTS)
            self.state = 315
            self.var_decl()
            self.state = 320
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 316
                    self.match(VerboseParser.P_COMMA)
                    self.state = 317
                    self.type_expr() 
                self.state = 322
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 323
                self.match(VerboseParser.P_COMMA)


            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 326
                self.match(VerboseParser.END)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def inline_part(self):
            return self.getTypedRuleContext(VerboseParser.Inline_partContext,0)


        def FUNCTION(self):
            return self.getToken(VerboseParser.FUNCTION, 0)

        def block(self):
            return self.getTypedRuleContext(VerboseParser.BlockContext,0)


        def return_type_decl_part(self):
            return self.getTypedRuleContext(VerboseParser.Return_type_decl_partContext,0)


        def name_decl_part(self):
            return self.getTypedRuleContext(VerboseParser.Name_decl_partContext,0)


        def target_decl_part(self):
            return self.getTypedRuleContext(VerboseParser.Target_decl_partContext,0)


        def arguments_decl_part(self):
            return self.getTypedRuleContext(VerboseParser.Arguments_decl_partContext,0)


        def getRuleIndex(self):
            return VerboseParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = VerboseParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.inline_part()
            self.state = 330
            self.match(VerboseParser.FUNCTION)
            self.state = 332
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 331
                self.return_type_decl_part()


            self.state = 335
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 334
                self.name_decl_part()


            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38 or _la==39:
                self.state = 337
                self.target_decl_part()


            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 340
                self.arguments_decl_part()


            self.state = 343
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Module_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def section(self):
            return self.getTypedRuleContext(VerboseParser.SectionContext,0)


        def function(self):
            return self.getTypedRuleContext(VerboseParser.FunctionContext,0)


        def var_decl(self):
            return self.getTypedRuleContext(VerboseParser.Var_declContext,0)


        def P_PERIOD(self):
            return self.getToken(VerboseParser.P_PERIOD, 0)

        def getRuleIndex(self):
            return VerboseParser.RULE_module_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModule_item" ):
                listener.enterModule_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModule_item" ):
                listener.exitModule_item(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModule_item" ):
                return visitor.visitModule_item(self)
            else:
                return visitor.visitChildren(self)




    def module_item(self):

        localctx = VerboseParser.Module_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_module_item)
        try:
            self.state = 350
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 345
                self.section()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.function()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.var_decl()
                self.state = 348
                self.match(VerboseParser.P_PERIOD)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Section_headerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return VerboseParser.RULE_section_header

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TargetContext(Section_headerContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a VerboseParser.Section_headerContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def target_decl_part(self):
            return self.getTypedRuleContext(VerboseParser.Target_decl_partContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTarget" ):
                listener.enterTarget(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTarget" ):
                listener.exitTarget(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTarget" ):
                return visitor.visitTarget(self)
            else:
                return visitor.visitChildren(self)



    def section_header(self):

        localctx = VerboseParser.Section_headerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_section_header)
        try:
            localctx = VerboseParser.TargetContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.target_decl_part()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEGIN(self):
            return self.getToken(VerboseParser.BEGIN, 0)

        def END(self):
            return self.getToken(VerboseParser.END, 0)

        def section_header(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.Section_headerContext)
            else:
                return self.getTypedRuleContext(VerboseParser.Section_headerContext,i)


        def module_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.Module_itemContext)
            else:
                return self.getTypedRuleContext(VerboseParser.Module_itemContext,i)


        def getRuleIndex(self):
            return VerboseParser.RULE_section

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSection" ):
                listener.enterSection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSection" ):
                listener.exitSection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSection" ):
                return visitor.visitSection(self)
            else:
                return visitor.visitChildren(self)




    def section(self):

        localctx = VerboseParser.SectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==38 or _la==39:
                self.state = 354
                self.section_header()
                self.state = 359
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 360
            self.match(VerboseParser.BEGIN)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 36)) & ~0x3f) == 0 and ((1 << (_la - 36)) & 538772749) != 0):
                self.state = 361
                self.module_item()
                self.state = 366
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 367
            self.match(VerboseParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[5] = self.access_expr_sempred
        self._predicates[8] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def access_expr_sempred(self, localctx:Access_exprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 1)
         




