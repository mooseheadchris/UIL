# **UIL COMPUTER SCIENCE WRITTEN TEST – 2025 REGION**

**Note:** Correct responses are based on **Java SE Development Kit 22 (JDK 22)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

| Question 1                                                            |                                                                                 |  |  |
|-----------------------------------------------------------------------|---------------------------------------------------------------------------------|--|--|
| Which of the following is equivalent to the expression 394811 / 2224? |                                                                                 |  |  |
| A) 2437<br>B) 728<br>C) A212                                          | D) 13304<br>E) None are equivalent.                                             |  |  |
| Question 2                                                            |                                                                                 |  |  |
| What is output by the code to the right?                              |                                                                                 |  |  |
| A) -2<br>B) 2<br>C) 0<br>D) -1                                        | out.println(212 / 43 - 394 / 63);                                               |  |  |
| E) There is no output due to a compile error.                         |                                                                                 |  |  |
| Question 3                                                            |                                                                                 |  |  |
| What is output by the code to the right?                              |                                                                                 |  |  |
| A) true<br>B) false<br>C) TRUE<br>D) FALSE                            | out.printf("%B",-17);                                                           |  |  |
| E) There is no output due to a runtime error.                         |                                                                                 |  |  |
| Question 4                                                            | String s = "InfinityStone";                                                     |  |  |
| What is output by the code to the right?                              | s.substring(1, s.length() - 2);                                                 |  |  |
| A) nityStoit<br>B) InfinityStone207                                   | s += s.charAt(2) + s.charAt(5);                                                 |  |  |
| C) nitySto221<br>D) InfinityStonefi                                   | s.substring(3);                                                                 |  |  |
| E) There is no output due to a runtime error.                         | out.println(s);                                                                 |  |  |
| Question 5                                                            | boolean a = true ^ true;<br>a = a & !a    a ^ !a && a   !a;                     |  |  |
| What is output by the code to the right?                              |                                                                                 |  |  |
| A) true<br>B) false                                                   | out.println(a);                                                                 |  |  |
| Question 6                                                            |                                                                                 |  |  |
| What is output by the code to the right?                              | double g = 5.55;<br>int i = Math.round(g);                                      |  |  |
| A) 5<br>B) 6.0<br>C) 6                                                |                                                                                 |  |  |
| D) There is no output due to a compile error.                         | out.println(g);                                                                 |  |  |
| E) There is no output due to a runtime error.                         |                                                                                 |  |  |
| Question 7                                                            | int i = 9;<br>if(i < 10    i++ > 10)<br>out.print(1);<br>if(i < 10 && i++ > 10) |  |  |
| What is output by the code to the right?                              |                                                                                 |  |  |
| A) 1211                                                               |                                                                                 |  |  |
| B) 1311                                                               | out.print(2);                                                                   |  |  |
| C) 310                                                                | else                                                                            |  |  |
| D) 1310                                                               | out.print(3);                                                                   |  |  |
| E) 210                                                                | out.print(i);                                                                   |  |  |
| Question 8                                                            | int i = 78 % 13 ^ 28;                                                           |  |  |
| What is output by the code to the right?                              | i += 212 - 39   51 / 2;                                                         |  |  |
| A) 727<br>B) 81<br>C) 130<br>D) 87                                    | i = 134 & i * 5 + 77;                                                           |  |  |
| E) There is no output due to a compile error.                         | out.println(i);                                                                 |  |  |

