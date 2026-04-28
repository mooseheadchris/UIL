# **UIL COMPUTER SCIENCE WRITTEN TEST – 2025 INVITATIONAL A**

**Note:** Correct responses are based on **Java SE Development Kit 22 (JDK 22)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

| Question 1                                                      |                                        |  |  |  |
|-----------------------------------------------------------------|----------------------------------------|--|--|--|
| Which of the following is not equivalent to the expression 4378 | + 101012?                              |  |  |  |
| A) 103104<br>B) 4648<br>C) 13416                                | D) 1001101002<br>E) All are equivalent |  |  |  |
| Question 2                                                      |                                        |  |  |  |
| What is output by the code to the right?                        |                                        |  |  |  |
| A) 55<br>B) 11<br>C) 7<br>D) 19                                 | out.println(3+4 % 1+2 * 5+6);          |  |  |  |
| E) There is no output due to a compile error.                   |                                        |  |  |  |
| Question 3                                                      |                                        |  |  |  |
| What is output by the code to the right?                        |                                        |  |  |  |
| A) 2.346<br>B) 2.34567                                          | out.printf("%.3f",2.34567);            |  |  |  |
| C) 2.34<br>D) 2.345                                             |                                        |  |  |  |
| E) There is no output due to a runtime error.                   |                                        |  |  |  |
| Question 4                                                      | String a = "Chilis";                   |  |  |  |
| What is output by the code to the right?                        | String b = "BabyBackRibs";             |  |  |  |
| A) BackRiblis<br>B) BackRilis                                   | b = b.substring(3, 11);                |  |  |  |
| C) yBackRibilis<br>D) yBackRiilis                               | a = b + a.substring(2);                |  |  |  |
| E) There is no output due to a runtime error.                   | out.println(a);                        |  |  |  |
| Question 5                                                      | boolean a = true;                      |  |  |  |
| What is output by the code to the right?                        | boolean b = a ^ !a;                    |  |  |  |
| A) true<br>B) false                                             | a = a   b & !a   !b;                   |  |  |  |
| C) There is no output due to a syntax error.                    | out.println(a);                        |  |  |  |
| Question 6                                                      |                                        |  |  |  |
| What is output by the code to the right?                        | double a = 2.45;                       |  |  |  |
| A) 3<br>B) 2.5<br>C) 3.0<br>D) 2.0                              | out.println(Math.ceil(a));             |  |  |  |
| E) There is no output due to a runtime error.                   |                                        |  |  |  |
| Question 7<br>What is output by the code to the right?          | int i = 10;<br>if(i++ == 11)           |  |  |  |
| A) 212<br>B) 112                                                | out.print(1);                          |  |  |  |
|                                                                 | else if(i++ == 11);                    |  |  |  |
| C) 1212<br>D) 211                                               | out.print(2);                          |  |  |  |
| E) There is no output due to a runtime error.                   | out.println(i);                        |  |  |  |
| Question 8<br>int a = 17 -<br>8 * 3;                            |                                        |  |  |  |
| What is output by the code to the right?                        | int b = a + 11 / 2;                    |  |  |  |
| A) 864<br>B) -14<br>C) 513<br>D) 14                             | out.println(a * b);                    |  |  |  |
| E) There is no output due to a runtime error.                   |                                        |  |  |  |

```
Question 9
How many *s are output by the code to the right?
A) 27 B) 33 C) 29 D) 30
E) There is no output due to a runtime error.
                                                   for(int y = 0; y < 12; y++)
                                                        for(int c = 1; c < y; c *= 2)
                                                              out.print("*");
                                                   out.println();
Question 10
What is the output by the code to the right?
A) 55
B) 67
C) 7
D) There is no output due to a compile error.
E) There is no output due to a runtime error.
                                                   int[] i = new int[] {
                                                    17, 12, 9, 8, 39, 3
                                                   };
                                                   i[2] += i[4];
                                                   i[1] -= i[3];
                                                   int b = i[2];
                                                   b += i[1] + i[5];
                                                   out.println(b);
Question 11
Which of the following packages contains the File class?
A) java.lang.* B) java.awt.* C) java.util.* D) java.io.* E) None of the above.
Question 12
What is output by the code to the right?
A) 456 B) 106
C) 561 D) 121
E) There is no output due to a runtime error.
                                                   int sum = 1;
                                                   for(int y = 0; y < 15; y++)
                                                        for(int x = 0; x < y; x++)
                                                              sum += x;
                                                   out.println(sum);
Question 13
What is the order of precedence for the operators to the right?
A) II, IV, III, I B) IV, II, I, III
C) IV, II, III, I D) III, II, IV, I
E) II, IV, I, III
                                                   I. || (logical)
                                                   II. ++ (post)
                                                   III. & (bitwise)
                                                   IV. –- (pre)
Question 14
What is output by the code to the right?
A) 8 B) 64 C) 16 D) 32
E) There is no output due to a runtime error.
                                                   out.println(Integer.SIZE);
Question 15
What is the output by the code to the right?
A) [B, C, D]
B) [D, C, A]
C) [A, C, D]
D) [D, B, A]
E) There is no output due to a compile error.
                                                   ArrayList<String> a;
                                                   a = new ArrayList<String>();
                                                   a.add("A");
                                                   a.add("B");
                                                   a.add("C");
                                                   a.remove(1);
                                                   a.add("D");
                                                   out.println(a);
Question 16
What is output by the code to the right?
A) 1234ABCD
B) [Ljava.lang.String;@156643d4
C) Output cannot be determined until runtime.
D) There is no output due to a compile error.
E) There is no output due to a runtime error.
                                                   String s = "1234ABCD";
                                                   char[]c = s.toCharArray();
                                                   out.println(c);
```

