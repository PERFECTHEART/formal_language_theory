# Generated from sql.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sqlParser import sqlParser
else:
    from sqlParser import sqlParser

# This class defines a complete generic visitor for a parse tree produced by sqlParser.

class sqlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by sqlParser#query.
    def visitQuery(self, ctx:sqlParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#selectStatement.
    def visitSelectStatement(self, ctx:sqlParser.SelectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#insertStatement.
    def visitInsertStatement(self, ctx:sqlParser.InsertStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#deleteStatement.
    def visitDeleteStatement(self, ctx:sqlParser.DeleteStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#updateStatement.
    def visitUpdateStatement(self, ctx:sqlParser.UpdateStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#selectList.
    def visitSelectList(self, ctx:sqlParser.SelectListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#selectItem.
    def visitSelectItem(self, ctx:sqlParser.SelectItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#tableList.
    def visitTableList(self, ctx:sqlParser.TableListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#tableItem.
    def visitTableItem(self, ctx:sqlParser.TableItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#columnList.
    def visitColumnList(self, ctx:sqlParser.ColumnListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#valueList.
    def visitValueList(self, ctx:sqlParser.ValueListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#setClause.
    def visitSetClause(self, ctx:sqlParser.SetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#setItem.
    def visitSetItem(self, ctx:sqlParser.SetItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#groupByClause.
    def visitGroupByClause(self, ctx:sqlParser.GroupByClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#groupItemList.
    def visitGroupItemList(self, ctx:sqlParser.GroupItemListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#function.
    def visitFunction(self, ctx:sqlParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#whereClause.
    def visitWhereClause(self, ctx:sqlParser.WhereClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#condition.
    def visitCondition(self, ctx:sqlParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#expression.
    def visitExpression(self, ctx:sqlParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#simpleExpression.
    def visitSimpleExpression(self, ctx:sqlParser.SimpleExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#comparisonExpression.
    def visitComparisonExpression(self, ctx:sqlParser.ComparisonExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#operator.
    def visitOperator(self, ctx:sqlParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#logicalOperator.
    def visitLogicalOperator(self, ctx:sqlParser.LogicalOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:sqlParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by sqlParser#value.
    def visitValue(self, ctx:sqlParser.ValueContext):
        return self.visitChildren(ctx)



del sqlParser