#### **Question 9** How many \*'s are output by the code to the right? **A)** 5 **B)** 6 **C)** 7 **D)** 8 **E)** There is no output due to an infinite loop. for(int y=9; y < 123; y=y \* 2 - 7) out.print("\*"); **Question 10** What is output by the code to the right? **A)** [1, 118, 634, 212] **B)** [33, 124, 74, 10, 3] **C)** [0, 118, 634, 212] **D)** [34, 122, 74, 10, 3] **E)** There is no output due to a runtime error. int[][] mat = new int[][] { {23, 5, -9, 212}, {34, 89, 74, 10, 3}, {341, 895, 284} }; for(int i = 0; i < 3; i++) { mat[i][i] += mat[i][0]--; mat[0][i] -= mat[i][i]++; mat[0][i] \*= -1; } out.println( Arrays.toString(mat[0])); **Question 11** What is output by the code to the right? **A)** Koie **B)** SB Th3 **C)** Koie 8293m **D)** Th3 **E)** There is no output due to a runtime error. String k = "123\nSB Th3\tKoie 8293m"; Scanner sc = new Scanner(k); sc.nextLine(); sc.next(); sc.next(); out.println(sc.next()); **Question 12** What is output by the code to the right? **A)** 245 **B)** 185 **C)** 266 **D)** 336 **E)** There is no output due to an infinite loop. int sum = 0; for(int y = 5; y < 16; y++) for(int x = y; x >= 10; x--) sum += x; out.println(sum); **Question 13** What is the order of precedence for the operators to the right? **A)** II, I, III, IV **B)** II, III, IV, I **C)** III, II, I, IV **D)** III, II, IV, I **E)** II, III, I, IV I. | (bitwise) II. ++(pre) III. \* IV. || (logical) **Question 14** What is output by the code to the right? **A)** 80 int[] sizes = new int[] { Double.SIZE, Float.SIZE, Long.SIZE, Integer.SIZE,

- **B)** 96
- **C)** 64
- **D)** 128
- **E)** There is no output due to a runtime error.

```
 Short.SIZE, Byte.SIZE 
}; 
Arrays.sort(sizes); 
out.print(sizes[3]+sizes[4]);
```

What is output by the line marked //q15 in the code to the right?

- **A)** [GHIJK, LMNOP]
- **B)** [GHIJK, LMNOP, WXYZ]
- **C)** [ABC, DEF, QRS, TUV]
- **D)** [ABC, DEF, QRS, TUV, WXYZ]
- **E)** There is no output due to an infinite loop.

## **Question 16**

What is output by the line marked //q16 in the code to the right?

- **A)** HJMOXZ **B)** ACDFQSTV
- **C)** BERU **D)** GIKLNPWY
- **E)** There is no output due to a compile error.

#### **Question 17**

Which of the following lines in the code to the right will be the first to create a compile-time error?

- **A)** //line 01 **B)** //line 02
- **C)** //line 03 **D)** //line 04
- **E)** //line 05 **F)** //line 06
- **G)** //line 07 **H)** //line 08
- **I)** //line 09 **J)** //line 10
- **K)** The code will compile without error but will create a runtime error.
- **L)** The code will both compile and run without error.

```
ArrayList<String> a; 
a = new ArrayList<String>(); 
a.add("ABC");a.add("DEF"); 
a.add("GHIJK");a.add("LMNOP"); 
a.add("QRS");a.add("TUV"); 
a.add("WXYZ"); 
a.removeIf(s -> s.length() < 4); 
out.println(a); //q15 
a.forEach(s ->{ 
 for (int i = 0; i < s.length(); i += 2) 
 out.print(s.charAt(i)); 
}); //q16
```

```
public void method1( 
 int a, // line 01 
 final int b // line 02 
) { 
 int c = a + b; // line 03 
 final int d = a * b; // line 04 
 out.printf("%d %d %d %d\n", 
 a, b, c, d); // line 05 
 a = a + 1; // line 06 
 b = b + 1; // line 07 
 c = c + 1; // line 08 
 d = d + 1; // line 09 
 out.printf("%d %d %d %d\n", 
 a, b, c, d); // line 10
```

### **Question 18**

Which of the following lines in the code to the right will be the first to create a compile-time error?

- **A)** //line 01 **B)** //line 02

- **C)** //line 03 **D)** //line 04
- **E)** //line 05 **F)** //line 06
- **G)** //line 07 **H)** //line 08
- **I)** //line 09 **J)** //line 10

- **K)** //line 11 **L)** //line 12
- **M)** //line 13
- **N)** The code will compile without error but will create a runtime error.
- **O)** The code will both compile and run without error.

