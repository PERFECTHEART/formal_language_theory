grammar sql;

query: selectStatement
    | insertStatement
    | deleteStatement
    | updateStatement
    ;

selectStatement: 'SELECT' selectList 'FROM' tableList (whereClause)? (groupByClause)? ;
insertStatement: 'INSERT INTO' ID ( '(' columnList ')' )? 'VALUES' '(' valueList ')' ;
deleteStatement: 'DELETE FROM' ID ( whereClause ) ;
updateStatement: 'UPDATE' ID 'SET' setClause ( whereClause ) ;
selectList: '*' | selectItem (',' selectItem )* ;
selectItem: ID | function ;
tableList: ID | tableItem (',' tableItem )* ;
tableItem: ID ( ' AS' ID )? ;
columnList: ID (',' ID)* ;
valueList: value (',' value)* ;
setClause: setItem (',' setItem)* ;
setItem: ID '=' value ;
groupByClause: 'GROUP BY' groupItemList ;
groupItemList: ID (',' ID)* ;
function: SUM '(' ID ')' ;
whereClause: 'WHERE' condition ;
condition: expression (logicalOperator expression)* ;
expression: simpleExpression | comparisonExpression ;
simpleExpression: ( ID | value ) operator ( ID | value) ;
comparisonExpression: simpleExpression comparisonOperator simpleExpression ;
operator: '+' | '-' | '*' | '/' ;
logicalOperator: 'AND' | 'OR' ;
comparisonOperator: '=' | '<>' | '<=' | '>=' | '<' | '>' ;
value: STRING | NUMBER | 'NULL' ;
WS : [ \n\r\t]+ -> skip ;
STRING: '\'' (~'\'')* '\'' ;
NUMBER: DIGIT+ ('.' DIGIT+)? | '.' DIGIT+ ;
ID: LETTER (LETTER | DIGIT | '_')* ;
fragment LETTER: [a-zA-Z] ;
fragment DIGIT: [0-9] ;
