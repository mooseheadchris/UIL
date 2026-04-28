# **UIL COMPUTER SCIENCE WRITTEN TEST – 2025 DISTRICT**

**Note:** Correct responses are based on **Java SE Development Kit 22 (JDK 22)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

| Question 1                                                                |           |                                                         |  |
|---------------------------------------------------------------------------|-----------|---------------------------------------------------------|--|
| Which of the following is not equivalent to the expression 25237 + AB716? |           |                                                         |  |
| A) 285611<br>B) 71538                                                     | C) 116115 | D) 1042315<br>E) All are equivalent                     |  |
| Question 2                                                                |           |                                                         |  |
| What is output by the code to the right?                                  |           |                                                         |  |
| A) 1<br>B) 9<br>C) 7                                                      | D) 0      | out.println(1 + 2 * 3 - 4 / 5);                         |  |
| E) There is no output due to a compile error.                             |           |                                                         |  |
| Question 3                                                                |           |                                                         |  |
| What is output by the code to the right?                                  |           |                                                         |  |
| A) abcde<br>B) abc                                                        |           | out.printf("%3S","abcde");                              |  |
| C) ABCDE<br>D) ABC                                                        |           |                                                         |  |
| E) There is no output due to a runtime error.                             |           |                                                         |  |
| Question 4                                                                |           |                                                         |  |
| What is output by the code to the right?                                  |           | String str = "CountDooku";                              |  |
| A) untDoot<br>B) ntDookt                                                  |           | str = str.substring(0,8);                               |  |
| C) ntDookn<br>D) untDoon                                                  |           | str += str.charAt(3);<br>out.println(str.substring(2)); |  |
| E) There is no output due to a runtime error.                             |           |                                                         |  |
| Question 5                                                                |           | boolean a = false;                                      |  |
| What is output by the code to the right?                                  |           | boolean b = true;                                       |  |
| A) true<br>B) false                                                       |           | a  = !b & a ^ b & !a;                                   |  |
| C) There is no output due to a syntax error.                              |           | out.println(a);                                         |  |
| Question 6                                                                |           |                                                         |  |
| What is output by the code to the right?                                  |           | int y = 9;                                              |  |
| A) 9<br>B) 8<br>C) 8.0<br>D) 9.0                                          |           | double x = 8.0;<br>out.print(Math.max(y,x));            |  |
| E) There is no output due to a runtime error.                             |           |                                                         |  |
| Question 7                                                                |           | int i = 0, ii = 10, n = 0;                              |  |
| What is output by the code to the right?                                  |           | for(;i <= ii;) {                                        |  |
| A) 22 32<br>B) 20 30                                                      |           | ii++;<br>i += ii / 10;<br>n++;                          |  |
| C) 21 31<br>D) 19 29                                                      |           |                                                         |  |
| E) There is no output due to a runtime error.                             |           | }                                                       |  |
|                                                                           |           | out.println(n+" "+ii);                                  |  |
| Question 8                                                                |           | int a = 34 + 21 & 9;                                    |  |
| What is output by the code to the right?                                  |           | int b = a   39 % 7;                                     |  |
| A) 101<br>B) 8<br>C) 36                                                   | D) 6      | a ^= b * 9 / 5;                                         |  |
| E) There is no output due to a runtime error.                             |           | out.println(a);                                         |  |

