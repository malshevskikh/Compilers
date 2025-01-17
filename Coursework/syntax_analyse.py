#----------------------------------СИНТАКСИЧЕСКИЙ_АНАЛИЗ----------------------------------

import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from main import tokens
from main import data


#------------------ГРАММАТИКИ_ОБЪЯВЛЕНИЯ------------------
'''
1. standart_type -> integer  | char | boolean
2. standart_string -> string | string [num]
3. identifier_list -> id | identifier_list, id
4. type -> standart _type | array [int_num … int_num] of standart_type | standart_string
5. complex_declar -> identifier_list: type; | complex_declar identifier_list: type;
6. declarations -> var identifier_list: type; | var identifier_list: type; complex_declar
'''

def p_standart_type(p):
    '''
    standart_type : INTEGER
                | CHAR
                | BOOLEAN
    '''
    p[0] = p[1]


def p_standart_string(p):
    '''
    standart_string : STRING
                    | STRING OPEN_SQUARE_BR NUMBER CLOSE_SQUARE_BR
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 5:
        if 0 < int(p[3]) <= 255:
            p[0] = p[1] + p[2] + p[3] + p[4]

def p_identifier_list(p):
    '''
    identifier_list : ID
                    | identifier_list COMMA ID
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2] + p[3]

def p_type(p):
    '''
    type : standart_type
        | ARRAY OPEN_SQUARE_BR NUMBER POINT POINT NUMBER CLOSE_SQUARE_BR OF standart_type
        | standart_string
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 10:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8] + p[9]

def p_complex_declar(p):
    '''
    complex_declar : identifier_list COLON type SEMICOLON
                | complex_declar identifier_list COLON type SEMICOLON
    '''
    if len(p) == 5:
        p[0] = p[1] + p[2] + p[3] + p[4]
    elif len(p) == 6:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]

def p_declarations(p):
    '''
    declarations : VAR identifier_list COLON type SEMICOLON
                | VAR identifier_list COLON type SEMICOLON complex_declar
    '''
    if len(p) == 6:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    elif len(p) == 7:
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_error(p):
    print(f'Syntax error at {p.value!r}')


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('enter > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s)
