# Compilers
<!-- UNIVERSITY LOGO -->
<div align="center">
  <a href="https://bmstu.ru">
    <img src="https://user-images.githubusercontent.com/67475107/225371733-8fd6f639-bf62-49bd-866c-4e08116fa20c.png" alt="University logo" height="200">
  </a>
  
  Developed by Maxim Alshevskikh (<a href="https://www.linkedin.com/in/maxim-alshevskikh-b473b42b3/">LinkedIn</a>)
  <br/>
</div>


<h2>Lab №1. Write a program that takes a random right-linear grammar as input and performs the following transformations (Напишите программу, которая в качестве входа принимает произвольную праволинейную  грамматику, и выполняет следующие преобразования):</h2>
<h3>In english:</h3>
<ol>
  <li>Given a right-linear grammar, constructs a standard system of equations with regular coefficients, the unknowns of which are the nonterminals of the original grammar.</li>
  <li> Solves a standard system of equations with regular coefficients.</li>
  <li> Given a regular expression that is a solution to a standard system of equations with regular coefficients, constructs an Nondeterministic Finite Automaton (NFA).</li>
  <li> Deterministically models an NFA.</li>
</ol>
<h3>In russian:</h3>
<ol>
  <li>По праволинейной грамматике строит стандартную систему уравнений с регулярными коэффициентами, неизвестными которой служат нетерминалы исходной грамматики.</li>
  <li>Решает стандартную систему уравнений с регулярными коэффициентами.</li>
  <li>По регулярному выражению, являющемуся решением стандартной системой уравнений с регулярными коэффициентами, строит недетерминированный конечный автомат (НКА).</li>
  <li>Детерминировано моделирует НКА.</li>
</ol>

<h3>Result:</h3>

<h4>Input (example of right-linear grammar):</h4>

