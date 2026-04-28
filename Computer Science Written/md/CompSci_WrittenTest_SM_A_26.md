# **UIL COMPUTER SCIENCE WRITTEN TEST – 2026 INVITATIONAL A**

**Note:** Correct responses are based on **Java SE Development Kit 25 (JDK 25)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 25 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

| Question 1<br>Which of the following is the base 2 representation of 81610? |                                                |
|-----------------------------------------------------------------------------|------------------------------------------------|
| A) 11001100002<br>B) 11011011012<br>C) 11011010002                          | D) 11001100012<br>E) 11011010102               |
|                                                                             |                                                |
| Question 2<br>What is output by the code to the right?                      | int result = 2 + 3 * 4 - 6 / 3;                |
| A) 4<br>B) 5<br>C) 10<br>D) 11<br>E) 12                                     | out.println(result);                           |
| Question 3                                                                  |                                                |
| What is output by the code to the right?                                    |                                                |
| A) x = 5, y = 2.8<br>B) x = 5, y = 2.7                                      | out.printf<br>("x = %d, y = %.1f\n", 5, 2.75); |
| C) x = 5, y = 2.75<br>D) x = %d, y = %.1f                                   |                                                |
| E) There is no output due to an error.                                      |                                                |
| Question 4                                                                  |                                                |
| What is output by the code to the right?                                    | String s = "Java Rocks";                       |
| A) Java<br>B) Roc                                                           | int len = s.length();                          |
| C) Rocks<br>D) Rock                                                         | String t = s.substring(5, len);                |
| E) ava                                                                      | out.println(t);                                |
| Question 5                                                                  |                                                |
| What is output by the code to the right?                                    | boolean result = true    false && !false;      |
| A) false<br>B) true                                                         | out.println(result);                           |
| Question 6                                                                  | double a = -3.7;                               |
| What is output by the code to the right?                                    | double b = 2.0;                                |
| A) -3.7<br>B) 3.7                                                           | double c = Math.abs(a);                        |
| C) 2.0<br>D) 2                                                              | out.println(Math.max(b, c));                   |
| Question 7                                                                  |                                                |
| What is output by the code to the right?                                    | int x = 4;                                     |
| A) 10<br>B) 11                                                              | x = x + 2 * 3;<br>x = x - 1;                   |
| C) 12<br>D) 9                                                               | out.println(x);                                |
| E) 13                                                                       |                                                |
| Question 8                                                                  | int score = 85;                                |
| What is output by the code to the right?                                    | if(score >= 90) {                              |
| A) D                                                                        | out.println("A");                              |
| B) C                                                                        | } else if(score >= 80) {<br>out.println("B");  |
| C) A                                                                        | } else {                                       |
| D) B                                                                        | out.println("C");                              |
| E) ABC                                                                      | }                                              |

# **Question 9** What is output by the code to the right? **A)** 0 1 2 3 **B)** 1 2 3 4 **C)** 0 1 2 3 4 **D)** 0 1 2 **E)** 1 2 3 for(int i = 1; i <= 3; i++) { out.print(i + " "); } **Question 10** Which of the following correctly creates an int array of length 4 and sets its first element to 10? **A)** int[] a = new int[4]; **B)** int[] a = new int[4]; a[1] = 10; a[0] = 10; **C)** int[4] a = {10}; **D)** int a = new int[4]; a[0] = 10; **E)** int[] a = {10}; **Question 11** Which standard Scanner method could not read the value 129 as input from a file? **A)** nextLine() **B)** next() **C)** nextInt() **D)** nextDouble() **E)** nextByte() **Question 12** What is output by the code to the right? **A)** 10 **B)** 11 **C)** 15 **D)** 6 **E)** 9 int sum = 0; for(int i = 1; i <= 4; i++) { sum += i; } out.println(sum); **Question 13** What is output by the code to the right? **A)** 0 **B)** 2 **C)** 3 **D)** 1 **E)** 11 int result = 3 + 4 \* 2 > 10 ? 1 : 0; out.println(result); **Question 14** Which of the following primitive data types can store the largest whole-number value? **A)** byte **B)** short **C)** int **D)** long **E)** char **Question 15** Which of the following correctly declares and creates an ArrayList that stores String objects? **A)** ArrayList list = new ArrayList<String>(); **B)** ArrayList<String> list = new ArrayList<String>(); **C)** ArrayList<String> list = new ArrayList<string>(); **D)** ArrayList<String> list = new ArrayList<int>(); **E)** None of the above. **Question 16** What is output by the code to the right? **A)** 23 **B)** 13 **C)** 123 try { int i = 1; i = i / --i; out.print(1); } catch (ArithmeticException e) {

}

out.print(2);

out.print(3);

} finally {

**D)** There is no output due to a compile error. **E)** There is no output due to a runtime error.

