import ply.lex as lexx
#import ply.yacc as yacc
from ply.lex import lex
from ply.yacc import yacc
import graphviz
import llvm_file
import llvm_file_complex_math
import os

#----------------------------------ТОКЕНИЗАЦИЯ----------------------------------

reserved = {
    'var': 'VAR',
    'integer': 'INTEGER',
    'char': 'CHAR',
    'boolean': 'BOOLEAN',
    'string': 'STRING',
    'array': 'ARRAY',
    'of': 'OF',
    'for': 'FOR',
    'while': 'WHILE',
    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'mod': 'MOD',
    'div': 'DIV',
    'and': 'AND',
    'or': 'OR',
    'True': 'TRUE',
    'False': 'FALSE',
    'do': 'DO',
    'function': 'FUNCTION',
    'to': 'TO',
    'downto': 'DOWNTO'
}

tokens = ["ID", "COMMA", "OPEN_SQUARE_BR", "CLOSE_SQUARE_BR", "SEMICOLON", "COLON", "NUMBER", "POINT",
          "PLUS", "MINUS", "DIVISION", "MULTIPLICATION", "EQUALITY",
          "EQUALS", "MORE", "MORE_OR_EQUAL", "LESS", "LESS_OR_EQUAL", "NOT_EQUAL",
          "OPEN_BR", "CLOSE_BR", "QUOTE"] + list(reserved.values())

# для каждого токена из массива мы должны написать его определение вида t_ИМЯТОКЕНА = регулярка
#-?([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|[1-2][0-9][0-9][0-9][0-9]|3[0-1][0-9][0-9][0-9]|32[0-7][0-9][0-9]|327[0-5][0-9]|3276[0-7])
t_EQUALITY = r':='
t_COMMA = r'\,'
t_OPEN_SQUARE_BR = r'\['
t_CLOSE_SQUARE_BR = r'\]'
t_SEMICOLON = r'\;'
t_COLON = r'\:'
#t_NUMBER = r'-?([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|[1-2][0-9][0-9][0-9][0-9]|3[0-1][0-9][0-9][0-9]|32[0-7][0-9][0-9]|327[0-5][0-9]|3276[0-7])'
t_POINT = r'\.'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVISION = r'\/'
t_MULTIPLICATION = r'\*'
t_MORE_OR_EQUAL = r'>='
t_LESS_OR_EQUAL = r'<='
t_NOT_EQUAL = r'<>'
t_EQUALS = r'\='
t_MORE = r'\>'

t_LESS = r'\<'


t_OPEN_BR = r'\('
t_CLOSE_BR = r'\)'
t_QUOTE = r'\''

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

t_ignore = ' \t'


# Ignored token with an action associated with it
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print(f'Illegal character {t.value[0]!r}')
    t.lexer.skip(1)


'''
lexer1 = lexx.lex()
data = "var i,j,n:integer;"

# Даем лексеру какие-то входные данные
lexer1.input(data)

# Токенизировать

while True:
    tok = lexer1.token()
    if not tok:
        break # Нет больше ввода
    print(tok)
    #list_of_tokins.append(tok)
'''

#----------------------------------ГРАММАТИЧЕСКИЙ_АНАЛИЗ----------------------------------


#------------------ГРАММАТИКИ_ОБЪЯВЛЕНИЯ_ДАННЫХ------------------
'''
1. standart_type -> integer  | char | boolean
2. standart_string -> string | string [num]
3. identifier_list -> id | identifier_list, id
4. type -> standart _type | array [int_num … int_num] of standart_type | standart_string
5. complex_declar -> identifier_list: type; | complex_declar identifier_list: type;
6. declarations -> var identifier_list: type; | var identifier_list: type; complex_declar
'''

#------------------ГРАММАТИКИ_ОБЪЯВЛЕНИЯ_ФУНКЦИЙ/ЦИКЛОВ------------------
'''
7. standart_subprogram -> function id ( parameter_list ): standart_type;
8. parameter_list -> identifier_list : type | parameter_list; identifier_list : type
9. standart_cycle -> standart_while  | standart_for
10. standart_while -> while ( logic_expression )  do compound_statement
	                | while ( logic_expression )  do simple_statement
	                | while ( relational_expression )  do compound_statement
	                | while ( relational_expression )  do simple_statement
11. standart_for -> for variable := int_num to int_num do compound_statement
                    | for variable := int_num downto int_num do compound_statement                    
'''

class Expr: pass


class Main(Expr):
    def __init__(self, rule):
        self.type = "main_rule"
        self.rule = rule


class Declarations_without_complex_declar(Expr):
    def __init__(self, identifier_list, type):
        self.type = "declarations"
        self.identifier_list = identifier_list
        self.type = type

    def display_data(self):
        print("type:", self.type, "|", "var ", self.identifier_list, ":", self.type, ";")


class Declarations_with_complex_declar(Expr):
    def __init__(self, identifier_list, type, complex_declar):
        self.type = "declarations"
        self.identifier_list = identifier_list
        self.type = type
        self.complex_declar = complex_declar

class Math_sign(Expr):
    def __init__(self, math_sign):
        self.type = "math_sign"
        self.math_sign = math_sign

    def display_data(self):
        print("type:", self.type, "|", "math_sign:", self.math_sign)


class Simple_math(Expr):
    def __init__(self, left, op, right):
        self.type = "simple_math"
        self.left = left
        self.op = op
        self.right = right

    def display_data(self):
        print("type:", self.type, "|", self.left, self.op, self.right)