**Question 9** What is output by the code to the right? **A)** 9 **B)** 611 **C)** 610 **D)** 10 **E)** There is no output due to a runtime error. int i = 9; if(i < 10) i++; else if(i < 10) i--; else out.print(6); out.println(i); **Question 10** What is the output by the code to the right? **A)** 1 **B)** 3 **C)** 5 **D)** 2 **E)** There is no output due to a runtime error. int[] i = new int[] { 3, 2, 5, 4, 1, 0 }; int j = 3; for(int k = 0; k < 25; k++) j = i[j]; out.println(i[j]); **Question 11** Which of the following packages contains the Scanner class? **A)** java.lang.\* **B)** java.awt.\* **C)** java.util.\* **D)** java.io.\* **E)** None of the above. **Question 12** What is output by the code to the right? **A)** 109 **B)** 97 **C)** 128 **D)** 115 **E)** There is no output due to a runtime error. int sum = 1; for(int y = 0; y < 12; y++) { sum += y; for(int x = 0; x < y / 2; x++) sum ++; } out.println(sum); **Question 13** What is the order of precedence for the operators to the right? **A)** III, IV, II, I **B)** IV, III, I, II **C)** IV, III, II, I **D)** III, II, IV, I **E)** III, II, I, IV I. ?: II. + (additive) III. % IV. >>> **Question 14** What is output by the code to the right? **A)** 8 **B)** 64 **C)** 4 **D)** 32 **E)** There is no output due to a compile error. out.println(Double.BYTES); **Question 15** What is the output by the code to the right? **A)** [-17, 451, 1] **B)** [212, 451, -17] **C)** [1, 451, -17] **D)** [-17, 451, 212] **E)** There is no output due to a compile error. ArrayList<Integer> a; a = new ArrayList<Integer>(); a.add(1); a.add(212); a.add(451); a.remove(1); a.add(-17); out.println(a); **Question 16** What is the output by the code to the right? **A)** Greater **B)** Not Greater **C)** -1 **D)** 1 **E)** There is no output due to a compile error. out.print("instanceof".compareTo("int") > 4 ? "Greater" : "Not Greater");

Which of the following values is a possible value that the expression to the right may resolve to?

- A) 22.8
- **B)** 23
- **C)** 36.0

- D) A and B
- E) A and C

### Question 18

Using interval notation where a '[' or ']' represents an inclusive value, and a '(' or ')' represents an exclusive value, which of the following denotes the set of all possible values that can be returned by the method call to the right?

- **A)** [21,57)
- **B)** [21,57]
- **c)** (21,57]
- **D)** [21, 36)
- E) None of the above.

### Question 19

Which of the following best classifies the graph to the right?

- A) Undirected, Weighted, and Acyclic.
- B) Undirected and Unweighted.
- C) Directed and Unweighted.
- **D)** Directed, Weighted, and Acyclic.
- E) Directed, Weighted, and Cyclic.

### Question 20

Which of the following algorithms are guaranteed to produce the shortest path between two specific nodes in the graph to the right?

- A) Dijkstra's Algorithm
- B) Bellman-Ford Algorithm
- C) Floyd-Warshall AlgorithmW
- D) Both B and C
- E) All of the above.

### Question 21

What is the shortest path between the node labeled A and the node labeled J in the graph to the right?

- **A)** 18
- **B)** 19
- **c)** 20
- **D)** 21

E) None of the above.

### Question 22

How many ordered pairs of A, B, and C, make the boolean expression to the right resolve to true?

- **A)** 0
- **B)** 3
- **c)** 5
- **D)** 7
- **E)** 8

### Question 23

What is output by the code to the right?

- **A)** 2042 0
- **B)** 1438 2042
- **C)** 0 1438
- **D)** 2042 1438
- E) There is no output due to a runtime error.

$$(Math.random() * 36) + 21$$

![](_page_2_Figure_50.jpeg)

$$\overline{A \oplus \overline{C * B}} + \overline{A \oplus \overline{C} \oplus B}$$

int x = 1438; int y = 2042; x ^= y ^= x ^= y; out.println(x+" "+y);

What could replace <1\*> in the code to the right so that the A class compiles and functions as intended?

- A) this.y = n \* 2;
  y = n;
  B) super(n \* 2, n);
  C) super(n \* 2);
  y = n;
  D) super(n \* 2);
  super(n);
- E) More than one of the above.

### Question 25

What is the output by the line marked //q25 in the client code to the right?

**A)** 3 8