```
} 
public void method2( 
 ArrayList<Integer> a, // line 01 
 final ArrayList<Integer> b // line 02 
) { 
 ArrayList<Integer> c = 
 new ArrayList<>(a); // line 03 
 final ArrayList<Integer> d = 
 new ArrayList<>(a); // line 04 
 out.printf("%d %d %d %d\n", 
 a.size(), b.size(), 
 c.size(), d.size()); // line 05 
 a.add(1); // line 06 
 b.add(2); // line 07 
 c.add(3); // line 08 
 d.add(4); // line 09 
 a = new ArrayList<>(a); // line 10 
 b = new ArrayList<>(b); // line 11 
 c = new ArrayList<>(c); // line 12 
 d = new ArrayList<>(d); // line 13 
}
```

Which of the following concepts is demonstrated by the add methods in the classes to the right?

- **A)** Overriding
- **B)** Overloading
- **C)** Abstraction
- **D)** A and B
- **E)** All of the above.

# **Question 20**

Which of the following concepts is demonstrated by the toString method in the classes to the right?

- **A)** Overriding
- **B)** Overloading
- **C)** Abstraction
- **D)** A and B
- **E)** All of the above.

# **Question 21**

What is output by the line marked //q21 in the code to the right?

- **A)** 7
- **B)** 10
- **C)** 13
- **D)** There is no output due to a compile error.
- **E)** There is no output due to a runtime error.

#### **Question 22**

What is output by the line marked //q22 in the code to the right?

- **A)** 7
- **B)** 12
- **C)** 24
- **D)** There is no output due to a compile error.
- **E)** There is no output due to a runtime error.

# **Question 23**

What is output by the line marked //q23 in the client code to the right?

- **A)** AB
- **B)** BA
- **C)** Output cannot be determined until runtime.
- **D)** There is no output due to a compile error.
- **E)** There is no output due to a runtime error.

```
class A{ 
 private int y; 
 String s; 
 public A(String str) { 
 s = str; 
 y = 7; 
 } 
 public int get() { 
 return y; 
 } 
 public void add() { 
 y += 3; 
 } 
 public String toString() { 
 return s; 
 } 
} 
class B extends A{ 
 int y; 
 public B(String str, int i) { 
 super(str); 
 y = i; 
 } 
 public void add(int i) { 
 y += i; 
 } 
} 
///////////client code/////////// 
A a = new A("A"); 
B b = new B("B", 12); 
a.add(); 
out.println(a.get()); //q21 
b.add(12); 
out.println(b.get()); //q22 
out.println(a+b); //q23
```

Which of the following could replace <1\*> in the code to the right and have the code compile without error (including the client code)?

- A) public
- B) final
- C) protected
- D) static
- E) Replace all instances of <1\*> with nothing (delete it and leave the space blank).

# Question 25

Assuming that <1\*> has been filled in properly in the code to the right, what is output by the client code to the right?

- A) Hello there!
  May the force be with you.
- B) May the force be with you. Hello there!
- C) Hello there! Hello there!
- D) May the force be with you.
  May the force be with you.
- **E)** The output cannot be determined until runtime.

# Question 26

Which of the following is equivalent to the logic circuit diagram to the right?

- A)  $\overline{A} + \overline{B} \oplus \overline{C * D}$
- B)  $\bar{A} + \bar{B} \oplus \overline{C + D}$
- c)  $\overline{A} * \overline{B} \oplus \overline{C + D}$
- **D)** More than one of the above.
- E) None of the above.

# Question 27

How many permutations of true and false assignments to A, B, C, and D output true in the circuit diagram to the right?

- **A)** 2
- **B)** 4
- **C)** 7
- **D)** 10
- **E)** 13

# Question 28

Suppose we replaced input D with a second instance/pin/line of input C. How many permutations of true and false assignments to A, B, and C output true in the modified circuit diagram proposed?

- **A)** 2
- **B)** 4
- **C)** 5
- **D)** 7
- **E)** 8