class Complex_math(Expr):
    def __init__(self, left, op, right):
        self.type = "simple_math"
        self.left = left
        self.op = op
        self.right = right

    def display_data(self):
        print("type:", self.type, "|", self.left, self.op, self.right)


class Identifier_list(Expr):
    def __init__(self, ID):
        self.type = "ID"
        self.ID = ID

class Node:
    def __init__(self, type, children=None,leaf=None):
         self.type = type
         if children:
              self.children = children
         else:
              self.children = [ ]
         self.leaf = leaf

    def display_data(self):
        print("type of rule:", self.type, "|", "children:", self.children, "|", "leaf:", self.leaf)


ast_list = []
#list_of


#правило для всего
def p_main(p):
    '''
    main : declarations
        | standart_subprogram
        | if_statement
        | expression
        | standart_cycle
    '''
    #print(p[0], p[1])
    p[0] = Node("main_rule", p[1])
    #print(p[0].children)
    p[0].display_data()
    s = Node("main_rule", p[1])
    s.display_data()
    #print("1")
    #p[0] = ['main_rule', p[1]]



#---------------Основные_правила--------------

def p_declarations(p):
    '''
    declarations : VAR identifier_list COLON type SEMICOLON
                | VAR identifier_list COLON type SEMICOLON complex_declar
    '''
    #print(len(p), p[0], p[1])
    if len(p) == 6:
        #p[0] = p[1] + ' ' + p[2] + p[3] + p[4] + p[5]
        #p[0] = ['declarations', p[2], p[4]]
        p[0] = Declarations_without_complex_declar(p[2], p[4])
        s = Node('declarations', [p[2], p[4]], [p[1], p[3], p[5]])
        s.display_data()
        #print(s, s.type, s.identifier_list)
    elif len(p) == 7:
        #p[0] = p[1] + ' ' + p[2] + p[3] + p[4] + p[5] + '\n' + ' ' + p[6]
        p[0] = ['declarations', p[2], p[4], p[6]]
        s = Node('declarations', [p[2], p[4], p[6]], [p[1], p[3], p[5]])
        s.display_data()


def p_standart_subprogram(p):
    '''
    standart_subprogram : FUNCTION ID OPEN_BR parameter_list CLOSE_BR COLON standart_type SEMICOLON
    '''
    #print(p[0], p[1], p[2], p[3], p[4], p[5], p[6], p[7], p[8])
    #p[0] = p[1] + ' ' + p[2] + p[3] + p[4] + p[5] +  p[6] + ' ' + p[7] + p[8]
    p[0] = ['standart_subprogram', p[4], p[7]]
    s = Node('standart_subprogram', [p[4], p[7]], [p[1], p[2], p[3], p[5], p[6], p[8]])
    s.display_data()


#-----------IF_THEN_ELSE-------------

#def p_if_then_else_statement(p):
#    '''
#    if_then_else_statement : if_statement then_statement else_statement SEMICOLON
#	                    | if_statement then_statement SEMICOLON
#    '''
#    print("if_then_else_statement", p[0], p[1])
#    if len(p) == 4:
#        p[0] = p[1] + p[2] + p[3]
#        #print(p[0])
#    elif len(p) == 5:
#        p[0] = p[1] + p[2] + p[3] + p[4]


def p_if_statement(p):
    '''
    if_statement : IF OPEN_BR logic_expression CLOSE_BR EQUALS boolean_value then_else_statement
                | IF OPEN_BR relational_expression CLOSE_BR then_else_statement
    '''
    #print("if_statement", p[0], p[1], p[2], p[3], p[4], p[5], p[6])
    if len(p) == 6:
        #p[0] = p[1] + ' ' + p[2] + p[3] + p[4] + ' ' + p[5]
        #print("{}{}", p[0])
        p[0] = ['if_statement', p[2], p[5]]
        s = Node('if_statement', [p[3], p[5]], [p[1], p[2], p[4]])
        s.display_data()
    elif len(p) == 8:
        #p[0] = p[1] + ' ' + p[2] + p[3] + p[4] + ' ' + p[5] + ' ' + p[6] + ' ' + p[7]
        #print("()()()", p[0])
        p[0] = ['if_statement', p[3], p[6], p[7]]
        s = Node('if_statement', [p[3], p[6], p[7]], [p[1], p[2], p[4], p[5]])
        s.display_data()

def p_then_else_statement(p):
    '''
    then_else_statement : THEN compound_statement
                | THEN simple_statement
                | THEN compound_statement ELSE compound_statement
                | THEN simple_statement ELSE compound_statement
                | THEN compound_statement ELSE simple_statement
                | THEN simple_statement ELSE simple_statement
    '''
    #print("then_statement", p[0], p[1], p[2])
    #p[0] = p[1] + p[2] + p[3]
    #print(p[0])
    if len(p) == 3:
        p[0] = p[1] + ' ' + p[2]
        #p[0] = ['then_else_statement', p[2]]
        s = Node('then_else_statement', p[2], p[1])
        s.display_data()
    elif len(p) == 5:
        #p[0] = p[1] + '\n' + ' ' + p[2] + '\n' + p[3] + '\n' + ' ' + p[4]
        p[0] = ['then_else_statement', p[2], p[4]]
        s = Node('then_else_statement', [p[2], p[4]], [p[1], p[3]])
        s.display_data()


#def p_else_statement(p):
#    '''
#    else_statement : ELSE compound_statement SEMICOLON
#                | ELSE simple_statement SEMICOLON
#    '''
#    p[0] = p[1] + p[2] + p[3]