**B)** 3 4

**C)** 6 8

- **D)** 6 4
- E) There is no output due to a compile error.

### Question 26

Assuming any errors above the line marked //q26 have been corrected, what is the output by the line marked //q26 in the client code to the right?

- **A)** 8
- **B)** 10
- **C)** Output cannot be determined until runtime.
- **D)** There is no output due to a compile error.
- E) There is no output due to a runtime error.

### Question 27

Assuming any errors above the line marked //q27 have been corrected, what is the output by the line marked //q27 in the client code to the right?

- **A)** 12
- **B)** 13
- C) Output cannot be determined until runtime.
- **D)** There is no output due to a compile error.
- E) There is no output due to a runtime error.

### Question 28

Which of the following are equivalent to the Logic Circuit to the right?

- A)  $\overline{\overline{A} + B} * (C \oplus \overline{D})$
- $\overline{\bar{A} + \bar{B}} * (C \oplus \bar{D})$
- c)  $\overline{(A*\bar{B})*(C\oplus\bar{D})}$
- $\mathbf{D)} \ \overline{(A*B)*(C \oplus \overline{D})}$
- $E) \ \overline{A*\bar{B}} + \overline{C \oplus \bar{D}}$
- F)  $\overline{A*B} + \overline{C \oplus \overline{D}}$ H)  $\overline{A} + \overline{B} + C*\overline{D} + \overline{C}*D$
- **G)**  $\bar{A} + B + C * \bar{D} + \bar{C} * D$ **J)** Options A, C, E, and G.
- K) Options B, D, F, and H.
- L) None of the above.

```
class A{
    int y;
    public A(int n) {
        y = n;
    public int get() {
        return y;
class B extends A{
    int y;
    public B(int n) {
        <1*>
    public void add() {
        y++;
///////client code/////////
A = new A(3);
B b = new B(4);
String s = "";
s += a.qet() + " ";
out.println(s+b.get()); //q25
b.add();
b.add();
out.println(b); //q26
Ac = new B(6);
c.add();
```

![](_page_3_Picture_37.jpeg)

out.println(c.get()); //q27

The process of going from Option A to Option C in the previous question is an example of which Boolean Algebra Identity? A copy of the options has been provided for you below:

> Question 28, Option A: ̅+ ∗ ( ⊕ ) Question 28, Option C: ( ∗ ) ∗ ( ⊕ )

- **A)** Law of Absorption **B)** Exclusive NOR Law **C)** DeMorgan's Law **D)** Double Negative Law **E)** Disappearing Opposite

### **Question 30**

Consider the following snippets of Option F and Option H from Question 28. The process of going from Snippet 1 to Snippet 2 is an example of which Boolean Algebra Identity?

> Snippet 1 (Question 28, Option F): ⊕ Snippet 2 Question 28, Option H): ∗ + ̅∗

- **A)** Law of Absorption **B)** Exclusive NOR Law **C)** DeMorgan's Law **D)** Double Negative Law **E)** Disappearing Opposite

### **Question 31**

What is output by the code to the right?

- **A)** [3, 6, 9] [2, 5, 8] [1, 4, 7]
- **B)** [3, 4, 1] [2, 5, 2] [1, 6, 3]
- **C)** 3 6 9 2 5 8 1 4 7
- **D)** 7 4 1 8 5 2 9 6 3
- **E)** 9 2 7 4 5 8 3 6 1
- **F)** There is no output due to a runtime error.

## int[][] m = new int[][] { {1, 2, 3}, {4, 5, 6}, {7, 8, 9} }; int n = m.length; for (int i = 0; i < n / 2; i++) { for (int j = i; j < n - i - 1; j++) { int temp = m[i][j]; m[i][j] = m[j][n - 1 - i]; m[j][n - 1 - i] = m[n - 1 - i][n - 1 - j]; m[n - 1 - i][n - 1 - j] = m[n - 1 - j][i]; m[n - 1 - j][i] = temp; } } for(int i = 0; i < n; i++) { out.println(Arrays.toString(m[i]) .replaceAll("[\\[\\],]", "")); }

