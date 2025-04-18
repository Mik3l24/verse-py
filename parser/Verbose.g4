/** ANTLR4 grammar for the Verbose programming language.

//STYLE GUIDE (for multiline rules)
rule_name
: pattern1
| pattern2
| long
  pattern
-> function_name
;

*/
grammar Verbose;

options {
  language = Python3;
}


// Lexer rules
WS: [ \t\r\n]+ -> skip;
INLINE_COMMENT: '//' ~[\r\n]* -> skip;

V_FLOAT: DIGIT* '.' DIGIT+;
V_INTEGER: DIGIT+;
V_INTEGER_HEX: '0x' [0-9a-fA-F]+;
V_INTEGER_BIN: '0b' [01_]+;
V_STRING: '"' ( ~["\\] | '\\' . )* '"'; // FUTURE - state based strings?

P_PERIOD: '.';
P_COMMA: ',';
P_SEMIC: ';';
P_ACCESSOR: '\'' | '\'s';

L_PARENTHESIS: '(';
R_PARENTHESIS: ')';
L_BRACKET: '[';
R_BRACKET: ']';
L_BRACE: '{';
R_BRACE: '}';

// Operators
O_PLUS: '+';
O_MINUS: '-';
O_TIMES: '*';
O_DIVIDE: '/';

O_EQUAL: '=' | '==';
O_NOT_EQUAL: '!=';
O_LESS: '<';
O_GREATER: '>';
O_LESS_EQUAL: '<=';
O_GREATER_EQUAL: '>=';

O_BIT_AND: '&';
O_BIT_OR: '|';
O_BIT_XOR: '^';
O_BIT_NOT: 'inverted' | '~';


// Keywords
NAMED: 'named';
FROM: 'from';
WITH: 'with';
TO: 'to';

FUNCTION: 'function';
ARGUMENTS: 'arguments';
TARGETS: 'targets';
TARGET: 'target';
WHILE: 'while';
IF: 'if';
ELSE: 'else';
RETURNING: 'returning';

INLINE: 'inline';
FORCED: 'forced';
OPTIONAL: 'optional';

RETURN: 'return';
BREAK: 'break';
CONTINUE: 'continue';

PROCEDURE: 'procedure';
DO: 'do';
BEGIN: 'begin';
END: 'end';

VARIABLE: 'variable';
CONSTANT: 'constant';
POINTER: 'pointer';

ASSIGNED: 'assigned';
ASSIGN: 'assign';
VALUE: 'value';

INDEX: 'index';
AT: 'at';

NOT: 'not';

CALL: 'call';

SIZEOF: 'sizeof' | 'sizeOf';

TYPE: 'type';
IS: 'is';

V_IDENTIFIER: [a-zA-Z_] [a-zA-Z0-9_]*;

// FUTURE - Compiler instructions
// will probably need state-based lexer rules
// since they'll be a sequence of arbitrary space-separated words
// ex. `compiler arg1 2 arg3.`


// Helper rules
fragment DIGIT: [0-9];


// Parser rules
// Starting rule
module: module_item* EOF;

//# Common
function_access: V_IDENTIFIER;

inline_part
: OPTIONAL? INLINE
|
;

//# Expressions
//## In-expression calls
expr_call
: CALL function_access
| CALL? function_access WITH ARGUMENTS? call_arguments P_SEMIC?
;

//## Access expressions (variables, dereference, array access, member access)
access_expr
: AT expression P_SEMIC? # Dereference
| access_expr P_ACCESSOR V_IDENTIFIER # MemberAccess
| access_expr AT expression P_SEMIC? # ArrayAccess
| V_IDENTIFIER # Variable
;

//## Generic expressions
sizeof_expr
: SIZEOF type_expr
;

expression
: (V_INTEGER|V_INTEGER_HEX|V_INTEGER_BIN) # Int
| V_FLOAT # Float
| V_STRING # String
| sizeof_expr # Sizeof
// Parethesis
| L_PARENTHESIS expression R_PARENTHESIS # Molec
| L_BRACKET expression R_BRACKET # Molec
| L_BRACE expression R_BRACE # Molec
// Unary operators
| O_MINUS expression # UnaryOp
| O_BIT_NOT expression # UnaryOp
| NOT expression # UnaryOp
// Binary operators
| expression operator=(O_TIMES|O_DIVIDE) expression # BinaryOp
| expression operator=(O_PLUS|O_MINUS) expression # BinaryOp
| expression operator=(O_BIT_AND|O_BIT_XOR|O_BIT_OR) expression # BinaryOp
// Expressions that may need termination
| expr_call # Call
| access_expr # Access
// Comparison operators
| expression operator=(O_EQUAL|O_NOT_EQUAL|O_LESS|O_GREATER|O_LESS_EQUAL|O_GREATER_EQUAL) expression # BinaryOp
;


//# Typing
type_expr
: mutability_node
| simple_type_expr
;

mutability_node: mut=(CONSTANT | VARIABLE) simple_type_expr;

simple_type_expr
: V_IDENTIFIER
| pointer_node
;

pointer_node: POINTER TO type_expr;


//# Statements
statement
: (call_statement
| var_decl
| assignment
| break_statement
| continue_statement
| return_statement
)? P_PERIOD
;



assignment
: ASSIGN access_expr VALUE expression
;

//## Call statements
/** Standard arguments */
call_argument
: expression
;

call_arguments
: (call_argument P_COMMA)* call_argument P_COMMA?
;
// TODO refactor the expression call to use the above rules

/** These argments may be implicitly passed by pointer/reference. */
call_target
: access_expr
;

call_statement
: function_access call_target? WITH ARGUMENTS? call_arguments
| function_access call_target
| CALL? function_access
;

//## Variable declaration
var_decl
: inline_part type_expr name_decl_part (ASSIGNED expression)?
;

//## Control flow statements
// Optional labels on blocks are a replacement for goto
// Useful for breaking out of nested loops, etc.
break_statement
: BREAK V_IDENTIFIER? 
;

continue_statement
: CONTINUE V_IDENTIFIER? 
;

return_statement
: RETURN expression?
;


//# Blocks
block_item
: statement
| block
| if
| while
| do_while
// Allow function declarations in blocks?
;

block
: (PROCEDURE|DO) name_decl_part? block_item* (END)
// The do keyword could be made optional in some blocks?
;

if
: IF expression block (ELSE (block|if))?
;

while
: WHILE expression block
;

do_while
: block WHILE expression P_PERIOD
;

//# Declarations
//## Function
return_type_decl_part
: RETURNING type_expr
;

name_decl_part
: NAMED V_IDENTIFIER
;

target_decl_part
: (TARGET|TARGETS) var_decl (P_COMMA type_expr)* P_COMMA? END?
;

arguments_decl_part
: ARGUMENTS var_decl (P_COMMA type_expr)* P_COMMA? END?
;

function
: inline_part
  FUNCTION
  return_type_decl_part?
  name_decl_part?
  target_decl_part?
  arguments_decl_part?
  block
;

//## Type
type_decl
: TYPE NAMED? V_IDENTIFIER IS type_expr
;

//## Module
module_item
: section
| function
| var_decl P_PERIOD
// Future
| type_decl P_PERIOD
//| compiler_instruction
//| include_decl
;

section_header
: target_decl_part # Target
// More in the future, like generics, public etc.
;

section
: section_header* BEGIN module_item* END
;