#------------------------------------


def p_expression(p):
    '''
    expression : math_expression
                | logic_expression
                | relational_expression
                | assignment_expression
    '''
    #p[0] = p[1]
    p[0] = Node("expression", p[1])
    #print(p[0].children, p[0].leaf)
    p[0].display_data()
    #p[0] = ['expression', p[1]]
    #print("2")


def p_standart_cycle(p):
    '''
    standart_cycle : standart_while
                    | standart_for
    '''
    #p[0] = p[1]
    p[0] = ['standart_cycle', p[1]]
    s = Node('standart_cycle', p[1])
    s.display_data()

#---------------------------------------------


def p_parameter_list(p):
    '''
    parameter_list : identifier_list COLON type
                    | parameter_list SEMICOLON identifier_list COLON type
    '''
    if len(p) == 4:
        #p[0] = p[1] + p[2] + p[3]
        p[0] = ['parameter_list', p[1], p[3]]
        s = Node('parameter_list', [p[1], p[3]], p[2])
        s.display_data()
    elif len(p) == 6:
        #p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        p[0] = ['parameter_list', p[1], p[3], p[5]]
        s = Node('parameter_list', [p[1], p[3], p[5]], [p[2], p[4]])
        s.display_data()


def p_type(p):
    '''
    type : standart_type
        | ARRAY OPEN_SQUARE_BR NUMBER POINT POINT NUMBER CLOSE_SQUARE_BR OF standart_type
        | standart_string
    '''
    #print(len(p), p[0], p[1], p[2], ";;;", p[3], p[4], ";;;", p[5], p[6], p[7])
    if len(p) == 2:
        #p[0] = p[1]
        p[0] = ['type', p[1]]
        s = Node('type', p[1])
        s.display_data()
    elif len(p) >= 10:
        #p[0] = p[1] + p[2] + str(p[3]) + p[4] + p[5] + str(p[6]) + p[7] + ' ' + p[8] + ' ' + p[9]
        p[0] = ['type', p[9]]
        s = Node('type', [p[8]], [p[1], p[2], p[3], p[4], p[5], p[6], p[7]])
        s.display_data()



def p_identifier_list(p):
    '''
    identifier_list : ID
                    | identifier_list COMMA ID
    '''
    #print(len(p), p[0], p[1])
    if len(p) == 2:
        #p[0] = p[1]
        p[0] = ['identifier_list', p[1]]
        s = Node('identifier_list', [], p[1])
        s.display_data()
    elif len(p) == 4:
        #p[0] = p[1] + p[2] + p[3]
        p[0] = ['identifier_list', p[1]]
        s = Node('identifier_list', p[1], p[3])
        s.display_data()

def p_complex_declar(p):
    '''
    complex_declar : identifier_list COLON type SEMICOLON
                | complex_declar identifier_list COLON type SEMICOLON
    '''
    if len(p) == 5:
        #p[0] = p[1] + p[2] + p[3] + p[4] + '\n' + ' '
        p[0] = ['complex_declar', p[1], p[3]]
        s = Node('complex_declar', [p[1], p[3]], [p[2], p[4]])
        s.display_data()
    elif len(p) == 6:
        #p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + '\n' + ' '
        p[0] = ['complex_declar', p[1], p[2], p[4]]
        s = Node('complex_declar', [p[1], p[2], p[4]], [p[3], p[5]])
        s.display_data()

def p_standart_type(p):
    '''
    standart_type : INTEGER
                | CHAR
                | BOOLEAN
    '''
    #p[0] = p[1]
    p[0] = ['standart_type', p[1]]
    s = Node('standart_type', [], p[1])
    s.display_data()


def p_standart_string(p):
    '''
    standart_string : STRING
                    | STRING OPEN_SQUARE_BR NUMBER CLOSE_SQUARE_BR
    '''
    if len(p) == 2:
        #p[0] = p[1]
        p[0] = ['standart_string', p[1]]
        s = Node('standart_string', [], p[1])
        s.display_data()
    elif len(p) == 5:
        if 0 < p[3] <= 255:
            #p[0] = p[1] + p[2] + str(p[3]) + p[4]
            p[0] = ['standart_string', p[1], p[2], str(p[3]), p[4]]
            s = Node('standart_string', [], [p[2], str(p[3]), p[4]])
            s.display_data()


#------------------------



def p_standart_while(p):
    '''
    standart_while : WHILE OPEN_BR logic_expression CLOSE_BR DO compound_statement
                    | WHILE OPEN_BR logic_expression CLOSE_BR DO simple_statement
                    | WHILE OPEN_BR relational_expression CLOSE_BR DO compound_statement
                    | WHILE OPEN_BR relational_expression CLOSE_BR DO simple_statement
    '''
    #print(len(p), p[1], p[2], p[3], p[4], p[5], p[6])
    #p[0] = p[1] + p[2] + p[3] + p[4] + ' ' + p[5] + ' '+ p[6]
    p[0] = ['standart_while', p[3], p[6]]
    s = Node('standart_while', [p[3], p[6]], [p[1], p[2], p[4], p[5]])
    s.display_data()



def p_standart_for(p):
    '''
    standart_for : FOR ID EQUALITY NUMBER TO NUMBER DO compound_statement
                | FOR ID EQUALITY NUMBER DOWNTO NUMBER DO compound_statement
    '''
    if (p[4] < p[6] and p[5] == 'to') or (p[4] > p[6] and p[5] == 'downto'):
        #p[0] = p[1] + ' ' + p[2] + p[3] + str(p[4]) + ' ' + p[5] + ' ' + str(p[6]) + ' ' + p[7] + p[8]
        p[0] = ['standart_for', p[8]]
        s = Node('standart_for', p[8], [p[1], p[2], p[3], p[4], p[5], p[6], p[7]])
        s.display_data()

