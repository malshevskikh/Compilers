#Пример праволинейной грамматики G:
# S -> 0A | 1S | e
# A -> 0B | 1A
# B -> 0S | 1B
import graphviz


def grammatic_input():
    print("Ввести правила - 1/взять правила по умолчанию - 2?")
    f0 = int(input())
    l1 = []
    if f0 == 1:
        print("Введите правила праволинейной грамматики G, которые имеют вид A->aB или A->a")
        m1 = True
        while m1 == True:
            print("Добавить новое прравило?")
            print("Да - 1/Нет - 2?")
            f1 = int(input())
            if f1 == 1:
                l2 = []
                left_part = input("Введите левую часть правила без пробелов:")
                m2 = True
                l2.append(left_part)
                while m2 == True:
                    right_part = input("Введите правую часть правила без пробелов:")
                    #print(left_part, "->",right_part)
                    l2.append(right_part)
                    print("Добавить еще правую часть?")
                    print("Да - 1/Нет - 2?")
                    f2 = int(input())
                    if f2 == 2:
                        m2 = False
                l1.append(l2)
            elif f1 == 2:
                m1 = False
    elif f0 == 2:
        l1 = [["S", "0A", "1S", "e"],
              ["A", "0B", "1A"],
              ["B", "0S", "1B"]]
    for i in l1:
        l3 = i[1:]
        #print(l3)
        print(i[0], "->", '|'.join(l3))
    return l1

def transform_grm_to_reg(list_of_grm):
    #print(list_of_grm)
    c = 1
    list_of_reg = []
    l1 = []
    for i in list_of_grm:
        l2 = []
        old_v = i[0]
        new_v = "X" + str(c)
        l2.append(old_v)
        l2.append(new_v)
        l1.append(l2)
        c = c +1
    #print(l1)
    for i in list_of_grm:
        s1 = []
        for j in i:
            m1 = False
            for k in l1:
                if k[0] in j:
                    a = j.replace(k[0], k[1])
                    #print(k[0], j, k[1], a)
                    s1.append(a)
                    m1 = True
            if m1 == False:
                s1.append(j)
        list_of_reg.append(s1)
    return list_of_reg

def check_lemma(number, stm):
    #Лемма
    #print("---------------------------------------------")
    #print("Проверка на лемму:", stm)
    for i in range(len(stm)):
        for j in range(len(stm[i])):
            if "+" in stm[i][j] or "-" in stm[i][j] or "/" in stm[i][j] or "*" in stm[i][j]:
                flag = True
                variables = stm[i][j].split(' ')
                #print(variables)
                k= 0
                while flag == True:
                    if variables[k] == "+":
                        if k < len(variables) - 1:
                            #print(variables[k - 1], variables[k], variables[k + 1])
                            first_term = variables[k - 1]
                            sign = variables[k]
                            second_term = variables[k + 1]
                            if first_term == second_term:
                                if k < len(variables) - 2:
                                    variables = variables[:k - 1] + [first_term] + variables[k + 2:]
                                elif k == len(variables) - 2:
                                    variables = variables[:k - 1] + [first_term]
                            elif first_term == "∅" or second_term == "∅":
                                if first_term == "∅":
                                    if k < len(variables) - 2:
                                        variables = variables[:k - 1] + [second_term] + variables[k + 2:]
                                    elif k == len(variables) - 2:
                                        variables = variables[:k - 1] + [second_term]
                                elif second_term == "∅":
                                    if k < len(variables) - 2:
                                        variables = variables[:k - 1] + [first_term] + variables[k + 2:]
                                    elif k == len(variables) - 2:
                                        variables = variables[:k - 1] + [first_term]
                        #print("Самый новый 1:", k, variables)
                    elif variables[k] == "*":
                        if k < len(variables) - 1:
                            #print(variables[k - 1], variables[k], variables[k + 1])
                            first_term = variables[k - 1]
                            sign = variables[k]
                            second_term = variables[k + 1]
                            if first_term == "e" or second_term == "e":
                                if first_term == "e":
                                    if k < len(variables) - 2:
                                        variables = variables[:k - 1] + [sign, second_term] + variables[k + 2:]
                                    elif k == len(variables) - 2:
                                        variables = variables[:k - 1] + [sign, second_term]
                                elif second_term == "e":
                                    if k < len(variables) - 2:
                                        variables = variables[:k - 1] + [first_term, sign] + variables[k + 2:]
                                    elif k == len(variables) - 2:
                                        variables = variables[:k - 1] + [first_term, sign]
                            elif first_term == "∅" or second_term == "∅":
                                if first_term == "∅":
                                    if k < len(variables) - 2:
                                        variables = variables[:k - 1] + [first_term] + variables[k + 2:]
                                    elif k == len(variables) - 2:
                                        variables = variables[:k - 1] + [first_term]
                                elif second_term == "∅":
                                    if k < len(variables) - 2:
                                        variables = variables[:k - 1] + [second_term] + variables[k + 2:]
                                    elif k == len(variables) - 2:
                                        variables = variables[:k - 1] + [second_term]
                        #print("Самый новый 1:", k, variables)

                    if k == len(variables) - 1:
                        flag = False
                    k = k + 1
                res = " ".join(variables)
                stm[i][j] = res