What could replace <1\*> in the code to the right so that it will compile and run without error.

- A) push
- B) offer
- C) add

- **D)** Both B and C.
- E) All of the above.

## Question 18

Assuming <1\*> is filled in correctly, which of the following could not be found in the output by the code to the right?

- **A)** 191
- **B)** 15
- **C)** 190
- **D)** 13
- E) More than one of the above.

## Question 19

What is the big  $\boldsymbol{\mathcal{O}}$  runtime of the code to the right

- **A)**  $O(N \log \log N)$
- B) O(N)

C)  $\mathcal{O}(N^2)$ 

- **D)**  $O(\log \log N)$
- **E)**  $\mathcal{O}(N^2 \log \log N)$

## Question 20

Which of the lines in the code to the right first causes an error (compile- or run-time)?

**A)** //1

**B)** //2

**C)** //4

- **D)** //3
- E) None of the above. All lines will be error-free.

## Question 21

What is output if the following call is made to the function  ${\tt fun}$  to the right?  ${\tt fun}$  (-7);

**A)** -7

**B)** -212

**C)** 0

- **D)** 212
- **E)** There is no output due to a runtime error.

### Question 22

What is output if the following call is made to the function fun to the right? fun(14);

**A)** -83

**B)** -89

**C)** -86

- **D)** -80
- **E)** There is no output due to a runtime error.

```
Queue<Integer> s;
s = new LinkedList<Integer>();
for(int y = 0; y < 100; y++) {
   int i = 13;
   i += (int)(Math.random() * 178);
   s.<1*>(i);
}
while(!s.isEmpty())
   out.println(s.poll());
```

```
int i = 1, j = 0;

j *= 8.9; //1
\ni /= j++; //2
\ni += ++i; //3

j += (i -= 1); //4
```

```
int fun(int n) {
   int i = 7;
   if(n < 0)
      return -212;
   if(n%2 == 1)
      i = 10;
   return i + fun(n - 1);
}</pre>
```

What can replace **<1\*>** in the code to the right so that the code compiles and runs without error?

- **A)** private **B)** abstract
- **C)** parent **D)** public
- **E)** More than one of the above.

## **Question 24**

What can replace **<2\*>** in the code to the right so that the code compiles and runs without error?

- **A)** Nothing is required. **B)** super(m)
- **C)** super() **D)** A or C
- **E)** Any of the above.

## **Question 25**

What can replace **<3\*>** in the code to the right so that the code compiles and the getNum method returns the sum of values n and m?

- **A)** m + super.getNum()
- **B)** n + m
- **C)** getNum() + super.getNum()
- **D)** A or B
- **E)** All of the above.

## **Question 26**

Assuming **<1\*>**, **<2\*>**, and **<3\*>** are filled in correctly, what is output by the line marked //q26 in the code to the right?

- **A)** 17 17 **B)** 7 10

- **C)** 7 17 **D)** 17 10
- **E)** There is no output due to a runtime error.

#### **Question 27**

Assuming **<1\*>**, **<2\*>**, and **<3\*>** are filled in correctly, what is output by the line marked //q27 in the code to the right?

- **A)** null
- **B)** null null
- **C)** The output is an empty line with one space.
- **D)** There is no output due to a compile error.
- **E)** There is no output due to a runtime error.

#### **Question 28**

What is output by the code to the right?

- **A)** false false **B)** false true
- **C)** true false **D)** true true
- **E)** There is no output due to a compile error.

```
abstract class A { 
 int n; 
 String s; 
 int getNum() { 
 return n; 
 } 
 <1*> String getS(); 
} 
class B extends A { 
 int m; 
 public B(int m) { 
 <2*>; 
 this.m = m; 
 } 
 String getS() { 
 return s; 
 } 
 int getNum() { 
 return <3*>; 
 } 
} 
/////////// client code ////////////
A a = new B(7); 
B b = new B(10); 
String s = "" + a.getNum(); 
s += " " + b.getNum(); 
out.println(s); //q26 
s = a.getS() + " "; 
s += b.getS(); 
out.println(s); //q27
```

```
String mat = "theupsidedown"; 
String r = "[c-w]+\\D?"; 
String o = "" + mat.matches(r); 
r = "\\w?{8,15}"; 
o += " " + mat.matches(r); 
out.println(o);
```

What is output by the code to the right?

**A)** 98 **B)** 104

**C)** 106 **D)** 127

**E)** There is no output due to a runtime error.

```
int i = 0b1000101; 
String s = Integer.toString(i, 6); 
i = Integer.parseInt(s, 7); 
s = Integer.toString(i, 9); 
i = Integer.parseInt(s); 
out.println(i);
```

Use the following graph for questions 30-33:

![](_page_4_Picture_9.jpeg)