```
class Jedi {
   public static void speak() {
      out.println("May the force
```

![](_page_4_Picture_36.jpeg)

What is the correct compile-time error with the code to the right as well as the appropriate way to resolve the error?

- **A)** They keyword final is not a valid modifier to a class definition. To resolve, remove all final modifiers to the class definition.
- **B)** Abstract classes can only define abstract methods and cannot define abstract fields. To resolve, remove the declaration of the name variable and the constructor from the abstract class and add the same variable definition to the three sub-classes. Then, instead of calling the parent constructor using super, instead assign the (now) local field name to the value previously passed using super.
- **C)** Class definitions modified with the keyword final prevents other classes from inheriting from it. To resolve, remove the class definition of EnemyJett, as the client code does not rely on this class existing. Alternatively, if we needed the EnemyJett class to exist, have the EnemyJett class instead inherit from the Agent abstract class instead of the Jett class.
- **D)** Classes that are declared as abstract, if inherited, need to use the implements keyword instead of the extends keyword. To resolve, replace all instances of extends with implements.
- **E)** Abstract classes can never appear as the datatype of a variable declaration – only concrete classes or primitive datatypes can. To resolve, replace the datatype of the tejo variable with Tejo, and replace the datatype of the jett variable with the Jett object.

## **Question 30**

Assuming that the correct compile-time error identified above has been resolved using its correct resolution method, what is output by the client code to the right?

```
A) Tejo: This is how it ends! 
 Jett: Watch this! 
B) Tejo: This is how it ends! 
 Jett: Get out of my way! 
C) Tejo: This is how it ends! 
 Jett: Watch this! 
 Jett: Get out of my way!
```

- **D)** There is no output, despite the program compiling and running without error.
- **E)** The output cannot be determined until runtime.

```
abstract class Agent { 
 public final String name; 
 public Agent(String name) { 
 this.name = name; 
 } 
 public abstract void ult(); 
} 
final class Tejo extends Agent { 
 public Tejo() { 
 super("Tejo"); 
 } 
 public void ult() { 
 out.printf("%s: This is 
 how it ends!\n", 
 name); 
 } 
} 
final class Jett extends Agent { 
 public Jett() { 
 super("Jett"); 
 } 
 public void ult() { 
 out.printf("%s: Watch 
 this!\n", name); 
 } 
} 
class EnemyJett extends Jett { 
 public EnemyJett() { 
 super("Jett"); 
 } 
 public void ult() { 
 out.printf("%s: Get out of 
 my way!\n", name); 
 } 
} 
////////// Client Code ////////// 
Agent tejo = new Tejo(); 
Agent jett = new Jett(); 
tejo.ult(); 
jett.ult();
```

What can replace **<1\*>** in the code to the right so that any object which implements the Comparable interface can be stored within the new object DataStructure?

- **A)** T
- **B)** Comparable
- **C)** ? extends Comparable
- **D)** T extends Comparable<T>
- **E)** None of the above

### **Question 32**

Assuming that **<1\*>** has been filled in properly, what can replace **<2\*>** in the code to the right so that any object which implements the Comparable interface can be stored within the new object DataStructure?

- **A)** T
- **B)** Comparable
- **C)** ? extends Comparable
- **D)** T extends Comparable<T>
- **E)** None of the above

#### **Question 33**

What is the tightest upper bound on the time complexity of the extract() method in the code to the right?

- **A)**
- **B)** 
   log
- **C)** √
- **D)** 1
- **E)** log

# **Question 34**

The class DataStructure in the code to the right is an implementation of what well-known data structure?

- **A)** Dequeue
- **B)** AVL Tree
- **C)** Binary Search Tree
- **D)** Min-Heap
- **E)** Max-Heap