#------------------------


#------------------ГРАММАТИКИ_ОБЪЯВЛЕНИЯ_------------------
'''
12. expression -> math_expression
                | logic_expression
                | relational_expression
                | assignment_expression

13. compound_statement ->
    begin
	simple_statement
	end

14. simple_statement -> statement_list

15. statement_list -> statement
                    | statement_list ; statement

16. statement -> assignment_expression | standart_cycle


17. logic_expression -> simple_logic
                    | complex_logic

18. simple_logic -> variable log_sign variable

19. relational_expression -> simple_rel 
                            | complex_rel

20. simple_rel -> variable rel_sign variable 
                | variable rel_sign math_value 
                | variable rel_sign str ###(по сути одно и тоже  с variable rel_sign chr)
                | math_value rel_sign math_value ### бесполезно
                | str rel_sign str ### бесполезно
                | chr rel_sign chr ### бесполезно

21. log_sign -> and | or

22. rel_sign -> = | > | < | <> | >= | <= 

'''



'''

23. assignment_expression -> variable := int_num 
                        | variable := real_num
                        | variable := str 
                        | variable := boolean_value | variable := math_expression
                        | variable := logic_expression


24. math_expression -> simple_math 
                    | complex_math


25. complex_math -> ( simple_math ) math_sign variable
                    | ( simple_math ) math_sign math_value
                    | ( simple_math ) math_sign ( simple_math )
                    | ( complex_math ) math_sign variable
                    | ( complex_math ) math_sign ( simple_math )
                    | ( complex_math ) math_sign ( complex_math )


26. simple_math -> variable math_sign variable
                | variable math_sign math_value
                | math_value math_sign variable
                | math_value math_sign math_value


27. complex_logic -> ( simple_logic ) sign variable 
                    | ( simple_logic ) sign ( simple_logic ) 
	                | ( complex_logic ) sign variable
	                | ( complex _logic ) sign ( simple_logic )

28. complex_rel -> simple_math rel_sign variable
                | complex _math rel_sign variable 
                | math_expression rel_sign math_expression


29. if_then_else_statement -> 
    if_statement
		then_statement
		else_statement ; 
	|
	if_statement
		then_statement ;

30. if_statement -> if logic_expression
                | if relational_expression

31. then_statement -> then compound_statement
                | then simple_statement

32. else_statement -> else compound_statement 
                | else simple_statement

33. boolean_value -> True 
                    | False

34. math_sign -> + | - | / | * | div | mod


'''

#------------------------


def p_assignment_expression(p):
    '''
    assignment_expression : ID EQUALITY NUMBER
                        | ID EQUALITY QUOTE ID QUOTE
                        | ID EQUALITY boolean_value
                        | ID EQUALITY math_expression
                        | ID EQUALITY logic_expression
    '''
    #print(";;;;;", len(p), p[1], p[2], p[3])
    if len(p) == 4:
        #p[0] = p[1] + ' ' + p[2] + ' ' + str(p[3])
        #print(p[0])
        if type(p[3]) == int:
            p[0] = ['assignment_expression', p[1], p[2], str(p[3])]
            s = Node('assignment_expression', [], [p[1], p[2], p[3]])
            s.display_data()

        else:
            p[0] = ['assignment_expression', p[1], p[2], p[3]]
            s = Node('assignment_expression', p[3], [p[1], p[2]])
            s.display_data()

    elif len(p) == 6:
        s = Node('assignment_expression', [], [p[1], p[2], p[3], p[4], p[5]])
        s.display_data()

    #    p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4] + p[5]
    #    p[0] = ['assignment_expression', p[1], p]


def p_relational_expression(p):
    '''
    relational_expression : simple_rel
                            | complex_rel
    '''
    #p[0] = p[1]
    p[0] = ['relational_expression', p[1]]
    s = Node('relational_expression', p[1])
    s.display_data()