def check_brackets(number, stm):
    #раскрытие скобок
    #print("раскрытие скобок:", stm)
    for i in range(len(stm)):
        for j in range(1, len(stm[i])):
            if ("(" or ")" or "*") in stm[i][j]:
                variables = stm[i][j].split(' ')
                #print(variables)
                p1 = stm[i][j].count("(") + stm[i][j].count(")")
                p2 = 0
                l = 0
                without_brackets = []
                d = len(variables) - 1
                flag = True
                #print(p1, p2)

                open_brackets = []
                close_brackets = []
                for m in range(len(variables)):
                    if variables[m] == "(":
                        open_brackets.append(m)
                    elif variables[m] == ")":
                        close_brackets.append(m)
                #print(open_brackets)
                #print(close_brackets)
                if p1 == 2 or open_brackets[1] - open_brackets[0] > close_brackets[0] - open_brackets[0]:
                    while flag == True:
                        if p1 == p2:
                            while l != d:
                                without_brackets.append(variables[l])
                                l = l + 1
                            if l == d:
                                flag = False
                        else:
                            while variables[l] != "(":
                                without_brackets.append(variables[l])
                                l = l + 1

                            #print("До скобки:", without_brackets)
                            if variables[l] == "(":
                                p2 = p2 + 1
                                without_brackets.pop(len(without_brackets) - 2)
                                without_brackets.pop(len(without_brackets) - 1)
                                #print("Удаление:", without_brackets)
                                perem = variables[l-2]
                                sign = variables[l-1]
                                l = l + 1
                                while (variables[l] != ")"):
                                    #print(variables[l])
                                    if variables[l] != "+" and variables[l] != "-" and variables[l] != "*" and variables[l] != "/":
                                        without_brackets.append(perem)
                                        without_brackets.append(sign)
                                        without_brackets.append(variables[l])
                                    elif variables[l] == "+" or variables[l] == "-" or variables[l] == "*" or variables[l] == "/":
                                        without_brackets.append(variables[l])
                                    l = l + 1
                                p2 = p2 + 1
                                #print(l)

                            #print("После скобки:", l,  without_brackets)
                            if l == d:
                                flag = False
                    variables = without_brackets
                    res = " ".join(variables)
                    #print(i, j)
                    stm[i][j] = res
                elif p1 > 2 or open_brackets[1] - open_brackets[0] < close_brackets[0] - open_brackets[0]:
                    #print(open_brackets)
                    #print(close_brackets)
                    not_empty_lists = True
                    while not_empty_lists == True:
                        op = open_brackets[len(open_brackets) - 1]
                        cl = close_brackets[0]
                        f = 0
                        without_brackets_local = []
                        #print(op, cl, variables)
                        while f != op:
                            #print(f, variables[f])
                            without_brackets_local.append(variables[f])
                            f = f + 1
                        #print("До скобки:", without_brackets_local)
                        if variables[f] == "(":
                            without_brackets_local.pop(len(without_brackets_local) - 2)
                            without_brackets_local.pop(len(without_brackets_local) - 1)
                            #print("Удаление:", without_brackets_local)
                            perem = variables[f - 2]
                            sign = variables[f - 1]
                            f = f + 1
                            while f != cl:
                                if variables[f] != "+" and variables[f] != "-" and variables[f] != "*" and variables[f] != "/":
                                    without_brackets_local.append(perem)
                                    without_brackets_local.append(sign)
                                    without_brackets_local.append(variables[f])
                                elif variables[f] == "+" or variables[f] == "-" or variables[f] == "*" or variables[f] == "/":
                                    without_brackets_local.append(variables[f])
                                f = f + 1
                        #print("После скобки:", f, without_brackets_local)

                        open_brackets.pop(len(open_brackets) - 1)
                        close_brackets.pop(0)

                        #print(without_brackets_local)
                        #print(variables)
                        variables = without_brackets_local + variables[cl + 1:]
                        #print(variables)

                        if open_brackets == [] and close_brackets == []:
                            not_empty_lists = False
                        else:
                            not_empty_lists = True
                    res = " ".join(variables)
                    #print(i, j)
                    stm[i][j] = res