```
class DataStructure<<1*>> { 
 private ArrayList<<2*>> arr; 
 public DataStructure(int n) { 
 arr = new ArrayList<<2*>>(); 
 } 
 private void swap(int i, int j) { 
 <2*> temp = arr.get(i); 
 arr.set(i, arr.get(j)); 
 arr.set(j, temp); 
 } 
 public void insert(<2*> val) { 
 int i = arr.size(); 
 int parent = (i - 1) / 2; 
 arr.add(val); 
 while (i > 0 && arr.get(i).compareTo( 
 arr.get(parent)) < 0) 
 { 
 swap(i, parent); 
 i = parent; 
 parent = (i - 1) / 2; 
 } 
 } 
 public <2*> extract() { 
 if (arr.isEmpty()) { 
 return null; 
 } 
 <2*> min = arr.get(0); 
 <2*> last = arr.remove(arr.size() - 1); 
 if (!arr.isEmpty()) { 
 arr.set(0, last); 
 int i = 0; 
 while (true) { 
 int l = (2 * i) + 1; 
 int r = (2 * i) + 2; 
 int minIndex = i; 
 if (l < arr.size() && arr.get(l) 
 .compareTo(arr.get(minIndex)) 
 < 0) 
 { 
 minIndex = l; 
 } 
 if (r < arr.size() && arr.get(r) 
 .compareTo(arr.get(minIndex)) 
 < 0) 
 { 
 minIndex = r; 
 } 
 if (minIndex == i) { 
 break; 
 } 
 swap(i, minIndex); 
 i = minIndex; 
 } 
 } 
 return min; 
 }
```

}

Given a sorted array of = elements, **in terms of** , which of the following is the tightest upper bound for the fastest way to find the index of a specific element **among the elements**?

A) 
$$\mathcal{O}(m) = \boxed{\mathcal{O}(n^2)}$$

**B)** 
$$\mathcal{O}(m) = \mathcal{O}(\sqrt{n^2}) = \boxed{\mathcal{O}(n)}$$

C) 
$$\mathcal{O}(m) = \mathcal{O}((\log n^2)^2) = \mathcal{O}((2\log n)^2) = \mathcal{O}(4\log^2 n) = \boxed{\mathcal{O}(\log^2 n)}$$

**D)** 
$$\mathcal{O}(m) = \mathcal{O}(\log(n^2)) = \mathcal{O}(2\log n) = \boxed{\mathcal{O}(\log n)}$$

$$\mathbf{E)} \ \mathcal{O}(m) = \boxed{\mathcal{O}(1)}$$

# **Question 36**

Given a sorted singly-linked list of = elements, **in terms of** , which of the following is the tightest upper bound for the fastest way to find the index of a specific element **among the elements**?

A) 
$$\mathcal{O}(m) = \boxed{\mathcal{O}(n^2)}$$

B) 
$$\mathcal{O}(m) = \mathcal{O}(\sqrt{n^2}) = \boxed{\mathcal{O}(n)}$$

C) 
$$\mathcal{O}(m) = \mathcal{O}((\log n^2)^2) = \mathcal{O}((2\log n)^2) = \mathcal{O}(4\log^2 n) = \boxed{\mathcal{O}(\log^2 n)}$$

**D)** 
$$\mathcal{O}(m) = \mathcal{O}(\log(n^2)) = \mathcal{O}(2\log n) = \boxed{\mathcal{O}(\log n)}$$

**E)** 
$$\mathcal{O}(m) = \boxed{\mathcal{O}(1)}$$

# **Question 37**

The code to the right demonstrates which of the following design patterns?

- **A)** Singleton
- **B)** Object Pool
- **C)** Builder
- **D)** Prototype
- **E)** Factory Method.

```
class Something { 
 private static Something something; 
 private Something() {} 
 public Something createSomething() { 
 if(something == null) { 
 return new Something(); 
 } 
 return something; 
 } 
}
```

## **Question 38**

Which of the following sorting algorithms **does not** have its worst case time complexity equal to  log ?

- **A)** Heap Sort **B)** Merge Sort **C)** Quick Sort **D)** Option B and C. **E)** None of the above.

#### **Question 39**

Suppose that you have a complete, directed, weighted graph with no negative edges and you use Dijkstra's algorithm to solve the single-source shortest path problem. In terms of , the number of vertices in the graph, and , the number of edges in the graph, what is the tightest asymptotic upper bound for solving this problem? Express your answer in Big- notation.