def p_complex_rel(p):
    '''
    complex_rel : simple_math rel_sign ID
                | complex_math rel_sign ID
                | ID rel_sign simple_math
                | ID rel_sign complex_math
                | simple_math rel_sign NUMBER
                | complex_math rel_sign NUMBER
                | NUMBER rel_sign simple_math
                | NUMBER rel_sign complex_math
                | OPEN_BR simple_math CLOSE_BR rel_sign ID
                | OPEN_BR complex_math CLOSE_BR rel_sign ID
                | ID rel_sign OPEN_BR simple_math CLOSE_BR
                | ID rel_sign OPEN_BR complex_math CLOSE_BR
                | OPEN_BR simple_math CLOSE_BR rel_sign NUMBER
                | OPEN_BR complex_math CLOSE_BR rel_sign NUMBER
                | NUMBER rel_sign OPEN_BR simple_math CLOSE_BR
                | NUMBER rel_sign OPEN_BR complex_math CLOSE_BR
                | math_expression rel_sign math_expression
                | OPEN_BR math_expression CLOSE_BR rel_sign OPEN_BR math_expression CLOSE_BR
    '''

    if len(p) == 4:
        if (type(p[1]) == int) or (type(p[3]) == int):
            if type(p[1]) == int:
                #p[0] = str(p[1]) + ' ' + p[2] + ' ' + p[3]
                p[0] = ['complex_rel', str(p[1]), p[2], p[3]]
                s = Node('complex_rel', str(p[1]), [p[2], p[3]])
                s.display_data()
            elif type(p[3]) == int:
                #p[0] = p[1] + ' ' + p[2] + ' ' + str(p[3])
                p[0] = ['complex_rel', p[1], p[2], str(p[3])]
                s = Node('complex_rel', [p[1], p[2]], str(p[3]))
                s.display_data()
        else:
            #p[0] = p[1] + ' ' + p[2] + ' ' + p[3]
            p[0] = ['complex_rel', p[1], p[2], p[3]]
            if ('+' in p[1]) or ('-' in p[1]) or ('*' in p[1]) or ('/' in p[1]) or ('mod' in p[1]) or ('div' in p[1]):
                s = Node('complex_rel', [p[1], p[2]], p[3])
                s.display_data()
            else:
                s = Node('complex_rel', [p[2], p[3]], p[1])
                s.display_data()

    if len(p) == 6:
        #print("???", "p[0]=", p[0], "p[1]=", p[1], "p[2]=", p[2], "p[3]=", p[3], "p[4]=", p[4], "p[5]=", p[5])
        if (type(p[1]) == int) or (type(p[5]) == int):
            if type(p[1]) == int:
                #p[0] = str(p[1]) + ' ' + p[2] + ' ' + p[3] + p[4] + p[5]
                p[0] = ['complex_rel', str(p[1]), p[2], p[4]]
                s = Node('complex_rel', [p[2], p[4]], [str(p[1]), p[3], p[5]])
                s.display_data()
                #print("1")
            elif type(p[5]) == int:
                #p[0] = p[1] + p[2] + p[3] + ' ' + p[4] + ' ' +str(p[5])
                p[0] = ['complex_rel', p[2], p[4], str(p[5])]
                #print("2")
                s = Node('complex_rel', [p[2], p[4]], [p[1], p[3], str(p[5])])
                s.display_data()
        else:
            #print("3")
            #if p[2] == '<' or p[2] == '>' or p[2] == '=' or p[2] == '<=' or p[2] == '>=' or p[2] == '<>':
            if p[5] == ')':
                #p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4] + p[5]
                p[0] = ['complex_rel', p[1], p[2], p[4]]
                #print("4")
            #elif p[4] == '<' or p[4] == '>' or p[4] == '=' or p[4] == '<=' or p[4] == '>=' or p[4] == '<>':
            elif p[1] == '(':
                #p[0] = p[1] + p[2] + p[3] + ' ' + p[4] + ' ' + p[5]
                p[0] = ['complex_rel', p[2], p[4], p[5]]
                #print("5")
            s = Node('complex_rel', [p[2], p[4]], [p[1], p[3], p[5]])
            s.display_data()
    elif len(p) == 8:
        #p[0] = p[1] + p[2] + p[3] + ' ' + p[4] + ' ' + p[5] + p[6] + p[7]
        p[0] = ['complex_rel', p[2], p[4], p[6]]
        s = Node('complex_rel', [p[2], p[4], p[6]], [p[1], p[3], p[5], p[7]])
        s.display_data()


def p_math_expression(p):
    '''
    math_expression : simple_math
                    | complex_math
    '''
    p[0] = p[1]
    s = Node("math_expression", p[1])
    #print(p[0].children, p[0].leaf)
    s.display_data()
    #p[0] = ['math_expression', p[1]]
    #print("3")


def p_logic_expression(p):
    '''
    logic_expression : simple_logic
                    | complex_logic
    '''
    #print("logic_expression", p[0], p[1])
    #p[0] = p[1]
    p[0] = ['logic_expression', p[1]]
    s = Node('logic_expression', p[1])
    s.display_data()


def p_complex_math(p):

    '''
    complex_math : OPEN_BR simple_math CLOSE_BR math_sign ID
                | OPEN_BR simple_math CLOSE_BR math_sign NUMBER
                | ID math_sign OPEN_BR simple_math CLOSE_BR
                | NUMBER math_sign OPEN_BR simple_math CLOSE_BR
                | OPEN_BR simple_math CLOSE_BR math_sign OPEN_BR simple_math CLOSE_BR
                | OPEN_BR simple_math CLOSE_BR math_sign OPEN_BR complex_math CLOSE_BR
                | OPEN_BR complex_math CLOSE_BR math_sign ID
                | OPEN_BR complex_math CLOSE_BR math_sign OPEN_BR simple_math CLOSE_BR
                | OPEN_BR complex_math CLOSE_BR math_sign OPEN_BR complex_math CLOSE_BR
    '''

    #print(p[0], p[1], p[2], p[3], p[4], p[5])
    if len(p) == 6:
        if type(p[5]) == int:
            #p[0] = p[1] + p[2] + p[3] + ' ' + p[4] + ' ' + str(p[5])
            p[0] = ['complex_math', p[2], p[4], str(p[5])]
            s = Node('complex_math', [p[2], p[4]], [p[1], p[3], str(p[5])])
            s.display_data()

            #l = []
            #l.append(p[2].left)
            #l.append(p[2].op)
            #l.append(p[2].right)
            #llvm_file_complex_math.complex_math_three_objects(l, p[4].math_sign, p[5])

        elif type(p[1]) == int:
            #p[0] = str(p[1]) + ' ' + p[2] + ' ' + p[3] + p[4] + p[5]
            p[0] = ['complex_math', str(p[1]), p[2], p[4]]
            s = Node('complex_math', [p[2], p[4]], [str(p[1]), p[3], p[5]])
            s.display_data()
            #llvm_file_complex_math.complex_math_three_objects(p[4].children, p[2].math_sign, p[1])

        else:
            if p[2] == '+' or p[2] == '-' or p[2] == '/' or p[2] == '*' or p[2] == 'div' or p[2] == 'mod':
                #p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4] + p[5]
                p[0] = ['complex_math', p[1], p[2], p[4]]
                s = Node('complex_math', [p[2], p[4]], [p[1], p[3], p[5]])
                s.display_data()
            elif p[4] == '+' or p[4] == '-' or p[4] == '/' or p[4] == '*' or p[4] == 'div' or p[4] == 'mod':
                #p[0] = p[1] +  p[2] + p[3] + ' ' + p[4] + ' ' + p[5]
                p[0] = ['complex_math', p[2], p[4], p[5]]
                s = Node('complex_math', [p[2], p[4]], [p[1], p[3], p[5]])
                s.display_data()

    elif len(p) == 8:
        #p[0] = p[1] + p[2] + p[3] + ' ' + p[4] + ' ' + p[5] + p[6] + p[7]
        p[0] = ['complex_math', p[2], p[4], p[6]]
        s = Node('complex_math', [p[2], p[4], p[6]], [p[1], p[3], p[5], p[7]])
        s.display_data()
    #print("3")


