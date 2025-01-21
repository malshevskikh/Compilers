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
