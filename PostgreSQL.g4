grammar PostgreSQL;

// Ключевые слова
SELECT: 'SELECT';
FROM: 'FROM';
WHERE: 'WHERE';
GROUP_BY: 'GROUP BY';
ORDER_BY: 'ORDER BY';
LIMIT: 'LIMIT';
AND: 'AND';
OR: 'OR';
IS: 'IS';
NULL: 'NULL';
NOT: 'NOT';
BETWEEN: 'BETWEEN';
IN: 'IN';

// Идентификаторы
IDENTIFIER: [a-zA-Z_][a-zA-Z0-9_]*;

// Цифровые литералы
NUMBER: [0-9]+;

// Строковые литералы
STRING: '\'' (~'\'')* '\'';

// Символы
EQUALS: '=';
LESS_THAN: '<';
GREATER_THAN: '>';
LESS_THAN_OR_EQUAL: '<=';
GREATER_THAN_OR_EQUAL: '>=';
NOT_EQUAL: '<>';

// Пропуск пробелов и табуляций
WS: [ \t\r\n]+ -> skip; // пропуск пробелов, табуляций, переводов строк

// Определение правил
query: (statement (';' WS*)?)+; // Множество запросов, разделенных точкой с запятой, с пропуском пробелов после точки с запятой
statement: SELECT select_list FROM table_references where_clause? group_by_clause? order_by_clause? limit_clause?;
select_list: (select_item (',' select_item)*) | '*';
select_item: expression;
table_references: IDENTIFIER (',' IDENTIFIER)*;
where_clause: WHERE condition;
group_by_clause: GROUP_BY expression_list;
order_by_clause: ORDER_BY expression_list;
limit_clause: LIMIT NUMBER;

// Определение выражений
expression: IDENTIFIER | NUMBER | STRING;

expression_list: expression (',' expression)*;

condition: (expression (comparison_op expression)+) // Оператор сравнения множественный
    | expression BETWEEN expression AND expression
    | expression IN '(' expression_list ')'
    | expression IS NULL
    | expression IS NOT NULL
    | '(' condition ')' // Добавляем поддержку скобок для группировки условий
    | NOT condition // Добавляем поддержку оператора NOT для отрицания условия
    | condition logical_op condition; // Добавляем логические операторы между условиями


comparison_op: EQUALS | LESS_THAN | GREATER_THAN | LESS_THAN_OR_EQUAL | GREATER_THAN_OR_EQUAL | NOT_EQUAL;

// Логические операторы
logical_op: AND | OR;
