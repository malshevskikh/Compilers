import re
import sys

'''
1-ОЕ ПРАВИЛО: <программа> -> <блок>
2-ОЕ ПРАВИЛО: <блок> -> { <список операторов> }
3-Е ПРАВИЛО: <список операторов> -> <оператор> <хвост> | <оператор>
4-ОЕ ПРАВИЛО: <хвост> -> ; <оператор> <хвост> | ; <оператор>
5-ОЕ ПРАВИЛО: <оператор> -> <идентификатор>==<выражение> | <блок>
6-ОЕ ПРАВИЛО: <выражение> -> <простое выражение> | <простое выражение> <операция отношения> <простое выражение>
7-ОЕ ПРАВИЛО: <простое выражение> -> <терм> | <знак> <терм> | <простое выражение> <операция типа сложения> <терм>
8-ОЕ ПРАВИЛО: <терм> -> <фактор> | <терм> <операция типа умножения> <фактор>
9-ОЕ ПРАВИЛО: <фактор> -> <идентификатор> | <константа> | ( < простое выражение > ) | not <фактор>
-----------------------------------------------------------------
10-ОЕ ПРАВИЛО: <операция отношения> -> = | <> | < | <= | > | >=
11-ОЕ ПРАВИЛО: <знак> -> +|-
12-ОЕ ПРАВИЛО: <операция типа сложения> -> + | - | or
13-ОЕ ПРАВИЛО: <операция типа умножения> -> * | / | div | mod | and
'''

'''
E - Expression - <выражение>
S - Simple expression - <простое выражение>
T - Term - <терм>
F - Factor - <фактор>
r - relational operation - <операция отношения>
s - sign - <знак>
a - addition - <операция типа сложения>
m - multiplication - <операция типа умножения>
'''


P = [["E", "S", "SrS"],
     ["S", "T", "sT", "SaT"],
     ["T", "F", "TmF"],
     ["F", "id", "const", "(S)", "notF"],
     ["r", "=", "<>", "<", "<=", ">", ">="],
     ["s", "+", "-"],
     ["a", "+", "-", "or"],
     ["m", "*", "/", "div", "mod", "and"]]


example = "((a+b)>=(c/2))"
example1 = "b*c*12<>d-f+e"
example2 = "((aBc+b)=(c/2))"
example3 = "((a+b)<=(c/2))"
example4 = "((a<b)<>(c/2))"
example5 = "((-((a+b)-c)/3))"
example6 = "((a+b)-5/2+q<a/b+123-0)"
example7 = "((amod2)div3>=(c/b*2))"
example8 = "((a<2)div3>=(c/b*2))"

main_example = "int main() { M==((a+b)>=(c/2)) }"
main_example2 = "void main() { A==((a+b)-5/2+q)div20; C==u/12+s*999; { B==((-((a+b)-c)/3)) }}"
main_example3 = "int main() { A==((a+b)-5/2+q)div20; C==u/12+s*999; B==((-((a+b)-c)/3)) }"

example9 = "((a+b)-5/2+q)div20"

def Parser(P, ex, main_ex):
    print('''
1-ОЕ ПРАВИЛО: <программа> -> <блок>
2-ОЕ ПРАВИЛО: <блок> -> { <список операторов> }
3-Е ПРАВИЛО: <список операторов> -> <оператор> <хвост> | <оператор>
4-ОЕ ПРАВИЛО: <хвост> -> ; <оператор> <хвост> | ; <оператор>
5-ОЕ ПРАВИЛО: <оператор> -> <идентификатор>==<выражение> | <блок>
6-ОЕ ПРАВИЛО: <выражение> -> <простое выражение> | <простое выражение> <операция отношения> <простое выражение>
7-ОЕ ПРАВИЛО: <простое выражение> -> <терм> | <знак> <терм> | <простое выражение> <операция типа сложения> <терм>
8-ОЕ ПРАВИЛО: <терм> -> <фактор> | <терм> <операция типа умножения> <фактор>
9-ОЕ ПРАВИЛО: <фактор> -> <идентификатор> | <константа> | ( < простое выражение > ) | not <фактор>
-----------------------------------------------------------------
10-ОЕ ПРАВИЛО: <операция отношения> -> = | <> | < | <= | > | >=
11-ОЕ ПРАВИЛО: <знак> -> +|-
12-ОЕ ПРАВИЛО: <операция типа сложения> -> + | - | or
13-ОЕ ПРАВИЛО: <операция типа умножения> -> * | / | div | mod | and
''')
    print(main_ex)
    print(ex)
    #Проверка на парвило E->S|SrS
    #first_rule(ex)
    fifth_rule(main_ex)

