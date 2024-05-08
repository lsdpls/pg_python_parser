from PostgreSQLVisitor import PostgreSQLVisitor
from PostgreSQLParser import PostgreSQLParser

class QueryBuilder(PostgreSQLVisitor):
    def visitQuery(self, ctx:PostgreSQLParser.QueryContext):
        statements = [self.visit(statement) for statement in ctx.statement()]
        return statements

    def visitStatement(self, ctx:PostgreSQLParser.StatementContext):
        select_list = self.visit(ctx.select_list())
        from_clause = self.visit(ctx.table_references())
        where_clause = self.visit(ctx.where_clause()) if ctx.where_clause() else None
        group_by_clause = self.visit(ctx.group_by_clause()) if ctx.group_by_clause() else None
        order_by_clause = self.visit(ctx.order_by_clause()) if ctx.order_by_clause() else None
        limit_clause = self.visit(ctx.limit_clause()) if ctx.limit_clause() else None
        return {
            "select_list": select_list,
            "from_clause": from_clause,
            "where_clause": where_clause,
            "group_by_clause": group_by_clause,
            "order_by_clause": order_by_clause,
            "limit_clause": limit_clause
        }

    def visitSelect_list(self, ctx:PostgreSQLParser.Select_listContext):
        return [self.visit(select_item) for select_item in ctx.select_item()]

    def visitSelect_item(self, ctx:PostgreSQLParser.Select_itemContext):
        return self.visit(ctx.expression())

    def visitTable_references(self, ctx:PostgreSQLParser.Table_referencesContext):
        return [table.getText() for table in ctx.IDENTIFIER()]

    def visitWhere_clause(self, ctx:PostgreSQLParser.Where_clauseContext):
        return self.visit(ctx.condition())

    def visitGroup_by_clause(self, ctx:PostgreSQLParser.Group_by_clauseContext):
        return [self.visit(expression) for expression in ctx.expression_list().expression()]

    def visitOrder_by_clause(self, ctx:PostgreSQLParser.Order_by_clauseContext):
        return [self.visit(expression) for expression in ctx.expression_list().expression()]

    def visitLimit_clause(self, ctx:PostgreSQLParser.Limit_clauseContext):
        return int(ctx.NUMBER().getText())

    def visitExpression(self, ctx:PostgreSQLParser.ExpressionContext):
        if ctx.IDENTIFIER():
            return ctx.IDENTIFIER().getText()
        elif ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Remove quotes

    def visitCondition(self, ctx:PostgreSQLParser.ConditionContext):
        if ctx.logical_op():
            left_condition = self.visit(ctx.condition(0))
            op = ctx.logical_op().getText()
            right_condition = self.visit(ctx.condition(1))
            return {"left_condition": left_condition, "op": op, "right_condition": right_condition}
        elif ctx.comparison_op():
            conditions = []
            for i in range(len(ctx.comparison_op())):
                left = self.visit(ctx.expression(i))
                op = ctx.comparison_op(i).getText()
                right = self.visit(ctx.expression(i + 1))
                conditions.append({"left": left, "op": op, "right": right})
            return conditions
        elif ctx.BETWEEN():
            left = self.visit(ctx.expression(0))
            lower_bound = self.visit(ctx.expression(1))
            upper_bound = self.visit(ctx.expression(2))
            return {"left": left, "op": "BETWEEN", "lower_bound": lower_bound, "upper_bound": upper_bound}
        elif ctx.IN():
            left = self.visit(ctx.expression(0))
            values = [self.visit(expr) for expr in ctx.expression_list().expression()]
            return {"left": left, "op": "IN", "values": values}
        elif ctx.IS():
            left = self.visit(ctx.expression(0))
            null_check = "NULL" if ctx.NOT() is None else "NOT NULL"
            return {"left": left, "op": "IS", "right": null_check}
        else:
            return None  # Add this line to handle empty condition context


# Example usage
if __name__ == "__main__":
    from antlr4 import *
    from PostgreSQLLexer import PostgreSQLLexer
    from PostgreSQLParser import PostgreSQLParser

    query = "SELECT column1, column2 FROM table1 WHERE column3 = 'value' ORDER BY column1 LIMIT 10; SELECT column1 FROM table1 WHERE column3 <= 'value' AND column2 <> 'value'ORDER BY column1 LIMIT 10;"
    
    # Create input stream from the query
    input_stream = InputStream(query)
    
    # Create lexer for the input stream
    lexer = PostgreSQLLexer(input_stream)
    
    # Get all tokens from the lexer
    token_stream = CommonTokenStream(lexer)
    
    # Create parser for the token stream
    parser = PostgreSQLParser(token_stream)
    
    # Parse the query and get the root of the parse tree
    tree = parser.query()

    # Create a visitor instance
    visitor = QueryBuilder()

    # Build the query
    query_dict = visitor.visit(tree)

    # Print the query dictionary
    print(query_dict)
