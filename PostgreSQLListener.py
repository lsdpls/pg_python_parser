# Generated from PostgreSQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PostgreSQLParser import PostgreSQLParser
else:
    from PostgreSQLParser import PostgreSQLParser

# This class defines a complete listener for a parse tree produced by PostgreSQLParser.
class PostgreSQLListener(ParseTreeListener):

    # Enter a parse tree produced by PostgreSQLParser#query.
    def enterQuery(self, ctx:PostgreSQLParser.QueryContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#query.
    def exitQuery(self, ctx:PostgreSQLParser.QueryContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#statement.
    def enterStatement(self, ctx:PostgreSQLParser.StatementContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#statement.
    def exitStatement(self, ctx:PostgreSQLParser.StatementContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#select_list.
    def enterSelect_list(self, ctx:PostgreSQLParser.Select_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#select_list.
    def exitSelect_list(self, ctx:PostgreSQLParser.Select_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#select_item.
    def enterSelect_item(self, ctx:PostgreSQLParser.Select_itemContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#select_item.
    def exitSelect_item(self, ctx:PostgreSQLParser.Select_itemContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#table_references.
    def enterTable_references(self, ctx:PostgreSQLParser.Table_referencesContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#table_references.
    def exitTable_references(self, ctx:PostgreSQLParser.Table_referencesContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#where_clause.
    def enterWhere_clause(self, ctx:PostgreSQLParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#where_clause.
    def exitWhere_clause(self, ctx:PostgreSQLParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:PostgreSQLParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:PostgreSQLParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:PostgreSQLParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:PostgreSQLParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#limit_clause.
    def enterLimit_clause(self, ctx:PostgreSQLParser.Limit_clauseContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#limit_clause.
    def exitLimit_clause(self, ctx:PostgreSQLParser.Limit_clauseContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#expression.
    def enterExpression(self, ctx:PostgreSQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#expression.
    def exitExpression(self, ctx:PostgreSQLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#expression_list.
    def enterExpression_list(self, ctx:PostgreSQLParser.Expression_listContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#expression_list.
    def exitExpression_list(self, ctx:PostgreSQLParser.Expression_listContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#condition.
    def enterCondition(self, ctx:PostgreSQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#condition.
    def exitCondition(self, ctx:PostgreSQLParser.ConditionContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#comparison_op.
    def enterComparison_op(self, ctx:PostgreSQLParser.Comparison_opContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#comparison_op.
    def exitComparison_op(self, ctx:PostgreSQLParser.Comparison_opContext):
        pass


    # Enter a parse tree produced by PostgreSQLParser#logical_op.
    def enterLogical_op(self, ctx:PostgreSQLParser.Logical_opContext):
        pass

    # Exit a parse tree produced by PostgreSQLParser#logical_op.
    def exitLogical_op(self, ctx:PostgreSQLParser.Logical_opContext):
        pass



del PostgreSQLParser