def checking_X_in_stm(main_string):
    #print("Опредление X в уравнении:", main_string)
    Xi = main_string[0]
    right_side = main_string[1:]
    aXi = []
    Beta = []
    for i in right_side:
        if Xi in i:
            aXi.append(i)
        else:
            Beta.append(i)
    new_system = []
    if len(aXi) == 1:
        new_system.append(Xi)
        new_system = new_system + aXi
        new_system = new_system + Beta
        main_string = new_system
    elif len(aXi) > 1:
        #print("aXi в функции:", aXi)
        massive = []
        just_Xi = []
        Xi_with_br = ''
        for j in aXi:
            var = j.split(' + ')
            massive = massive + var
        #print("djnfkv", massive)
        for k in massive:
            if Xi in k:
                a = k.replace(Xi, '')
                just_Xi.append(a)
                massive.remove(k)
        Xi_with_br = Xi_with_br + "("
        for e in just_Xi:
            if e != just_Xi[len(just_Xi) - 1]:
                Xi_with_br = Xi_with_br + e + " + "
            else:
                Xi_with_br = Xi_with_br + e + ")" + Xi

        #print("eiievive", Xi_with_br, massive)
        new_system.append(Xi)
        new_system.append(Xi_with_br)
        new_system = new_system + massive
        main_string = new_system
    #print("why???? ", main_string)
    return main_string

def step5_and_step6(stm, solves, alpaBeta):
    #print(stm)
    #print(solves)
    #print(alpaBeta)
    final_solving = []
    list_of_Xi = []
    for i in range(len(stm) - 1, -1, -1):
        list_of_Xi.append(stm[i][0])
    #print(list_of_Xi)

    c = 0
    i = 0
    main_stm = stm
    for i in range(len(stm)-1, -1, -1):
        asd = []
        Xi = stm[i][0]
        solves[0][0] = Xi
        #print(Xi)
        #print(main_stm)
        asd.append(Xi)
        asd.append(solves[0][1])
        final_solving.append(asd)
        #solves = []
        qwe = []
        qwe.append(Xi)
        #qwe.append()
        #solves.append(qwe)
        main_stm.pop(len(main_stm) - 1)
        #print(main_stm)
        #print("решения:", solves)
        for j in range(len(main_stm) - 1, -1, -1):
            for k in range(len(main_stm[j])):
                if k > 0:
                    if Xi in main_stm[j][k]:
                        main_stm[j][k] = main_stm[j][k].replace(Xi, solves[0][1])

        #print(main_stm)
        Beta = []
        aXi = ""
        alphaBeta = ""
        if main_stm != []:
            f = main_stm[len(main_stm)-1]
            #print("f", f)
            for m in range(len(f)):
                if m > 0:
                    if f[0] in f[m]:
                        aXi = aXi + f[m]
                    else:
                        Beta.append(f[m])
            alpha = aXi.replace(f[0], "")
            if len(Beta) > 1:
                alphaBeta = alpha + " * " + "( " + ' + '.join(Beta) + " )"
            elif len(Beta) == 1:
                alphaBeta = alpha + " * " + ' + '.join(Beta)
        #print("aXi", aXi)
        #print("решения2:", solves)

        #print("alphaBeta", alphaBeta)
        solves[0][1] = alphaBeta
    #print("Полноценное решение:", final_solving)
    return final_solving