def first_rule(exp):
    print("6-ОЕ ПРАВИЛО: <выражение> -> <простое выражение> | <простое выражение> <операция отношения> <простое выражение>  ДЛЯ", exp)
    regular1 = "((=)|(<>)|(>=)|(>)|(<=)|(<))"
    #проверка на 1-е парвило
    x = re.search(regular1, exp)
    if x == None:
        # exp - <простое выражение>
        #print("<простое выражение>")
        #print(exp)
        exp = delete_brackets(exp)
        #print(exp)
        print("Удаление лишних, ненужных скобок, если такие имеются:", exp)
        #list_of_relational_oper = find_relational_operation(exp)
        #Проверка на о, что нужно еще раскрывать скобки или нет
        list_of_br, exp = find_brackets_and_relatioanl_operation(exp)
        #print(list_of_br, exp)
        list_of_simple_expressions = []
        list_of_simple_expressions.append(exp)
        print(list_of_simple_expressions, "- <простое выражение>")
    else:
        # exp - <простое выражение> <операция отношения> <простое выражение>
        #print("<простое выражение> <операция отношения> <простое выражение>")
        exp = delete_brackets(exp)
        print("Удаление лишних, ненужных скобок, если такие имеются:", exp)
        list_of_relational_oper = find_relational_operation(exp)
        #Проверка на о, что нужно еще раскрывать скобки или нет
        list_of_br, exp = find_brackets_and_relatioanl_operation(exp)
        #print("dddd", list_of_br, exp)
        list_of_simple_expressions = cut_exp(exp, list_of_br, list_of_relational_oper)
        #print("Список простых выражений:", list_of_simple_expressions)
        #l = re.search(">=", exp)
        #print(l.start(), l.end())
        print(list_of_simple_expressions, "- <простое выражение> <операция отношения> <простое выражение>")
    second_rule(list_of_simple_expressions)


def delete_brackets(ex):
    # Проверка на скобки
    counter_of_brackets = 0
    indexes_open_brackets = []
    indexes_close_brackets = []
    ex_str = ''
    for i in range(0, len(ex)):
        if ex[i] == "(" or ex[i] == ")":
            counter_of_brackets = counter_of_brackets + 1
            if ex[i] == "(":
                indexes_open_brackets.append(i)
            elif ex[i] == ")":
                indexes_close_brackets.append(i)
    #print(counter_of_brackets, indexes_open_brackets, indexes_close_brackets)

    if len(indexes_open_brackets) != len(indexes_close_brackets):
        print("ОШИБКА! отуствует одна открывающая или закрывающая скобка")
        sys.exit()
    # нет ошибки при проверке на скобки
    elif len(indexes_open_brackets) == len(indexes_close_brackets) and indexes_open_brackets != [] and indexes_close_brackets != []:
        list_of_ex_in_br = []
        if ex[0] == "(" and ex[len(ex) - 1] == ")" and len(indexes_open_brackets) > 1 and len(indexes_close_brackets) > 1:
            flag_for_brackets = False
            for i in range(1, len(ex) - 1):
                #print(ex[i])
                if ex[i] == "(":
                    flag_for_brackets = False
                elif ex[i] == ")":
                    flag_for_brackets = True
            if flag_for_brackets == True:
                #print("ок")
                ex_l = list(ex)
                #print(ex_l)
                ex_l.pop(0)
                ex_l.pop(-1)
                #print(ex_l)
                ex_str = ''.join(ex_l)
                #print(ex_str)
            elif flag_for_brackets == False:
                print("ОШИБКА! отуствует одна открывающая или закрывающая скобка")
                sys.exit()
        else:
            ex_str = ex
    else:
        ex_str = ex
    return ex_str


def find_relational_operation(ex):
    #print("rrrrr:", ex)
    l = []
    for i in range(0, len(ex)):
        a = []
        if ex[i] == "=":
            if ex[i-1] != "<" and ex[i-1] != ">":
                a.append(i)
                a.append(ex[i])
                l.append(a)
        elif ex[i] == "<":
            if ex[i-1] != "=":
                if ex[i+1] == "=" or ex[i+1] == ">":
                    a.append(i)
                    a.append(ex[i])
                    a.append(i+1)
                    a.append(ex[i+1])
                else:
                    a.append(i)
                    a.append(ex[i])
                l.append(a)
        elif ex[i] == ">":
            if ex[i-1] != "<":
                if ex[i + 1] == "=":
                    a.append(i)
                    a.append(ex[i])
                    a.append(i+1)
                    a.append(ex[i+1])
                else:
                    a.append(i)
                    a.append(ex[i])
                l.append(a)
    #print(l)
    return l


