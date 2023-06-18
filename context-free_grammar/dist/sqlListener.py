# Generated from sql.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .sqlParser import sqlParser
else:
    from sqlParser import sqlParser

# This class defines a complete listener for a parse tree produced by sqlParser.
class sqlListener(ParseTreeListener):

    # Enter a parse tree produced by sqlParser#query.
    def enterQuery(self, ctx:sqlParser.QueryContext):
        pass

    # Exit a parse tree produced by sqlParser#query.
    def exitQuery(self, ctx:sqlParser.QueryContext):
        pass


    # Enter a parse tree produced by sqlParser#selectStatement.
    def enterSelectStatement(self, ctx:sqlParser.SelectStatementContext):
        pass

    # Exit a parse tree produced by sqlParser#selectStatement.
    def exitSelectStatement(self, ctx:sqlParser.SelectStatementContext):
        pass


    # Enter a parse tree produced by sqlParser#insertStatement.
    def enterInsertStatement(self, ctx:sqlParser.InsertStatementContext):
        pass

    # Exit a parse tree produced by sqlParser#insertStatement.
    def exitInsertStatement(self, ctx:sqlParser.InsertStatementContext):
        pass


    # Enter a parse tree produced by sqlParser#deleteStatement.
    def enterDeleteStatement(self, ctx:sqlParser.DeleteStatementContext):
        pass

    # Exit a parse tree produced by sqlParser#deleteStatement.
    def exitDeleteStatement(self, ctx:sqlParser.DeleteStatementContext):
        pass


    # Enter a parse tree produced by sqlParser#updateStatement.
    def enterUpdateStatement(self, ctx:sqlParser.UpdateStatementContext):
        pass

    # Exit a parse tree produced by sqlParser#updateStatement.
    def exitUpdateStatement(self, ctx:sqlParser.UpdateStatementContext):
        pass


    # Enter a parse tree produced by sqlParser#selectList.
    def enterSelectList(self, ctx:sqlParser.SelectListContext):
        pass

    # Exit a parse tree produced by sqlParser#selectList.
    def exitSelectList(self, ctx:sqlParser.SelectListContext):
        pass


    # Enter a parse tree produced by sqlParser#selectItem.
    def enterSelectItem(self, ctx:sqlParser.SelectItemContext):
        pass

    # Exit a parse tree produced by sqlParser#selectItem.
    def exitSelectItem(self, ctx:sqlParser.SelectItemContext):
        pass


    # Enter a parse tree produced by sqlParser#tableList.
    def enterTableList(self, ctx:sqlParser.TableListContext):
        pass

    # Exit a parse tree produced by sqlParser#tableList.
    def exitTableList(self, ctx:sqlParser.TableListContext):
        pass


    # Enter a parse tree produced by sqlParser#tableItem.
    def enterTableItem(self, ctx:sqlParser.TableItemContext):
        pass

    # Exit a parse tree produced by sqlParser#tableItem.
    def exitTableItem(self, ctx:sqlParser.TableItemContext):
        pass


    # Enter a parse tree produced by sqlParser#columnList.
    def enterColumnList(self, ctx:sqlParser.ColumnListContext):
        pass

    # Exit a parse tree produced by sqlParser#columnList.
    def exitColumnList(self, ctx:sqlParser.ColumnListContext):
        pass


    # Enter a parse tree produced by sqlParser#valueList.
    def enterValueList(self, ctx:sqlParser.ValueListContext):
        pass

    # Exit a parse tree produced by sqlParser#valueList.
    def exitValueList(self, ctx:sqlParser.ValueListContext):
        pass


    # Enter a parse tree produced by sqlParser#setClause.
    def enterSetClause(self, ctx:sqlParser.SetClauseContext):
        pass

    # Exit a parse tree produced by sqlParser#setClause.
    def exitSetClause(self, ctx:sqlParser.SetClauseContext):
        pass


    # Enter a parse tree produced by sqlParser#setItem.
    def enterSetItem(self, ctx:sqlParser.SetItemContext):
        pass

    # Exit a parse tree produced by sqlParser#setItem.
    def exitSetItem(self, ctx:sqlParser.SetItemContext):
        pass


    # Enter a parse tree produced by sqlParser#groupByClause.
    def enterGroupByClause(self, ctx:sqlParser.GroupByClauseContext):
        pass

    # Exit a parse tree produced by sqlParser#groupByClause.
    def exitGroupByClause(self, ctx:sqlParser.GroupByClauseContext):
        pass


    # Enter a parse tree produced by sqlParser#groupItemList.
    def enterGroupItemList(self, ctx:sqlParser.GroupItemListContext):
        pass

    # Exit a parse tree produced by sqlParser#groupItemList.
    def exitGroupItemList(self, ctx:sqlParser.GroupItemListContext):
        pass


    # Enter a parse tree produced by sqlParser#function.
    def enterFunction(self, ctx:sqlParser.FunctionContext):
        pass

    # Exit a parse tree produced by sqlParser#function.
    def exitFunction(self, ctx:sqlParser.FunctionContext):
        pass


    # Enter a parse tree produced by sqlParser#whereClause.
    def enterWhereClause(self, ctx:sqlParser.WhereClauseContext):
        pass

    # Exit a parse tree produced by sqlParser#whereClause.
    def exitWhereClause(self, ctx:sqlParser.WhereClauseContext):
        pass


    # Enter a parse tree produced by sqlParser#condition.
    def enterCondition(self, ctx:sqlParser.ConditionContext):
        pass

    # Exit a parse tree produced by sqlParser#condition.
    def exitCondition(self, ctx:sqlParser.ConditionContext):
        pass


    # Enter a parse tree produced by sqlParser#expression.
    def enterExpression(self, ctx:sqlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by sqlParser#expression.
    def exitExpression(self, ctx:sqlParser.ExpressionContext):
        pass


    # Enter a parse tree produced by sqlParser#simpleExpression.
    def enterSimpleExpression(self, ctx:sqlParser.SimpleExpressionContext):
        pass

    # Exit a parse tree produced by sqlParser#simpleExpression.
    def exitSimpleExpression(self, ctx:sqlParser.SimpleExpressionContext):
        pass


    # Enter a parse tree produced by sqlParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:sqlParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by sqlParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:sqlParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by sqlParser#operator.
    def enterOperator(self, ctx:sqlParser.OperatorContext):
        pass

    # Exit a parse tree produced by sqlParser#operator.
    def exitOperator(self, ctx:sqlParser.OperatorContext):
        pass


    # Enter a parse tree produced by sqlParser#logicalOperator.
    def enterLogicalOperator(self, ctx:sqlParser.LogicalOperatorContext):
        pass

    # Exit a parse tree produced by sqlParser#logicalOperator.
    def exitLogicalOperator(self, ctx:sqlParser.LogicalOperatorContext):
        pass


    # Enter a parse tree produced by sqlParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:sqlParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by sqlParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:sqlParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by sqlParser#value.
    def enterValue(self, ctx:sqlParser.ValueContext):
        pass

    # Exit a parse tree produced by sqlParser#value.
    def exitValue(self, ctx:sqlParser.ValueContext):
        pass



del sqlParser