def solving_sys_of_reg(system):
    #print(system)
    alphaBeta_final = ""
    list_of_solving = []
    for i in range(len(system)):
        if i != len(system)-1:
            #print("Тута:", system[i])
            m = checking_X_in_stm(system[i])
            system[i] = m
            #print("jjjjjj ", m)
            Xi = system[i][0]
            right_side = system[i][1:]
            #print(right_side)
            Beta = []

            aXi = ""
            for j in right_side:
                if Xi in j:
                    aXi = aXi + j
                else:
                    Beta.append(j)
            new_system = []
            #print("alpha:", aXi)
            #print("Beta:", Beta)
            new_system.append(Xi)
            new_system.append(aXi)
            new_system = new_system + Beta
            system[i] = new_system
            #print(Xi, " = ", aXi, " + ",' + '.join(Beta))
            alpha = aXi.replace(Xi, '')
            #print( Xi, " = ", aXi, " + ", ' + '.join(Beta))
            #print("alpha", alpha, " * ", "(",' + '.join(Beta), ")")
            alphaBeta = ""
            if len(Beta) > 1:
                alphaBeta = alpha + " * " + "( " + ' + '.join(Beta) + " )"
            elif len(Beta) == 1:
                alphaBeta = alpha + " * " + ' + '.join(Beta)
            #print("alphaBeta", alphaBeta)

            for k in range(len(system)):
                if k > i:
                    for l in range(len(system[k])):
                        if l > 0:
                            if Xi in system[k][l]:
                                system[k][l] = system[k][l].replace(Xi, alphaBeta)
                    #print("Новая строка:", system[k])

            #check_lemma(i, system)
            #print("Перед входом: ", system)
            #check_brackets(i, system)
            #print("Убрали скобки:", system)
            #check_lemma(i, system)
            #print("Применили леммы:", system)

        else:
            m = checking_X_in_stm(system[i])
            #print("jjjjjj ", m)
            system[i] = m
            Xi = system[i][0]
            right_side = system[i][1:]
            aXi = ""
            Beta = []
            for j in right_side:
                if Xi in j:
                    aXi = aXi + j
                else:
                    Beta.append(j)
            #print("aXi....", aXi)
            alpha = aXi.replace(Xi, '')
            #print(Beta)
            if len(Beta) > 1:
                alphaBeta_final = alpha + " * " + "( " + ' + '.join(Beta) + " )"
            elif len(Beta) == 1:
                alphaBeta_final = alpha + " * " + ' + '.join(Beta)
            #print(system[i])
            qwe = []
            qwe.append(Xi)
            qwe.append(alphaBeta_final)
            list_of_solving.append(qwe)

    solving_problem = step5_and_step6(system, list_of_solving, alphaBeta_final)
    #print(solving_problem)
    return solving_problem



