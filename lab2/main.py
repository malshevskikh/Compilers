
grammatic1 = [["E","E+T","T"],
         ["T", "T*F", "F"],
         ["F", "(E)", "a"]]

grammatic2 = [["S","Aa","b"],
              ["A","Ac","Sd","Eps"]]

grammatic4 = [["A","BC","a"],
              ["B","CA","Ab"],
              ["C","AB","CC","a"]]

grammatic5 = [["E","E+T","T"],
         ["F", "(E)", "a"]]

grammatic6 = [["S", "A", "B"],
              ["A", "a"],
              ["B", "b", "C"],
              ["C", "c"],
              ["E", "e"]]


def delete_left_recursion(gramm):
    print("------------------", gramm, "---------------------")
    #------------------------ШАГ №1----------------------------
    no_term = []
    all_new_rules = []
    for i in gramm:
        no_term.append(i[0])
    all_new_rules = []
    counter_i = no_term
    print("N = ", no_term)
    i = 0
    j = -100
    #print(i, counter_i[0])
    n = len(no_term) - 1
    flag2 = True
    flag4 = True
    flag3 = True
    flag_for_list = False
    flag_to_stop = False
    g = 0
    q = 0
    # ----------------------------------------------------------
    counter = 1
    while (flag_to_stop == False):
        print("Итерация №", counter)
        print("i=", i, "j=", j)
        # ------------------------ШАГ №2----------------------------
        print("Шаг 2 ")
        print("Текущая грамматика: ", gramm)
        if flag2:
            gramm_for_func = gramm
            #print(gramm_for_func)
            gramm = step2(gramm_for_func, counter_i, g, i)
            #print("gramm", gramm)
            #print("gramm_for_func", gramm_for_func)
            if gramm != gramm_for_func:
                flag_for_list = True
            else:
                flag_for_list = False
        print("Новая грамматика", gramm)
        # ----------------------------------------------------------
        # ------------------------ШАГ №3----------------------------
        print("Шаг 3")
        #print("i=", i, "j=", j)
        if flag3:
            if i == n:
                break
            else:
                i = i + 1
                if flag_for_list == True:
                    g = g + 2
                else:
                    g = g + 1
                j = 0
                q = 0
        print("i=", i, "j=", j)
        # ------------------------ШАГ №4----------------------------
        print("Шаг 4")
        print("Текущая грамматика: ", gramm)
        if flag4:
            gramm_for_func = gramm
            gramm = step4(gramm_for_func, no_term, g, q)
        print("Новая грамматика", gramm)
        # ------------------------ШАГ №5----------------------------
        print("Шаг5")
        #print("i=", i, "j=", j)
        if j == i - 1:
            flag2 = True
            flag3 = True
        else:
            j = j + 1
            flag4 = True
            flag2 = False
            flag3 = False
            if flag_for_list != True:
                q = q + 2
            else:
                q = q + 1
        print("i=", i, "j=", j)
        #print("Грамматика после преобразования:", gramm)
        flag_for_list = False
        print()
        counter = counter + 1
    print("Результат:", gramm)