| Question 40                                                    | The stack is initially empty. |
|----------------------------------------------------------------|-------------------------------|
| What is the sum of all elements that remain in the stack after | Push 18                       |
| the process denoted to the right completes?                    | Push 12                       |
|                                                                | Push 25                       |
|                                                                | Push 19                       |
|                                                                | Pop                           |
|                                                                | Pop                           |
|                                                                | Push 17                       |
|                                                                | Push 32                       |
|                                                                | Push 36                       |
|                                                                | Push 24                       |
|                                                                | Peek                          |
|                                                                | Peek                          |
|                                                                | Pop                           |
|                                                                | Push 56                       |
|                                                                | Push 17                       |
|                                                                | Pop                           |
|                                                                | Process Complete              |

![](_page_9_Picture_0.jpeg)

# **UIL COMPUTER SCIENCE – 2024-2025 REGION**

**Questions** (+6 points for each correct answer, -2 points for each incorrect answer)

1) C 11) A 21) B 31) D

2) A 12) A 22) A 32) A

3) C 13) E 23) D 33) E

4) B 14) B 24) D 34) D

5) A 15) B 25) A 35) D

6) D 16) D 26) C 36) A

7) D 17) G 27) D 37) A

8) C 18) K 28) B 38) C

9) B 19) B 29) C \*

39) or 

10) C 20) A 30) A \*

40) 171

**Note:** Correct responses are based on **Java SE Development Kit 22 (JDK 22)** from Sun Microsystems, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

*<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.*

# Explanations:

| 1.  | C | Simple base conversion (Convert to base 10 then simple division, convert answers as well).                                                                                                                                                                                                                                                                                                                                                                          |
|-----|---|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2.  | A | Simple expression solving (PEMDAS)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 3.  | C | %B will output FALSE if the parameter is null or the literal false, otherwise it will output<br>TRUE.                                                                                                                                                                                                                                                                                                                                                               |
| 4.  | B | Strings are immutable, so both substring calls do not affect the original string, and the<br>characters will be converted to ints and added together before they are appended to the end<br>of the string.                                                                                                                                                                                                                                                          |
| 5.  | A | Simple boolean expression.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 6.  | D | Math.round(double) will return a long, so there is a compile error trying to store that<br>value in an int.                                                                                                                                                                                                                                                                                                                                                         |
| 7.  | D | Simple if<br>else solution, but    and && short circuit if the first expression guarantees the<br>entire expression is false, and i++ will return the original value then increment it afterwards.                                                                                                                                                                                                                                                                  |
| 8.  | C | Simple expression solving, order of operations will play a part                                                                                                                                                                                                                                                                                                                                                                                                     |
| 9.  | B | Simple output loop tracing.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 10. | C | Simple matrix and loop tracing.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 11. | A | Scanner tracing, nextLine will get all data up to a \n, next will grab all characters up to the<br>next whitespace character.                                                                                                                                                                                                                                                                                                                                       |
| 12. | A | Simple loop tracing.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 13. | E | Java order of precedence.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 14. | B | Need to know that arrays are 0-indexed, and all of the sizes of the data types listed.                                                                                                                                                                                                                                                                                                                                                                              |
| 15. | B | The removeIf does exactly what it sounds like, and the list will contain all of the elements with<br>length greater than or equal to 4.                                                                                                                                                                                                                                                                                                                             |
| 16. | D | The forEach method will print out every other item in the list, starting at position 0.                                                                                                                                                                                                                                                                                                                                                                             |
| 17. | G | When a variable storing a primitive datatype is assigned the keyword final, its contents can be<br>read; however, its value cannot be changed after its initial declaration. Any parameter of a<br>method can be declared as final and, if the datatype is also primitive, then the same rule<br>applies. The first time that the code attempts to change the value of a final primitive is the line<br>marked //line 07 and will create a compile-time error.      |
| 18. | K | When a variable storing an object is assigned the keyword final, the only action that cannot<br>be performed on that variable is re-assigning what object the variable points to. Thus,<br>attempting to modify the underlying structure is actually allowed. However, the first time that<br>the code attempts to change what object a final variable is pointing to is the line marked<br>//line 11 and will create a compile-time error.                         |
| 19. | B | Overloading is correct, because the add() method is inherited from class A into class B, so<br>there are two add methods with different parameter combinations. See this definition of<br>overloading from Oracle: https://docs.oracle.com/javase/specs/jls/se8/html/jls-8.html#jls-8.4.9                                                                                                                                                                           |
| 20. | A | The toString method of the Object class is overridden by class A.                                                                                                                                                                                                                                                                                                                                                                                                   |
| 21. | B | The get method will return the value 10 from a (the instance of class A), which began with 7<br>and added 3.                                                                                                                                                                                                                                                                                                                                                        |
| 22. | A | The get method will get 7, from the underlying instance of class A that b (the instance of class<br>B) is built on. This 7 is not affected by the call to add, since add will only affect the instance in<br>class B. The reason the 7 is returned, is because it is a private instance variable in the class<br>where get() was defined, and Java gives this higher precedence than the same named variable<br>in the subclass, even when the method is inherited. |
| 23. | D | You cannot add these types together, if you want both toString methods to be accessed,<br>you'd need to have ""+a+b instead.                                                                                                                                                                                                                                                                                                                                        |
| 24. | D | Applying the keyword static to a nested class makes it associated with its outer class, but<br>does not require an instance of the outer class to be able to access. Since the client code<br>attempts to access the ObiWan class without creating an instance of the Jedi class, the<br>keyword static is required.                                                                                                                                                |