### **Question 32**

What is the output by the line marked //q32 in the client code to the right?

### **Question 33**

What is the output by the line marked //q33 in the client code to the right?

- **A)** 15 **B)** 20 **C)** 21 **D)** 35 **E)** 56

### **Question 34**

Which of the following calls to the function rec would be equivalent to the output by the line marked //q34 in the client code to the right?

- **A)** rec(6,11) **B)** rec(11,6)
- **C)** rec(7,12) **D)** rec(12,7)
- **E)** None of the above.

**A)** 0 **B)** 1 **C)** 2 **D)** 4 **E)** 5 public static int rec(int r, int c) { if(c > r) { return 0; } else if(c <= 1 || r <= 1) { return 1; } return rec(r-1, c) + rec(r-1, c-1); } ////////////// client code ////////////// out.println(rec(3,2)); //q32 out.println(rec(8,5)); //q33 out.println(rec(10,6) + rec(10,5)); //q34

The function rec(r,c) from the previous 3 questions is an implementation of which well-known recursive formula?

### **A)** Fibonacci Sequence **B)** Pascal's Triangle **C)** Fast Exponentiation **D)** Factorial of a Number **E)** Triangular Numbers

#### **Question 36**

Which of the following could replace **<1\*>** in the code to the right and have the code compile without error?

- **A)** public **B)** protected **C)** private
- **D)** Replace all instances of **<1\*>** with nothing (delete it and leave the space blank).
- **E)** More than one of the above.

### **Question 37**

Which of the following could replace **<2\*>** in the code to the right so that the code execution only takes the respective branch if lock is an example of the BakeryLock or FilterLock classes, respectively?

- **A)** extends **B)** implements
- **C)** instanceof **D)** super
- **E)** More than one of the above.

BakeryLock lock(10)

### **Question 38**

Which of the following could replace **<3\*>** in the code to the right so that when the client code is executed, the following is printed:

```
func1() 
BakeryLock unlock(10) 
FilterLock cs.lock() 
func2() 
FilterLock cs.unlock() 
A) ((FilterLock) lock).func2(); 
B) FilterLock.class.cast(lock).func2(); 
C) try { 
  lock.getClass().getMethod("func2"). 
 invoke(lock); 
 } catch (Exception e) { 
  e.printStackTrace(); 
 }
```

- **D)** Options A and C.
- **E)** All of the above.
- **F)** None of the above.

```
interface Lock { 
 public void lock(); 
 public void unlock(); 
} 
class BakeryLock implements Lock { 
 private int n; 
 public BakeryLock(int n) { 
 this.n = n; 
 } 
   <1*> void lock() { 
 out.printf( 
 "BakeryLock lock(%d)\n", n); 
 } 
   <1*> void unlock() { 
 out.printf( 
 "BakeryLock unlock(%d)\n", n); 
 } 
 public void func1() { 
 out.println("func1()"); 
 } 
} 
class FilterLock implements Lock { 
 private String name; 
 public FilterLock(String s) { 
 this.name = s; 
 } 
   <1*> void lock() { 
 out.printf( 
 "FilterLock %s.lock()\n", name); 
 } 
   <1*> void unlock() { 
 out.printf( 
 "FilterLock %s.unlock()\n", name); 
 } 
 public void func2() { 
 out.println("func2()"); 
 } 
} 
//////////////// client code //////////////// 
Lock[] locks = new Lock[] { 
 new BakeryLock(10), new FilterLock("cs") 
}; 
for(Lock lock : locks) { 
 lock.lock(); 
 if(lock <2*> BakeryLock) { 
 ((BakeryLock) lock).func1(); 
 } else if(lock <2*> FilterLock) { 
 <3*> 
 } 
 lock.unlock(); 
}
```

