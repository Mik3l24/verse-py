from typing import override

from antlr4 import *
from antlr4.Token import CommonToken

from parser.VerboseVisitor import VerboseVisitor
from parser.VerboseParser import VerboseParser as Par
from parser.VerboseLexer import VerboseLexer as Lex

from vast import *
from vast.base import Location, VASTNode


class Transformer(VerboseVisitor):

    @override
    def visitModule(self, ctx:Par.ModuleContext):
        return VModule(
            items=[self.visit(child) for child in ctx.children if isinstance(child, Par.Module_itemContext)],
            name=None,
            location=Location(ctx.start.line, ctx.start.column),
        )


    @override
    def visitFunction_access(self, ctx:Par.Function_accessContext):
        # This simple implementation is fine, but only until we implement function namespaces
        return VNameAccess(name=ctx.children[0].symbol.text)


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
            elif isinstance(child, CommonToken):
                qualifier = {
                    # Lex.ENTRYPOINT: FuncQualifiers.ENTRYPOINT,
                    # TODO - add more qualifiers
                }.get(child.type, None)
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
        return VUnaryOp(expr=self.visit(ctx.expr), op=op, location=Location(ctx.start.line, ctx.start.column))


    @override
    def visitMolec(self, ctx:Par.MolecContext):
        # Purely grammatical node, leaving at default is fine
        return self.visitChildren(ctx)


    @override
    def visitString(self, ctx:Par.StringContext):
        # TODO - implement string parsing - to handle escape sequences
        return VLiteral(ctx.children[0].symbol.text, VFundamentalType("String", Constness.CONSTANT),
                        location=Location(ctx.start.line, ctx.start.column))


    @override
    def visitInt(self, ctx:Par.IntContext):
        text: str = ctx.children[0].symbol.text
        # Do int parsing
        # TODO implement something better, that can handle more int literal types
        num = int(text)
        return VLiteral(num, VFundamentalType("Int", Constness.CONSTANT),
                        location=Location(ctx.start.line, ctx.start.column))


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
                         location=Location(ctx.start.line, ctx.start.column))


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
            return VNamedType(ctx.name.text, location=Location(ctx.start.line, ctx.start.column))
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
                           location=Location(ctx.start.line, ctx.start.column))


    @override
    def visitCall_argument(self, ctx:Par.Call_argumentContext):
        # Another grammatical rule
        return self.visitChildren(ctx)


    @override
    def visitCall_arguments(self, ctx:Par.Call_argumentsContext):
        # Should return a list - but need to ignore commas in children?
        # Unfortunately, using labels does not work - it doesn't produce a list.
        # Ok, detecting if it's a token should work, as a single arg should be wrapped in a rule
        return [self.visit(child) for child in ctx.children if not isinstance(child, CommonToken)]


    @override
    def visitCall_target(self, ctx:Par.Call_targetContext):
        # In the future - may be a longer list. However, atm only one target is allowed
        return [self.visit(ctx.children[0])]


    @override
    def visitCall_statement(self, ctx:Par.Call_statementContext):
        func = self.visit(ctx.func)
        targets = self.visit(ctx.target) if ctx.target else None # Should return a list
        args = self.visit(ctx.args) if ctx.args else None
        return VCall(func=func, targets=targets, args=args,
                     location=Location(ctx.start.line, ctx.start.column),)


    @override
    def visitVar_decl(self, ctx:Par.Var_declContext):
        return VVariable(
            name=self.visit(ctx.name),
            type=self.visit(ctx.type_),
            qualifiers=self.visit(ctx.qualifiers),
            init_value=self.visit(ctx.value) if ctx.value else None,

            location=Location(ctx.start.line, ctx.start.column),
        )


    @override
    def visitBreak_statement(self, ctx:Par.Break_statementContext):
        return VBreak(VBreak.Kind.BREAK, ctx.label.text if ctx.label is not None else "",
                      location=Location(ctx.start.line, ctx.start.column),)


    @override
    def visitContinue_statement(self, ctx:Par.Continue_statementContext):
        return VBreak(VBreak.Kind.CONTINUE, ctx.label.text if ctx.label is not None else "",
                      location=Location(ctx.start.line, ctx.start.column),)


    @override
    def visitReturn_statement(self, ctx:Par.Return_statementContext):
        return VReturn([self.visit(ctx.expr)], # atm, only one return value supported in grammar.
                       location=Location(ctx.start.line, ctx.start.column),)


    @override
    def visitBlock_item(self, ctx:Par.Block_itemContext):
        # A yet another grammatical rule
        return self.visitChildren(ctx)


    @override
    def visitBlock(self, ctx:Par.BlockContext):
        return VBlock(
            label=ctx.label,
            body=[
                # Quick way to only add the statement parts of the block
                # Though, how efficient is list comprehension?
                self.visit(child) for child in ctx.children if isinstance(child, Par.Block_itemContext)
            ],
            location=Location(ctx.start.line, ctx.start.column),
        )


    @override
    def visitIf(self, ctx:Par.IfContext):
        return VIf(cond=self.visit(ctx.expr), block=self.visit(ctx.bl), else_block=self.visit(ctx.elbl or ctx.elifbl),
                   location=Location(ctx.start.line, ctx.start.column),)


    @override
    def visitWhile(self, ctx:Par.WhileContext):
        return VWhile(cond=self.visit(ctx.expr), block=self.visit(ctx.bl), is_do_while=False,
                      location=Location(ctx.start.line, ctx.start.column),)


    @override
    def visitDo_while(self, ctx:Par.Do_whileContext):
        return VWhile(cond=self.visit(ctx.expr), block=self.visit(ctx.bl), is_do_while=True,
                      location=Location(ctx.start.line, ctx.start.column),)


    @override
    def visitReturn_type_decl_part(self, ctx:Par.Return_type_decl_partContext):
        return self.visitChildren(ctx)


    @override
    def visitName_decl_part(self, ctx:Par.Name_decl_partContext):
        return self.visitChildren(ctx)


    @override
    def visitTarget_decl_part(self, ctx:Par.Target_decl_partContext):
        return [self.visit(child) for child in ctx.children if isinstance(child, Par.Var_declContext)]


    @override
    def visitArguments_decl_part(self, ctx:Par.Arguments_decl_partContext):
        return [self.visit(child) for child in ctx.children if isinstance(child, Par.Var_declContext)]


    @override
    def visitFunction(self, ctx:Par.FunctionContext):
        # Might need to be refactored to allow a freer function signature
        return VFunction(
            qualifiers=self.visit(ctx.qualifiers),
            return_type=self.visit(ctx.type_) if ctx.type_ else None,
            name=self.visit(ctx.name) if ctx.name else None,
            c_name=None,
            targets=self.visit(ctx.target) if ctx.target else None,
            args=self.visit(ctx.args) if ctx.args else None,
            body=self.visit(ctx.bl) if ctx.bl else None,

            location=Location(ctx.start.line, ctx.start.column),
        )


    @override
    def visitType_decl(self, ctx:Par.Type_declContext):
        return VTypeDeclaration(
            name=ctx.name.text,
            type=self.visit(ctx.type_),

            location=Location(ctx.start.line, ctx.start.column),
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