def making_nka(regulars):
    #print("Регулярные выражения", regulars)
    all_graphs = []
    if len(regulars) > 1:
        for reg in regulars:
            #print(reg)
            #print("Текущее регулярное выражение: ", reg)
            for i in range(1, len(reg)):
                count_of_statement = 1  # счетчик состояний

                #print(reg[i])
                nka = reg[i]
                nka = nka.replace(" ", "")
                #print(nka)
                nka = list(nka)
                #print(nka)

                name_of_file = "nka_graph_" + reg[0]
                #print(name_of_file)
                f = graphviz.Digraph('NKA', filename=name_of_file)
                f.attr(rankdir='LR', size='8,5')

                f.node('Q0')
                f.attr('node', shape='doublecircle')

                f.edge('Q0', 'Q1', label='Eps')

                list_of_transit = []
                asd = []
                asd.append('Q0')
                asd.append('Q1')
                asd.append('Eps')
                list_of_transit.append(asd)
                index_of_state_before_plus = 0
                index_of_state_before_brc = 0

                list_of_open_brackets = []
                list_of_pluses = []
                potencial_start_of_plus = []
                for j in range(len(nka)):
                    #print("Текущий символ ", count_of_statement, " ", nka[j])

                    if nka[j] == "(":
                        list_of_open_brackets.append(j)
                        potencial_start_of_plus.append(j)
                        statement1 = "Q" + str(count_of_statement)
                        statement2 = "Q" + str(count_of_statement + 1)
                        lab = "Eps"
                        f.edge(statement1, statement2, label='Eps')
                        asd = []
                        asd.append(statement1)
                        asd.append(statement2)
                        asd.append(lab)
                        asd.append(j)
                        list_of_transit.append(asd)
                        count_of_statement = count_of_statement + 1

                    elif nka[j] == "+":
                        potencial_start_of_plus.append(j)
                        #print(j, nka[j], list_of_transit)

                        list_of_pluses.append(j)
                        #print("потенциальные плюсы", potencial_start_of_plus)
                        ili = find_plus(nka, j, index_of_state_before_plus, potencial_start_of_plus)
                        #print("sjdfdf", ili)


                        potencial_start_of_plus.remove(j)
                        potencial_start_of_plus.remove(ili[0])
                        #print("потенциальные плюсы", potencial_start_of_plus)
                        #print(index_of_state_before_plus)

                        if nka[ili[0] - 1] == "*" and ili[0] != 0:
                            statement1 = "Q" + str(ili[0])
                        else:
                            statement1 = "Q" + str(ili[0] + 1)
                        #print("А вот и он", statement1)
                        statement2 = "Q" + str(index_of_state_before_plus + 1)
                        lab = "Eps"
                        #print(statement1)
                        #print(statement2)

                        f.edge(statement1, statement2, label='Eps')
                        # print(statement1, statement2, nka[j])
                        asd = []
                        asd.append(statement1)
                        asd.append(statement2)
                        asd.append(lab)
                        asd.append(j)
                        list_of_transit.append(asd)

                        count_of_statement = index_of_state_before_plus + 1

                        #print(j, nka[j], list_of_transit)

                    elif nka[j] == "*":
                        #print(index_of_state_before_plus, nka[index_of_state_before_plus])
                        #print(index_of_state_before_brc, nka[index_of_state_before_brc])
                        if nka[j-1] == ")":
                            list_of_nes_statement = find_conctat(nka, j, index_of_state_before_brc, index_of_state_before_plus, list_of_open_brackets, list_of_transit)
                            #print(count_of_statement)
                            #print("YYYYYYEEEEEESSSSSS%   ", list_of_nes_statement)

                            statement1 = "Q" + str(count_of_statement)
                            statement2 = str(list_of_nes_statement[1])
                            lab = "Eps"
                            f.edge(statement1, statement2, label='Eps')
                            asd = []
                            asd.append(statement1)
                            asd.append(statement2)
                            asd.append(lab)
                            asd.append(j)
                            list_of_transit.append(asd)
                            count_of_statement = count_of_statement + 1

                            statement1 = "Q" + str(count_of_statement - 1)
                            statement2 = "Q" + str(count_of_statement)
                            lab = "Eps"
                            f.edge(statement1, statement2, label='Eps')
                            asd = []
                            asd.append(statement1)
                            asd.append(statement2)
                            asd.append(lab)
                            # asd.append(j)
                            list_of_transit.append(asd)

                            statement1 = str(list_of_nes_statement[0])
                            statement2 = "Q" + str(count_of_statement)
                            lab = "Eps"
                            f.edge(statement1, statement2, label='Eps')
                            asd = []
                            asd.append(statement1)
                            asd.append(statement2)
                            asd.append(lab)
                            #asd.append(j)
                            list_of_transit.append(asd)
                            #scount_of_statement = count_of_statement + 1

                            list_of_open_brackets.pop()

                        index_of_state_before_plus = count_of_statement

                    elif nka[j] == ")":
                        #print("))))))))))", list_of_pluses)
                        state_before_plus = find_plus_between_brackets(nka, list_of_pluses, list_of_transit, j, list_of_open_brackets)
                        #print(state_before_plus)
                        if j < len(nka) - 1:
                            if nka[j + 1] != "*":
                                statement1 = "Q" + str(count_of_statement)
                                statement2 = "Q" + str(count_of_statement + 1)
                                lab = "Eps"
                                f.edge(statement1, statement2, label='Eps')
                                asd = []
                                asd.append(statement1)
                                asd.append(statement2)
                                asd.append(lab)
                                asd.append(j)
                                #asd.append("aaaaaaaaaaa")
                                list_of_transit.append(asd)
                                count_of_statement = count_of_statement + 1
                                list_of_open_brackets.pop()

                            else:
                                statement1 = "Q" + str(count_of_statement)
                                statement2 = "Q" + str(count_of_statement + 1)
                                lab = "Eps"
                                f.edge(statement1, statement2, label='Eps')
                                asd = []
                                asd.append(statement1)
                                asd.append(statement2)
                                asd.append(lab)
                                asd.append(j)
                                # asd.append("aaaaaaaaaaa")
                                list_of_transit.append(asd)
                                count_of_statement = count_of_statement + 1

                            statement1 = state_before_plus[0]
                            statement2 = "Q" + str(count_of_statement)
                            f.edge(statement1, statement2, label='Eps')
                            asd = []
                            asd.append(statement1)
                            asd.append(statement2)
                            asd.append(lab)
                            asd.append(j)
                            # asd.append("aaaaaaaaaaa")
                            list_of_transit.append(asd)

                        else:
                            statement1 = "Q" + str(count_of_statement)
                            statement2 = "Q" + str(count_of_statement + 1)
                            lab = "Eps"
                            f.edge(statement1, statement2, label='Eps')
                            asd = []
                            asd.append(statement1)
                            asd.append(statement2)
                            asd.append(lab)
                            asd.append(j)
                            # asd.append("aaaaaaaaaaa")
                            list_of_transit.append(asd)
                            count_of_statement = count_of_statement + 1

                            statement1 = state_before_plus[0]
                            statement2 = "Q" + str(count_of_statement)
                            f.edge(statement1, statement2, label='Eps')
                            asd = []
                            asd.append(statement1)
                            asd.append(statement2)
                            asd.append(lab)
                            asd.append(j)
                            # asd.append("aaaaaaaaaaa")
                            list_of_transit.append(asd)

                        #print(statement1)
                        #print(statement2)
                        if j == len(nka) - 1:
                            statement1 = "Q" + str(count_of_statement)
                            statement2 = "Q" + str(count_of_statement + 1)
                            lab = "Eps"
                            f.edge(statement1, statement2, label='Eps')
                            asd = []
                            asd.append(statement1)
                            asd.append(statement2)
                            asd.append(lab)
                            asd.append(j)
                            # asd.append("aaaaaaaaaaa")
                            list_of_transit.append(asd)
                            count_of_statement = count_of_statement + 1

                    else:
                        if j < len(nka) - 1:
                            if nka[j + 1] != "*" and nka[j + 1] != "+" and nka[j + 1] != "(" and nka[j + 1] != ")":
                                statement1 = "Q" + str(count_of_statement)
                                statement2 = "Q" + str(count_of_statement + 1)
                                f.edge(statement1, statement2, label=nka[j])
                                #print(statement1, statement2, nka[j])
                                asd = []
                                asd.append(statement1)
                                asd.append(statement2)
                                asd.append(nka[j])
                                asd.append(j)
                                list_of_transit.append(asd)

                                statement1 = "Q" + str(count_of_statement + 1)
                                statement2 = "Q" + str(count_of_statement + 2)
                                lab = "Eps"
                                f.edge(statement1, statement2, label='Eps')
                                asd = []
                                asd.append(statement1)
                                asd.append(statement2)
                                asd.append(lab)
                                list_of_transit.append(asd)
                                count_of_statement = count_of_statement + 2

                            elif nka[j + 1] == "*":
                                statement1 = "Q" + str(count_of_statement)
                                statement2 = "Q" + str(count_of_statement)
                                f.edge(statement1, statement2, label=nka[j])
                                # print(statement1, statement2, nka[j])
                                asd = []
                                asd.append(statement1)
                                asd.append(statement2)
                                asd.append(nka[j])
                                asd.append(j)
                                list_of_transit.append(asd)

                                statement1 = "Q" + str(count_of_statement)
                                statement2 = "Q" + str(count_of_statement + 1)
                                lab = "Eps"
                                f.edge(statement1, statement2, label='Eps')
                                asd = []
                                asd.append(statement1)
                                asd.append(statement2)
                                asd.append(lab)
                                asd.append(j + 1)
                                list_of_transit.append(asd)
                                count_of_statement = count_of_statement + 1

                            elif nka[j + 1] == "+":
                                statement1 = "Q" + str(count_of_statement)
                                statement2 = "Q" + str(count_of_statement + 1)
                                f.edge(statement1, statement2, label=nka[j])
                                #print(statement1, statement2, nka[j])
                                asd = []
                                asd.append(statement1)
                                asd.append(statement2)
                                asd.append(nka[j])
                                asd.append(j)
                                list_of_transit.append(asd)
                                index_of_state_before_plus = count_of_statement + 1

                            elif nka[j + 1] == ")":
                                statement1 = "Q" + str(count_of_statement)
                                statement2 = "Q" + str(count_of_statement + 1)
                                f.edge(statement1, statement2, label=nka[j])
                                #print(statement1, statement2, nka[j])
                                asd = []
                                asd.append(statement1)
                                asd.append(statement2)
                                asd.append(nka[j])
                                asd.append(j)
                                #asd.append("фффффффффф")
                                list_of_transit.append(asd)
                                index_of_state_before_brc = count_of_statement
                                count_of_statement = count_of_statement + 1

                            elif nka[j + 1] == "(":
                                #print(nka[j], list_of_transit)

                                statement1 = "Q" + str(count_of_statement)
                                statement2 = "Q" + str(count_of_statement + 1)
                                f.edge(statement1, statement2, label=nka[j])
                                #print(statement1, statement2, nka[j])
                                asd = []
                                asd.append(statement1)
                                asd.append(statement2)
                                asd.append(nka[j])
                                asd.append(j)
                                list_of_transit.append(asd)
                                index_of_state_before_brc = count_of_statement
                                count_of_statement = count_of_statement + 1

                                statement1 = "Q" + str(count_of_statement)
                                statement2 = "Q" + str(count_of_statement + 1)
                                lab = "Eps"
                                f.edge(statement1, statement2, label='Eps')
                                asd = []
                                asd.append(statement1)
                                asd.append(statement2)
                                asd.append(lab)
                                list_of_transit.append(asd)
                                count_of_statement = count_of_statement + 1

                                #print(list_of_transit)


                #f.view()
                print("--------Список переходов между состояниями для", nka, "----------")
                for stat in list_of_transit:
                    print(stat)
                print("-------------------------")
                f.node(list_of_transit[len(list_of_transit) - 1][1])

                f.view()
                all_graphs.append(list_of_transit)

    return all_graphs