Consider that you have an array of integers of size named arr that you wish to convert into a PriorityQueue<Integer> named pq by calling pq.offer(arr[i]) for each i in the range 0 through − 1. What is the tightest asymptotic upper bound on this set of operations? Express your answer in Big- notation in terms of .

#### **Question 40**

Convert the prefix expression to the right into the equivalent fully parenthesized infix expression.

\* + A - B C / D - E + F G

![](_page_7_Picture_0.jpeg)

# **UIL COMPUTER SCIENCE – 2024-2025 DISTRICT**

**Questions** (+6 points for each correct answer, -2 points for each incorrect answer)

1) E 11) C 21) A 31) C

2) C 12) B 22) D 32) C

3) C 13) D 23) C 33) D

4) D 14) A 24) C 34) B

5) A 15) C 25) A 35) B

6) D 16) B 26) C 36) A

7) B 17) E 27) D 37) C

8) B 18) A 28) J 38) E

9) D 19) D 29) C \*

39) ( lg )

10) A 20) D 30) B \*

40) See Explanation

**Note:** Correct responses are based on **Java SE Development Kit 22 (JDK 22)** from Sun Microsystems, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

*<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.*

### Explanations:

| 1.  | E | All of the values are equivalent                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2.  | C | Simple order of operations problem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 3.  | C | printf is formatting output, "%3S", greater than 3 columns so 3 is ignored, S means<br>capitalized.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 4.  | D | Simple substring problem, substring is inclusive of first value, exclusive of last (if present)                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 5.  | A | Simple boolean solving                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 6.  | D | Math.max(double x, double y) is called, which returns the larger value, but cast to a<br>double since it is the integer value.                                                                                                                                                                                                                                                                                                                                                                                            |
| 7.  | B | Simple tracing problem, trace out each value during each iteration of the loop.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 8.  | B | Simple order of operations problem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 9.  | D | else will not happen if ANY if before it is triggered. In a sequence of if-else if-else if<br>else, only one statement will be activated, no matter how many there are.                                                                                                                                                                                                                                                                                                                                                   |
| 10. | A | Array problem, 25 times you move through the array values, but it cycles every 6.<br>25 % 6 = 1, so just do the operation once.                                                                                                                                                                                                                                                                                                                                                                                           |
| 11. | C | Scanner class is in the java.util package                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 12. | B | Just trace the loop, you could also estimate and knock out the wrong answers                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 13. | D | Simple order of precedence                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 14. | A | double = 64 bits = 4 bytes (8 bits each)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 15. | C | Add to the end, ArrayLists are 0-indexed. Trace it out. Removing 1 will remove the object at<br>index 1, not the Object 1 itself.                                                                                                                                                                                                                                                                                                                                                                                         |
| 16. | B | The strings "instanceof" and "int" first differ on the characters 's' and 't', respectively. The<br>characters 's' and 't' have ASCII values of 115 and 116, respectively. Since we are comparing<br>the first string to the second string, and s comes before t, and they differ by a single ASCII value,<br>the output of the compareTo statement is -1. The boolean expression resolves to false, and<br>the ternary operator selects "Not Greater" as the return value.                                               |
| 17. | E | The range of the statement is [21,57), and the return type of Math.random() is double.<br>Both options A and C are contained in this range and are represented as a double. Option B,<br>despite being within the valid range, is represented as an int, and, therefore, is not a possible<br>value of the expression since it must be a double.                                                                                                                                                                          |
| 18. | A | As previously stated, the range is [21, 57).                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 19. | D | The graph is directed, which can be noted by the arrow tips, weighted, which can be noted by<br>the weights on the edges, and acyclic, since the graph contains no cycles (flows from node  to<br>node  ).                                                                                                                                                                                                                                                                                                               |
| 20. | D | All three algorithms are shortest path algorithms that can be used to find the shortest path<br>between a specific pair of nodes. Both Dijkstra's and Bellman-Ford find the shortest path from a<br>single node to all other nodes, while Floyd-Warshall finds the shortest path between all pairs of<br>nodes (hence, it can be used to find a specific pair, even if it provides more info than what is<br>needed).<br>Dijkstra's algorithm has a stipulation that the graph must not contain any negative edges. Since |
|     |   | the graph contains a single negative edge, Dijkstra's algorithm is not guaranteed to work<br>(depending on the order that vertices of equivalent potential weight are processed, the query of<br>node  to node  may fail in this case as it may explore vertex  before exploring vertex ). The<br>other two algorithms have a stipulation that the graph must not contain a negative edge cycle<br>reachable from the source. Since the graph is acyclic, this is not an issue.                                          |
| 21. | A | There are two shortest paths from  to   in this graph. Those are  " # \$ % &  , and<br>% &  , both have weight of 18.                                                                                                                                                                                                                                                                                                                                                                                                   |

