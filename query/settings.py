from query.engine import Postgres
from query.engine import Mysql

ENGINES = {
    'postgres': Postgres,
    'mysql': Mysql
}

WHERE_SPECIAL_ARGUMENTS = {
    '_notin': ' NOT IN ',
    '_in': ' IN '
}

AUTOMATIC_JOINS_PLACEHOLDER = '__'


FIELD_OR_TABLES_FORMAT = '"{}"'

FIELD_FORMAT = '{table}.{field}'

# Select clause config
SELECT_FORMAT = 'SELECT {distinct}{select} FROM "{froms}" '

# Distinct
DISTINCT_CLAUSE_FORMAT = 'DISTINCT '

# Joins Config
JOIN_CLAUSE_FORMAT = 'INNER JOIN {to_table_join} {alias} ON ({from_table_join}."{join}_id" = {to_table_join_name_or_alias}."id")'

# Where clause config
WHERE_CLAUSE_FORMAT = 'WHERE {where_conditions} '
WHERE_AND_CONNECTOR_FORMAT = ' AND '
WHERE_EQUAL_OPERATION_FORMAT = ' = '

# Order by clause config
ORDER_BY_CLAUSE_FORMAT = 'ORDER BY {order_by_conditions} '
ORDER_BY_ASC_FORMAT = 'ASC'
ORDER_BY_DESC_FORMAT = 'DESC'

# Limit clause config 
LIMIT_FORMAT = 'LIMIT {num}'

VALUE_STRING_FORMAT = "'{}'"
VALUE_LIST_FORMAT = '({})'
VALUE_TUPLE_FORMAT = '{}'
VALUE_NULL_FORMAT = 'NULL'

VALUE_SINGLE_QUOTE_FORMAT = "''"
VALUE_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'