## **Question 17** What is output by the code to the right? **A)** X = 81 **B)** X = X **C)** 0 = X **D)** X = 88 **E)** There is no output due to a runtime error. char A = 'X'; int B = 81; out.print(B < A ? A : 0); out.print(" = "); out.print(B > A ? B : A); **Question 18** What is output by the line marked //q18 in the client code to the right? **A)** [5, 9, 13, 17, 25, 1] **B)** [1, 5, 9, 13, 17, 25] **C)** [17, 25, 1, 5, 9, 13] **D)** [13, 17, 25, 1, 5, 9] **E)** There is no output due to a runtime error. ArrayList<Integer> a; a = new ArrayList<Integer>(); for(int y = 1; y < 30; y += 4) a.add(y); Collections.rotate(a, -3); a.remove(2); a.remove(3); out.println(a); //q18 a.add(212); a.removeIf(x -> x % 3 == 2); out.println(a); //q19 **Question 19** What is output by the line marked //q19 in the client code to the right? **A)** [13, 21, 1, 9] **B)** [17, 5, 212] **C)** [13, 25, 1, 9] **D)** [21, 25, 1, 9, 13] **E)** There is no output due to a runtime error. **Question 20** What is output by the code to the right? **A)** 117 **B)** 81 **C)** 165 **D)** 80 **E)** There is no output due to a runtime error. out.println(17 | 45 ^ 74 & 88); **Question 21**

What is output by the line marked //q21 in the client code to the right?

- **A)** 8 **B)** 13
- **C)** 12 **D)** 5
- **E)** There is no output due to a runtime error.

#### **Question 22**

What is output by the line marked //q22 in the client code to the right?

- **A)** 987 **B)** 128
- **C)** 465 **D)** 37
- **E)** There is no output due to a runtime error.

## **Question 23**

What is output by the line marked //q23 in the client code to the right?

- **A)** 7739 **B)** 616

- **C)** 2048 **D)** 28657
- **E)** There is no output due to a runtime error.

```
public int recur(int i) {
    if(i < 0)
         return 1;
    if(i % 5 < 2)
         return recur(i - 2) + 
                      recur(i - 3);
    else
         return recur(i - 2);
}
//////////////client code/////////////
out.println(recur(10)); //q21
out.println(recur(32)); //q22
out.println(recur(51)); //q23
```

What could replace **<1\*>** in the code to the right so that the A class compiles and functions as intended?

```
A) self.i = i;
 self.s = s;
B) this.i = i;
 this.s = s;
C) i = i;
 s = s;
D) super(i,s);
```

**E)** More than one of the above.

#### **Question 25**

What could replace **<2\*>** in the code to the right so that the B class compiles and functions as intended, intializing the i instance variable with value 7?

```
A) super(s, 7);
B) super.A(7, s);
C) super(7, s);
D) super.A(s, 7);
E) super();
```

## **Question 26**

What is the output by the line marked //q26 in the client code to the right?

```
A) 4 10 10
B) 4 10 8
C) 4 8 8
```

**E)** There is no output due to a compile error.

#### **Question 27**

**D)** 3 7 7

What is the output by the line marked //q27 in the client code to the right?

```
A) c 10
B) c 16
C) c 14
```

**D)** There is no output due to a compile error.

**E)** There is no output due to a runtime error.

## **Question 28**

What is the output by the code to the right?

```
A) true
B) false
```

**C)** Output cannot be determined until runtime.

**D)** There is no output due to a compile error.