def find_brackets_and_relatioanl_operation(ex):
    # Проверка на скобки
    indexes_open_brackets = []
    indexes_close_brackets = []
    ex_str = ''
    for i in range(0, len(ex)):
        if ex[i] == "(" or ex[i] == ")":
            if ex[i] == "(":
                indexes_open_brackets.append(i)
            elif ex[i] == ")":
                indexes_close_brackets.append(i)
    #print(indexes_open_brackets, indexes_close_brackets)
    f1 = True
    a = []
    l = []
    for i in range(0, len(ex)):
        #print(i)
        if i in indexes_open_brackets:
            if f1 == False:
                l.append(a)
                a = []
                a.append(i)
                f1 = False
            elif f1 == True:
                a.append(i)
                f1 = False
        elif i in indexes_close_brackets:
            #print("RRRRR")
            if f1 == False:
                a.append(i)
                l.append(a)
                a = []
                f1 = True
            elif f1 == True:
                #print("qqqq", l)
                j = len(l) - 1
                f2 = True
                while f2 != False:
                    if len(l[j]) > 1:
                        j = j - 1
                    elif len(l[j]) == 1:
                        l[j].append(i)
                        f2 = False
                    elif j == 0:
                        f2 = False
    new_ex = ''
    f3 = False
    for i in range(len(l)):
        if l[i][0] == 0 and l[i][1] == len(ex) - 1:
            new_ex = delete_brackets(ex)
            f3 = True
    if f3 == True:
        find_brackets_and_relatioanl_operation(new_ex)
    elif f3 == False:
        new_ex = ex
    return l, new_ex


def cut_exp(ex, list_of_brackets, list_of_r_o):
    res = []
    if len(list_of_r_o) == 1:
        #print(list_of_r_o)
        if len(list_of_r_o[0]) > 2:
            #print(list_of_brackets)
            f1 = True
            for i in range(0, len(list_of_brackets)):
                if list_of_brackets[i][0] < list_of_r_o[0][0] < list_of_brackets[i][1] and list_of_brackets[i][0] < list_of_r_o[0][2] < list_of_brackets[i][1]:
                    f1 = False
            if f1 == False:
                print("Ошибка, конструкция выражения построена неправильно нкжно либо <простое выражение> | <простое выражение> <операция отношения> <простое выражение>")
                sys.exit()
            else:
                #print("Все ок")
                p1 = ex[:list_of_r_o[0][0]]
                p2 = ex[list_of_r_o[0][2] + 1:]
                res.append(p1)
                res.append(p2)
        elif len(list_of_r_o[0]) == 2:
            f1 = True
            for i in range(0, len(list_of_brackets)):
                if list_of_brackets[i][0] < list_of_r_o[0][0] < list_of_brackets[i][1]:
                    f1 = False
            if f1 == False:
                print("Ошибка, конструкция выражения построена неправильно нкжно либо <простое выражение> | <простое выражение> <операция отношения> <простое выражение>")
                sys.exit()
            else:
                print("Все ок")
                p1 = ex[:list_of_r_o[0][0]]
                p2 = ex[list_of_r_o[0][0] + 1:]
                res.append(p1)
                res.append(p2)
    elif len(list_of_r_o) > 1:
        print("Ошибка, конструкция выражения построена неправильно нкжно либо <простое выражение> | <простое выражение> <операция отношения> <простое выражение>")
        sys.exit()
    return res


def find_brackets_addition(s):
    # Проверка на скобки

    indexes_open_brackets = []
    indexes_close_brackets = []
    ex_str = ''
    for i in range(0, len(s)):
        if s[i] == "(" or s[i] == ")":
            if s[i] == "(":
                indexes_open_brackets.append(i)
            elif s[i] == ")":
                indexes_close_brackets.append(i)
    # print(indexes_open_brackets, indexes_close_brackets)
    f1 = True
    a = []
    l = []
    for i in range(0, len(s)):
        # print(i)
        if i in indexes_open_brackets:
            if f1 == False:
                l.append(a)
                a = []
                a.append(i)
                f1 = False
            elif f1 == True:
                a.append(i)
                f1 = False
        elif i in indexes_close_brackets:
            # print("RRRRR")
            if f1 == False:
                a.append(i)
                l.append(a)
                a = []
                f1 = True
            elif f1 == True:
                # print("qqqq", l)
                j = len(l) - 1
                f2 = True
                while f2 != False:
                    if len(l[j]) > 1:
                        j = j - 1
                    elif len(l[j]) == 1:
                        l[j].append(i)
                        f2 = False
                    elif j == 0:
                        f2 = False
    #Поиск операций сложения
    #print(l)
    l_a = []
    b = []
    for i in range(0, len(s)):
        if s[i] == "+" or s[i] == "-":
            b.append(i)
            l_a.append(b)
            b = []
        elif s[i] == "o" and s[i+1] == "r":
            b.append(i)
            b.append(i+1)
            l_a.append(b)
            b = []
    #print(l_a)
    return l, l_a