def step2(gramm, counter_i, i, left):
    all_new_rules = []
    Aalpha = []
    Beta = []
    aaa = []
    bbb = []
    for r in range(1, len(gramm[i])):
        # print(gramm[i][j])
        #print(counter_i[i])
        #print(counter_i)
        if (gramm[i][r][0] == counter_i[left]) and (gramm[i][r] != "Eps"):
            # print(gramm[i][j][0], "=", val, "Левая рекурсия")
            Aalpha.append(gramm[i][r])
            aaa.append(gramm[i][r])
        else:
            Beta.append(gramm[i][r])
            bbb.append(gramm[i][r])
    #print("alpha", Aalpha)
    #print("Beta", Beta)
    #print("aaa", aaa)
    #print("bbb", bbb)
    #print("counter_i", counter_i, "i", i)
    if Aalpha != []:
        new_rule = list(gramm[i][0]) + Aalpha + Beta
        #print("Beta", Beta)
        #print("Alpha", Aalpha)
        rule_with_shtrih = gramm[i][0] + "'"

        for r in range(0, len(bbb)):
            if bbb[r] == "Eps":
                bbb.pop(r)
            else:
                bbb[r] = bbb[r]
        for r in range(0, len(aaa)):
            aaa[r] = aaa[r][1:]
        for r in range(0, len(Beta)):
            if Beta[r] != "Eps":
                Beta[r] = Beta[r] + rule_with_shtrih
            else:
                Beta[r] = rule_with_shtrih
        for r in range(0, len(Aalpha)):
            Aalpha[r] = Aalpha[r][1:] + rule_with_shtrih
        l1 = []
        l2 = []
        l1.append(rule_with_shtrih)
        l2.append(gramm[i][0])
        #print("11111", rule_with_shtrih, type(rule_with_shtrih), list(rule_with_shtrih), l1)
        #print("ddddd", gramm[i][0])
        #print(l2)
        #print(bbb)
        #print(Beta)
        rule1 = l2 + bbb + Beta
        rule2 = l1 + aaa + Aalpha + ["Eps"]
        #print("rule1", rule1)
        #print("rule2", rule2)
        all_new_rules.append(rule1)
        all_new_rules.append(rule2)
        # print("ааааааааа: ",all_new_rules)
        # print("еееееееее:", gramm)
        gr1 = gramm[:i]
        gr2 = gramm[i + 1:]
        gramm = gr1 + all_new_rules + gr2
        # print("qqqqqqqq:", gr1, gr2)
    else:
        new_rule = list(counter_i[left]) + Beta
        #print("Новое правило:", new_rule)
        gramm[i] = new_rule
        # all_new_rules.append(new_rule)
        #j = 0
    #print("новая грамматика:", gramm)
    return gramm

def step4(gramm, no_term, i, j):
    #print("i =", i, "j =", j)
    #print("Текущее правило", gramm[i])
    #print("Правило для проверки рекурсии", gramm[j])
    new_rule_changing = []
    new_rule_changing.append(gramm[i][0])
    #print(new_rule_changing)
    for r in range(1, len(gramm[i])):
        if (gramm[i][r][0] == no_term[j]) and (gramm[i][r] != "Eps"):
            elem = gramm[i][r]
            elem_without_rule = elem[1:]
            changing = gramm[j][1:]
            new_change = [x + elem_without_rule for x in changing]
            new_rule_changing = new_rule_changing + new_change
        else:
            new_rule_changing.append(gramm[i][r])
    gramm[i] = new_rule_changing
    return gramm


def del_unreachable_char(gramm):
    print("Правила:", gramm)
    optional_gramm = []
    for hh in gramm:
        optional_gramm.append(hh)
    #----------------подготовка-----------------
    G = []
    G_new = []
    Term = []
    No_term = []
    R = []
    E = []
    for i in range(0, len(gramm)):
        R.append(gramm[i])
        for j in range(0, len(gramm[i])):
            #print(gramm[i][j])
            if i == 0 and j == 0:
                E.append(gramm[i][j])
            #for r in range(0, len(gramm[i][j])):
            #print(gramm[i][j][r])
            if len(gramm[i][j]) == 1:
                if (gramm[i][j] not in Term) and (gramm[i][j] not in No_term):
                    Term, No_term = check(gramm[i][j], Term, No_term)
            elif len(gramm[i][j]) > 1:
                if (gramm[i][j] not in Term) and (gramm[i][j] not in No_term):
                    Term, No_term = modern_check(gramm[i][j], Term, No_term)
    G.append(No_term)
    G.append(Term)
    G.append(R)
    G.append(E)
    print("Грамматика G:", G)
    #Начало алгоритма
    V_cur = []
    V_new = []
    V_prev = []
    #---------------------Шаг 1---------------------
    V_cur.append(G[3][0])
    i = 0
    flag_to_stop = False
    while flag_to_stop == False:
        #print("V_cur_000", V_cur)
        #print("V_new_000", V_new)
        if i <= len(gramm) - 1:
            #---------------------Шаг 2---------------------
            vr_arr = []
            #print("V_cur_000", V_cur)
            #print("V_new_000", V_new)
            #print("i", i, "gramm", gramm[i])


            #if optional_gramm != []:
            flag_to_start = False
            #Проверка на то, что дальше имеет смысл проверять
            for k in V_cur:
                for l in optional_gramm:
                    if k == l[0]:
                        flag_to_start = True

            #print("flag_to_start", flag_to_start)

            if flag_to_start == True:
                for j in range(1, len(gramm[i])):
                    if (gramm[i][j] not in vr_arr) and (gramm[i][j]!=gramm[i][0]):
                        l = fix(gramm[i][j])
                        #print("l", l)
                        #vr_arr.append(gramm[i][j])
                        for r in l:
                            if r not in vr_arr:
                                vr_arr.append(r)
                        #vr_arr = vr_arr + l
                #print(vr_arr)
                V_new = V_new + V_cur
                for w in vr_arr:
                    if w not in V_new:
                        V_new.append(w)

                #print("V_cur", V_cur)
                #print("V_new", V_new)
                if V_new != V_cur:
                    i = i + 1
                    V_prev = V_new
                else:
                    flag_to_stop = True
                V_cur = V_new
                V_new = []
        else:
            if V_prev == V_cur:
                flag_to_stop = True

        if optional_gramm != []:
            optional_gramm.pop(0)
        else:
            break

        #print("gramm", gramm)
        #print("optional_gramm", optional_gramm)

    V_e = V_cur
    print("V_e:", V_e)
    new_Term = []
    new_No_term = []
    new_R = []
    new_E = []
    new_G = []
    #--------------Новые терминалы--------------
    for i in V_e:
        if i in No_term:
            new_No_term.append(i)
    #--------------Новые нетерминалы--------------
    for i in V_e:
        if i in Term:
            new_Term.append(i)

    new_G.append(new_No_term)
    new_G.append(new_Term)
    #--------------Новые правила--------------
    new_G.append(G[2])
    #--------------Новый начальный терминал--------------
    new_G.append(G[3])
    print("Новая грамматика G':", new_G)