**E)** There is no output due to a runtime error.

```
class A{
    int i;
    String s;
    public A(int i, String s) {
         <1*>
    }
    public int add() {
         return ++i;
    }
    public String toString() {
         return s+" "+i;
    }
}
class B extends A{
    public B(String s) {
         <2*>;
    }
    public int add() {
         i += 2;
         super.add();
         return i;
    }
}
///////////client code////////////
A a = new A(3, "a");
B b = new B("b");
A c = new B("c");
String o = "" + a.add();
o += " " + b.add();
o += " " + c.add();
out.println(o); //q26
c.add();
c.add();
out.println(c); //q27
```

```
String s1 = "H3llo Th3r3!";
String s2 = "H..{2,4}\\S..{2,5}";
s1 = "" + s1.matches(s2);
out.println(s1);
```

What could replace **<?\*>** in the code to the right so that the code compiles and executes as intended?

- **A)** add **B)** push
- **C)** append **D)** A and B.
- **E)** Any of the above.

#### **Question 30**

What is the output by the code to the right?

- **A)** [Purple, Orange, Red]
- **B)** [Green, Yellow, Red]
- **C)** [Purple, Red, Yellow]
- **D)** [Blue, Purple, Yellow]
- **E)** There is no output due to a compile error.

#### **Question 31**

Assume that the elements to the right are inserted into an Unbalanced Binary Search Tree where duplicate elements are **not added** to the tree.

How many internal nodes will the tree have?

- **A)** 15 **B)** 13
- **C)** 10 **D)** 16

**E)** 9

## **Question 32**

Under the same assumption as Question 31, how many leaf nodes will the tree have?

- **A)** 1 **B)** 5
- **C)** 3 **D)** 4

**E)** 7

## **Question 33**

Under the same assumption as Question 31, what is the diameter of the tree?

- **A)** 8 **B)** 6
- **C)** 9 **D)** 10
- **E)** 4

## **Question 34**

Under the same assumption as Question 31, what is the worstcase time complexity for the operation search() in an Unbalanced Binary Search Tree? You may assume that is the number of elements in the tree.

- **A)** (() ) **B)** (
- 2 )

- **C)** () **D)** (√)
- **E)** (() )

```
Stack<String> stack;
stack = new Stack<String>();
stack.<?*>("Blue");
stack.<?*>("Purple");
stack.<?*>("Orange");
stack.pop();
stack.<?*>("Green");
stack.pop();
stack.<?*>("Yellow");
stack.<?*>("Red");
stack.pop();
out.println(stack);
```

34, 86, 28, 29, 33, 14, 52, 31, 92, 14, 15, 92, 31, 92, 105, 95, 97, 118

Which of the following could replace **<1\*>** to ensure that any classes that are stored as data within this data structure are compatible with the Comparable interface?

- **A)** extends **B)** implements
- **C)** requires **D)** Either A or B.
- **E)** None of the above.

#### **Question 36**

Which of the following lines of code could replace **<2\*>** so that the function peek() properly returns the value of the data stored in head?

- **A)** return head.data
- **B)** return this.head.data
- **C)** return this.head
- **D)** Either A or B.
- **E)** All of the above.

## **Question 37**

Which of the following well-known data structures is the class DataStruct an implementation of?

- **A)** LinkedList **B)** Queue
- **C)** Stack **D)** Vector

**E)** Deque

#### **Question 38**

Which of the following classes would not be able to be stored within this data structure?

- **A)** Integer **B)** String
- **C)** BigInteger **D)** double[]
- **E)** None of the above.

```
public class DataStruct<T <1*> Comparable<T>> {
    private class Node {
           public T data;
           public Node next;
           public Node(T d, Node n) {
                 this.data = d;
                 this.next = n;
           }
    }
    private Node head;
    private int size;
    public DataStruct() {
           this.size = 0;
           this.head = null;
    }
    public T peek() {
           if(head == null) {
                 return null;
           }
           <2*>
    }
    public T pop() {
           T data = this.head.data;
           this.head = this.head.next;
           this.size--;
           return data;
    }
    public T push(T data) {
           Node newHead = new 
                 Node(data, this.head);
           this.head = newHead;
           this.size++;
           return data;
    }
    public int size() {
           return size;
    }
```

}

Evaluate the following postfix expression. Assume that the ^ operator refers to the power operator, and that / is performed as integer division.

252 42 36 - 2 ^ / -2 -34 89 + \* +

#### **Question 40**

Determine the longest simple cycle in the undirected graph to the right. Note that if multiple such solutions exist, chose the one that is lexicographically first.

![](_page_6_Picture_5.jpeg)

