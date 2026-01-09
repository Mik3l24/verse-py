from typing import override

from antlr4 import *
from antlr4.Token import CommonToken

from parser.VerboseVisitor import VerboseVisitor
from parser.VerboseParser import VerboseParser as Par
from parser.VerboseLexer import VerboseLexer as Lex

from vast import *
from vast.base import Location, VASTNode

from .meta import LOCATION
from . import intrinsics

import re
import codecs

ESCAPE_SEQUENCE_RE = re.compile(r"""
    ( \\U[0-9a-fA-F]{8}
    | \\u[0-9a-fA-F]{4}
    | \\x[0-9a-fA-F]{2}
    | \\[0-7]{1,3}
    | \\N\{[^}]+}
    | \\[\\'"abfnrtv]
    )""", re.UNICODE | re.VERBOSE)

# Thanks, https://stackoverflow.com/a/24519338
def decode_escapes(text: str) -> str:
    def replace_escape(match):
        try:
            return codecs.decode(match.group(0), "unicode_escape")
        except UnicodeDecodeError:
            return match.group(0)
    return ESCAPE_SEQUENCE_RE.sub(replace_escape, text)

def clean_string_literal(text: str) -> str:
    text = text.strip("\"")
    text = decode_escapes(text)
    return text


class Transformer(VerboseVisitor):

    @override
    def visitModule(self, ctx:Par.ModuleContext):
        return VModule(
            items=[self.visit(child) for child in ctx.children if isinstance(child, Par.Module_itemContext)],
            name=None,
            meta={LOCATION: Location(ctx.start.line, ctx.start.column)},
        )


    @override
    def visitFunction_access(self, ctx:Par.Function_accessContext):
        # This simple implementation is fine, but only until we implement function namespaces
        return VNameAccess(name=ctx.children[0].symbol.text, meta={LOCATION: Location(ctx.start.line, ctx.start.column)})


    @override
    def visitInline_part(self, ctx:Par.Inline_partContext):
        if ctx.children[0].symbol.type == Lex.OPTIONAL:
            raise NotImplementedError("Optional inline not implemented yet")
        return Qualifiers.INLINE


    @override
    def visitQualifiers_part(self, ctx:Par.Qualifiers_partContext):
        qualifiers = Qualifiers.NONE
        if ctx.children is None:
            return qualifiers
        for child in ctx.children:
            qualifier = None
            if isinstance(child, Par.Inline_partContext):
                qualifier = self.visit(child)
            elif child.symbol and isinstance(child.symbol, CommonToken):
                qualifier = {
                    Lex.EXTERNAL: Qualifiers.EXTERNAL,
                    # Lex.ENTRYPOINT: FuncQualifiers.ENTRYPOINT,
                    # TODO - add more qualifiers
                }.get(child.symbol.type, None)
            if qualifier is None:
                raise ValueError(f"Unknown qualifier: {child}")
            qualifiers |= qualifier
        return qualifiers


    @override
    def visitExpr_call(self, ctx:Par.Expr_callContext):
        raise NotImplementedError("Expression function call not implemented yet")
        return self.visitChildren(ctx)


    @override
    def visitArrayAccess(self, ctx:Par.ArrayAccessContext):
        return VArrayAccess(self.visit(ctx.array), self.visit(ctx.index))


    @override
    def visitVariable(self, ctx:Par.VariableContext):
        return VNameAccess(ctx.name.text)


    @override
    def visitMemberAccess(self, ctx:Par.MemberAccessContext):
        return VMemberAccess(self.visit(ctx.source), ctx.member.text)


    @override
    def visitDereference(self, ctx:Par.DereferenceContext):
        return VDeref(self.visit(ctx.expr))


    @override
    def visitOf_expr(self, ctx:Par.Of_exprContext):
        match ctx.variant.type:
            case Lex.SIZE:
                raise NotImplementedError("Sizeof not implemented yet")
            case Lex.LOCATION:
                raise NotImplementedError("Variable's pointer getter not implemented yet")
            case Lex.CODE:
                raise NotImplementedError("Function's pointer getter not implemented yet")
            case Lex.MIN:
                raise NotImplementedError("Min not implemented yet")
            case Lex.MAX:
                raise NotImplementedError("Max not implemented yet")
        return self.visitChildren(ctx)


    @override
    def visitFloat(self, ctx:Par.FloatContext):
        raise NotImplementedError("Float literal not implemented yet")
        return self.visitChildren(ctx)


    @override
    def visitUnaryOp(self, ctx:Par.UnaryOpContext):
        # Enum re-mapping
        op: VUnaryOp.Op = {
            Lex.O_MINUS: VUnaryOp.Op.NEG,
            Lex.O_BIT_NOT: VUnaryOp.Op.BITNOT,
            Lex.NOT: VUnaryOp.Op.NOT,
        }.get(ctx.operator.type, None)
        return VUnaryOp(expr=self.visit(ctx.expr), op=op, meta={LOCATION: Location(ctx.start.line, ctx.start.column)})


    @override
    def visitMolec(self, ctx:Par.MolecContext):
        # Purely grammatical node, leaving at default is fine
        return self.visitChildren(ctx)


    @override
    def visitString(self, ctx:Par.StringContext):
        text: str = ctx.children[0].symbol.text
        text = clean_string_literal(text)
        return VStringLiteral(value=text, type=intrinsics.util_types["CString"],
                        meta={LOCATION: Location(ctx.start.line, ctx.start.column)})


    @override
    def visitInt(self, ctx:Par.IntContext):
        text: str = ctx.children[0].symbol.text
        # Do int parsing
        # TODO implement something better, that can handle more int literal types
        num = int(text)
        return VIntLiteral(value=num, type=intrinsics.fundamental_types["Int32"],
                        meta={LOCATION: Location(ctx.start.line, ctx.start.column)})


    @override
    def visitBinaryOp(self, ctx:Par.BinaryOpContext):
        # Enum re-mapping
        operator: VBinaryOp.Op = {
            # Arithmetic
            Lex.O_PLUS: VBinaryOp.Op.ADD,
            Lex.O_MINUS: VBinaryOp.Op.SUB,
            Lex.O_TIMES: VBinaryOp.Op.TIMES,
            Lex.O_DIVIDE: VBinaryOp.Op.DIV,
            # Bitwise
            Lex.O_BIT_AND: VBinaryOp.Op.BITAND,
            Lex.O_BIT_OR: VBinaryOp.Op.BITOR,
            Lex.O_BIT_XOR: VBinaryOp.Op.BITXOR,
            # Comparison
            Lex.O_EQUAL: VBinaryOp.Op.EQUAL,
            Lex.O_NOT_EQUAL: VBinaryOp.Op.NOTEQ,
            Lex.O_LESS: VBinaryOp.Op.LESS,
            Lex.O_GREATER: VBinaryOp.Op.GREATER,
            Lex.O_LESS_EQUAL: VBinaryOp.Op.LESSEQ,
            Lex.O_GREATER_EQUAL: VBinaryOp.Op.GREATEREQ,
            # Logic
            Lex.AND: VBinaryOp.Op.AND,
            Lex.OR: VBinaryOp.Op.OR,
        }.get(ctx.operator.type, None)
        if operator is None:
            # This error should only happen when an operator is defined in the grammar but implemented here
            raise ValueError(f"Unknown operator: {ctx.operator.text}")

        return VBinaryOp(self.visit(ctx.children[0]), self.visit(ctx.children[2]), operator,
                         meta={LOCATION: Location(ctx.start.line, ctx.start.column)})


    @override
    def visitType_expr(self, ctx:Par.Type_exprContext):
        # Grammatical rule, default implementation is fine
        return self.visitChildren(ctx)


    @override
    def visitMutability_node(self, ctx:Par.Mutability_nodeContext):
        mut: Constness = {
            Lex.CONSTANT: Constness.CONSTANT,
            Lex.VARIABLE: Constness.VARIABLE,
        }.get(ctx.mut.type, None)
        if mut is None:
            raise ValueError(f"Unknown variable type: {ctx.mut.text}")
        type: VType = self.visit(ctx.expr)
        type.constness = mut
        return type


    @override
    def visitSimple_type_expr(self, ctx:Par.Simple_type_exprContext):
        if ctx.name is not None: # We must have named type
            return VNamedType(ctx.name.text, meta={LOCATION: Location(ctx.start.line, ctx.start.column)})
        return self.visitChildren(ctx)


    @override
    def visitPointer_node(self, ctx:Par.Pointer_nodeContext):
        kind: VPointerType.Kind = {
            Lex.POINTER: VPointerType.Kind.POINTER,
            Lex.REFERENCE: VPointerType.Kind.REFERENCE,
        }.get(ctx.ptr_kind.type, None)
        return VPointerType(self.visit(ctx.expr), kind)


    @override
    def visitStatement(self, ctx:Par.StatementContext):
        # Again, a grammatical rule, don't need to do anything special
        return self.visit(ctx.children[0])


    @override
    def visitAssignment(self, ctx:Par.AssignmentContext):
        return VAssignment(self.visit(ctx.target), self.visit(ctx.value),
                           meta={LOCATION: Location(ctx.start.line, ctx.start.column)})


    @override
    def visitCall_argument(self, ctx:Par.Call_argumentContext):
        # Another grammatical rule
        return self.visitChildren(ctx)


    @override
    def visitCall_arguments(self, ctx:Par.Call_argumentsContext):
        # Should return a list - but need to ignore commas in children?
        # Unfortunately, using labels does not work - it doesn't produce a list.
        # Ok, detecting if it's a token should work, as a single arg should be wrapped in a rule
        return [self.visit(child) for child in ctx.children if not isinstance(child, TerminalNode)]


    @override
    def visitCall_target(self, ctx:Par.Call_targetContext):
        # In the future - may be a longer list. However, atm only one target is allowed
        return [self.visit(ctx.children[0])]


    @override
    def visitCall_statement(self, ctx:Par.Call_statementContext):
        func = self.visit(ctx.func)
        targets = self.visit(ctx.target) if ctx.target else [] # Should return a list
        args = self.visit(ctx.args) if ctx.args else []
        return VCall(func=func, targets=targets, args=args,
                     meta={LOCATION: Location(ctx.start.line, ctx.start.column)},)


    @override
    def visitVar_decl(self, ctx:Par.Var_declContext):
        return VVariable(
            name=self.visit(ctx.name),
            type=self.visit(ctx.type_),
            qualifiers=self.visit(ctx.qualifiers),
            init_value=self.visit(ctx.value) if ctx.value else None,

            meta={LOCATION: Location(ctx.start.line, ctx.start.column)},
        )


    @override
    def visitBreak_statement(self, ctx:Par.Break_statementContext):
        return VBreak(VBreak.Kind.BREAK, ctx.label.text if ctx.label is not None else "",
                      meta={LOCATION: Location(ctx.start.line, ctx.start.column)},)


    @override
    def visitContinue_statement(self, ctx:Par.Continue_statementContext):
        return VBreak(VBreak.Kind.CONTINUE, ctx.label.text if ctx.label is not None else "",
                      meta={LOCATION: Location(ctx.start.line, ctx.start.column)},)


    @override
    def visitReturn_statement(self, ctx:Par.Return_statementContext):
        return VReturn([self.visit(ctx.expr)], # atm, only one return value supported in grammar.
                       meta={LOCATION: Location(ctx.start.line, ctx.start.column)},)


    @override
    def visitBlock_item(self, ctx:Par.Block_itemContext):
        # A yet another grammatical rule
        return self.visit(ctx.children[0])


    @override
    def visitBlock(self, ctx:Par.BlockContext):
        return VBlock(
            label=ctx.label,
            body=[
                # Quick way to only add the statement parts of the block
                # Though, how efficient is list comprehension?
                self.visit(child) for child in ctx.children if isinstance(child, Par.Block_itemContext)
            ],
            meta={LOCATION: Location(ctx.start.line, ctx.start.column)},
        )


    @override
    def visitIf(self, ctx:Par.IfContext):
        return VIf(cond=self.visit(ctx.expr), block=self.visit(ctx.bl), else_block=self.visit(ctx.elbl or ctx.elifbl),
                   meta={LOCATION: Location(ctx.start.line, ctx.start.column)},)


    @override
    def visitWhile(self, ctx:Par.WhileContext):
        return VWhile(cond=self.visit(ctx.expr), block=self.visit(ctx.bl), is_do_while=False,
                      meta={LOCATION: Location(ctx.start.line, ctx.start.column)},)


    @override
    def visitDo_while(self, ctx:Par.Do_whileContext):
        return VWhile(cond=self.visit(ctx.expr), block=self.visit(ctx.bl), is_do_while=True,
                      meta={LOCATION: Location(ctx.start.line, ctx.start.column)},)


    @override
    def visitReturn_type_decl_part(self, ctx:Par.Return_type_decl_partContext):
        return self.visitChildren(ctx)


    @override
    def visitName_decl_part(self, ctx:Par.Name_decl_partContext):
        return ctx.children[1].symbol.text

    @override
    def visitFunction_name_decl_part(self, ctx:Par.Function_name_decl_partContext):
        name = ctx.name.text if ctx.name else None
        if ctx.extern_type:
            extern_type_token: CommonToken = ctx.extern_type
            extern_kind = extern_type_token.text
            if extern_type_token.type == Lex.V_STRING:
                extern_kind = clean_string_literal(extern_kind)
            extern_kind = VFunction.ExternKind(extern_kind)
        else:
            extern_kind = VFunction.ExternKind.NOT_EXTERN
        extern_name = ctx.extern_name.text if ctx.extern_name else None
        return name, extern_kind, extern_name

    @override
    def visitTarget_decl_part(self, ctx:Par.Target_decl_partContext):
        return [self.visit(child) for child in ctx.children if isinstance(child, Par.Var_declContext)]


    @override
    def visitArguments_decl_part(self, ctx:Par.Arguments_decl_partContext):
        return [self.visit(child) for child in ctx.children if isinstance(child, Par.Var_declContext)]


    @override
    def visitFunction(self, ctx:Par.FunctionContext):
        # Might need to be refactored to allow a freer function signature
        name, extern_kind, extern_name = self.visit(ctx.names)
        if name is None:
            name = extern_name
            # If extern_name is None, it will be set to None in VFunction
            # But it's ok for anonymous functions.
        return VFunction(
            qualifiers=self.visit(ctx.qualifiers),
            return_type=self.visit(ctx.type_) if ctx.type_ else None,
            name=name,
            extern_kind=extern_kind,
            extern_name=extern_name,
            targets=self.visit(ctx.target) if ctx.target else None,
            args=self.visit(ctx.args) if ctx.args else None,
            body=self.visit(ctx.bl) if ctx.bl else None,

            meta={LOCATION: Location(ctx.start.line, ctx.start.column)},
        )


    @override
    def visitType_decl(self, ctx:Par.Type_declContext):
        return VTypeDeclaration(
            name=ctx.name.text,
            type=self.visit(ctx.type_),

            meta={LOCATION: Location(ctx.start.line, ctx.start.column)},
        )


    @override
    def visitModule_item(self, ctx:Par.Module_itemContext):
        # So many organizational grammatical rules...
        return self.visit(ctx.children[0])


    @override
    def visitTarget_section_header(self, ctx:Par.Target_section_headerContext):
        # TODO rename to TargetSectionHeader
        raise NotImplementedError("Target section not implemented yet")
        return self.visitChildren(ctx)


    @override
    def visitSection(self, ctx:Par.SectionContext):
        raise NotImplementedError("Section not implemented yet")
        # Might be a bit more difficult to parse out the headers and items from how the rule is written atm
        return self.visitChildren(ctx)