def check(elem, term, no_term):
    #print(elem)
    if elem.isalpha() == True:
        term.append(elem)
    elif (elem.isalpha() == False) and (elem.isdigit() == False):
        no_term.append(elem)
    return term, no_term

def modern_check(elem, term, no_term):
    indexes_of_symbols = []
    variables = []
    for i in range(0, len(elem)):
        if (elem[i].isalpha() == False) and (elem[i].isdigit() == False):
            indexes_of_symbols.append(i)
            if elem[i] not in no_term:
                no_term.append(elem[i])
    var = ''
    for i in range(0, len(elem)):
        if (elem[i].isalpha() == True) or (elem[i].isdigit() == True):
            #print("AAAAAA", elem[i])
            var = var + elem[i]
            #print()
            if (i == len(elem) - 1):
                variables.append(var)
        else:
            #print("слово", var)
            if var != '':
                variables.append(var)
            var = ''
    #print(variables)
    for i in variables:
        if i not in term:
            term.append(i)
    return term, no_term

def fix(elem):
    indexes_of_symbols = []
    variables = []
    list_of_elements = []
    if len(elem) > 1:
        for i in range(0, len(elem)):
            if (elem[i].isalpha() == False) and (elem[i].isdigit() == False):
                indexes_of_symbols.append(i)
                if elem[i] not in list_of_elements:
                    list_of_elements.append(elem[i])
        var = ''
        for i in range(0, len(elem)):
            if (elem[i].isalpha() == True) or (elem[i].isdigit() == True):
                #print("AAAAAA", elem[i])
                var = var + elem[i]
                #print()
                if (i == len(elem) - 1):
                    variables.append(var)
            else:
                #print("слово", var)
                if var != '':
                    variables.append(var)
                var = ''
        #print(variables)
        for i in variables:
            if i not in list_of_elements:
                list_of_elements.append(i)
    elif len(elem) == 1:
        list_of_elements.append(elem[0])
    return list_of_elements


if __name__ == '__main__':
    #left_recursion(grammatic1)
    delete_left_recursion(grammatic1)
    print()
    print("------------------------------------")
    #left_recursion(grammatic1)
    delete_left_recursion(grammatic2)
    print()
    print("------------------------------------")
    #delete_left_recursion(grammatic3)
    #print()
    delete_left_recursion(grammatic4)
    print()
    print("------------------------------------")
    #left_recursion(grammatic3)
    del_unreachable_char(grammatic1)
    print()
    print("------------------------------------")
    print()
    del_unreachable_char(grammatic5)
    print()
    print("------------------------------------")
    print()
    del_unreachable_char(grammatic6)
    print()
    print("------------------------------------")


