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
// TODO add multiline comment

V_FLOAT: DIGIT* '.' DIGIT+;
V_INTEGER: DIGIT+;
V_INTEGER_HEX: '0x' [0-9a-fA-F_]+;
V_INTEGER_OCT: '0o' [0-7_]+;
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
EXTERNAL: 'external';

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
REFERENCE : 'reference';

ASSIGNED: 'assigned';
ASSIGN: 'assign';
VALUE: 'value';

INDEX: 'index';
AT: 'at';

NOT: 'not';
AND: 'and';
OR: 'or';

CALL: 'call';

SIZE: 'size';
LOCATION: 'location';
MAX: 'max';
MIN: 'min';
CODE: 'code';
OF: 'of';

TYPE: 'type';
IS: 'is';
IN: 'in';

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
function_access
: (V_IDENTIFIER
// Keywords allowed as function names:
| AND | OR
| MAX | MIN
);

inline_part
: OPTIONAL? INLINE
;

qualifiers_part
: (inline_part
    | EXTERNAL
    )* // Might add more in future, then replace ? with *
;

//# Expressions
//## In-expression calls
expr_call
: CALL? func=function_access target=call_target? WITH ARGUMENTS? args=call_arguments P_SEMIC?
| CALL? func=function_access target=call_target
| CALL func=function_access
;

//## Access expressions (variables, dereference, array access, member access)
access_expr
: AT expr=expression P_SEMIC? # Dereference
| source=access_expr P_ACCESSOR member=V_IDENTIFIER # MemberAccess // Might want to access type properties here? Though, by name should be enough for now
| array=access_expr AT index=expression P_SEMIC? # ArrayAccess
| name=V_IDENTIFIER # Variable
;

//## Other expressions
of_expr
: variant=SIZE OF type_expr
| variant=(MAX|MIN) OF V_IDENTIFIER // Of a fundamental type.
| variant=LOCATION OF access_expr
| variant=CODE OF function_access // Needs a distinct construction from LOCATION OF, as functions have a separate namespace.
;

// TODO - cast expressions

//## Generic expressions
expression
: (V_INTEGER|V_INTEGER_HEX|V_INTEGER_OCT|V_INTEGER_BIN) # Int
| V_FLOAT # Float
| V_STRING # String
| of_expr # Molec
// Parethesis
| L_PARENTHESIS expression R_PARENTHESIS # Molec
| L_BRACKET expression R_BRACKET # Molec
| L_BRACE expression R_BRACE # Molec
// Unary operators
| operator=O_MINUS expression # UnaryOp
| operator=O_BIT_NOT expression # UnaryOp
| operator=NOT expression # UnaryOp
// Binary operators
| expression operator=(O_TIMES|O_DIVIDE) expression # BinaryOp
| expression operator=(O_PLUS|O_MINUS) expression # BinaryOp
| expression operator=(O_BIT_AND|O_BIT_XOR|O_BIT_OR) expression # BinaryOp
// Expressions that may need termination
| expr_call # Molec
| access_expr # Molec
// Comparison operators
| expression operator=(O_EQUAL|O_NOT_EQUAL|O_LESS|O_GREATER|O_LESS_EQUAL|O_GREATER_EQUAL) expression # BinaryOp
| expression operator=AND expression # BinaryOp
| expression operator=OR expression # BinaryOp
;


//# Typing
type_expr
: mutability_node
| simple_type_expr
;

mutability_node: mut=(CONSTANT | VARIABLE) expr=simple_type_expr;

simple_type_expr
: name=V_IDENTIFIER
| pointer_node
;

pointer_node: ptr_kind=(POINTER|REFERENCE) TO expr=type_expr;


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
: ASSIGN target=access_expr VALUE value=expression
;

//## Call statements
/** Standard arguments */
call_argument
: expression
;

call_arguments
: (args=call_argument P_COMMA)* args=call_argument P_COMMA?
;
// TODO refactor the expression call to use the above rules

/** These argments may be implicitly passed by pointer/reference. */
call_target
: access_expr
;

call_statement
: func=function_access target=call_target? WITH ARGUMENTS? args=call_arguments
| func=function_access target=call_target
| CALL? func=function_access
;

//## Variable declaration
var_decl
: qualifiers=qualifiers_part type=type_expr name=name_decl_part (ASSIGNED value=expression)?
;

//## Control flow statements
// Optional labels on blocks are a replacement for goto
// Useful for breaking out of nested loops, etc.
break_statement
: BREAK label=V_IDENTIFIER?
;

continue_statement
: CONTINUE label=V_IDENTIFIER?
;

return_statement
: RETURN expr=expression?
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
: (PROCEDURE|DO) label=name_decl_part? block_item* (END)
// The do keyword could be made optional in some blocks?
;

if
: IF expr=expression bl=block (ELSE (elbl=block|elifbl=if))?
;

while
: WHILE expr=expression bl=block
;

do_while
: bl=block WHILE expr=expression P_PERIOD
;

//# Declarations
//## Function
return_type_decl_part
: RETURNING type=type_expr
;

name_decl_part
: NAMED name=V_IDENTIFIER
;

function_name_decl_part
: NAMED name=V_IDENTIFIER
| NAMED name=V_IDENTIFIER? IN extern_type=(V_IDENTIFIER|V_STRING) extern_name=V_IDENTIFIER
;

target_decl_part
: (TARGET|TARGETS) var_decl (P_COMMA var_decl)* P_COMMA? END?
;

arguments_decl_part
: ARGUMENTS var_decl (P_COMMA var_decl)* P_COMMA? END?
;

function
: qualifiers=qualifiers_part
  FUNCTION
  type=return_type_decl_part?
  names=function_name_decl_part?
  target=target_decl_part?
  args=arguments_decl_part?
  (bl=block|P_PERIOD)

| qualifiers=qualifiers_part
  FUNCTION
  names=function_name_decl_part?
  type=return_type_decl_part?
  target=target_decl_part?
  args=arguments_decl_part?
  (bl=block|P_PERIOD)
;

//## Type
type_decl
: TYPE NAMED? name=V_IDENTIFIER IS type=type_expr
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
: target_decl_part # Target_section_header
// More in the future, like generics, public etc.
;

section
: headers=section_header* BEGIN items=module_item* END // TODO - no, labels don't work like this
;
