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
        4,1,62,364,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,1,0,1,0,1,1,3,1,74,8,1,1,1,1,1,3,1,78,8,1,1,2,1,2,
        1,2,1,2,3,2,84,8,2,3,2,86,8,2,1,3,3,3,89,8,3,1,3,1,3,1,3,3,3,94,
        8,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,102,8,4,3,4,104,8,4,1,4,1,4,1,4,
        5,4,109,8,4,10,4,12,4,112,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,121,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,147,8,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,5,6,161,8,6,10,6,12,6,164,9,6,1,
        7,1,7,3,7,168,8,7,1,8,1,8,1,8,1,9,1,9,3,9,175,8,9,1,10,1,10,1,10,
        1,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,187,8,11,1,11,1,11,1,12,
        1,12,1,12,1,12,1,12,1,13,1,13,1,14,1,14,1,14,5,14,201,8,14,10,14,
        12,14,204,9,14,1,14,1,14,3,14,208,8,14,1,15,1,15,1,16,1,16,3,16,
        214,8,16,1,16,1,16,3,16,218,8,16,1,16,3,16,221,8,16,1,17,1,17,1,
        17,1,17,1,17,3,17,228,8,17,1,18,1,18,3,18,232,8,18,1,19,1,19,3,19,
        236,8,19,1,20,1,20,3,20,240,8,20,1,21,1,21,1,21,1,21,1,21,3,21,247,
        8,21,1,22,1,22,3,22,251,8,22,1,22,5,22,254,8,22,10,22,12,22,257,
        9,22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,1,23,3,23,267,8,23,3,23,
        269,8,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,
        1,26,1,27,1,27,1,27,1,28,1,28,1,28,1,28,5,28,290,8,28,10,28,12,28,
        293,9,28,1,28,3,28,296,8,28,1,28,3,28,299,8,28,1,29,1,29,1,29,1,
        29,5,29,305,8,29,10,29,12,29,308,9,29,1,29,1,29,3,29,312,8,29,1,
        29,3,29,315,8,29,1,30,1,30,3,30,319,8,30,1,30,3,30,322,8,30,1,30,
        3,30,325,8,30,1,30,3,30,328,8,30,1,30,1,30,1,31,1,31,1,31,1,31,1,
        31,3,31,337,8,31,1,32,1,32,1,33,5,33,342,8,33,10,33,12,33,345,9,
        33,1,33,1,33,5,33,349,8,33,10,33,12,33,352,9,33,1,33,1,33,1,34,5,
        34,357,8,34,10,34,12,34,360,9,34,1,34,1,34,1,34,0,2,8,12,35,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,56,58,60,62,64,66,68,0,8,1,0,18,19,1,0,16,17,1,0,26,28,
        1,0,20,25,1,0,52,53,1,0,48,49,2,0,8,8,51,51,1,0,36,37,392,0,70,1,
        0,0,0,2,77,1,0,0,0,4,85,1,0,0,0,6,88,1,0,0,0,8,103,1,0,0,0,10,120,
        1,0,0,0,12,146,1,0,0,0,14,167,1,0,0,0,16,169,1,0,0,0,18,174,1,0,
        0,0,20,176,1,0,0,0,22,186,1,0,0,0,24,190,1,0,0,0,26,195,1,0,0,0,
        28,202,1,0,0,0,30,209,1,0,0,0,32,211,1,0,0,0,34,222,1,0,0,0,36,229,
        1,0,0,0,38,233,1,0,0,0,40,237,1,0,0,0,42,246,1,0,0,0,44,248,1,0,
        0,0,46,260,1,0,0,0,48,270,1,0,0,0,50,274,1,0,0,0,52,279,1,0,0,0,
        54,282,1,0,0,0,56,285,1,0,0,0,58,300,1,0,0,0,60,316,1,0,0,0,62,336,
        1,0,0,0,64,338,1,0,0,0,66,343,1,0,0,0,68,358,1,0,0,0,70,71,5,62,
        0,0,71,1,1,0,0,0,72,74,5,44,0,0,73,72,1,0,0,0,73,74,1,0,0,0,74,75,
        1,0,0,0,75,78,5,42,0,0,76,78,1,0,0,0,77,73,1,0,0,0,77,76,1,0,0,0,
        78,3,1,0,0,0,79,80,5,61,0,0,80,86,3,0,0,0,81,83,3,6,3,0,82,84,5,
        8,0,0,83,82,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,79,1,0,0,0,85,
        81,1,0,0,0,86,5,1,0,0,0,87,89,5,61,0,0,88,87,1,0,0,0,88,89,1,0,0,
        0,89,90,1,0,0,0,90,91,3,0,0,0,91,93,5,32,0,0,92,94,5,35,0,0,93,92,
        1,0,0,0,93,94,1,0,0,0,94,95,1,0,0,0,95,96,3,28,14,0,96,7,1,0,0,0,
        97,98,6,4,-1,0,98,104,5,62,0,0,99,101,3,10,5,0,100,102,5,8,0,0,101,
        100,1,0,0,0,101,102,1,0,0,0,102,104,1,0,0,0,103,97,1,0,0,0,103,99,
        1,0,0,0,104,110,1,0,0,0,105,106,10,1,0,0,106,107,5,9,0,0,107,109,
        5,62,0,0,108,105,1,0,0,0,109,112,1,0,0,0,110,108,1,0,0,0,110,111,
        1,0,0,0,111,9,1,0,0,0,112,110,1,0,0,0,113,114,5,59,0,0,114,121,3,
        12,6,0,115,116,5,58,0,0,116,117,3,8,4,0,117,118,5,59,0,0,118,119,
        3,12,6,0,119,121,1,0,0,0,120,113,1,0,0,0,120,115,1,0,0,0,121,11,
        1,0,0,0,122,123,6,6,-1,0,123,147,5,4,0,0,124,147,5,3,0,0,125,147,
        5,5,0,0,126,127,5,10,0,0,127,128,3,12,6,0,128,129,5,11,0,0,129,147,
        1,0,0,0,130,131,5,12,0,0,131,132,3,12,6,0,132,133,5,13,0,0,133,147,
        1,0,0,0,134,135,5,14,0,0,135,136,3,12,6,0,136,137,5,15,0,0,137,147,
        1,0,0,0,138,139,5,17,0,0,139,147,3,12,6,9,140,141,5,29,0,0,141,147,
        3,12,6,8,142,143,5,60,0,0,143,147,3,12,6,7,144,147,3,8,4,0,145,147,
        3,4,2,0,146,122,1,0,0,0,146,124,1,0,0,0,146,125,1,0,0,0,146,126,
        1,0,0,0,146,130,1,0,0,0,146,134,1,0,0,0,146,138,1,0,0,0,146,140,
        1,0,0,0,146,142,1,0,0,0,146,144,1,0,0,0,146,145,1,0,0,0,147,162,
        1,0,0,0,148,149,10,6,0,0,149,150,7,0,0,0,150,161,3,12,6,7,151,152,
        10,5,0,0,152,153,7,1,0,0,153,161,3,12,6,6,154,155,10,4,0,0,155,156,
        7,2,0,0,156,161,3,12,6,5,157,158,10,3,0,0,158,159,7,3,0,0,159,161,
        3,12,6,4,160,148,1,0,0,0,160,151,1,0,0,0,160,154,1,0,0,0,160,157,
        1,0,0,0,161,164,1,0,0,0,162,160,1,0,0,0,162,163,1,0,0,0,163,13,1,
        0,0,0,164,162,1,0,0,0,165,168,3,16,8,0,166,168,3,18,9,0,167,165,
        1,0,0,0,167,166,1,0,0,0,168,15,1,0,0,0,169,170,7,4,0,0,170,171,3,
        18,9,0,171,17,1,0,0,0,172,175,5,62,0,0,173,175,3,20,10,0,174,172,
        1,0,0,0,174,173,1,0,0,0,175,19,1,0,0,0,176,177,5,54,0,0,177,178,
        5,33,0,0,178,179,3,14,7,0,179,21,1,0,0,0,180,187,3,32,16,0,181,187,
        3,34,17,0,182,187,3,24,12,0,183,187,3,36,18,0,184,187,3,38,19,0,
        185,187,3,40,20,0,186,180,1,0,0,0,186,181,1,0,0,0,186,182,1,0,0,
        0,186,183,1,0,0,0,186,184,1,0,0,0,186,185,1,0,0,0,186,187,1,0,0,
        0,187,188,1,0,0,0,188,189,5,6,0,0,189,23,1,0,0,0,190,191,5,56,0,
        0,191,192,3,8,4,0,192,193,5,57,0,0,193,194,3,12,6,0,194,25,1,0,0,
        0,195,196,3,12,6,0,196,27,1,0,0,0,197,198,3,26,13,0,198,199,5,7,
        0,0,199,201,1,0,0,0,200,197,1,0,0,0,201,204,1,0,0,0,202,200,1,0,
        0,0,202,203,1,0,0,0,203,205,1,0,0,0,204,202,1,0,0,0,205,207,3,26,
        13,0,206,208,5,7,0,0,207,206,1,0,0,0,207,208,1,0,0,0,208,29,1,0,
        0,0,209,210,3,8,4,0,210,31,1,0,0,0,211,213,3,0,0,0,212,214,3,30,
        15,0,213,212,1,0,0,0,213,214,1,0,0,0,214,220,1,0,0,0,215,217,5,32,
        0,0,216,218,5,35,0,0,217,216,1,0,0,0,217,218,1,0,0,0,218,219,1,0,
        0,0,219,221,3,28,14,0,220,215,1,0,0,0,220,221,1,0,0,0,221,33,1,0,
        0,0,222,223,3,2,1,0,223,224,3,14,7,0,224,227,3,54,27,0,225,226,5,
        55,0,0,226,228,3,12,6,0,227,225,1,0,0,0,227,228,1,0,0,0,228,35,1,
        0,0,0,229,231,5,46,0,0,230,232,5,62,0,0,231,230,1,0,0,0,231,232,
        1,0,0,0,232,37,1,0,0,0,233,235,5,47,0,0,234,236,5,62,0,0,235,234,
        1,0,0,0,235,236,1,0,0,0,236,39,1,0,0,0,237,239,5,45,0,0,238,240,
        3,12,6,0,239,238,1,0,0,0,239,240,1,0,0,0,240,41,1,0,0,0,241,247,
        3,22,11,0,242,247,3,44,22,0,243,247,3,46,23,0,244,247,3,48,24,0,
        245,247,3,50,25,0,246,241,1,0,0,0,246,242,1,0,0,0,246,243,1,0,0,
        0,246,244,1,0,0,0,246,245,1,0,0,0,247,43,1,0,0,0,248,250,7,5,0,0,
        249,251,3,54,27,0,250,249,1,0,0,0,250,251,1,0,0,0,251,255,1,0,0,
        0,252,254,3,42,21,0,253,252,1,0,0,0,254,257,1,0,0,0,255,253,1,0,
        0,0,255,256,1,0,0,0,256,258,1,0,0,0,257,255,1,0,0,0,258,259,7,6,
        0,0,259,45,1,0,0,0,260,261,5,39,0,0,261,262,3,12,6,0,262,268,3,44,
        22,0,263,266,5,40,0,0,264,267,3,44,22,0,265,267,3,46,23,0,266,264,
        1,0,0,0,266,265,1,0,0,0,267,269,1,0,0,0,268,263,1,0,0,0,268,269,
        1,0,0,0,269,47,1,0,0,0,270,271,5,38,0,0,271,272,3,12,6,0,272,273,
        3,44,22,0,273,49,1,0,0,0,274,275,3,44,22,0,275,276,5,38,0,0,276,
        277,3,12,6,0,277,278,5,6,0,0,278,51,1,0,0,0,279,280,5,41,0,0,280,
        281,3,14,7,0,281,53,1,0,0,0,282,283,5,30,0,0,283,284,5,62,0,0,284,
        55,1,0,0,0,285,286,7,7,0,0,286,291,3,14,7,0,287,288,5,7,0,0,288,
        290,3,14,7,0,289,287,1,0,0,0,290,293,1,0,0,0,291,289,1,0,0,0,291,
        292,1,0,0,0,292,295,1,0,0,0,293,291,1,0,0,0,294,296,5,7,0,0,295,
        294,1,0,0,0,295,296,1,0,0,0,296,298,1,0,0,0,297,299,5,51,0,0,298,
        297,1,0,0,0,298,299,1,0,0,0,299,57,1,0,0,0,300,306,5,35,0,0,301,
        302,3,34,17,0,302,303,5,7,0,0,303,305,1,0,0,0,304,301,1,0,0,0,305,
        308,1,0,0,0,306,304,1,0,0,0,306,307,1,0,0,0,307,309,1,0,0,0,308,
        306,1,0,0,0,309,311,3,34,17,0,310,312,5,7,0,0,311,310,1,0,0,0,311,
        312,1,0,0,0,312,314,1,0,0,0,313,315,5,51,0,0,314,313,1,0,0,0,314,
        315,1,0,0,0,315,59,1,0,0,0,316,318,5,34,0,0,317,319,3,52,26,0,318,
        317,1,0,0,0,318,319,1,0,0,0,319,321,1,0,0,0,320,322,3,54,27,0,321,
        320,1,0,0,0,321,322,1,0,0,0,322,324,1,0,0,0,323,325,3,56,28,0,324,
        323,1,0,0,0,324,325,1,0,0,0,325,327,1,0,0,0,326,328,3,58,29,0,327,
        326,1,0,0,0,327,328,1,0,0,0,328,329,1,0,0,0,329,330,3,44,22,0,330,
        61,1,0,0,0,331,337,3,66,33,0,332,337,3,60,30,0,333,334,3,34,17,0,
        334,335,5,6,0,0,335,337,1,0,0,0,336,331,1,0,0,0,336,332,1,0,0,0,
        336,333,1,0,0,0,337,63,1,0,0,0,338,339,3,56,28,0,339,65,1,0,0,0,
        340,342,3,64,32,0,341,340,1,0,0,0,342,345,1,0,0,0,343,341,1,0,0,
        0,343,344,1,0,0,0,344,346,1,0,0,0,345,343,1,0,0,0,346,350,5,50,0,
        0,347,349,3,62,31,0,348,347,1,0,0,0,349,352,1,0,0,0,350,348,1,0,
        0,0,350,351,1,0,0,0,351,353,1,0,0,0,352,350,1,0,0,0,353,354,5,51,
        0,0,354,67,1,0,0,0,355,357,3,62,31,0,356,355,1,0,0,0,357,360,1,0,
        0,0,358,356,1,0,0,0,358,359,1,0,0,0,359,361,1,0,0,0,360,358,1,0,
        0,0,361,362,5,0,0,1,362,69,1,0,0,0,44,73,77,83,85,88,93,101,103,
        110,120,146,160,162,167,174,186,202,207,213,217,220,227,231,235,
        239,246,250,255,266,268,291,295,298,306,311,314,318,321,324,327,
        336,343,350,358
    ]