| 25.  | А | Note that the two speak methods are not linked in any way (as you might have with                       |
|------|---|---------------------------------------------------------------------------------------------------------|
|      |   | inheritance) and therefore, the first line calls the ObiWan class's speak method, and the               |
|      |   | second line calls the Jedi class's speak method.                                                        |
| 26.  | С | Both $A$ and $B$ are fed into a NOT gate, which are both fed into a NAND gate. $C$ and $D$ are fed into |
|      |   | a NOR gate. The output of the NAND and the NOR gate are fed into an XOR gate.                           |
| 27.  | D | The following is a copy of the truth table for the expression in the logic diagram:                     |
|      |   | $A \mid B \mid C \mid D \mid \overline{A} * \overline{B} \oplus \overline{C} + \overline{D}$            |
|      |   | F F F F T                                                                                               |
|      |   | F F F T  F                                                                                              |
|      |   | F   F   T   F   F                                                                                       |
|      |   | F   F   T   T   F                                                                                       |
|      |   | F   T   F   F                                                                                           |
|      |   | $F \mid T \mid F \mid T \mid T$                                                                         |
|      |   |                                                                                                         |
|      |   |                                                                                                         |
|      |   |                                                                                                         |
|      |   | T   F   F   T   T   T   T   T   T   T                                                                   |
|      |   | $\dot{T}   \dot{F}   \dot{T}   \dot{T}   \dot{T}  $                                                     |
|      |   | † †  <b>;</b>   <b>;</b>   <b>;</b>   <b>;</b>                                                          |
|      |   | Ť   Ť   Ě   Ť   Ť                                                                                       |
|      |   | T   T   F   T                                                                                           |
|      |   | T   T   T   T                                                                                           |
|      |   | Of the 16 permutations, 10 are true and 8 are false.                                                    |
| 28.  | В | The following is a copy of the truth table for the expression proposed in question 32:                  |
|      |   | $A \mid B \mid C \mid \overline{A} * \overline{B} \oplus \overline{C + C}$                              |
|      |   | F F F T                                                                                                 |
|      |   | F F T F                                                                                                 |
|      |   | F   T   F   F                                                                                           |
|      |   | $F \mid T \mid T \mid T$                                                                                |
|      |   | T   F   F   F                                                                                           |
|      |   | T   F   T   T   T   T   T   T   T   T                                                                   |
|      |   | $\frac{1}{1}$                                                                                           |
|      |   | Of the 8 permutations, 4 are true, and 4 are false.                                                     |
| 29.  | С | This option is the only one that correctly acknowledges both the error with the code, as well as a      |
|      |   | valid/acceptable method of resolving the error.                                                         |
| 30.  | A | Assuming that we used one of the two resolution methods mentioned in option C from question             |
| 50.  |   | 28, then the client code will first call the Tejo class's ult method, and then the Jett class's         |
|      |   | ult method. There is no error in referencing the name field of the Agent class without the              |
|      |   | super modifier (otherwise, an option about this would have been written for question 28 since           |
|      |   | there is only one error as mentioned).                                                                  |
| 31.  | D | This will require the use of generics, hence the T. Moreover, since the problem asks that objects       |
| J    |   | implement the Comparable interface, we need to append extends Comparable <t>.</t>                       |
| 32.  | Α | Note that we don't have to specify T extends Comparable <t> for every other reference</t>               |
| J    | " | after having declared the properties of $T$ . Afterwards, we can just refer to the generic type $T$ ,   |
|      |   | since the compiler knows that T implements the Comparable interface by what we did in                   |
|      |   | question 33.                                                                                            |
| 33.  | E | The extract method is really the extractMin method from a heap algorithm, which means                   |
|      |   | that it runs in $O(\log_2 n)$ time. Note that the loop will run at most $O(\log_2 n)$ time since, after |
|      |   | each iteration, we cut down the search space by a factor of 2.                                          |
| 34.  | D | As previously stated, this is a heap, but since the element removed by the heap when the extract        |
| J-1. |   | method is called is the smallest value, that makes it a min-heap. Note that all data structures         |
|      |   | mentioned (except for option A) do have a tree-like structure, the only one that satisfies all          |
|      |   | I HICHLIUNCU TEACCUL IUI UULIUH ATUU HAVE A LICCTIKE SITUUTUE. HIC UHIV UHC HIAL SATISTICS AT           |

