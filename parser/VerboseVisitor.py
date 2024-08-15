# Generated from parser/Verbose.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .VerboseParser import VerboseParser
else:
    from VerboseParser import VerboseParser

# This class defines a complete generic visitor for a parse tree produced by VerboseParser.

class VerboseVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by VerboseParser#function_access.
    def visitFunction_access(self, ctx:VerboseParser.Function_accessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#inline_part.
    def visitInline_part(self, ctx:VerboseParser.Inline_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#expr_call.
    def visitExpr_call(self, ctx:VerboseParser.Expr_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#expr_call_nonterm.
    def visitExpr_call_nonterm(self, ctx:VerboseParser.Expr_call_nontermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#Variable.
    def visitVariable(self, ctx:VerboseParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#MemberAccess.
    def visitMemberAccess(self, ctx:VerboseParser.MemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#Nonterm.
    def visitNonterm(self, ctx:VerboseParser.NontermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#Dereference.
    def visitDereference(self, ctx:VerboseParser.DereferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#ArrayAccess.
    def visitArrayAccess(self, ctx:VerboseParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#UnaryOp.
    def visitUnaryOp(self, ctx:VerboseParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#Molec.
    def visitMolec(self, ctx:VerboseParser.MolecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#BinaryOp.
    def visitBinaryOp(self, ctx:VerboseParser.BinaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#type_expr.
    def visitType_expr(self, ctx:VerboseParser.Type_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#mutability_node.
    def visitMutability_node(self, ctx:VerboseParser.Mutability_nodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#simple_type_expr.
    def visitSimple_type_expr(self, ctx:VerboseParser.Simple_type_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#pointer_node.
    def visitPointer_node(self, ctx:VerboseParser.Pointer_nodeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#statement.
    def visitStatement(self, ctx:VerboseParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#assignment.
    def visitAssignment(self, ctx:VerboseParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#call_argument.
    def visitCall_argument(self, ctx:VerboseParser.Call_argumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#call_arguments.
    def visitCall_arguments(self, ctx:VerboseParser.Call_argumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#call_target.
    def visitCall_target(self, ctx:VerboseParser.Call_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#call_statement.
    def visitCall_statement(self, ctx:VerboseParser.Call_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#var_decl.
    def visitVar_decl(self, ctx:VerboseParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#break_statement.
    def visitBreak_statement(self, ctx:VerboseParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#continue_statement.
    def visitContinue_statement(self, ctx:VerboseParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#return_statement.
    def visitReturn_statement(self, ctx:VerboseParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#block_item.
    def visitBlock_item(self, ctx:VerboseParser.Block_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#block.
    def visitBlock(self, ctx:VerboseParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#if.
    def visitIf(self, ctx:VerboseParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#while.
    def visitWhile(self, ctx:VerboseParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#do_while.
    def visitDo_while(self, ctx:VerboseParser.Do_whileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#return_type_decl_part.
    def visitReturn_type_decl_part(self, ctx:VerboseParser.Return_type_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#name_decl_part.
    def visitName_decl_part(self, ctx:VerboseParser.Name_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#arguments_decl_part.
    def visitArguments_decl_part(self, ctx:VerboseParser.Arguments_decl_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#function.
    def visitFunction(self, ctx:VerboseParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#module_item.
    def visitModule_item(self, ctx:VerboseParser.Module_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by VerboseParser#module.
    def visitModule(self, ctx:VerboseParser.ModuleContext):
        return self.visitChildren(ctx)



del VerboseParser