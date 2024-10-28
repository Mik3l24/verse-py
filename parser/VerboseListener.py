# Generated from parser/Verbose.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .VerboseParser import VerboseParser
else:
    from VerboseParser import VerboseParser

# This class defines a complete listener for a parse tree produced by VerboseParser.
class VerboseListener(ParseTreeListener):

    # Enter a parse tree produced by VerboseParser#function_access.
    def enterFunction_access(self, ctx:VerboseParser.Function_accessContext):
        pass

    # Exit a parse tree produced by VerboseParser#function_access.
    def exitFunction_access(self, ctx:VerboseParser.Function_accessContext):
        pass


    # Enter a parse tree produced by VerboseParser#inline_part.
    def enterInline_part(self, ctx:VerboseParser.Inline_partContext):
        pass

    # Exit a parse tree produced by VerboseParser#inline_part.
    def exitInline_part(self, ctx:VerboseParser.Inline_partContext):
        pass


    # Enter a parse tree produced by VerboseParser#expr_call.
    def enterExpr_call(self, ctx:VerboseParser.Expr_callContext):
        pass

    # Exit a parse tree produced by VerboseParser#expr_call.
    def exitExpr_call(self, ctx:VerboseParser.Expr_callContext):
        pass


    # Enter a parse tree produced by VerboseParser#expr_call_nonterm.
    def enterExpr_call_nonterm(self, ctx:VerboseParser.Expr_call_nontermContext):
        pass

    # Exit a parse tree produced by VerboseParser#expr_call_nonterm.
    def exitExpr_call_nonterm(self, ctx:VerboseParser.Expr_call_nontermContext):
        pass


    # Enter a parse tree produced by VerboseParser#Variable.
    def enterVariable(self, ctx:VerboseParser.VariableContext):
        pass

    # Exit a parse tree produced by VerboseParser#Variable.
    def exitVariable(self, ctx:VerboseParser.VariableContext):
        pass


    # Enter a parse tree produced by VerboseParser#MemberAccess.
    def enterMemberAccess(self, ctx:VerboseParser.MemberAccessContext):
        pass

    # Exit a parse tree produced by VerboseParser#MemberAccess.
    def exitMemberAccess(self, ctx:VerboseParser.MemberAccessContext):
        pass


    # Enter a parse tree produced by VerboseParser#Nonterm.
    def enterNonterm(self, ctx:VerboseParser.NontermContext):
        pass

    # Exit a parse tree produced by VerboseParser#Nonterm.
    def exitNonterm(self, ctx:VerboseParser.NontermContext):
        pass


    # Enter a parse tree produced by VerboseParser#Dereference.
    def enterDereference(self, ctx:VerboseParser.DereferenceContext):
        pass

    # Exit a parse tree produced by VerboseParser#Dereference.
    def exitDereference(self, ctx:VerboseParser.DereferenceContext):
        pass


    # Enter a parse tree produced by VerboseParser#ArrayAccess.
    def enterArrayAccess(self, ctx:VerboseParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by VerboseParser#ArrayAccess.
    def exitArrayAccess(self, ctx:VerboseParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by VerboseParser#UnaryOp.
    def enterUnaryOp(self, ctx:VerboseParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by VerboseParser#UnaryOp.
    def exitUnaryOp(self, ctx:VerboseParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by VerboseParser#CallOrAccess.
    def enterCallOrAccess(self, ctx:VerboseParser.CallOrAccessContext):
        pass

    # Exit a parse tree produced by VerboseParser#CallOrAccess.
    def exitCallOrAccess(self, ctx:VerboseParser.CallOrAccessContext):
        pass


    # Enter a parse tree produced by VerboseParser#Literal.
    def enterLiteral(self, ctx:VerboseParser.LiteralContext):
        pass

    # Exit a parse tree produced by VerboseParser#Literal.
    def exitLiteral(self, ctx:VerboseParser.LiteralContext):
        pass


    # Enter a parse tree produced by VerboseParser#Molec.
    def enterMolec(self, ctx:VerboseParser.MolecContext):
        pass

    # Exit a parse tree produced by VerboseParser#Molec.
    def exitMolec(self, ctx:VerboseParser.MolecContext):
        pass


    # Enter a parse tree produced by VerboseParser#BinaryOp.
    def enterBinaryOp(self, ctx:VerboseParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by VerboseParser#BinaryOp.
    def exitBinaryOp(self, ctx:VerboseParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by VerboseParser#type_expr.
    def enterType_expr(self, ctx:VerboseParser.Type_exprContext):
        pass

    # Exit a parse tree produced by VerboseParser#type_expr.
    def exitType_expr(self, ctx:VerboseParser.Type_exprContext):
        pass


    # Enter a parse tree produced by VerboseParser#mutability_node.
    def enterMutability_node(self, ctx:VerboseParser.Mutability_nodeContext):
        pass

    # Exit a parse tree produced by VerboseParser#mutability_node.
    def exitMutability_node(self, ctx:VerboseParser.Mutability_nodeContext):
        pass


    # Enter a parse tree produced by VerboseParser#simple_type_expr.
    def enterSimple_type_expr(self, ctx:VerboseParser.Simple_type_exprContext):
        pass

    # Exit a parse tree produced by VerboseParser#simple_type_expr.
    def exitSimple_type_expr(self, ctx:VerboseParser.Simple_type_exprContext):
        pass


    # Enter a parse tree produced by VerboseParser#pointer_node.
    def enterPointer_node(self, ctx:VerboseParser.Pointer_nodeContext):
        pass

    # Exit a parse tree produced by VerboseParser#pointer_node.
    def exitPointer_node(self, ctx:VerboseParser.Pointer_nodeContext):
        pass


    # Enter a parse tree produced by VerboseParser#statement.
    def enterStatement(self, ctx:VerboseParser.StatementContext):
        pass

    # Exit a parse tree produced by VerboseParser#statement.
    def exitStatement(self, ctx:VerboseParser.StatementContext):
        pass


    # Enter a parse tree produced by VerboseParser#assignment.
    def enterAssignment(self, ctx:VerboseParser.AssignmentContext):
        pass

    # Exit a parse tree produced by VerboseParser#assignment.
    def exitAssignment(self, ctx:VerboseParser.AssignmentContext):
        pass


    # Enter a parse tree produced by VerboseParser#call_argument.
    def enterCall_argument(self, ctx:VerboseParser.Call_argumentContext):
        pass

    # Exit a parse tree produced by VerboseParser#call_argument.
    def exitCall_argument(self, ctx:VerboseParser.Call_argumentContext):
        pass


    # Enter a parse tree produced by VerboseParser#call_arguments.
    def enterCall_arguments(self, ctx:VerboseParser.Call_argumentsContext):
        pass

    # Exit a parse tree produced by VerboseParser#call_arguments.
    def exitCall_arguments(self, ctx:VerboseParser.Call_argumentsContext):
        pass


    # Enter a parse tree produced by VerboseParser#call_target.
    def enterCall_target(self, ctx:VerboseParser.Call_targetContext):
        pass

    # Exit a parse tree produced by VerboseParser#call_target.
    def exitCall_target(self, ctx:VerboseParser.Call_targetContext):
        pass


    # Enter a parse tree produced by VerboseParser#call_statement.
    def enterCall_statement(self, ctx:VerboseParser.Call_statementContext):
        pass

    # Exit a parse tree produced by VerboseParser#call_statement.
    def exitCall_statement(self, ctx:VerboseParser.Call_statementContext):
        pass


    # Enter a parse tree produced by VerboseParser#var_decl.
    def enterVar_decl(self, ctx:VerboseParser.Var_declContext):
        pass

    # Exit a parse tree produced by VerboseParser#var_decl.
    def exitVar_decl(self, ctx:VerboseParser.Var_declContext):
        pass


    # Enter a parse tree produced by VerboseParser#break_statement.
    def enterBreak_statement(self, ctx:VerboseParser.Break_statementContext):
        pass

    # Exit a parse tree produced by VerboseParser#break_statement.
    def exitBreak_statement(self, ctx:VerboseParser.Break_statementContext):
        pass


    # Enter a parse tree produced by VerboseParser#continue_statement.
    def enterContinue_statement(self, ctx:VerboseParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by VerboseParser#continue_statement.
    def exitContinue_statement(self, ctx:VerboseParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by VerboseParser#return_statement.
    def enterReturn_statement(self, ctx:VerboseParser.Return_statementContext):
        pass

    # Exit a parse tree produced by VerboseParser#return_statement.
    def exitReturn_statement(self, ctx:VerboseParser.Return_statementContext):
        pass


    # Enter a parse tree produced by VerboseParser#block_item.
    def enterBlock_item(self, ctx:VerboseParser.Block_itemContext):
        pass

    # Exit a parse tree produced by VerboseParser#block_item.
    def exitBlock_item(self, ctx:VerboseParser.Block_itemContext):
        pass


    # Enter a parse tree produced by VerboseParser#block.
    def enterBlock(self, ctx:VerboseParser.BlockContext):
        pass

    # Exit a parse tree produced by VerboseParser#block.
    def exitBlock(self, ctx:VerboseParser.BlockContext):
        pass


    # Enter a parse tree produced by VerboseParser#if.
    def enterIf(self, ctx:VerboseParser.IfContext):
        pass

    # Exit a parse tree produced by VerboseParser#if.
    def exitIf(self, ctx:VerboseParser.IfContext):
        pass


    # Enter a parse tree produced by VerboseParser#while.
    def enterWhile(self, ctx:VerboseParser.WhileContext):
        pass

    # Exit a parse tree produced by VerboseParser#while.
    def exitWhile(self, ctx:VerboseParser.WhileContext):
        pass


    # Enter a parse tree produced by VerboseParser#do_while.
    def enterDo_while(self, ctx:VerboseParser.Do_whileContext):
        pass

    # Exit a parse tree produced by VerboseParser#do_while.
    def exitDo_while(self, ctx:VerboseParser.Do_whileContext):
        pass


    # Enter a parse tree produced by VerboseParser#return_type_decl_part.
    def enterReturn_type_decl_part(self, ctx:VerboseParser.Return_type_decl_partContext):
        pass

    # Exit a parse tree produced by VerboseParser#return_type_decl_part.
    def exitReturn_type_decl_part(self, ctx:VerboseParser.Return_type_decl_partContext):
        pass


    # Enter a parse tree produced by VerboseParser#name_decl_part.
    def enterName_decl_part(self, ctx:VerboseParser.Name_decl_partContext):
        pass

    # Exit a parse tree produced by VerboseParser#name_decl_part.
    def exitName_decl_part(self, ctx:VerboseParser.Name_decl_partContext):
        pass


    # Enter a parse tree produced by VerboseParser#arguments_decl_part.
    def enterArguments_decl_part(self, ctx:VerboseParser.Arguments_decl_partContext):
        pass

    # Exit a parse tree produced by VerboseParser#arguments_decl_part.
    def exitArguments_decl_part(self, ctx:VerboseParser.Arguments_decl_partContext):
        pass


    # Enter a parse tree produced by VerboseParser#function.
    def enterFunction(self, ctx:VerboseParser.FunctionContext):
        pass

    # Exit a parse tree produced by VerboseParser#function.
    def exitFunction(self, ctx:VerboseParser.FunctionContext):
        pass


    # Enter a parse tree produced by VerboseParser#module_item.
    def enterModule_item(self, ctx:VerboseParser.Module_itemContext):
        pass

    # Exit a parse tree produced by VerboseParser#module_item.
    def exitModule_item(self, ctx:VerboseParser.Module_itemContext):
        pass


    # Enter a parse tree produced by VerboseParser#module.
    def enterModule(self, ctx:VerboseParser.ModuleContext):
        pass

    # Exit a parse tree produced by VerboseParser#module.
    def exitModule(self, ctx:VerboseParser.ModuleContext):
        pass



del VerboseParser