def find_plus(reg_exp, cur_index, prev_index, potencial_pluses):
    l1 = []
    i = cur_index - 1
    #print("текущий индекс перед плюсом", i)
    #print(reg_exp)
    while i > 0:
        #print(i, reg_exp[i])
        if (reg_exp[i] == "(" or reg_exp[i] == "+") and i in potencial_pluses:
            break
        else:
            i = i - 1

    start_of_ili = i
    #print(start_of_ili)

    i = cur_index + 1
    while (i <= len(reg_exp) - 1) or (reg_exp[i] != ")") or (reg_exp[i] != "+"):
        i = i + 1
        if i > len(reg_exp) - 1 or (reg_exp[i] != ")") or (reg_exp[i] != "+"):
            break

    end_of_ili = i

    l1.append(start_of_ili)
    l1.append(end_of_ili)
    l1.append(prev_index)
    #print(end_of_ili)
    #print(reg_exp)
    #print(potencial_pluses)
    return l1

def find_conctat(reg_exp, cur_index, prev_index_of_brc, prev_index_of_plus, open_brc, trans_list):
    res_list = []
    for i in range(len(trans_list)):
        if len(trans_list[i]) == 4:
            if trans_list[i][3] == open_brc[len(open_brc) - 1]:
                res_list.append(trans_list[i-1][0])
                res_list.append(trans_list[i][0])

    return  res_list