![pic1](https://github.com/user-attachments/assets/cde0b75e-e741-4d27-93ca-f71f220007d3)

<h4>Output:</h4>
<h5>System of equations according to right-linear grammar:</h5>

![pic2](https://github.com/user-attachments/assets/7058c06a-99df-4ee7-b1ee-3fd0688eb185)

<h5>Solution of a system of equations:</h5>

![pic3](https://github.com/user-attachments/assets/b8384632-142d-4c6d-9700-99989495a265)

<h5>List of state transitions in expression X3:</h5>

![pic4](https://github.com/user-attachments/assets/6c886239-29a5-4c90-8610-1b6916b48c7d)

<h5>List of state transitions in expression X2:</h5>

![pic5](https://github.com/user-attachments/assets/d78f6fde-81d4-4987-a68d-7725b2db6009)

<h5>List of transitions between states in expression X1:</h5>

![pic6](https://github.com/user-attachments/assets/6acbb740-73c5-413e-b3a1-6afd898697f9)

<h5>NFA for expression X3:</h5>

![pic7](https://github.com/user-attachments/assets/e3424969-3f54-401d-8ef4-7165a40056d9)

<h5>NFA for expression X2:</h5>

![pic8](https://github.com/user-attachments/assets/6c6c1115-86df-445c-95ff-71566eb1d5de)


<h5>NFA for expression X1</h5>

![pic9](https://github.com/user-attachments/assets/3658c44e-0532-43ae-9490-ea592d786638)


<h5>List of state transitions without Eps transitions in expressions X3, X2, X1:</h5>

![pic10](https://github.com/user-attachments/assets/1f92c225-6e3b-4dda-a9aa-42e02f945fd6)


<h5>Deterministic finite automaton (DFA) for X3:</h5>

![pic11](https://github.com/user-attachments/assets/b576e5be-ba09-4053-b115-cb2f1601396b)

<h5>DFA for X2:</h5>

![pic12](https://github.com/user-attachments/assets/886471ee-26ac-44ec-a8ed-ec0b82adf2da)

<h5>DFA for X1:</h5>

![pic13](https://github.com/user-attachments/assets/e233ccd2-8eec-4923-8375-06e195bc30e5)


<h2>Lab №2. Grammar transformations (Преобразования грамматик):</h2>
<h3>In english:</h3>
<ol>
  <li>Build a program that takes as input the given context-free grammar (CFG) G = (N,E,P,S) and transforms it into an equivalent CFG G' without left recursion.</li>
  <li>Build a program that takes as input an arbitrary CFG G = (N,E,P,S) and transforms it into an equivalent CFG G' = (N',E',P',S') that does not contain unreachable symbols.</li>
</ol>
<h3>In russian:</h3>
<ol>
  <li>Постройте программу, которая в качестве входа принимает приведенную контекстно-свободную грамматику (КС-грамматику) G = (N,E,P,S) и преобразует ее в эквивалентную КС-грамматику G' без левой рекурсии.</li>
  <li>Постройте программу, которая в качестве входа принимает произвольную КС-грамматику G = (N,E,P,S) и преобразует ее в эквивалентную КС-грамматику G' = (N',E',P',S'), не содержащую недостижимых символов.</li>
</ol>

<h3>Result:</h3>

<h4>Input (list of grammars):</h4>

![pic1](https://github.com/user-attachments/assets/8b51bcbb-a573-42f4-9c0f-cd0b9e510e04)

<h4>Output (detailed description of the algorithm for eliminating left recursion with the result):</h4>

![pic2](https://github.com/user-attachments/assets/24f09879-f5d5-457d-b53a-8495b38f1689)

![pic3](https://github.com/user-attachments/assets/6a1965e9-58c3-4d8d-9ceb-7c26d3c9f52d)


<h2>Lab №3. Parsing using recursive descent method (Синтаксический разбор с использованием метода рекурсивного спуска):</h2>

<img width="662" alt="Снимок экрана 2025-01-22 в 12 05 26" src="https://github.com/user-attachments/assets/762d2299-0a38-458b-ac30-4fb09a22c699" />

<h3>In english:</h3>
<ol>
  <li>Supplement the grammar with a block consisting of a sequence of assignment operators. Two variants of the extended grammar are proposed for implementation.</li>
  <li>For the modified grammar, write a program for descending syntactic analysis using the recursive descent method.</li>
</ol>
<h3>In russian:</h3>
<ol>
  <li>Дополнить грамматику блоком, состоящим из последовательности операторов присваивания. Для реализации предлагаются два варианта расширенной грамматики.</li>
  <li>Для модифицированной грамматики написать программу нисходящего синтаксического анализа с использованием метода рекурсивного спуска.</li>
</ol>

<h3>Result:</h3>
<h4>As one of the two grammar options, the C-style grammar was chosen as an additional one:</h4>

<img width="377" alt="Снимок экрана 2025-01-22 в 12 08 32" src="https://github.com/user-attachments/assets/7feab664-f934-44fd-9d89-2433aea7f2b7" />

<h4>Input string for checking:</h4>

![pic1](https://github.com/user-attachments/assets/3734b424-86f5-488b-bb6b-f9aaac62380a)


<h4>Output:</h4>

<h5>Input string and list of rules:</h5>

![pic2](https://github.com/user-attachments/assets/df7700ff-6ad9-43b7-a536-32f1c3c488a9)

<h5>Parsing the first part of the line:</h5>

![pic3](https://github.com/user-attachments/assets/161a690f-bc7e-4f46-91aa-279449a57b3b)

<h5>Parsing the second part of the line:</h5>

![pic4](https://github.com/user-attachments/assets/30e19d4e-63ca-433d-a49f-abcbba8f3419)

![pic4_1](https://github.com/user-attachments/assets/7b3c964b-b6fc-48f8-98ab-7db7a8c1c969)


<h5>Parsing the third part of the line:</h5>

![pic5](https://github.com/user-attachments/assets/d00a9f41-5265-41be-91f9-ccfac3b96e61)

<h5>Parsing the fourth part of the line:</h5>

![pic6](https://github.com/user-attachments/assets/0793a823-3451-42f0-9cdc-752acc13244b)

![pic6_1](https://github.com/user-attachments/assets/756f652e-2327-42ac-9b9b-156892d8f40e)

<h2>Course work. Compiler for Pascal programming language to Python programming language (Курсовая работа. Компилятор для языка программирования Pascal на языке программирования Python):</h2>

<h3>Task: Design a compiler in the Python programming language for the grammars of the Pascal programming language</h3>

<h3>Задание: сконструировать компилятор на языке программирования Python для грамматик языка программирования Pascal </h3>

<h3>Result:</h3>
<h4>1.Pascal syntax lines are entered. Example of Pascal code lines entered for the compiler (Вводятся строки с синтаксисом Pascal. Пример строк кода на Pascal, вводимых для компилятора:):</h4>
<img width="268" alt="image" src="https://github.com/user-attachments/assets/33b817bb-21f0-41d1-b3f9-20b300d28305" />

<h4>2.After selecting a code, for example the expression "5*10", the strings are passed to the parser constructor for lexical and syntactic analysis, as well as AST generation (После выбора кода, например выражения «5*10», строки передаются конструктору парсера для проведения лексического, синтаксического анализов, а также генерации AST):</h4>

<img width="288" alt="image" src="https://github.com/user-attachments/assets/eacd5d5e-68c0-426c-b075-9b74c90f5661" />

<h4>3.As a result of executing the code, an AST tree will be generated and when executing the code "5*10" the result will be "50" (В результате исполнения кода будет сгенерировано дерево AST и при выполнении кода «5*10» получится результат «50»):</h4>

<img width="482" alt="image" src="https://github.com/user-attachments/assets/9f5a2928-bf19-4e16-b49f-0d1bc9771c4f" />

<h4>4.Example of AST for input string 'ex9' (пример AST для входной строки):</h4>

<h4>1)</h4>
<img width="482" alt="image" src="https://github.com/user-attachments/assets/fa95108e-fde6-47dc-a29b-aed0aac9bfd2" />

<h4>2)</h4>
<img width="482" alt="image" src="https://github.com/user-attachments/assets/9d137b1e-913e-472f-961f-e531e0679465" />

<h4>3)</h4>
<img width="482" alt="image" src="https://github.com/user-attachments/assets/226906c6-ba85-49fe-be9a-b029af9558a1" />

