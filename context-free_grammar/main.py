from antlr4 import *
from dist.sqlLexer import sqlLexer
from dist.sqlParser import sqlParser
from dist.sqlVisitor import sqlVisitor

class sqlPrintVisitor(sqlVisitor):
    def visitQuery(self, ctx):
        print(f'Query: {self.visit(ctx.getChild(0))}')
    
    def visitSelectStatement(self, ctx):
        select_list = self.visit(ctx.selectList())
        table_list = self.visit(ctx.tableList())
        where_clause = self.visit(ctx.whereClause()) if ctx.whereClause() else ''
        group_by_clause = self.visit(ctx.groupByClause()) if ctx.groupByClause() else ''
        return f'SELECT {select_list} FROM {table_list} {where_clause} {group_by_clause}'
    
    def visitInsertStatement(self, ctx):
        table_name = ctx.ID(0).getText()
        column_list = self.visit(ctx.columnList()) if ctx.columnList() else ''
        values = self.visit(ctx.valueList())
        return f'INSERT INTO {table_name} {column_list} VALUES {values}'
    
    def visitDeleteStatement(self, ctx):
        table_name = ctx.ID().getText()
        where_clause = self.visit(ctx.whereClause()) if ctx.whereClause() else ''
        return f'DELETE FROM {table_name} {where_clause}'
    
    def visitUpdateStatement(self, ctx):
        table_name = ctx.ID().getText()
        set_clause = self.visit(ctx.setClause())
        where_clause = self.visit(ctx.whereClause()) if ctx.whereClause() else ''
        return f'UPDATE {table_name} SET {set_clause} {where_clause}'
    
    def visitSelectList(self, ctx):
        if ctx.getText() == '*':
            return '*'
        else:
            return ', '.join([self.visit(child) for child in ctx.children if isinstance(child, sqlParser.SelectItemContext)])
    
    def visitSelectItem(self, ctx):
        if ctx.ID():
            return ctx.ID().getText()
        else:
            return f'SUM({ctx.function().getText()[4:-1]})'
    
    def visitTableList(self, ctx):
        return ', '.join([self.visit(child) for child in ctx.children if isinstance(child, sqlParser.TableItemContext)])
    
    def visitTableItem(self, ctx):
        if ctx.ID(1):
            return f'{ctx.ID(0).getText()} AS {ctx.ID(1).getText()}'
        else:
            return ctx.ID(0).getText()
    
    def visitColumnList(self, ctx):
        return ', '.join([child.getText() for child in ctx.children if child.ID()])
    
    def visitValueList(self, ctx):
        return ', '.join([self.visit(child) for child in ctx.children if child.value()])
    
    def visitSetClause(self, ctx):
        return ', '.join([self.visit(child) for child in ctx.children if isinstance(child, sqlParser.SetItemContext)])
    
    def visitSetItem(self, ctx):
        column_name = ctx.ID().getText()
        value = self.visit(ctx.value())
        return f'{column_name} = {value}'
    
    def visitGroupItemList(self, ctx):
        return ', '.join([child.getText() for child in ctx.children if child.ID()])
    
    def visitCondition(self, ctx):
        children = [self.visit(child) for child in ctx.children if child.getText().strip()]
        return ' '.join(children)
    
    def visitSimpleExpression(self, ctx):
        left = ctx.getChild(0).getText()
        operator = self.visit(ctx.operator())
        right = ctx.getChild(2).getText()
        return f'{left} {operator} {right}'
    
    def visitComparisonExpression(self, ctx):
        left = self.visit(ctx.simpleExpression(0))
        operator = self.visit(ctx.comparisonOperator())
        right = self.visit(ctx.simpleExpression(1))
        return f'{left} {operator} {right}'
    
    def visitValue(self, ctx):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        else:
            return 'NULL'
    
    def visitOperator(self, ctx):
        return ctx.getText()
    
    def visitLogicalOperator(self, ctx):
        return ctx.getText()
    
    def visitComparisonOperator(self, ctx):
        return ctx.getText()

def main():
    input_stream = InputStream(input('Enter sql query: '))
    lexer = sqlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = sqlParser(stream)
    tree = parser.query()
    visitor = sqlPrintVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