def second_rule(list_of_s_e):
    print("7-ОЕ ПРАВИЛО: <простое выражение> -> <терм> | <знак> <терм> | <простое выражение> <операция типа сложения> <терм> ДЛЯ:", list_of_s_e)
    for i in range(0, len(list_of_s_e)):
        if list_of_s_e[i][0] == "+" or list_of_s_e[i][0] == "-":
            z = list_of_s_e[i][0]
            #print(list_of_s_e[i])
            list_of_s_e[i] = list_of_s_e[i][1:]
            #print(list_of_s_e[i])
            print(z, "- знак;",list_of_s_e[i], "- <терм>.")
            third_rule(list_of_s_e[i])
        if list_of_s_e[i][len(list_of_s_e[i])-1] == "+" or list_of_s_e[i][len(list_of_s_e[i])-1] == "-" or list_of_s_e[i][len(list_of_s_e[i])-1] == "/" or list_of_s_e[i][len(list_of_s_e[i])-1] == "*":
            print("Ошибка, конструкция выражения построена неправильно на конце не должно быть знака")
            sys.exit()
        list_of_br, list_of_add = find_brackets_addition(list_of_s_e[i])
        if list_of_br == [] and list_of_add == []:
            print(list_of_s_e[i], "- <терм>.")
            third_rule(list_of_s_e[i])
        elif list_of_br != [] and list_of_add == []:
            print(list_of_s_e[i], "- <терм>.")
            third_rule(list_of_s_e[i])
        elif list_of_add != [] and list_of_br != []:
            #print("1", list_of_br)
            #print("2", list_of_add)
            list_of_a_in_br = check_addition_in_br(list_of_s_e[i], list_of_add, list_of_br)
            #print("list_of_a_in_br", list_of_a_in_br)
            if list_of_a_in_br != []:
                if len(list_of_a_in_br[len(list_of_a_in_br) - 1]) == 1:
                    h = list_of_a_in_br[len(list_of_a_in_br) - 1][0]
                    part1 = list_of_s_e[i][:h]
                    part2 = list_of_s_e[i][h+1:]
                    #print("part1", part1)
                    #print("part2", part2)
                    print(part1, "- <простое выражение>;", list_of_s_e[i][h], "- <операция типа сложения>;", part2, "- <терм>.")
                    part_list1 = []
                    part_list1.append(part1)
                    second_rule(part_list1)
                    third_rule(part2)
                elif len(list_of_a_in_br[len(list_of_a_in_br) - 1]) == 2:
                    h = list_of_a_in_br[len(list_of_a_in_br) - 1][0]
                    e = list_of_a_in_br[len(list_of_a_in_br) - 1][1]
                    part1 = list_of_s_e[i][:h]
                    part2 = list_of_s_e[i][e+1:]
                    print(part1, "- <простое выражение>;", list_of_s_e[i][h] + list_of_s_e[i][e], "- <операция типа сложения>;", part2, "- <терм>.")
                    part_list1 = []
                    part_list1.append(part1)
                    second_rule(part_list1)
                    third_rule(part2)
            elif list_of_a_in_br == []:
                print(list_of_s_e[i], "- <терм>.")
                third_rule(list_of_s_e[i])
        elif list_of_add != [] and list_of_br == []:
            #print("list_of_add", list_of_add)
            if len(list_of_add[len(list_of_add) - 1]) == 1:
                h = list_of_add[len(list_of_add) - 1][0]
                part1 = list_of_s_e[i][:h]
                part2 = list_of_s_e[i][h + 1:]
                print(part1, "- <простое выражение>;", list_of_s_e[i][h], "- <операция типа сложения>;", part2, "- <терм>.")
                part_list1 = []
                part_list1.append(part1)
                second_rule(part_list1)
                third_rule(part2)
            elif len(list_of_add[len(list_of_add) - 1]) == 2:
                h = list_of_add[len(list_of_add) - 1][0]
                e = list_of_add[len(list_of_add) - 1][1]
                part1 = list_of_s_e[i][:h]
                part2 = list_of_s_e[i][e + 1:]
                print(part1, "- <простое выражение>;", list_of_s_e[i][h] + list_of_s_e[i][e], "- <операция типа сложения>;", part2, "- <терм>.")
                part_list1 = []
                part_list1.append(part1)
                second_rule(part_list1)
                third_rule(part2)



def check_addition_in_br(s, l1, l2):
    #print()
    list_of_a = []
    for i in range(0, len(l1)):
        list_of_a.append(l1[i])
    for i in range(0, len(l1)):
        #print(l1[i])
        #print(list_of_a)
        if len(l1[i]) == 1:
            for j in range(0, len(l2)):
                if l2[j][0] < l1[i][0] < l2[j][1]:
                    if l1[i] in list_of_a:
                        list_of_a.remove(l1[i])
        elif len(l1[i]) == 2:
            for j in range(0, len(l2)):
                if l2[j][0] < l1[i][0] < l2[j][1] and  l2[j][0] < l1[i][1] < l2[j][1]:
                    if l1[i] in list_of_a:
                        list_of_a.remove(l1[i])
    #print(list_of_a)
    return list_of_a