![](_page_7_Picture_0.jpeg)

## **UIL COMPUTER SCIENCE – 2024-2025 INVITATIONAL A**

Questions (+6 points for each correct answer, -2 points for each incorrect answer)

1) <u> </u>

11) <u>D</u>

21) <u>A</u>

31) <u>E</u>

2) <u>D</u>

12) <u> </u>

22) <u>B</u>

32) <u>B</u>

3) <u>A</u>

13) <u>A</u>

23) <u>C</u>

33) <u>C</u>

4) <u>C</u>

14) <u>D</u>

24) <u>B</u>

34) <u>C</u>

5) <u>A</u>

15) C

25) C

35) <u>A</u>

6) <u>C</u>

16) <u>A</u>

26) <u>A</u>

36) D

7) <u>A</u>

17) <u>D</u>

27) B

37) <u>C</u>

8) <u>D</u>

18) <u>D</u>

28) <u>A</u>

38) <u>D</u>

9) <u>C</u>

19) <u>C</u>

29) <u>D</u>

\*39) <u>-103</u>

10) <u>A</u>

20) <u>A</u>

30) <u>D</u>

\*40) <u>ADFCGA</u>

Note: Correct responses are based on Java SE Development Kit 22 (JDK 22) from Sun Microsystems, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.

## Explanations:

| 1.  | E | All of the values are equivalent                                                                            |
|-----|---|-------------------------------------------------------------------------------------------------------------|
| 2.  | D | Simple order of operations problem                                                                          |
| 3.  | A | Printf is formatting output, "%.3f" rounds<br>the decimal value to 3 places                                 |
| 4.  | C | Simple substring problem, substring is inclusive of first value, exclusive of last (if present)             |
| 5.  | A | Simple Boolean solving                                                                                      |
| 6.  | C | Math.ceil<br>returns next "whole" number as a double that is above the given value                          |
| 7.  | A | i++<br>returns value of i, THEN<br>increments, so value returned is one less than actual value              |
| 8.  | D | Simple order of operations problem                                                                          |
| 9.  | C | Simple math problem, tracing the loop                                                                       |
| 10. | A | Array problem, no tricks really just trace it out                                                           |
| 11. | D | File<br>class is in the java.io<br>package                                                                  |
| 12. | A | Just trace the loop, you could also estimate and knock out the wrong answers                                |
| 13. | A | Simple order of precedence                                                                                  |
| 14. | D | Integer = 32 bits                                                                                           |
| 15. | C | add to the end, Arraylists are 0-indexed. Trace it out.                                                     |
| 16. | A | char arrays print out like a string, all other array types do not print legibly.                            |
| 17. | D | In ternary, the char at the second term will be cast to an int if the first term is an int.                 |
| 18. | A | Arraylist tracing, rotate will rotate the list like a circle.                                               |
| 19. | C | Arraylist tracing, removeIf removes a value if the expression is true for it.                               |
| 20. | A | Simple bitwise tracing.                                                                                     |
| 21. | A | Simple recursion tracing.                                                                                   |
| 22. | B | Simple recursion tracing. There is a trick for this question, the answer will be equivalent to 2 ^ (n       |
|     |   | / 5 + 1).                                                                                                   |
| 23. | C | Simple recursion tracing. There is a trick for this question, the answer will be equivalent to 2 ^ (n       |
|     |   | / 5 + 1).                                                                                                   |
| 24. | B | this.i<br>points to the instance variable, i<br>points to the parameter in the constructor.                 |
| 25. | C | super(7, s)<br>is the only one that does not cause an error.                                                |
| 26. | A | For both of these question explanations I will refer to i<br>as the value of each class instance. Both      |
|     |   | instances of the B<br>class will be initialized with value 7, and their add<br>methods will add 3<br>every  |
|     |   | time they are called, giving both b<br>and c<br>a value of 10<br>(2 are added in the add<br>method of class |
|     |   | B, one is added in the super<br>call to the add<br>method of class A). The A a<br>will have value 3, and    |
|     |   | will add one when the add<br>method is called, giving a<br>a value of 4. c<br>is actually an instance of    |
|     |   | class B, because the B<br>constructor is called when it is initialized.                                     |
| 27. | B | Since c<br>is an instance of class B, and has a value of 10<br>after the code for question 26 (see the      |
|     |   | explanation for question 26). The add<br>method is called twice so the value will be 16<br>after the        |
|     |   | code has executed. The toString<br>method will return "c 16", as "c" is the string s<br>and the             |
|     |   | value is 16.                                                                                                |
| 28. | A | The value true<br>is returned because the pattern described by s2<br>is matched by the string s1.           |
|     |   | The pattern described by s2<br>is as follows: the character H, followed by 3-5 characters (.<br>means       |
|     |   | any character, do not need to be any specific character), followed by a non-whitespace character            |
|     |   | (\\S), followed by 3-6 characters (.<br>means any character, do not need to be any specific                 |
|     |   | character). {a,b}<br>after a character means a match will be between a<br>and b<br>occurrences of that      |
|     |   | character.                                                                                                  |
| 29. | D | The methods push<br>and add<br>both will work to add a value to a stack.                                    |
| 30. | D | Stack tracing, First in First out.                                                                          |