| 35. | D                                      | With an array, we can do $\mathcal{O}(1)$ random access of the list, which means that we can perform binary search on the list. Binary search takes $\mathcal{O}(\log_2 n)$ time, where $n$ is the array size. The input size is $m=n^2$ , so the total complexity is $\mathcal{O}(\log_2 n^2)=\mathcal{O}(2\log_2 n)=\mathcal{O}(\log_2 n)$                                                                                                                        |
|-----|----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 36. | А                                      | With a singly-linked list, we cannot do $\mathcal{O}(1)$ random access, and have to do a linear search for elements. Since the input size is $m=n^2$ , the total time complexity is $\mathcal{O}(n^2)$ .                                                                                                                                                                                                                                                            |
| 37. | А                                      | Singleton is a creational design pattern that lets you ensure that a class has only one instance, while providing a global access point to this instance.                                                                                                                                                                                                                                                                                                           |
| 38. | С                                      | Despite having an average time complexity of $\mathcal{O}(n \log_2 n)$ , Quick Sort is the only algorithm among the options that has a worst-case time complexity of $\mathcal{O}(n^2) \neq \mathcal{O}(n \log_2 n)$ .                                                                                                                                                                                                                                              |
| 39. | $\mathcal{O}(V^2)$ or $\mathcal{O}(E)$ | Note that since the graph is complete/dense, the best backing structure to use here isn't a heap (which would work in $\mathcal{O}((V+E)\log_2 V)$ time for a Binary Heap or $\mathcal{O}(V\log_2 V+E)$ time for a Fibonacci Heap) but instead a 2D array / matrix / adjacency list. Note that for a complete graph, $ E  \equiv  V ^2$ , so either $\mathcal{O}(V^2)$ or $\mathcal{O}(E)$ are acceptable answers, despite meaning two different things in general. |
| 40. | 171                                    | This is equivalent to the following sum: $18 + 12 + 17 + 32 + 36 + 56 = 171$                                                                                                                                                                                                                                                                                                                                                                                        |