def third_rule(expression):
    print("8-ОЕ ПРАВИЛО <терм> -> <фактор> | <терм> <операция типа умножения> <фактор> ДЛЯ:", expression)
    if expression[0] == "*" or expression[0] == "/":
        print("Ошибка, конструкция выражения построена неправильно в начале не должно быть знака")
        sys.exit()
    elif expression[len(expression) - 1] == "*" or expression[len(expression) - 1] == "/":
        print("Ошибка, конструкция выражения построена неправильно на конце не должно быть знака")
        sys.exit()
    stroka = expression[len(expression)-3:]
    if stroka == "mod" or stroka == "div" or stroka == "and":
        print("Ошибка, конструкция выражения построена неправильно на конце не должно быть данной конструкции")
        sys.exit()
    list_of_br, list_of_milti_oper = find_brackets_and_multiplication_oper(expression)
    #print("Список скобок", list_of_br)
    #print("Список операторов уиножения", list_of_milti_oper)
    if list_of_br == [] and list_of_milti_oper == []:
        print(expression, "- <фактор>")
        fourph_rule(expression)
    elif list_of_br != [] and list_of_milti_oper == []:
        print(expression, "- <фактор>")
        fourph_rule(expression)
    elif list_of_br != [] and list_of_milti_oper != []:
        list_of_multi_not_in_br = check_multiplication_in_br(list_of_milti_oper, list_of_br)
        if list_of_multi_not_in_br != []:
            if len(list_of_multi_not_in_br[len(list_of_multi_not_in_br) - 1]) == 1:
                h = list_of_multi_not_in_br[len(list_of_multi_not_in_br) - 1][0]
                part1 = expression[:h]
                part2 = expression[h + 1:]
                # print("part1", part1)
                # print("part2", part2)
                print(part1, "- <терм>;", expression[h], "- <операция типа умножения>;", part2, "- <фактор>.")
                third_rule(part1)
                fourph_rule(part2)

            elif len(list_of_multi_not_in_br[len(list_of_multi_not_in_br) - 1]) == 3:
                h = list_of_multi_not_in_br[len(list_of_multi_not_in_br) - 1][0]
                e = list_of_multi_not_in_br[len(list_of_multi_not_in_br) - 1][2]
                part1 = expression[:h]
                part2 = expression[e + 1:]
                print(part1, "- <терм>;", expression[h] + expression[h+1] + expression[e], "- <операция типа умножения>;", part2, "- <фактор>.")
                third_rule(part1)
                fourph_rule(part2)

        elif list_of_multi_not_in_br == []:
            print(expression, "- <фактор>")
            fourph_rule(expression)

    elif list_of_br == [] and list_of_milti_oper != []:
        if len(list_of_milti_oper[len(list_of_milti_oper) - 1]) == 1:
            h = list_of_milti_oper[len(list_of_milti_oper) - 1][0]
            part1 = expression[:h]
            part2 = expression[h + 1:]
            print(part1, "- <терм>;", expression[h], "- <операция типа умножения>;", part2, "- <фактор>.")
            third_rule(part1)
            fourph_rule(part2)
        elif len(list_of_milti_oper[len(list_of_milti_oper) - 1]) == 3:
            h = list_of_milti_oper[len(list_of_milti_oper) - 1][0]
            e = list_of_milti_oper[len(list_of_milti_oper) - 1][2]
            part1 = expression[:h]
            part2 = expression[e + 1:]
            print(part1, "- <терм>;", expression[h] + expression[h + 1] + expression[e], "- <операция типа умножения>;", part2, "- <фактор>.")
            third_rule(part1)
            fourph_rule(part2)



def find_brackets_and_multiplication_oper(s):
    # Проверка на скобки
    indexes_open_brackets = []
    indexes_close_brackets = []
    ex_str = ''
    for i in range(0, len(s)):
        if s[i] == "(" or s[i] == ")":
            if s[i] == "(":
                indexes_open_brackets.append(i)
            elif s[i] == ")":
                indexes_close_brackets.append(i)
    # print(indexes_open_brackets, indexes_close_brackets)
    f1 = True
    a = []
    l = []
    for i in range(0, len(s)):
        # print(i)
        if i in indexes_open_brackets:
            if f1 == False:
                l.append(a)
                a = []
                a.append(i)
                f1 = False
            elif f1 == True:
                a.append(i)
                f1 = False
        elif i in indexes_close_brackets:
            # print("RRRRR")
            if f1 == False:
                a.append(i)
                l.append(a)
                a = []
                f1 = True
            elif f1 == True:
                # print("qqqq", l)
                j = len(l) - 1
                f2 = True
                while f2 != False:
                    if len(l[j]) > 1:
                        j = j - 1
                    elif len(l[j]) == 1:
                        l[j].append(i)
                        f2 = False
                    elif j == 0:
                        f2 = False
    #print("l",l)
    #Поиск операций сложения
    multi = []
    b = []
    #print("строооооооокаааа", s)
    for i in range(0, len(s)):
        if s[i] == "*" or s[i] == "/":
            b.append(i)
            multi.append(b)
            b = []
        elif len(s)>=3:
            if (s[i] == "m" and s[i+1] == "o" and s[i+2] == "d") or  (s[i] == "d" and s[i+1] == "i" and s[i+2] == "v") or  (s[i] == "a" and s[i+1] == "n" and s[i+2] == "d"):
                b.append(i)
                b.append(i+1)
                b.append(i+2)
                multi.append(b)
                b = []
    #print(multi)
    return l, multi