def p_complex_logic(p):
    '''
    complex_logic : OPEN_BR simple_logic CLOSE_BR log_sign ID
                    | OPEN_BR simple_logic CLOSE_BR log_sign OPEN_BR simple_logic CLOSE_BR
	                | OPEN_BR complex_logic CLOSE_BR log_sign ID
	                | OPEN_BR complex_logic CLOSE_BR log_sign OPEN_BR simple_logic CLOSE_BR
    '''
    #print("complex_logic", p[0], p[1])
    if len(p) == 6:
        #p[0] = p[1] + p[2] + p[3] + ' ' + p[4] + ' ' + p[5]
        p[0] = ['complex_logic', p[2], p[4], p[5]]
        s = Node('complex_logic', [p[2], p[4]], [p[1], p[3], p[5]])
        s.display_data()
    elif len(p) == 8:
        #p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
        p[0] = ['complex_logic', p[2], p[4], p[5]]
        s = Node('complex_logic', [p[2], p[4], p[6]], [p[1], p[3], p[5], p[7]])
        s.display_data()


def p_simple_math(p):
    '''
    simple_math : ID math_sign ID
                | ID math_sign NUMBER
                | NUMBER math_sign ID
                | NUMBER math_sign NUMBER
    '''
    #print("||||", p[0], p[1], p[2], p[3])
    #p[0] = str(p[1]) + ' ' + p[2] + ' ' + str(p[3])
    #p[0] = Node("simple_math", p[2], [p[1], p[3]])
    p[0] = Simple_math(p[1], p[2].math_sign, p[3])
    #print("children:", p[0].children, "leaf:", p[0].leaf)
    #p[0].display_data()

    s = Node('simple_math', p[2], [p[1], p[3]])
    s.display_data()
    #print('aaaaaaaa оно здесь!!!', p[1], p[2].math_sign, p[3])

    #llvm_file.sum_two_parts(p[1], p[2].math_sign, p[3])

    #myCmd = os.popen('lli /Users/maksimalsevskih/Downloads/IU7/IU7sem2/compiler/Kurs_work/f1.ll').read()
    #print("результат сложения", myCmd)

    #print("4")


    
    #p[0] = ['simple_math', str(p[1]), p[2], str(p[3])]



def p_compound_statement(p):
    '''
    compound_statement : BEGIN simple_statement END
    '''
    #p[0] =  '\n' + p[1] + '\n' + ' ' + p[2] + '\n' + p[3]
    p[0] = ['compound_statement', p[1], p[2], p[3]]
    s = Node('compound_statement', p[2], [p[1], p[3]])
    s.display_data()


def p_simple_statement(p):
    '''
    simple_statement : statement_list
                    | empty
    '''
    #print(p[0], p[1])
    #p[0] = p[1]
    p[0] = ['simple_statement', p[1]]

    s = Node('simple_statement', p[1])
    s.display_data()


def p_statement_list(p):
    '''
    statement_list : statement
                    | statement_list SEMICOLON statement
    '''
    #print(p[0], p[1])
    if len(p) == 2:
        #p[0] = p[1]
        p[0] = ['statement_list', p[1]]
        s = Node('statement_list', p[1])
        s.display_data()
        #print("----")
    elif len(p) == 4:
        #p[0] = p[1] + p[2] + '\n' + ' ' + p[3]
        p[0] = ['statement_list', p[1], p[3]]
        s = Node('statement_list', [p[1], p[3]], p[2])
        s.display_data()



def p_statement(p):
    '''
    statement : assignment_expression
            | standart_cycle
    '''
    #p[0] = p[1]
    p[0] = ['statement', p[1]]
    s = Node('statement', p[1])
    s.display_data()



def p_simple_logic(p):
    '''
    simple_logic : ID log_sign ID
    '''
    #print("simple_logic", p[0], p[1], p[2], p[3])
    #p[0] = p[1] + ' ' + p[2] + ' ' + p[3]
    p[0] = ['simple_logic', p[1], p[2], p[3]]
    s = Node('simple_logic', p[2], [p[1], p[3]])
    s.display_data()


