# Generated from parser/Verbose.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,62,457,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,
        39,7,39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,
        45,2,46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,
        52,7,52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,
        58,2,59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,1,0,4,0,129,8,0,11,0,
        12,0,130,1,0,1,0,1,1,1,1,1,1,1,1,5,1,139,8,1,10,1,12,1,142,9,1,1,
        1,1,1,1,2,5,2,147,8,2,10,2,12,2,150,9,2,1,2,1,2,4,2,154,8,2,11,2,
        12,2,155,1,3,4,3,159,8,3,11,3,12,3,160,1,4,1,4,1,4,1,4,5,4,167,8,
        4,10,4,12,4,170,9,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,
        3,8,183,8,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,
        1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,3,19,
        208,8,19,1,20,1,20,1,20,1,21,1,21,1,22,1,22,1,23,1,23,1,23,1,24,
        1,24,1,24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,1,28,1,28,1,28,
        1,28,1,28,3,28,236,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,30,
        1,30,1,30,1,30,1,31,1,31,1,31,1,31,1,31,1,32,1,32,1,32,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,34,1,34,1,34,1,34,1,34,1,34,
        1,34,1,34,1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,36,
        1,36,1,36,1,36,1,36,1,36,1,36,1,37,1,37,1,37,1,37,1,37,1,37,1,38,
        1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,40,1,40,1,40,1,40,1,40,1,40,
        1,40,1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,1,41,1,41,1,42,1,42,
        1,42,1,42,1,42,1,42,1,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,
        1,43,1,44,1,44,1,44,1,44,1,44,1,44,1,44,1,45,1,45,1,45,1,45,1,45,
        1,45,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,46,1,47,1,47,1,47,
        1,47,1,47,1,47,1,47,1,47,1,47,1,47,1,48,1,48,1,48,1,49,1,49,1,49,
        1,49,1,49,1,49,1,50,1,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,51,
        1,51,1,51,1,51,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,52,1,53,
        1,53,1,53,1,53,1,53,1,53,1,53,1,53,1,54,1,54,1,54,1,54,1,54,1,54,
        1,54,1,54,1,54,1,55,1,55,1,55,1,55,1,55,1,55,1,55,1,56,1,56,1,56,
        1,56,1,56,1,56,1,57,1,57,1,57,1,57,1,57,1,57,1,58,1,58,1,58,1,59,
        1,59,1,59,1,59,1,60,1,60,1,60,1,60,1,60,1,61,1,61,5,61,451,8,61,
        10,61,12,61,454,9,61,1,62,1,62,0,0,63,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,
        37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,
        59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,37,75,38,77,39,79,40,
        81,41,83,42,85,43,87,44,89,45,91,46,93,47,95,48,97,49,99,50,101,
        51,103,52,105,53,107,54,109,55,111,56,113,57,115,58,117,59,119,60,
        121,61,123,62,125,0,1,0,6,3,0,9,10,13,13,32,32,2,0,10,10,13,13,2,
        0,34,34,92,92,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,
        1,0,48,57,466,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,
        9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,
        19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,
        29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,
        39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,
        49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,
        59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,0,67,1,0,0,0,0,
        69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,0,77,1,0,0,0,0,
        79,1,0,0,0,0,81,1,0,0,0,0,83,1,0,0,0,0,85,1,0,0,0,0,87,1,0,0,0,0,
        89,1,0,0,0,0,91,1,0,0,0,0,93,1,0,0,0,0,95,1,0,0,0,0,97,1,0,0,0,0,
        99,1,0,0,0,0,101,1,0,0,0,0,103,1,0,0,0,0,105,1,0,0,0,0,107,1,0,0,
        0,0,109,1,0,0,0,0,111,1,0,0,0,0,113,1,0,0,0,0,115,1,0,0,0,0,117,
        1,0,0,0,0,119,1,0,0,0,0,121,1,0,0,0,0,123,1,0,0,0,1,128,1,0,0,0,
        3,134,1,0,0,0,5,148,1,0,0,0,7,158,1,0,0,0,9,162,1,0,0,0,11,173,1,
        0,0,0,13,175,1,0,0,0,15,177,1,0,0,0,17,182,1,0,0,0,19,184,1,0,0,
        0,21,186,1,0,0,0,23,188,1,0,0,0,25,190,1,0,0,0,27,192,1,0,0,0,29,
        194,1,0,0,0,31,196,1,0,0,0,33,198,1,0,0,0,35,200,1,0,0,0,37,202,
        1,0,0,0,39,207,1,0,0,0,41,209,1,0,0,0,43,212,1,0,0,0,45,214,1,0,
        0,0,47,216,1,0,0,0,49,219,1,0,0,0,51,222,1,0,0,0,53,224,1,0,0,0,
        55,226,1,0,0,0,57,235,1,0,0,0,59,237,1,0,0,0,61,243,1,0,0,0,63,248,
        1,0,0,0,65,253,1,0,0,0,67,256,1,0,0,0,69,265,1,0,0,0,71,275,1,0,
        0,0,73,283,1,0,0,0,75,290,1,0,0,0,77,296,1,0,0,0,79,299,1,0,0,0,
        81,304,1,0,0,0,83,314,1,0,0,0,85,321,1,0,0,0,87,328,1,0,0,0,89,337,
        1,0,0,0,91,344,1,0,0,0,93,350,1,0,0,0,95,359,1,0,0,0,97,369,1,0,
        0,0,99,372,1,0,0,0,101,378,1,0,0,0,103,382,1,0,0,0,105,391,1,0,0,
        0,107,400,1,0,0,0,109,408,1,0,0,0,111,417,1,0,0,0,113,424,1,0,0,
        0,115,430,1,0,0,0,117,436,1,0,0,0,119,439,1,0,0,0,121,443,1,0,0,
        0,123,448,1,0,0,0,125,455,1,0,0,0,127,129,7,0,0,0,128,127,1,0,0,
        0,129,130,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,
        0,132,133,6,0,0,0,133,2,1,0,0,0,134,135,5,47,0,0,135,136,5,47,0,
        0,136,140,1,0,0,0,137,139,8,1,0,0,138,137,1,0,0,0,139,142,1,0,0,
        0,140,138,1,0,0,0,140,141,1,0,0,0,141,143,1,0,0,0,142,140,1,0,0,
        0,143,144,6,1,0,0,144,4,1,0,0,0,145,147,3,125,62,0,146,145,1,0,0,
        0,147,150,1,0,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,151,1,0,0,
        0,150,148,1,0,0,0,151,153,5,46,0,0,152,154,3,125,62,0,153,152,1,
        0,0,0,154,155,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,6,1,0,
        0,0,157,159,3,125,62,0,158,157,1,0,0,0,159,160,1,0,0,0,160,158,1,
        0,0,0,160,161,1,0,0,0,161,8,1,0,0,0,162,168,5,34,0,0,163,167,8,2,
        0,0,164,165,5,92,0,0,165,167,9,0,0,0,166,163,1,0,0,0,166,164,1,0,
        0,0,167,170,1,0,0,0,168,166,1,0,0,0,168,169,1,0,0,0,169,171,1,0,
        0,0,170,168,1,0,0,0,171,172,5,34,0,0,172,10,1,0,0,0,173,174,5,46,
        0,0,174,12,1,0,0,0,175,176,5,44,0,0,176,14,1,0,0,0,177,178,5,59,
        0,0,178,16,1,0,0,0,179,183,5,39,0,0,180,181,5,39,0,0,181,183,5,115,
        0,0,182,179,1,0,0,0,182,180,1,0,0,0,183,18,1,0,0,0,184,185,5,40,
        0,0,185,20,1,0,0,0,186,187,5,41,0,0,187,22,1,0,0,0,188,189,5,91,
        0,0,189,24,1,0,0,0,190,191,5,93,0,0,191,26,1,0,0,0,192,193,5,123,
        0,0,193,28,1,0,0,0,194,195,5,125,0,0,195,30,1,0,0,0,196,197,5,43,
        0,0,197,32,1,0,0,0,198,199,5,45,0,0,199,34,1,0,0,0,200,201,5,42,
        0,0,201,36,1,0,0,0,202,203,5,47,0,0,203,38,1,0,0,0,204,208,5,61,
        0,0,205,206,5,61,0,0,206,208,5,61,0,0,207,204,1,0,0,0,207,205,1,
        0,0,0,208,40,1,0,0,0,209,210,5,33,0,0,210,211,5,61,0,0,211,42,1,
        0,0,0,212,213,5,60,0,0,213,44,1,0,0,0,214,215,5,62,0,0,215,46,1,
        0,0,0,216,217,5,60,0,0,217,218,5,61,0,0,218,48,1,0,0,0,219,220,5,
        62,0,0,220,221,5,61,0,0,221,50,1,0,0,0,222,223,5,38,0,0,223,52,1,
        0,0,0,224,225,5,124,0,0,225,54,1,0,0,0,226,227,5,94,0,0,227,56,1,
        0,0,0,228,229,5,105,0,0,229,230,5,110,0,0,230,231,5,118,0,0,231,
        232,5,101,0,0,232,233,5,114,0,0,233,236,5,116,0,0,234,236,5,126,
        0,0,235,228,1,0,0,0,235,234,1,0,0,0,236,58,1,0,0,0,237,238,5,110,
        0,0,238,239,5,97,0,0,239,240,5,109,0,0,240,241,5,101,0,0,241,242,
        5,100,0,0,242,60,1,0,0,0,243,244,5,102,0,0,244,245,5,114,0,0,245,
        246,5,111,0,0,246,247,5,109,0,0,247,62,1,0,0,0,248,249,5,119,0,0,
        249,250,5,105,0,0,250,251,5,116,0,0,251,252,5,104,0,0,252,64,1,0,
        0,0,253,254,5,116,0,0,254,255,5,111,0,0,255,66,1,0,0,0,256,257,5,
        102,0,0,257,258,5,117,0,0,258,259,5,110,0,0,259,260,5,99,0,0,260,
        261,5,116,0,0,261,262,5,105,0,0,262,263,5,111,0,0,263,264,5,110,
        0,0,264,68,1,0,0,0,265,266,5,97,0,0,266,267,5,114,0,0,267,268,5,
        103,0,0,268,269,5,117,0,0,269,270,5,109,0,0,270,271,5,101,0,0,271,
        272,5,110,0,0,272,273,5,116,0,0,273,274,5,115,0,0,274,70,1,0,0,0,
        275,276,5,116,0,0,276,277,5,97,0,0,277,278,5,114,0,0,278,279,5,103,
        0,0,279,280,5,101,0,0,280,281,5,116,0,0,281,282,5,115,0,0,282,72,
        1,0,0,0,283,284,5,116,0,0,284,285,5,97,0,0,285,286,5,114,0,0,286,
        287,5,103,0,0,287,288,5,101,0,0,288,289,5,116,0,0,289,74,1,0,0,0,
        290,291,5,119,0,0,291,292,5,104,0,0,292,293,5,105,0,0,293,294,5,
        108,0,0,294,295,5,101,0,0,295,76,1,0,0,0,296,297,5,105,0,0,297,298,
        5,102,0,0,298,78,1,0,0,0,299,300,5,101,0,0,300,301,5,108,0,0,301,
        302,5,115,0,0,302,303,5,101,0,0,303,80,1,0,0,0,304,305,5,114,0,0,
        305,306,5,101,0,0,306,307,5,116,0,0,307,308,5,117,0,0,308,309,5,
        114,0,0,309,310,5,110,0,0,310,311,5,105,0,0,311,312,5,110,0,0,312,
        313,5,103,0,0,313,82,1,0,0,0,314,315,5,105,0,0,315,316,5,110,0,0,
        316,317,5,108,0,0,317,318,5,105,0,0,318,319,5,110,0,0,319,320,5,
        101,0,0,320,84,1,0,0,0,321,322,5,102,0,0,322,323,5,111,0,0,323,324,
        5,114,0,0,324,325,5,99,0,0,325,326,5,101,0,0,326,327,5,100,0,0,327,
        86,1,0,0,0,328,329,5,111,0,0,329,330,5,112,0,0,330,331,5,116,0,0,
        331,332,5,105,0,0,332,333,5,111,0,0,333,334,5,110,0,0,334,335,5,
        97,0,0,335,336,5,108,0,0,336,88,1,0,0,0,337,338,5,114,0,0,338,339,
        5,101,0,0,339,340,5,116,0,0,340,341,5,117,0,0,341,342,5,114,0,0,
        342,343,5,110,0,0,343,90,1,0,0,0,344,345,5,98,0,0,345,346,5,114,
        0,0,346,347,5,101,0,0,347,348,5,97,0,0,348,349,5,107,0,0,349,92,
        1,0,0,0,350,351,5,99,0,0,351,352,5,111,0,0,352,353,5,110,0,0,353,
        354,5,116,0,0,354,355,5,105,0,0,355,356,5,110,0,0,356,357,5,117,
        0,0,357,358,5,101,0,0,358,94,1,0,0,0,359,360,5,112,0,0,360,361,5,
        114,0,0,361,362,5,111,0,0,362,363,5,99,0,0,363,364,5,101,0,0,364,
        365,5,100,0,0,365,366,5,117,0,0,366,367,5,114,0,0,367,368,5,101,
        0,0,368,96,1,0,0,0,369,370,5,100,0,0,370,371,5,111,0,0,371,98,1,
        0,0,0,372,373,5,98,0,0,373,374,5,101,0,0,374,375,5,103,0,0,375,376,
        5,105,0,0,376,377,5,110,0,0,377,100,1,0,0,0,378,379,5,101,0,0,379,
        380,5,110,0,0,380,381,5,100,0,0,381,102,1,0,0,0,382,383,5,118,0,
        0,383,384,5,97,0,0,384,385,5,114,0,0,385,386,5,105,0,0,386,387,5,
        97,0,0,387,388,5,98,0,0,388,389,5,108,0,0,389,390,5,101,0,0,390,
        104,1,0,0,0,391,392,5,99,0,0,392,393,5,111,0,0,393,394,5,110,0,0,
        394,395,5,115,0,0,395,396,5,116,0,0,396,397,5,97,0,0,397,398,5,110,
        0,0,398,399,5,116,0,0,399,106,1,0,0,0,400,401,5,112,0,0,401,402,
        5,111,0,0,402,403,5,105,0,0,403,404,5,110,0,0,404,405,5,116,0,0,
        405,406,5,101,0,0,406,407,5,114,0,0,407,108,1,0,0,0,408,409,5,97,
        0,0,409,410,5,115,0,0,410,411,5,115,0,0,411,412,5,105,0,0,412,413,
        5,103,0,0,413,414,5,110,0,0,414,415,5,101,0,0,415,416,5,100,0,0,
        416,110,1,0,0,0,417,418,5,97,0,0,418,419,5,115,0,0,419,420,5,115,
        0,0,420,421,5,105,0,0,421,422,5,103,0,0,422,423,5,110,0,0,423,112,
        1,0,0,0,424,425,5,118,0,0,425,426,5,97,0,0,426,427,5,108,0,0,427,
        428,5,117,0,0,428,429,5,101,0,0,429,114,1,0,0,0,430,431,5,105,0,
        0,431,432,5,110,0,0,432,433,5,100,0,0,433,434,5,101,0,0,434,435,
        5,120,0,0,435,116,1,0,0,0,436,437,5,97,0,0,437,438,5,116,0,0,438,
        118,1,0,0,0,439,440,5,110,0,0,440,441,5,111,0,0,441,442,5,116,0,
        0,442,120,1,0,0,0,443,444,5,99,0,0,444,445,5,97,0,0,445,446,5,108,
        0,0,446,447,5,108,0,0,447,122,1,0,0,0,448,452,7,3,0,0,449,451,7,
        4,0,0,450,449,1,0,0,0,451,454,1,0,0,0,452,450,1,0,0,0,452,453,1,
        0,0,0,453,124,1,0,0,0,454,452,1,0,0,0,455,456,7,5,0,0,456,126,1,
        0,0,0,12,0,130,140,148,155,160,166,168,182,207,235,452,1,6,0,0
    ]

class VerboseLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    INLINE_COMMENT = 2
    V_FLOAT = 3
    V_INTEGER = 4
    V_STRING = 5
    P_PERIOD = 6
    P_COMMA = 7
    P_SEMIC = 8
    P_ACCESSOR = 9
    L_PARENTHESIS = 10
    R_PARENTHESIS = 11
    L_BRACKET = 12
    R_BRACKET = 13
    L_BRACE = 14
    R_BRACE = 15
    O_PLUS = 16
    O_MINUS = 17
    O_TIMES = 18
    O_DIVIDE = 19
    O_EQUAL = 20
    O_NOT_EQUAL = 21
    O_LESS = 22
    O_GREATER = 23
    O_LESS_EQUAL = 24
    O_GREATER_EQUAL = 25
    O_BIT_AND = 26
    O_BIT_OR = 27
    O_BIT_XOR = 28
    O_BIT_NOT = 29
    NAMED = 30
    FROM = 31
    WITH = 32
    TO = 33
    FUNCTION = 34
    ARGUMENTS = 35
    TARGETS = 36
    TARGET = 37
    WHILE = 38
    IF = 39
    ELSE = 40
    RETURNING = 41
    INLINE = 42
    FORCED = 43
    OPTIONAL = 44
    RETURN = 45
    BREAK = 46
    CONTINUE = 47
    PROCEDURE = 48
    DO = 49
    BEGIN = 50
    END = 51
    VARIABLE = 52
    CONSTANT = 53
    POINTER = 54
    ASSIGNED = 55
    ASSIGN = 56
    VALUE = 57
    INDEX = 58
    AT = 59
    NOT = 60
    CALL = 61
    V_IDENTIFIER = 62

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "','", "';'", "'('", "')'", "'['", "']'", "'{'", "'}'", 
            "'+'", "'-'", "'*'", "'/'", "'!='", "'<'", "'>'", "'<='", "'>='", 
            "'&'", "'|'", "'^'", "'named'", "'from'", "'with'", "'to'", 
            "'function'", "'arguments'", "'targets'", "'target'", "'while'", 
            "'if'", "'else'", "'returning'", "'inline'", "'forced'", "'optional'", 
            "'return'", "'break'", "'continue'", "'procedure'", "'do'", 
            "'begin'", "'end'", "'variable'", "'constant'", "'pointer'", 
            "'assigned'", "'assign'", "'value'", "'index'", "'at'", "'not'", 
            "'call'" ]

    symbolicNames = [ "<INVALID>",
            "WS", "INLINE_COMMENT", "V_FLOAT", "V_INTEGER", "V_STRING", 
            "P_PERIOD", "P_COMMA", "P_SEMIC", "P_ACCESSOR", "L_PARENTHESIS", 
            "R_PARENTHESIS", "L_BRACKET", "R_BRACKET", "L_BRACE", "R_BRACE", 
            "O_PLUS", "O_MINUS", "O_TIMES", "O_DIVIDE", "O_EQUAL", "O_NOT_EQUAL", 
            "O_LESS", "O_GREATER", "O_LESS_EQUAL", "O_GREATER_EQUAL", "O_BIT_AND", 
            "O_BIT_OR", "O_BIT_XOR", "O_BIT_NOT", "NAMED", "FROM", "WITH", 
            "TO", "FUNCTION", "ARGUMENTS", "TARGETS", "TARGET", "WHILE", 
            "IF", "ELSE", "RETURNING", "INLINE", "FORCED", "OPTIONAL", "RETURN", 
            "BREAK", "CONTINUE", "PROCEDURE", "DO", "BEGIN", "END", "VARIABLE", 
            "CONSTANT", "POINTER", "ASSIGNED", "ASSIGN", "VALUE", "INDEX", 
            "AT", "NOT", "CALL", "V_IDENTIFIER" ]

    ruleNames = [ "WS", "INLINE_COMMENT", "V_FLOAT", "V_INTEGER", "V_STRING", 
                  "P_PERIOD", "P_COMMA", "P_SEMIC", "P_ACCESSOR", "L_PARENTHESIS", 
                  "R_PARENTHESIS", "L_BRACKET", "R_BRACKET", "L_BRACE", 
                  "R_BRACE", "O_PLUS", "O_MINUS", "O_TIMES", "O_DIVIDE", 
                  "O_EQUAL", "O_NOT_EQUAL", "O_LESS", "O_GREATER", "O_LESS_EQUAL", 
                  "O_GREATER_EQUAL", "O_BIT_AND", "O_BIT_OR", "O_BIT_XOR", 
                  "O_BIT_NOT", "NAMED", "FROM", "WITH", "TO", "FUNCTION", 
                  "ARGUMENTS", "TARGETS", "TARGET", "WHILE", "IF", "ELSE", 
                  "RETURNING", "INLINE", "FORCED", "OPTIONAL", "RETURN", 
                  "BREAK", "CONTINUE", "PROCEDURE", "DO", "BEGIN", "END", 
                  "VARIABLE", "CONSTANT", "POINTER", "ASSIGNED", "ASSIGN", 
                  "VALUE", "INDEX", "AT", "NOT", "CALL", "V_IDENTIFIER", 
                  "DIGIT" ]

    grammarFileName = "Verbose.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