def check_multiplication_in_br(l1, l2):
    result = []
    for i in range(0, len(l1)):
        result.append(l1[i])
    for i in range(0, len(l1)):
        #print(l1[i])
        #print(list_of_a)
        if len(l1[i]) == 1:
            for j in range(0, len(l2)):
                if l2[j][0] < l1[i][0] < l2[j][1]:
                    if l1[i] in result:
                        result.remove(l1[i])
        elif len(l1[i]) == 3:
            for j in range(0, len(l2)):
                if l2[j][0] < l1[i][0] < l2[j][1] and  l2[j][0] < l1[i][1] < l2[j][1] and l2[j][0] < l1[i][2] < l2[j][1]:
                    if l1[i] in result:
                        result.remove(l1[i])
    print("знаки умножения вне скобок", result)
    return result


def fourph_rule(factor):
    print("9-ОЕ ПРАВИЛО <фактор> -> <идентификатор> | <константа> | ( < простое выражение > ) | not <фактор> ДЛЯ:", factor)
    if factor[0] == "(" and factor[len(factor)-1] == ")":
        new_factor = factor[1:]
        new_factor = new_factor[:-1]
        print(factor, "- ( < простое выражение > ).")
        list_of_simple_exp = []
        list_of_simple_exp.append(new_factor)
        second_rule(list_of_simple_exp)
    elif len(factor) > 3:
        if factor[0] == "n" and factor[1] == "o" and factor[2] == "t":
            new_factor = factor[3:]
            print(factor, "- not <фактор>")
            fourph_rule(new_factor)
    elif len(factor) == 1:
        identifier1 = "([A-Z])"
        identifier2 = "([a-z])"
        x1 = re.search(identifier1, factor)
        x2 = re.search(identifier2, factor)
        if factor.isdigit() == True:
            print(factor, "- <константа> (число 0-9)")
        elif x1 != None and x2 == None:
            print(factor, "- <идентификатор> (Нетерминалый символ)")
        elif x1 == None and x2 != None:
            print(factor, "- <идентификатор> (Терминальный символ)")
        elif x1 != None and x2 != None:
            print("Ошибка, конструкция составлена из нетерминальных и терминальных симоволов, что некорректно")
            sys.exit()
    elif len(factor) > 1:
        identifier1 = "([A-Z])"
        identifier2 = "([a-z])"
        x1 = re.search(identifier1, factor)
        x2 = re.search(identifier2, factor)
        if factor.isdigit() == True:
            print(factor, "- <константа> (число)")
        elif x1 != None and x2 == None:
            print(factor, "- <идентификатор> (Нетерминалый символ)")
        elif x1 == None and x2 != None:
            print(factor, "- <идентификатор> (Терминальный символ)")
        elif x1 != None and x2 != None:
            print("Ошибка, конструкция составлена из нетерминальных и терминальных симоволов, что некорректно")
            sys.exit()

def fifth_rule(prog):
    print("1-ОЕ ПРАВИЛО <программа> -> <блок> ДЛЯ:", prog)
    i1 = len("int main()")
    i2 = len("void main()")
    #print(prog)
    #print(i1)
    #print(i2)
    #print(prog[:i1])
    #print(prog[:i2])
    if prog[:i1] == "int main()" or prog[:i2] == "void main()":
        bl = ""
       #print("Вызов правила с блоком")
        if prog[:i1] == "int main()":
            bl = prog[i1:]
        elif prog[:i2] == "void main()":
            bl = prog[i2:]
        print(bl, "- <блок>")
        sixth_rule(bl)
    else:
        print("ОШИБКА! Программа в Си начинается либо с int main() либо с void main()")
        sys.exit()

def sixth_rule(block):
    print("2-ОЕ ПРАВИЛО <блок> -> { <список операторов> } ДЛЯ:", block)
    #print(block)

    #Удаляем ненужные пробелы
    i = 0
    if block[i] == ' ':
        while block[i] == ' ':
            i = i + 1
    block = block[i:]
    i = len(block) - 1
    if block[i] == ' ':
        while block[i] == ' ':
            i = i - 1
    block = block[:i+1]


    if block[0] == "{" and block[len(block) - 1] == "}":
        block = block[1:]
        block = block[:len(block) - 1]
        #print(block)
        print(block, "- { <список операторов> }")
        seventh_rule(block)
    else:
        print("ОШИБКА! Блок должен выглядеть следующим образом: <блок> -> { <список операторов> }")
        sys.exit()