def p_simple_rel(p):
    '''
    simple_rel : ID rel_sign ID
                | ID rel_sign NUMBER
                | ID rel_sign QUOTE ID QUOTE
    '''
    #print("simple_rel", p[0], p[1], p[2], p[3])
    if len(p) == 4:
        #print("###", p[0])
        #p[0] = p[1] + ' ' + p[2] + ' ' + str(p[3])
        p[0] = ['simple_rel', p[1], p[2], str(p[3])]
        s = Node('simple_rel', p[2], [p[1], p[3]])
        s.display_data()
    elif len(p) == 6:
        #p[0] = p[1] + ' ' + p[2] + ' ' + p[3] + p[4] + p[5]
        p[0] = ['simple_rel', p[1], p[2], p[3], p[4], p[5]]
        s = Node('simple_rel', p[2], [p[1], p[3], p[4], p[5]])
        s.display_data()


def p_log_sign(p):
    '''
    log_sign : AND
            | OR
    '''
    #p[0] = p[1]
    p[0] = ['log_sign', p[1]]
    s = Node('log_sign', [], p[1])
    s.display_data()


def p_rel_sign(p):
    '''
    rel_sign : MORE_OR_EQUAL
            | LESS_OR_EQUAL
            | NOT_EQUAL
            | MORE
            | LESS
            | EQUALS
    '''
    #print("rrrr", p[0], p[1])
    #p[0] = p[1]
    p[0] = ['rel_sign', p[1]]
    s = Node('rel_sign', [], p[1])
    s.display_data()


def p_boolean_value(p):
    '''
    boolean_value : TRUE
                    | FALSE
    '''
    #p[0] = p[1]
    p[0] = ['boolean_value', p[1]]
    s = Node('boolean_value', [], p[1])


def p_math_sign(p):
    '''
    math_sign : PLUS
                | MINUS
                | DIVISION
                | MULTIPLICATION
                | DIV
                | MOD
    '''
    #p[0] = p[1]
    #p[0] = ['math_sign', p[1]]
    p[0] = Math_sign(p[1])
    #print(p[0], p[0].math_sign)
    p[0].display_data()
    #print("5")


def p_empty(p):
    'empty :'
    pass


def p_error(p):
    #print("aaaa", p)
    print(f'Syntax error at {p.value!r}')



lexer = lex()

parser = yacc()




ex1 = '''var counter:integer;'''

ex2 = '''var i,j,n:integer;
                w:char;
                a,b:boolean;
                l:array[1..10] of integer;
                s1:string;
                s2:string[10];'''

ex3 = '''function f2(r,u:boolean):integer;'''

#expressions
ex4 = '''(10 div 2) / (12 / (s + 1))'''

ex5 = '''qwe := (10 div 2) / (12 / (s + 1))'''

ex6 = '''( (c / 2) - 4) = abc'''

ex7= '''(((a and b) and d) or qwe ) or c'''

ex8 = '''while (a >= b) do 
            begin
                i := i + 1;
                qwe := (10 div 2) / (12 / (s + 1))
            end'''

ex9 = '''for i:=1 to 10 do
            begin
                i := i + 1;
                qwe := (10 div 2) / (12 / (s + 1))
            end
            '''

ex10 = '''if (a > b) then a:=a+1; b:=2
                else c:=1'''

ex11 = '''(4 + 3) / ( 9 -  2)'''

ex12 = '''10 * 5'''

ex13 = '''(4 + 6) / 2'''




#----------

print("example: ", ex9)
ast = parser.parse(ex9)
print("-------------")
print(ast_list)
for i in ast_list:
    print(i.display_data)

lis_of_v = []

def printing(prev, header, counter, ast, list_of_el):
    a_tree = graphviz.Digraph('AST', filename='AST.gv',
                         node_attr={'color': 'lightblue2', 'style': 'filled'})
    a_tree.attr(size='8,5')

    #print("НОВЫЙ:", ast)
    if len(ast) > 1 and type(ast) == list:
        print(ast[0], '-', ast[1:])

        #if prev == ast[0]:
        #    a_tree.node('El' + str(counter), label=ast[0])
        #    print( ast[0], '-', 'El' + str(counter))
        #    counter = counter + 1
        #else:
        #    if ast[0] not in header:
        #        a_tree.node('El' + str(counter), label=ast[0])
        #        header.append(ast[0])
        #        print( ast[0], '-', 'El' + str(counter))
        #        counter = counter + 1


        #-----------
        #print("s:", len(s[0]), s[0])
        #if len(ast) > 1:
        for i in range(1, len(ast)):
            if type(ast[i]) == list:
                a = []
                a.append(ast[0])
                a.append(ast[i][0])
                list_of_el.append(a)
                #a_tree.edge(ast[0], ast[i][0])
                #if prev != ast[i][0]:
                #    if ast[i][0] not in header:
                #        a_tree.node('El' + str(counter), label=ast[i][0])
                #        header.append(ast[i][0])
                #        print(ast[i][0], '-', 'El' + str(counter))
                #        counter = counter + 1
                #else:
                #    a_tree.node('El' + str(counter), label=ast[i][0])
                #    print(ast[i][0], '-', 'El' + str(counter))
                #    counter = counter + 1

            else:
                a = []
                a.append(ast[0])
                a.append(ast[i])
                list_of_el.append(a)
                #a_tree.edge(ast[0], ast[i])

                #if prev != ast[i]:
                #    if ast[i] not in header:
                #        a_tree.node('El' + str(counter), label=ast[i])
                #        header.append(ast[i])
                #        print(ast[i], '-', 'El' + str(counter))
                #        counter = counter + 1
                #else:
                #    a_tree.node('El' + str(counter), label=ast[i])
                #    print(ast[i][0], '-', 'El' + str(counter))
                #    counter = counter + 1

        #-----------
        for i in range(1, len(ast)):
            printing(prev, header, counter, ast[i], list_of_el)
    return list_of_el