#### **Question 30**

Which of the following accurately describes graph pictured above?

- **A)** Undirected Unweighted **B)** Undirected Weighted **C)** Directed Weighted **D)** Directed Unweighted

### **Question 31**

What is the cost of the shortest path from Node to node  in graph pictured above?

- **A)** 23 **B)** 31 **C)** 25 **D)** 26 **E)** 28

#### **Question 32**

Which of the following describes Node in graph pictured above?

- **A)** Isolated **B)** Sink **C)** Source **D)** All of the above. **E)** None of the above.

#### **Question 33**

What is the shortest cost path from Node to node in graph pictured above?

- **A) B) C) D) E)**

## **Question 34**

What is output by the code to the right?

- **A)** 8 **B)** 4
- **C)** 2 **D)** 1
- **E)** There is no output due to an error.

```
import static java.lang.System.*; 
public class Q34 { 
 public static final int NUM_BYTES = NUM_BITS / 8; 
 public static final int NUM_BITS = Integer.SIZE; 
 public static void main(String[] args) { 
 out.println(NUM_BYTES); 
 }
```

}

What is output by the code to the right?

- **A)** 8 **B)** 4 **C)** 2
- **D)** There is no output due to a compilation error on L1.
- **E)** There is no output due to a compilation error on L2.

# **Question 36**

What is output by the code to the right?

**A)** 5 **B)** 5

1\_000\_000\_009 1000000009

**C)** 1\_000\_000\_009 **D)** 1000000009 5 5

**E)** There is no output due to an error.

## **Question 37**

Which of the following changes to the program to the right will cause the program to run without error?

- **A)** Do nothing. The code will run without error as is.
- **B)** Remove the underscores from L1.
- **C)** Change L2 to System.out.println(5);.
- **D)** Wrap L2 in a static block (i.e., static { … } ).
- **E)** Remove L3.

#### **Question 38**

Assuming that the correct choice from question 37 has been implemented in the code to the right, what will be the output of the modified program?

1\_000\_000\_009 1000000009

**A)** 5 **B)** 5

**C)** 1\_000\_000\_009 **D)** 1000000009 5 5

**E)** None of the above.

#### **Question 39**

What is the minimum number of nodes that need to be *added* to the tree to the right to make it a *full* binary tree? Write your answer in the blank provided on your answer sheet for this question.

## **Question 40**

What is the minimum number of nodes that need to be *added* to the tree to the right to make it a *complete* binary tree? Write your answer in the blank provided on your answer sheet for this question.

```
import static java.lang.System.*; 
public class Q35 { 
 public final int NUM_BYTES = NUM_BITS / 8; // L1 
 public static final int NUM_BITS = Long.SIZE; 
 public static void main(String[] args) { 
 out.println(NUM_BYTES); // L2 
 } 
}
```

```
import static java.lang.System.*; 
public class Q36_37_38 { 
 private static final int MOD = 1_000_000_009; // L1 
 out.println(5); // L2 
 public static void main(String[] args) { 
 out.println(MOD); // L3 
 } 
}
```

![](_page_5_Figure_38.jpeg)

![](_page_6_Picture_0.jpeg)

# **UIL COMPUTER SCIENCE – 2025-2026 INVITATIONAL A**

**Questions** (+6 points for each correct answer, -2 points for each incorrect answer)

1) A 11) E 21) B 31) A

2) E 12) A 22) C 32) D

3) A 13) D 23) B 33) A

4) C 14) D 24) D 34) E

5) B 15) B 25) D 35) E

6) B 16) A 26) B 36) E

7) D 17) D 27) B 37) D

8) D 18) A 28) C 38) B

9) E 19) B 29) C \*

39) 5

10) B 20) B 30) C \*

40) 8

**Note:** Correct responses are based on **Java SE Development Kit 25 (JDK 25)** from Sun Microsystems, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

*<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.*

# Explanations:

