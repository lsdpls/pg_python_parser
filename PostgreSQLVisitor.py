# Generated from PostgreSQL.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .PostgreSQLParser import PostgreSQLParser
else:
    from PostgreSQLParser import PostgreSQLParser

# This class defines a complete generic visitor for a parse tree produced by PostgreSQLParser.

class PostgreSQLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PostgreSQLParser#query.
    def visitQuery(self, ctx:PostgreSQLParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#statement.
    def visitStatement(self, ctx:PostgreSQLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#select_list.
    def visitSelect_list(self, ctx:PostgreSQLParser.Select_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#select_item.
    def visitSelect_item(self, ctx:PostgreSQLParser.Select_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#table_references.
    def visitTable_references(self, ctx:PostgreSQLParser.Table_referencesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#where_clause.
    def visitWhere_clause(self, ctx:PostgreSQLParser.Where_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#group_by_clause.
    def visitGroup_by_clause(self, ctx:PostgreSQLParser.Group_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#order_by_clause.
    def visitOrder_by_clause(self, ctx:PostgreSQLParser.Order_by_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#limit_clause.
    def visitLimit_clause(self, ctx:PostgreSQLParser.Limit_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#expression.
    def visitExpression(self, ctx:PostgreSQLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#expression_list.
    def visitExpression_list(self, ctx:PostgreSQLParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#condition.
    def visitCondition(self, ctx:PostgreSQLParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#comparison_op.
    def visitComparison_op(self, ctx:PostgreSQLParser.Comparison_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PostgreSQLParser#logical_op.
    def visitLogical_op(self, ctx:PostgreSQLParser.Logical_opContext):
        return self.visitChildren(ctx)



del PostgreSQLParser