def seventh_rule(list_of_oper):
    print("3-Е ПРАВИЛО <список операторов> -> <опреатор> <хвост> | <оператор> ДЛЯ:", list_of_oper)
    #print(list_of_oper)

    # Удаляем ненужные пробелы
    i = 0
    if list_of_oper[i] == ' ':
        while list_of_oper[i] == ' ':
            i = i + 1
    list_of_oper = list_of_oper[i:]
    i = len(list_of_oper) - 1
    if list_of_oper[i] == ' ':
        while list_of_oper[i] == ' ':
            i = i - 1
    list_of_oper = list_of_oper[:i+1]
    #print("БЕЗ пробелов")
    #print(list_of_oper)

    list_of_br, list_of_semicolon = find_brackets_and_sign(list_of_oper)
    #print(list_of_br, list_of_semicolon)
    # Проверка это оператор с хвостом или нет
    if list_of_br == [] and list_of_semicolon == []:
        # 100% оператор
        print(list_of_oper, "- <оператор>")
        nineth_rule(list_of_oper)
    elif list_of_br != [] and list_of_semicolon == []:
        # 100% оператор
        print(list_of_oper, "- <оператор>")
        nineth_rule(list_of_oper)
    elif list_of_semicolon != [] and list_of_br == []:
        # 100% оператор и хвост
        #print("нужно разделить")
        i = 0
        while list_of_oper[i] != ";":
            i = i + 1
        #print(list_of_oper[:i])
        #print(list_of_oper[i:])
        oper = list_of_oper[:i]
        tail = list_of_oper[i:]
        print(oper, tail, "- <опреатор> <хвост>")
        nineth_rule(oper)
        eighth_rule(tail)

    elif list_of_br != [] and list_of_semicolon != []:
        # 100% оператор и хвост
        list_of_semicolon_not_in_br = check_semicolon_in_brackets(list_of_semicolon, list_of_br)
        #print(list_of_semicolon_not_in_br)
        if list_of_semicolon_not_in_br == []:
            # 100% оператор
            nineth_rule(list_of_oper)
        elif list_of_semicolon_not_in_br != []:
            #print("нужно разделить")
            i = 0
            while list_of_oper[i] != ";":
                i = i + 1
            #print(list_of_oper[:i])
            #print(list_of_oper[i:])
            oper = list_of_oper[:i]
            tail = list_of_oper[i:]
            print(oper, tail, "- <опреатор> <хвост>")
            nineth_rule(oper)
            eighth_rule(tail)


def find_brackets_and_sign(list_of_operators):
    # Проверка на фигурные скобки
    indexes_open_brackets = []
    indexes_close_brackets = []
    ex_str = ''
    for i in range(0, len(list_of_operators)):
        if list_of_operators[i] == "{" or list_of_operators[i] == "}":
            if list_of_operators[i] == "{":
                indexes_open_brackets.append(i)
            elif list_of_operators[i] == "}":
                indexes_close_brackets.append(i)
    # print(indexes_open_brackets, indexes_close_brackets)
    f1 = True
    a = []
    l = []
    for i in range(0, len(list_of_operators)):
        # print(i)
        if i in indexes_open_brackets:
            if f1 == False:
                l.append(a)
                a = []
                a.append(i)
                f1 = False
            elif f1 == True:
                a.append(i)
                f1 = False
        elif i in indexes_close_brackets:
            # print("RRRRR")
            if f1 == False:
                a.append(i)
                l.append(a)
                a = []
                f1 = True
            elif f1 == True:
                # print("qqqq", l)
                j = len(l) - 1
                f2 = True
                while f2 != False:
                    if len(l[j]) > 1:
                        j = j - 1
                    elif len(l[j]) == 1:
                        l[j].append(i)
                        f2 = False
                    elif j == 0:
                        f2 = False
    #print("l",l)
    # Поиск точки с запятой
    # print(l)
    l_semicolon = []
    b = []
    for i in range(0, len(list_of_operators)):
        if list_of_operators[i] == ";":
            b.append(i)
            l_semicolon.append(b)
            b = []
    #print(l_semicolon)
    return l, l_semicolon


def check_semicolon_in_brackets(l1, l2):
    result = []
    for i in range(0, len(l1)):
        result.append(l1[i])
    for i in range(0, len(l1)):
        #print(l1[i])
        #print(list_of_a)
        #if len(l1[i]) == 1:
        for j in range(0, len(l2)):
            if l2[j][0] < l1[i][0] < l2[j][1]:
                if l1[i] in result:
                    result.remove(l1[i])
    #print("точка с запятой вне скобок", result)
    return result