def moving_in_ast(ast):
    print("!!!!", ast)
    if ast[0] == 'main_rule':
        n1_ast = ast[1]
        if n1_ast[0] == 'declarations':
            print('Объявление')
            for i in range(1, len(n1_ast)):
                if type(n1_ast[i]) == list:
                    print(n1_ast[i])
        elif n1_ast[0] == 'standart_subprogram':
            print('Подпрограмма (функция)')
        elif n1_ast[0] == 'if_statement':
            print('if выражение')
        elif n1_ast[0] == 'expression':
            n2_ast = n1_ast[1]
            print('Выражение', n2_ast)
            if n2_ast[0] == 'math_expression':
                print("Математическое")
                n3_ast = n2_ast[1]
                if n3_ast[0] == "simple_math":
                    print("Простое выражение", n3_ast)
                    for i in range(1, len(n3_ast)):
                        print(n3_ast[i])
                elif n3_ast[0] == "complex_math":
                    print("Сложное выражение",n3_ast)
            elif n2_ast[0] == 'logic_expression':
                print("Логическое")
            elif n2_ast[0] == 'relational_expression':
                print("Отношение")
            elif n2_ast[0] == 'assignment_expression':
                print("Присвоение")
        elif n1_ast[0] == 'standart_cycle':
            print('Стандартный цикл')



print("start: ", ast, ast.children)
c = 0
header = []
prev = ''
#moving_in_ast(ast)
#l1 = printing(prev, header, c, ast, lis_of_v)

#print("АСД как список:", l1)

'''
1. standart_type -> integer  | char | boolean
2. standart_string -> string | string [num]
3. identifier_list -> id | identifier_list, id
4. declarations -> var identifier_list: type;
4.1. complex_declar -> identifier_list: type; | complex_declar identifier_list: type;
5. type -> standart _type | array [int_num … int_num] of standart_type | standart_string
6. standart_subprogram -> function id args : standart_type ;
7. args -> ( parameter_list ) | -
8. parameter_list -> identifier_list : type | parameter_list ; identifier_list : type
9. standart_cycle -> standart_while  | standart_for
10. standart_while -> while ( logic_expression )  do compound_statement
	| while ( logic_expression )  do simple_statement
	| while ( relational_expression )  do simple_statement
	| while ( relational_expression )  do simple_statement
11. standart_for -> for variable := int_num to int_num do compound_statement | for variable := int_num downto int_num do compound_statement
expression -> math_expression | logic_expression | relational_expression | assignment_expression
12. compound_statement -> 
	begin
	simple_statement
	end
13. assignment_expression -> variable := int_num | variable := real_num | variable := str 
	| variable := boolean_value | variable := math_expression
	| variable := logic_expression
14. math_value -> int_num | real_num
15. boolean_value -> True | False
16. math_expression -> simple_math | complex_math
17. simple_math -> variable math_sign variable | variable math_sign math_value | math_value math_sign variable | math_value math_sign math_value
18. math_sign -> + | - | / | * | div | mod
19. complex_math -> ( simple_math ) math_sign variable | ( simple_math ) math_sign math_value 
    | ( simple_math ) math_sign ( simple_math ) 
    | ( complex_math ) math_sign variable | ( complex_math ) math_sign ( simple_math ) | ( complex_math ) math_sign ( complex_math )
20. logic_expression -> simple logic | complex_logic
21. simple logic -> variable log_sign variable
22. log_sign -> not | and | or |
23. complex_logic -> ( simple_logic ) sign variable | ( simple_logic ) sign ( simple_logic ) 
	| ( complex_logic ) sign variable | ( complex _logic ) sign ( simple_logic )
24. relational_expression -> simple_rel | complex_rel
25. simple_rel -> variable rel_sign variable | variable rel_sign math_value 
    | variable rel_sign str 
    | variable rel_sign chr 
    | math_value rel_sign math_value 
    | str  rel_sign str 
    | chr rel_sign chr
26. complex_rel -> simple_math rel_sign variable
    | complex _math rel_sign variable 
    | math_expression rel_sign math_expression
27. rel_sign -> = | > | < | <> | >= | <= 
28. simple_statement -> statement_list | -
29. statement_list -> statement | statement_list ; statement
30. if_then_else_statement ->
	if_statement
		then_statement
		else_statement ; 
	|
	if_statement
		then_statement ;
31. if_statement -> if logic_expression | if relational_expression
32. then_statement -> then compound_statement | then simple_statement
33. else_statement -> else compound_statement | else simple_statement
34. statement -> assignment_expression | standart_cycle | complex_statement
'''


'''
#Сложение 2-х чисел типа integer
integer = ir.IntType(32)
fnty = ir.FunctionType(integer, ())

func = ir.Function(m, fnty, name="main")
# Now implement the function
block = func.append_basic_block(name="entry")
builder = ir.IRBuilder(block)

result = builder.add(ir.Constant(integer, 5), ir.Constant(integer, 4), name="res")

fmt_arg = builder.bitcast(global_fmt, voidptr_ty)
builder.call(printf, [fmt_arg, result])
builder.ret(result)

print(m)
'''