class VerboseParser ( Parser ):

    grammarFileName = "Verbose.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'.'", "','", "';'", "<INVALID>", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "'+'", "'-'", 
                     "'*'", "'/'", "<INVALID>", "'!='", "'<'", "'>'", "'<='", 
                     "'>='", "'&'", "'|'", "'^'", "<INVALID>", "'named'", 
                     "'from'", "'with'", "'to'", "'function'", "'arguments'", 
                     "'targets'", "'target'", "'while'", "'if'", "'else'", 
                     "'returning'", "'inline'", "'forced'", "'optional'", 
                     "'return'", "'break'", "'continue'", "'procedure'", 
                     "'do'", "'begin'", "'end'", "'variable'", "'constant'", 
                     "'pointer'", "'assigned'", "'assign'", "'value'", "'index'", 
                     "'at'", "'not'", "'call'" ]

    symbolicNames = [ "<INVALID>", "WS", "INLINE_COMMENT", "V_FLOAT", "V_INTEGER", 
                      "V_STRING", "P_PERIOD", "P_COMMA", "P_SEMIC", "P_ACCESSOR", 
                      "L_PARENTHESIS", "R_PARENTHESIS", "L_BRACKET", "R_BRACKET", 
                      "L_BRACE", "R_BRACE", "O_PLUS", "O_MINUS", "O_TIMES", 
                      "O_DIVIDE", "O_EQUAL", "O_NOT_EQUAL", "O_LESS", "O_GREATER", 
                      "O_LESS_EQUAL", "O_GREATER_EQUAL", "O_BIT_AND", "O_BIT_OR", 
                      "O_BIT_XOR", "O_BIT_NOT", "NAMED", "FROM", "WITH", 
                      "TO", "FUNCTION", "ARGUMENTS", "TARGETS", "TARGET", 
                      "WHILE", "IF", "ELSE", "RETURNING", "INLINE", "FORCED", 
                      "OPTIONAL", "RETURN", "BREAK", "CONTINUE", "PROCEDURE", 
                      "DO", "BEGIN", "END", "VARIABLE", "CONSTANT", "POINTER", 
                      "ASSIGNED", "ASSIGN", "VALUE", "INDEX", "AT", "NOT", 
                      "CALL", "V_IDENTIFIER" ]

    RULE_function_access = 0
    RULE_inline_part = 1
    RULE_expr_call = 2
    RULE_expr_call_nonterm = 3
    RULE_access_expr = 4
    RULE_access_expr_nonterm = 5
    RULE_expression = 6
    RULE_type_expr = 7
    RULE_mutability_node = 8
    RULE_simple_type_expr = 9
    RULE_pointer_node = 10
    RULE_statement = 11
    RULE_assignment = 12
    RULE_call_argument = 13
    RULE_call_arguments = 14
    RULE_call_target = 15
    RULE_call_statement = 16
    RULE_var_decl = 17
    RULE_break_statement = 18
    RULE_continue_statement = 19
    RULE_return_statement = 20
    RULE_block_item = 21
    RULE_block = 22
    RULE_if = 23
    RULE_while = 24
    RULE_do_while = 25
    RULE_return_type_decl_part = 26
    RULE_name_decl_part = 27
    RULE_target_decl_part = 28
    RULE_arguments_decl_part = 29
    RULE_function = 30
    RULE_module_item = 31
    RULE_section_header = 32
    RULE_section = 33
    RULE_module = 34

    ruleNames =  [ "function_access", "inline_part", "expr_call", "expr_call_nonterm", 
                   "access_expr", "access_expr_nonterm", "expression", "type_expr", 
                   "mutability_node", "simple_type_expr", "pointer_node", 
                   "statement", "assignment", "call_argument", "call_arguments", 
                   "call_target", "call_statement", "var_decl", "break_statement", 
                   "continue_statement", "return_statement", "block_item", 
                   "block", "if", "while", "do_while", "return_type_decl_part", 
                   "name_decl_part", "target_decl_part", "arguments_decl_part", 
                   "function", "module_item", "section_header", "section", 
                   "module" ]

    EOF = Token.EOF
    WS=1
    INLINE_COMMENT=2
    V_FLOAT=3
    V_INTEGER=4
    V_STRING=5
    P_PERIOD=6
    P_COMMA=7
    P_SEMIC=8
    P_ACCESSOR=9
    L_PARENTHESIS=10
    R_PARENTHESIS=11
    L_BRACKET=12
    R_BRACKET=13
    L_BRACE=14
    R_BRACE=15
    O_PLUS=16
    O_MINUS=17
    O_TIMES=18
    O_DIVIDE=19
    O_EQUAL=20
    O_NOT_EQUAL=21
    O_LESS=22
    O_GREATER=23
    O_LESS_EQUAL=24
    O_GREATER_EQUAL=25
    O_BIT_AND=26
    O_BIT_OR=27
    O_BIT_XOR=28
    O_BIT_NOT=29
    NAMED=30
    FROM=31
    WITH=32
    TO=33
    FUNCTION=34
    ARGUMENTS=35
    TARGETS=36
    TARGET=37
    WHILE=38
    IF=39
    ELSE=40
    RETURNING=41
    INLINE=42
    FORCED=43
    OPTIONAL=44
    RETURN=45
    BREAK=46
    CONTINUE=47
    PROCEDURE=48
    DO=49
    BEGIN=50
    END=51
    VARIABLE=52
    CONSTANT=53
    POINTER=54
    ASSIGNED=55
    ASSIGN=56
    VALUE=57
    INDEX=58
    AT=59
    NOT=60
    CALL=61
    V_IDENTIFIER=62

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_function_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
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
        self.enterRule(localctx, 2, self.RULE_inline_part)
        self._la = 0 # Token type
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==44:
                    self.state = 72
                    self.match(VerboseParser.OPTIONAL)


                self.state = 75
                self.match(VerboseParser.INLINE)
                pass
            elif token in [52, 53, 54, 62]:
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
        self.enterRule(localctx, 4, self.RULE_expr_call)
        try:
            self.state = 85
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(VerboseParser.CALL)
                self.state = 80
                self.function_access()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 81
                self.expr_call_nonterm()
                self.state = 83
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                if la_ == 1:
                    self.state = 82
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
        self.enterRule(localctx, 6, self.RULE_expr_call_nonterm)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==61:
                self.state = 87
                self.match(VerboseParser.CALL)


            self.state = 90
            self.function_access()
            self.state = 91
            self.match(VerboseParser.WITH)
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 92
                self.match(VerboseParser.ARGUMENTS)


            self.state = 95
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_access_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                localctx = VerboseParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 98
                self.match(VerboseParser.V_IDENTIFIER)
                pass
            elif token in [58, 59]:
                localctx = VerboseParser.NontermContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 99
                self.access_expr_nonterm()
                self.state = 101
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                if la_ == 1:
                    self.state = 100
                    self.match(VerboseParser.P_SEMIC)


                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = VerboseParser.MemberAccessContext(self, VerboseParser.Access_exprContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_access_expr)
                    self.state = 105
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 106
                    self.match(VerboseParser.P_ACCESSOR)
                    self.state = 107
                    self.match(VerboseParser.V_IDENTIFIER) 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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
        self.enterRule(localctx, 10, self.RULE_access_expr_nonterm)
        try:
            self.state = 120
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [59]:
                localctx = VerboseParser.DereferenceContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 113
                self.match(VerboseParser.AT)
                self.state = 114
                self.expression(0)
                pass
            elif token in [58]:
                localctx = VerboseParser.ArrayAccessContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.match(VerboseParser.INDEX)
                self.state = 116
                self.access_expr(0)
                self.state = 117
                self.match(VerboseParser.AT)
                self.state = 118
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
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = VerboseParser.LiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 123
                self.match(VerboseParser.V_INTEGER)
                pass

            elif la_ == 2:
                localctx = VerboseParser.LiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 124
                self.match(VerboseParser.V_FLOAT)
                pass

            elif la_ == 3:
                localctx = VerboseParser.LiteralContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 125
                self.match(VerboseParser.V_STRING)
                pass

            elif la_ == 4:
                localctx = VerboseParser.MolecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 126
                self.match(VerboseParser.L_PARENTHESIS)
                self.state = 127
                self.expression(0)
                self.state = 128
                self.match(VerboseParser.R_PARENTHESIS)
                pass

            elif la_ == 5:
                localctx = VerboseParser.MolecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(VerboseParser.L_BRACKET)
                self.state = 131
                self.expression(0)
                self.state = 132
                self.match(VerboseParser.R_BRACKET)
                pass

            elif la_ == 6:
                localctx = VerboseParser.MolecContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 134
                self.match(VerboseParser.L_BRACE)
                self.state = 135
                self.expression(0)
                self.state = 136
                self.match(VerboseParser.R_BRACE)
                pass

            elif la_ == 7:
                localctx = VerboseParser.UnaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 138
                self.match(VerboseParser.O_MINUS)
                self.state = 139
                self.expression(9)
                pass

            elif la_ == 8:
                localctx = VerboseParser.UnaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 140
                self.match(VerboseParser.O_BIT_NOT)
                self.state = 141
                self.expression(8)
                pass

            elif la_ == 9:
                localctx = VerboseParser.UnaryOpContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(VerboseParser.NOT)
                self.state = 143
                self.expression(7)
                pass

            elif la_ == 10:
                localctx = VerboseParser.AccessContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 144
                self.access_expr(0)
                pass

            elif la_ == 11:
                localctx = VerboseParser.CallContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 145
                self.expr_call()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 162
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 160
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = VerboseParser.BinaryOpContext(self, VerboseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 148
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 149
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==18 or _la==19):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 150
                        self.expression(7)
                        pass

                    elif la_ == 2:
                        localctx = VerboseParser.BinaryOpContext(self, VerboseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 151
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 152
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==16 or _la==17):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 153
                        self.expression(6)
                        pass

                    elif la_ == 3:
                        localctx = VerboseParser.BinaryOpContext(self, VerboseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 155
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 469762048) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 156
                        self.expression(5)
                        pass

                    elif la_ == 4:
                        localctx = VerboseParser.BinaryOpContext(self, VerboseParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 158
                        localctx.operator = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 66060288) != 0)):
                            localctx.operator = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 159
                        self.expression(4)
                        pass

             
                self.state = 164
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 14, self.RULE_type_expr)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [52, 53]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.mutability_node()
                pass
            elif token in [54, 62]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
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
        self.enterRule(localctx, 16, self.RULE_mutability_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            localctx.mut = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==52 or _la==53):
                localctx.mut = self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 170
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
        self.enterRule(localctx, 18, self.RULE_simple_type_expr)
        try:
            self.state = 174
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(VerboseParser.V_IDENTIFIER)
                pass
            elif token in [54]:
                self.enterOuterAlt(localctx, 2)
                self.state = 173
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
        self.enterRule(localctx, 20, self.RULE_pointer_node)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(VerboseParser.POINTER)
            self.state = 177
            self.match(VerboseParser.TO)
            self.state = 178
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
        self.enterRule(localctx, 22, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 180
                self.call_statement()

            elif la_ == 2:
                self.state = 181
                self.var_decl()

            elif la_ == 3:
                self.state = 182
                self.assignment()

            elif la_ == 4:
                self.state = 183
                self.break_statement()

            elif la_ == 5:
                self.state = 184
                self.continue_statement()

            elif la_ == 6:
                self.state = 185
                self.return_statement()


            self.state = 188
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
        self.enterRule(localctx, 24, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(VerboseParser.ASSIGN)
            self.state = 191
            self.access_expr(0)
            self.state = 192
            self.match(VerboseParser.VALUE)
            self.state = 193
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
        self.enterRule(localctx, 26, self.RULE_call_argument)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
        self.enterRule(localctx, 28, self.RULE_call_arguments)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 197
                    self.call_argument()
                    self.state = 198
                    self.match(VerboseParser.P_COMMA) 
                self.state = 204
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

            self.state = 205
            self.call_argument()
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 206
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
        self.enterRule(localctx, 30, self.RULE_call_target)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
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
        self.enterRule(localctx, 32, self.RULE_call_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.function_access()
            self.state = 213
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 5476377146882523136) != 0):
                self.state = 212
                self.call_target()


            self.state = 220
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 215
                self.match(VerboseParser.WITH)
                self.state = 217
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 216
                    self.match(VerboseParser.ARGUMENTS)


                self.state = 219
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
        self.enterRule(localctx, 34, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.inline_part()
            self.state = 223
            self.type_expr()
            self.state = 224
            self.name_decl_part()
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 225
                self.match(VerboseParser.ASSIGNED)
                self.state = 226
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
        self.enterRule(localctx, 36, self.RULE_break_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(VerboseParser.BREAK)
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 230
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
        self.enterRule(localctx, 38, self.RULE_continue_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(VerboseParser.CONTINUE)
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==62:
                self.state = 234
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
        self.enterRule(localctx, 40, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(VerboseParser.RETURN)
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8935141661240087608) != 0):
                self.state = 238
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
        self.enterRule(localctx, 42, self.RULE_block_item)
        try:
            self.state = 246
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 243
                self.if_()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 244
                self.while_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 245
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
        self.enterRule(localctx, 44, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            _la = self._input.LA(1)
            if not(_la==48 or _la==49):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 249
                self.name_decl_part()


            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4716382340257939520) != 0):
                self.state = 252
                self.block_item()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 258
            _la = self._input.LA(1)
            if not(_la==8 or _la==51):
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
        self.enterRule(localctx, 46, self.RULE_if)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(VerboseParser.IF)
            self.state = 261
            self.expression(0)
            self.state = 262
            self.block()
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==40:
                self.state = 263
                self.match(VerboseParser.ELSE)
                self.state = 266
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [48, 49]:
                    self.state = 264
                    self.block()
                    pass
                elif token in [39]:
                    self.state = 265
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
        self.enterRule(localctx, 48, self.RULE_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.match(VerboseParser.WHILE)
            self.state = 271
            self.expression(0)
            self.state = 272
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
        self.enterRule(localctx, 50, self.RULE_do_while)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self.block()
            self.state = 275
            self.match(VerboseParser.WHILE)
            self.state = 276
            self.expression(0)
            self.state = 277
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
        self.enterRule(localctx, 52, self.RULE_return_type_decl_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.match(VerboseParser.RETURNING)
            self.state = 280
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
        self.enterRule(localctx, 54, self.RULE_name_decl_part)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.match(VerboseParser.NAMED)
            self.state = 283
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

        def type_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.Type_exprContext)
            else:
                return self.getTypedRuleContext(VerboseParser.Type_exprContext,i)


        def TARGET(self):
            return self.getToken(VerboseParser.TARGET, 0)

        def TARGETS(self):
            return self.getToken(VerboseParser.TARGETS, 0)

        def P_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(VerboseParser.P_COMMA)
            else:
                return self.getToken(VerboseParser.P_COMMA, i)

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
        self.enterRule(localctx, 56, self.RULE_target_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            _la = self._input.LA(1)
            if not(_la==36 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 286
            self.type_expr()
            self.state = 291
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 287
                    self.match(VerboseParser.P_COMMA)
                    self.state = 288
                    self.type_expr() 
                self.state = 293
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 294
                self.match(VerboseParser.P_COMMA)


            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 297
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

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(VerboseParser.Var_declContext)
            else:
                return self.getTypedRuleContext(VerboseParser.Var_declContext,i)


        def P_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(VerboseParser.P_COMMA)
            else:
                return self.getToken(VerboseParser.P_COMMA, i)

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
        self.enterRule(localctx, 58, self.RULE_arguments_decl_part)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(VerboseParser.ARGUMENTS)
            self.state = 306
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,33,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 301
                    self.var_decl()
                    self.state = 302
                    self.match(VerboseParser.P_COMMA) 
                self.state = 308
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 309
            self.var_decl()
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 310
                self.match(VerboseParser.P_COMMA)


            self.state = 314
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 313
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
        self.enterRule(localctx, 60, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(VerboseParser.FUNCTION)
            self.state = 318
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 317
                self.return_type_decl_part()


            self.state = 321
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 320
                self.name_decl_part()


            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36 or _la==37:
                self.state = 323
                self.target_decl_part()


            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==35:
                self.state = 326
                self.arguments_decl_part()


            self.state = 329
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
        self.enterRule(localctx, 62, self.RULE_module_item)
        try:
            self.state = 336
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36, 37, 50]:
                self.enterOuterAlt(localctx, 1)
                self.state = 331
                self.section()
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 2)
                self.state = 332
                self.function()
                pass
            elif token in [42, 44, 52, 53, 54, 62]:
                self.enterOuterAlt(localctx, 3)
                self.state = 333
                self.var_decl()
                self.state = 334
                self.match(VerboseParser.P_PERIOD)
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
        self.enterRule(localctx, 64, self.RULE_section_header)
        try:
            localctx = VerboseParser.TargetContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 338
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
        self.enterRule(localctx, 66, self.RULE_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 343
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36 or _la==37:
                self.state = 340
                self.section_header()
                self.state = 345
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 346
            self.match(VerboseParser.BEGIN)
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4644359329296678912) != 0):
                self.state = 347
                self.module_item()
                self.state = 352
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 353
            self.match(VerboseParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


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
        self.enterRule(localctx, 68, self.RULE_module)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4644359329296678912) != 0):
                self.state = 355
                self.module_item()
                self.state = 360
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 361
            self.match(VerboseParser.EOF)
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
        self._predicates[4] = self.access_expr_sempred
        self._predicates[6] = self.expression_sempred
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
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         