def eighth_rule(tail):
    print("4-ОЕ ПРАВИЛО <хвост> -> ;<опреатор> <хвост> | ;<оператор> ДЛЯ:", tail)
    #print(tail)
    # Удаляем ненужные пробелы
    i = 0
    if tail[i] == ' ':
        while tail[i] == ' ':
            i = i + 1
    tail = tail[i:]
    i = len(tail) - 1
    if tail[i] == ' ':
        while tail[i] == ' ':
            i = i - 1
    tail = tail[:i + 1]
    #print("Без проблеоов")
    #print(tail)
    if (tail[0] != ";"):
        print("ОШИБКА! ';' отсутсвует ")
    else:
        #print()
        semicolon = tail[0]
        tail = tail[1:]
        #print(tail)
        # Удаляем ненужные пробелы
        i = 0
        if tail[i] == ' ':
            while tail[i] == ' ':
                i = i + 1
        tail = tail[i:]
        i = len(tail) - 1
        if tail[i] == ' ':
            while tail[i] == ' ':
                i = i - 1
        tail = tail[:i + 1]
        #print("Без пробелов")
        #print(tail)

        old_tail = tail
        #--------------------------------------------------------------------

        list_of_br, list_of_semicolon = find_brackets_and_sign(old_tail)
        # print(list_of_br, list_of_semicolon)
        # Проверка это оператор с хвостом или нет
        if list_of_br == [] and list_of_semicolon == []:
            # 100% оператор
            print(semicolon, old_tail, "- ; <оператор>")
            nineth_rule(old_tail)
        elif list_of_br != [] and list_of_semicolon == []:
            # 100% оператор
            print(semicolon, old_tail, "- ; <оператор>")
            nineth_rule(old_tail)
        elif list_of_semicolon != [] and list_of_br == []:
            # 100% оператор и хвост
            # print("нужно разделить")
            i = 0
            while old_tail[i] != ";":
                i = i + 1
            # print(list_of_oper[:i])
            # print(list_of_oper[i:])
            oper = old_tail[:i]
            tail = old_tail[i:]
            print(semicolon, oper, tail, "- ; <опреатор> <хвост>")
            nineth_rule(oper)
            eighth_rule(tail)

        elif list_of_br != [] and list_of_semicolon != []:
            # 100% оператор и хвост
            list_of_semicolon_not_in_br = check_semicolon_in_brackets(list_of_semicolon, list_of_br)
            # print(list_of_semicolon_not_in_br)
            if list_of_semicolon_not_in_br == []:
                # 100% оператор
                nineth_rule(old_tail)
            elif list_of_semicolon_not_in_br != []:
                # print("нужно разделить")
                i = 0
                while old_tail[i] != ";":
                    i = i + 1
                # print(list_of_oper[:i])
                # print(list_of_oper[i:])
                oper = old_tail[:i]
                tail = old_tail[i:]
                print(semicolon, oper, tail, "- ; <опреатор> <хвост>")
                nineth_rule(oper)
                eighth_rule(tail)
        #--------------------------------------------------------------------


def nineth_rule(operator):
    print("5-ОЕ ПРАВИЛО <опреатор> -> <идентификатор>==<выражение> | <блок> ДЛЯ:", operator)
    #print(operator)
    # Удаляем ненужные пробелы
    i = 0
    if operator[i] == ' ':
        while operator[i] == ' ':
            i = i + 1
    operator = operator[i:]
    i = len(operator) - 1
    if operator[i] == ' ':
        while operator[i] == ' ':
            i = i - 1
    operator = operator[:i + 1]
    #print("Без проблеоов")
    #print(operator)
    if operator[0] == "{" and operator[len(operator) - 1] == "}":
        sixth_rule(operator)
    else:
        #print("----")
        i = 0
        f1 = False
        while f1 == False:
            i = i + 1
            #print(i, operator[i])
            if (operator[i] == "=" and operator[i+1] == "="):
                f1 = True

        #print(i)
        #print(operator[:i])
        #print(operator[i+2:])
        iden = operator[:i]
        expres = operator[i+2:]
        if len(iden) == 1:
            identifier1 = "([A-Z])"
            identifier2 = "([a-z])"
            x1 = re.search(identifier1, iden)
            x2 = re.search(identifier2, iden)
            if x1 != None and x2 == None:
                print(iden, "- <идентификатор> (Нетерминалый символ)")
            elif x1 == None and x2 != None:
                print(iden, "- <идентификатор> (Терминальный символ)")
            elif x1 != None and x2 != None:
                print("Ошибка, конструкция составлена из нетерминальных и терминальных симоволов, что некорректно")
                sys.exit()
        elif len(iden) > 1:
            identifier1 = "([A-Z])"
            identifier2 = "([a-z])"
            x1 = re.search(identifier1, iden)
            x2 = re.search(identifier2, iden)
            if x1 != None and x2 == None:
                print(iden, "- <идентификатор> (Нетерминалый символ)")
            elif x1 == None and x2 != None:
                print(iden, "- <идентификатор> (Терминальный символ)")
            elif x1 != None and x2 != None:
                print("Ошибка, конструкция составлена из нетерминальных и терминальных симоволов, что некорректно")
                sys.exit()
        print(expres, "- <выражение>")
        print()
        first_rule(expres)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Parser(P, example9, main_example3)
    print()
    #Parser(P, example5)
    #print()
    #Parser(P, example7)
    #print()
    #Parser(P, example6)
    #print()
    #Parser(P, example2)
    #Parser(P, example8)
    #print()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