| 31. | E    | A copy of the binary search tree has been provided below:                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----|------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     |      |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|     |      | Internal nodes are those nodes that have 1 or more children. There are a total of 9 nodes that<br>have 1 or more child (nodes 34, 28, 14, 29, 33, 86, 92, 105, and 95).                                                                                                                                                                                                                                                                                                                                       |
| 32. | B    | Leaf nodes are those nodes that have no children of their own. There are a total of 5 nodes that<br>have no children of their own (nodes 15, 31, 52, 97, and 118).                                                                                                                                                                                                                                                                                                                                            |
| 33. | C    | The diameter of a tree is the greatest number of edges between any two nodes within the tree.<br>In the case of this tree, those nodes are 31 and 97, which have 9 edges between them.                                                                                                                                                                                                                                                                                                                        |
| 34. | C    | The worst-case scenario for an Unbalanced Binary Search Tree is that the nodes are inserted in<br>sorted order. This effectively creates a Linked List, which has a linear time complexity for search<br>operations.                                                                                                                                                                                                                                                                                          |
| 35. | A    | The key word extends<br>is the only one among the ones listed which allows to specify which<br>interfaces or classes the generic types must implement or inherit. This is commonly confused<br>with the implements<br>key word, which is used when declaring a class or interface that should<br>express the behaviors of another interface. The requires<br>key word, while a valid key word in<br>the Java library, denotes a required library within a module, and thus is irrelevant to this<br>question. |
| 36. | D    | Since there are no local versions of the variable head, either option A or option B will reference<br>the global head<br>variable and perform the function as intended. Option C will break since the<br>return type of the function is of type T<br>and not of provided type Node.                                                                                                                                                                                                                           |
| 37. | C    | This is a Stack<br>since it denotes the methods peek(), pop(), and push()<br>and has the FIFO<br>(First-in-First-out) property with regards to how elements are handled.<br>While the FIFO property can also be obtained using a Deque, for this to be a Deque, we would<br>need to have separate methods for peeking, pushing, and popping elements from both sides of<br>the Queue, which is not present in the provided implementation.                                                                    |
| 38. | D    | Integer, String, and BigInteger<br>all implement the Comparable<br>interface. While<br>double[]<br>can actually be stored in a normal Stack, since double[]<br>does not implement<br>the Comparable<br>interface, it cannot be stored in this implementation of a Stack.                                                                                                                                                                                                                                      |
| 39. | -103 | The following is the process of evaluating the postfix expression (elements shown in parenthesis<br>are the value pushed to the operand stack after performing the next operation):<br>252 42 36 -<br>2 ^ / -2 -34 89 + * +<br>252 (6) 2 ^ / -2 -34 89 + * +<br>252 (36) / -2 -34 89 + * +<br>(7) -2 -34 89 + * +<br>7 -2 (55) * +<br>7 (-110) +<br>(-103)                                                                                                                                                    |

| 40. | A D F C G A | A simple cycle is a cycle in a graph with no repeated vertices (except the first to denote this as                                                                                                                                                                                                                                                                                                                                                 |
|-----|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     | or          | being a cycle and not a non-cyclic path)                                                                                                                                                                                                                                                                                                                                                                                                           |
|     | ADFCGA      | Note that to make a cycle as lexicographically small as possible, simply choose the node within<br>the cycle with the lexicographically smallest label as the start of the cycle, and among its two (or<br>more) neighbors, select the one that is lexicographically smallest. This ensures that the<br>Three major simple cycles exist within the graph:<br>1.<br>𝐵 → 𝐽 → 𝐸 → 𝐾 → 𝐵<br>𝐷 → 𝐻 → 𝑀 → 𝐿 → 𝐼 → 𝐷<br>2.<br>𝐴 → 𝐷 → 𝐹 → 𝐶 → 𝐺 → 𝐴<br>3. |
|     |             | Of these, the largest simple cycle that is also the lexicographically smallest option is #3                                                                                                                                                                                                                                                                                                                                                        |