| 1.  | А | Simple base conversion.                                                                                                                                                                 |
|-----|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2.  | E | Multiplication/division first: $3 * 4 = 12$ , $6/3 = 2$ ; so $2 + 12 - 2 = 12$ .                                                                                                        |
| 3.  | A | %d prints 5; % .1f rounds 2 .75 to one decimal place $\rightarrow$ 2 .8; \n moves to the next line.                                                                                     |
| 4.  | C | Indexing: $J(0) a(1) v(2) a(3) (4) R(5) o(6) c(7) k(8) s(9)$ .                                                                                                                          |
| ٠.  |   | substring (5, len) gives characters at indices $5-8 \rightarrow \text{"Rock"}$ .                                                                                                        |
| 5.  | В | !false is true. We process && before   , so:false && true = false, then                                                                                                                 |
| J.  |   | true    false = true.                                                                                                                                                                   |
| 6.  | В | Math.abs(-3.7) is 3.7; Math.max(2.0, 3.7) is 3.7.                                                                                                                                       |
| 7.  | D | $+2*3 \rightarrow 4+6=10$ ; then $x-1 \rightarrow 10-1=9$ .                                                                                                                             |
| 8.  | D | $+2*3 \rightarrow 4+0=10$ , then $x=1\rightarrow 10=1=7$ .<br>85 is not $\geq 90$ but is $\geq 80$ , so the second branch runs $\rightarrow$ "B".                                       |
| 9.  | E | Loop runs with $i = 1, 2, 3$ ; prints "1 2 3 ".                                                                                                                                         |
|     | † |                                                                                                                                                                                         |
| 10. | В | Arrays are 0-indexed; first element is index 0. new int [4] creates a length-4 array.                                                                                                   |
| 11. | E | nextByte() can only read values between $-127$ and $128$                                                                                                                                |
| 12. | A | 1+2+3+4=10.                                                                                                                                                                             |
| 13. | D | Multiplication first: $4 * 2 = 8$ , so $3 + 8 = 11$ . $11 > 10$ is true, so ternary gives 1.                                                                                            |
| 14. | D | Among these, long has the largest range of whole numbers (64-bit vs 32-bit int, 16-bit short, 8-bit byte).                                                                              |
| 15. | В | Both sides should use String as the type parameter; int cannot be used as a generic type argument.                                                                                      |
| 16. | А | The exception caused by dividing by 0 is caught, so 2 and 3 are printed, but 1 is not as the error occurs before it can be printed.                                                     |
| 17. | D | Queue has offer () and add () methods, but no push ().                                                                                                                                  |
| 18. | A | The possible value range is [13,190].                                                                                                                                                   |
| 19. | В | Runtime of adding to the head and removing from the tail of a LinkedList (doubly-linked list                                                                                            |
|     |   | in Java) is $\mathcal{O}(1)$ , and we must do it $N$ times each so $N \cdot \mathcal{O}(1) = \mathcal{O}(N)$ . We do this twice, so we                                                  |
|     |   | get $\mathcal{O}(N+N) = \mathcal{O}(2N) = \mathcal{O}(N)$                                                                                                                               |
| 20. | В | No compile errors, and first runtime error is line $//2$ with dividing by $0$ .                                                                                                         |
| 21. | В | Simple recursion tracing, only the base case runs.                                                                                                                                      |
| 22. | С | Simple recursion tracing.                                                                                                                                                               |
| 23. | В | Only abstract works since the method is not defined in class A.                                                                                                                         |
| 24. | D | Only a default constructor exists for class A, and that is automatically called, even when no call is                                                                                   |
| 25  | _ | explicitly present.                                                                                                                                                                     |
| 25. | D | Variables m and n are accessible from class B, so we can use the super method or direct call for                                                                                        |
|     | _ | n; m must be accessed directly; and calling getNum() is infinite self-call.                                                                                                             |
| 26. | В | All instance variables in class A are 0, so the output is simply m for both instances.                                                                                                  |
| 27. | В | All instance variables in class A are null.                                                                                                                                             |
| 28. | С | Simple regex pattern matching (use <u>regexr.com</u> to check)                                                                                                                          |
| 29. | С | Base Conversion Tracing.                                                                                                                                                                |
| 30. | С | The graph has weights and, while several of the edges are bi-directional, there are some edges                                                                                          |
|     |   | which do not have a symmetric pair, and thus, is also directed.                                                                                                                         |
| 31. | Α | FHAB is the path with the least weight.                                                                                                                                                 |
| 32. | D | In a directed graph, a sink has no outbound edges, a source has no inbound edges, and an isolated vertex is one that has degree zero (both inbound and outbound). Thus, all 3 are true. |
| 33. | А | 17 is the cost for the correct path and the smallest option.                                                                                                                            |
| 34. | E | Note that you cannot reference a field before it is defined (forward reference), even if that field                                                                                     |
|     |   | is set to be static and final, so this creates a compilation error.                                                                                                                     |
| 35. | Е | The line marked $\mathbb{L}1$ is no longer the source of the compilation error as, despite the variable it's                                                                            |
| -   |   | referencing appearing after it, that variable is declared static, and thus, its value is made                                                                                           |
|     |   | available to the compiler before the Q35 class is initialized and thus $L2$ is compiled/calculated.                                                                                     |
|     |   |                                                                                                                                                                                         |
| 36. | F | Note that the reference to out.println(5): outside of the main method will create a                                                                                                     |
| 36. | E | Note that the reference to out.println(5); outside of the main method will create a compilation error as this is invalid Java syntax. Note that even if we used the full                |

![](_page_8_Figure_0.jpeg)