def find_plus_between_brackets(reg_exp, pluses, transit, cur_index, brackets):
    #print("__---____________")
    #print(reg_exp)
    #print(pluses)
    #print(cur_index)
    #print(brackets)
    #print(transit)
    #print("wwwwww", brackets[len(brackets) - 1])
    res = []
    i = cur_index
    start = 0
    while i != brackets[len(brackets) - 1]:
        i = i - 1
    #print(i)
    if reg_exp[i] == "(":
        start = i
    #print("индекс", i, start)
    end = cur_index
    i = 0
    #print(pluses[len(pluses) - 1] - 1)
    #print(start, " < ", pluses[len(pluses) - 1], " < ", end)
    if start < pluses[len(pluses) - 1] < end:
        for i in range(len(transit)):
            if len(transit[i]) == 4:
                #print(transit[i][3], " == ", pluses[len(pluses) - 1])
                if transit[i][3] == pluses[len(pluses) - 1] - 1:
                    #print("transit", transit[i])
                    res.append(transit[i][1])
    #print(res)
    return res

def deter_nka(regulars, nka_list):
    #print("Детерменированный НКА", regulars)
    num_of_reg = 0
    res = []
    for nka in nka_list:
        #print(nka)
        #print(regulars[num_of_reg])
        cur_reg = regulars[num_of_reg][1:]
        cur_reg = cur_reg[0].replace(' ', '')
        cur_reg = list(cur_reg)
        #print(cur_reg)
        #print("$$$$$$$$$$$$$$")
        dka = []
        for j in nka:
            #print(j)
            if j[2] != "Eps":
                dka.append(j)
        #print("-----------")
        new_dka = []
        #for i in dka:
            #print(i)
        i = 0
        c = 0
        potencial_plus = []
        open_brackets = []
        Q_start = ''
        Q_end = ''
        state_after_bracket = ''
        for i in range(len(cur_reg)):
            #print("===========")
            #print("Текущее", cur_reg[i], i, c)
            vr = []
            for sh in range(len(dka)):
                if i in dka[sh]:
                    vr = dka[sh]
            if vr != []:
                if Q_start == '' and Q_end == '':
                    if vr[0] != vr[1]:
                        vr[0] = "Q" + str(c)
                        vr[1] = "Q" + str(c + 1)
                        new_dka.append(vr)
                        c = c + 1
                        #print(c)
                    if vr[0] == vr[1]:
                        vr[0] = "Q" + str(c)
                        vr[1] = "Q" + str(c)
                        new_dka.append(vr)

                elif Q_start != '' and Q_end != '':
                    #print(c)
                    vr[0] = Q_start
                    vr[1] = "Q" + str(c)
                    new_dka.append(vr)
            else:
                if cur_reg[i] == "(":
                    potencial_plus.append(i)
                    open_brackets.append(i)

                elif cur_reg[i] == "+":
                    potencial_plus.append(i)
                    p = len(new_dka)
                    Q_end = new_dka[len(new_dka) - 1][1]
                    while p > 0:
                        # print(i, reg_exp[i])
                        if (cur_reg[p] == "(" or cur_reg[p] == "+"):
                            break
                        else:
                            p = p - 1
                    #print("Индекс ближайшего + или (", p)
                    after_p = p + 1
                    Q_start = ''
                    d = 0
                    #print(new_dka)
                    for d in range(len(new_dka)):
                        if new_dka[d][3] == after_p:
                            Q_start = new_dka[d][0]
                    #c = int(Q_start.replace("Q", ''))
                    #print(c)
                    #print("Q_start and Q_end", Q_start, Q_end)
                elif cur_reg[i] == ")":
                    if Q_start != '' and Q_end != '':
                        after_bracket = open_brackets[len(open_brackets) - 1] + 1
                        d = 0
                        for d in range(len(new_dka)):
                            if new_dka[d][3] == after_bracket:
                                state_after_bracket = new_dka[d][0]
                    Q_start = ''
                    Q_end = ''
                    #print(open_brackets)
                    open_brackets.pop()
                    #print(open_brackets)
                elif cur_reg[i] == "*":
                    if cur_reg[i - 1] == ")":
                        asd = []
                        asd.append("Q" + str(c))
                        asd.append(state_after_bracket)
                        asd.append("*")
                        asd.append(i)
                        new_dka.append(asd)
                        state_after_bracket = ''

        print("Без Epsion переходов для ", cur_reg)
        for u in new_dka:
            print(u)
            #dka.append(j)
        res.append(new_dka)
        num_of_reg = num_of_reg + 1

    return res

def drawing_dka(dka):
    #print(dka)
    q = 3
    for X in dka:
        f_name = "X" + str(q)
        name_of_file = "dka_graph_" + f_name

        f = graphviz.Digraph('DKA', filename=name_of_file)
        f.attr(rankdir='LR', size='8,5')

        f.node('Q0')
        f.attr('node', shape='doublecircle')

        for trs in X:
            f.edge(trs[0], trs[1], trs[2])
            #f.edge('Q0', 'Q1', label='Eps')

        f.view()
        q = q - 1

if __name__ == '__main__':
    list_of_rules = grammatic_input()
    list_of_reg = transform_grm_to_reg(list_of_rules)
    print(list_of_reg)
    print("Система уравнений: ")
    for i in list_of_reg:
        a = i[1:]
        print(i[0], "=", " + ".join(a))
    reg_list = solving_sys_of_reg(list_of_reg)
    print("Решения: ")
    for i in reg_list:
        print(i[0], "=", i[1])
    graphs = making_nka(reg_list)
    dka = deter_nka(reg_list, graphs)
    drawing_dka(dka)
    #print(graphs)