| D | The following is a copy of the truth table for the expression in question 17:                                                                                                                    |
|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | $A \mid B \mid C \mid \overline{A \oplus \overline{C * B}} + \overline{A \oplus \overline{C} \oplus B}$                                                                                          |
|   | $\begin{array}{c ccccccccccccccccccccccccccccccccccc$                                                                                                                                            |
|   | F F T                                                                                                                                                                                            |
|   | F T F T                                                                                                                                                                                          |
|   | $F \mid T \mid T \mid T$                                                                                                                                                                         |
|   | <u> </u>                                                                                                                                                                                         |
|   | T F T T T T                                                                                                                                                                                      |
|   | T   T   F   T   T   T   T   T   T   T                                                                                                                                                            |
|   |                                                                                                                                                                                                  |
| С | You can trace this, but this particular code will set $y$ to the value of $x$ and $x$ to $y$ .                                                                                                   |
| С | super call to constructor has to be the first line, then y must be set to n. Only C obeys both of                                                                                                |
|   | these rules.                                                                                                                                                                                     |
| Α | get method will get the $y$ variable from class A, and the $y$ in class A attached to B will be twice                                                                                            |
|   | the value given. So, the first get call will print 3, and the second will print 8 because it is called                                                                                           |
|   | from class B.                                                                                                                                                                                    |
| C | B class has no toString method, so it will print the memory address, which cannot be                                                                                                             |
|   | determined until runtime.                                                                                                                                                                        |
| ט | Compile error because the A class has no add method, and c is defined in the eyes of the                                                                                                         |
| 1 | compiler as an instance of A, even though in reality it is an instance of B.  Note that the symbol after the variable B is known as a "buffer" and simply passes on the value                    |
| J | of the input, unaltered. Options A, C, E, and G are equivalent to one another (C is derived by                                                                                                   |
|   | simplifying A, E is derived from simplifying C, and so on). Likewise, options B, D, F, and H are                                                                                                 |
|   | equivalent to one another. The only difference between Options A and B is that Option B                                                                                                          |
|   | incorrectly labels $B$ as $\overline{B}$ . Because of this, option J is the correct answer choice.                                                                                               |
| С | This is an example of DeMorgan's Law which states that $\overline{A+B}=\bar{A}*\bar{B}$ .                                                                                                        |
| В | This is an example of the Exclusive NOR Law which states that $\overline{A \oplus B} = A * B + \overline{A} * \overline{B}$                                                                      |
| С | Note that the set of nested for loops effectively rotates the square matrix 90 degrees counter-                                                                                                  |
|   | clockwise.                                                                                                                                                                                       |
| C | See the following recursive table:                                                                                                                                                               |
|   | $ \begin{array}{c cc} \hline \text{Call} & \text{Expression} & \text{Value} \\ \hline \text{Rec}(3,2) & \text{Rec}(2,2) + \text{rec}(2,1) & 1+1=2 \end{array} $                                  |
|   |                                                                                                                                                                                                  |
|   | Rec(2,2) Rec(1,2) + rec(1,1) $0 + 1 = 1$<br>Rec(1,2) Base Case #1 $0$                                                                                                                            |
|   | Rec(1,2) Base Case #1 0  Rec(1,1) Base Case #2 1                                                                                                                                                 |
|   | Rec(2,1) Base Case #2 1                                                                                                                                                                          |
|   |                                                                                                                                                                                                  |
| D | You could either create another recursive table for this, or, you could recognize this recursive                                                                                                 |
|   | function as being equivalent to the number appearing on the $r^{\rm th}$ row and $c^{\rm th}$ column of Pascal's                                                                                 |
|   | Triangle, and quickly determine the value.                                                                                                                                                       |
| В | Reverse engineer the values of $r$ and $c$ by looking at the last return statement in the $rec(r,c)$                                                                                             |
| - | function definition.                                                                                                                                                                             |
| R | As previously stated, this is Pascal's Triangle, where the value appearing on the $r^{\rm th}$ row and $c^{\rm th}$ column of the triangle is equivalent to the sum of the two numbers above it. |
| Δ | All options are valid ways to write a method; however, since the Lock interface specifies that                                                                                                   |
|   | the visibility of the two methods lock() and unlock() must be public, so too must be the                                                                                                         |
|   | implementations of those methods in the sub-classes.                                                                                                                                             |
| I |                                                                                                                                                                                                  |
| С | The key word instanceof tests to see if a reference variable is an instance of a particular                                                                                                      |
| С | The key word instanceof tests to see if a reference variable is an instance of a particular class, or is a subclass of some class or interface. Options A and B are used to show inheritance     |
|   | C C D J C B C C C B C A A A A A A A A A A A A A                                                                                                                                                  |

| 38. | E                                                                                                                                                                                                                                                              | Option A is the equivalent to how func1() was called for BakeryLock implementations of<br>Lock. Option B utilizes the cast method of a Class object, which can be statically retrieved<br>from the class literal of that object's type, which is determined at compile time. Option C utilizes<br>an inherited method from the Object class which determines the class of an object at runtime,<br>then calls the getMethod() method from the Class object, and invokes that method on the<br>passed lock object. Since option C has the class and method calls determined at runtime, it<br>must be surrounded in a try-catch block. All options are valid ways to call the method func2(). |  |  |  |
|-----|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
| 39. | ( lg )                                                                                                                                                                                                                                                         | Each call to offer() for a PriorityQueue (Java's implementation of a min-heap) takes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  |  |  |
|     | or                                                                                                                                                                                                                                                             | (lg ) time. This is performed  times, once for each of the  elements of arr. This yields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |  |  |
|     | ( log,<br>)                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |
|     | or                                                                                                                                                                                                                                                             | ⋅ (lg ) = ( lg )                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |  |  |
| 40. | ( log )                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |
|     | ( ( A + ( B – C ) ) * ( D / ( E - ( F + G ) ) ) )                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |
|     | To convert between prefix and infix, perform the following:                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |
|     | 1.<br>Read symbols from right to left                                                                                                                                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |
|     | 2.<br>If the symbol read is an operand, push it onto a stack.                                                                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |
|     | 3.<br>If the symbol read is an operator, pop the two values from the stack.                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |
|     | Create a string by concatenating the two operands and the operator, where string = (2nd top-most<br>4.<br>value <op> 1st top-most value)</op>                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |
|     | 5.                                                                                                                                                                                                                                                             | Repeat until entire string is read and stack only contains a single value. This is your fully parenthesized<br>infix-equation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |  |  |
|     | Note that the order in which variables occur, even for operators that exhibit the commutative and associative                                                                                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |
|     | properties, is important when translating between the two forms since the rule is generalized for all operators,<br>even those that don't exhibit these properties. Because of this, no other otherwise equivalent forms of this<br>equation will be accepted. |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |  |  |