# **UIL COMPUTER SCIENCE WRITTEN TEST – 2024 DISTRICT**

**Note:** Correct responses are based on **Java SE Development Kit 20 (JDK 20)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 20 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

```
Question 1i
 Find the product of 1100112 and 6410
 A) 64158 B) 64108 C) 7758 D) 63008 E) 62148
Question 2uesti
What is the output of the code segment to the right?
 A) -12 B) -8 C) -4 D) 1 E) 2
                                             out.print(12 - 27 + 17 % 10 / 2);
Question 3
 What is the output of the code segment to the right?
 A) 011
 11
 24
 B) 1411
 10
 24
 C) 1471
 11
 1
 D) 1471
 10
 24
 E) 1671
 10
 12
                                             int A = 14;
                                             int B = 16;
                                             int C = 9;
                                             int D = 9;
                                             out.print(A % B);
                                             out.print(B % C);
                                             out.println(A / D);
                                             out.print(C / D);
                                             out.println(D % C);
                                             out.println(A + B / C + D);
Question 4
 What is the output of the code segment to the right?
 A) A B) S C) C D) I E) T
                                             String St1 = "KANSAS";
                                             String St2 = "CITY";
                                             String St3 = St2+St1.substring(0,3);
                                             out.print(St3.charAt(5));
Question 5
 What is the output of the code segment to the right?
 A) true
B) false
                                             boolean A = true;
                                             boolean B = !A;
                                             boolean C = A || B;
                                             boolean D = B && C;
                                             boolean E = A ^ D;
                                             out.print(E); 
Question 6
 What is the output of the code segment to the right?
 A) 18 B) 21 C) 24 D) 28 E) 35
                                             int T = 0;
                                             for (int x=5; x<=10; x=x+2)
                                             T+=x;
                                             out.print(T);
```

#### **Question 7** What is the output of the code segment to the right? **A)** 2 **B)** 4 **C)** 8 **D)** 10 **E)** 16 double A = Math.floor(8.7); double B = Math.ceil(A - 0.1); double C = Math.sqrt(A + B); int D = (int) C; out.print(D); **Question 8** What is the output of the code segment to the right? **A)** 14 **B)** 15 **C)** 16 **D)** 17 **E)** 18 int A = 5; int B = A - 1; int C = B + 2; if (A > B) C++; if (C < A) B++; if (B < C) A++; out.print(A + B + C); **Question 9** What is the output of the code segment to the right? **A)** 6 **B)** 7 **C)** 8 **D)** 9 **E)** 10 int[] Stuff = {4,2,1,0,3}; int A = Stuff[Stuff[2]]; int B = Stuff[Stuff[3]]; int C = Stuff[Stuff[0]]; out.print(A + B + C); **Question 10** What is the output of the code segment to the right? **A)** 60 **B)** 65 **C)** 70 **D)** 75 **E)** 80 int[] elf = new int[50]; for(int x=0; x<=49; x++) elf[x] = x \* 2 + 5; out.print(elf[10] + elf[20]); **Question 11** What is output by the code segment to the right? **A)** [7,6,2,0,2] **B)** [7,5,4,3,2] **C)** [7,4,5,3,2] **D)** [7,2,4,0,2] **E)** [1,4,0,2,2] ArrayList<Integer>Fred; Fred = new ArrayList<Integer>(); Fred.add(7); Fred.add(5); Fred.add(8); Fred.add(3); Fred.add(9); Fred.add(1); Fred.add(4); Fred.add(0); Fred.add(2); Fred.set(5,2); Fred.add(4,6); for (int x=1; x<=5; x++) Fred.remove(1); out.print(Fred); **Question 12** What is the output of the code segment to the right? **A)** -5 -4 -3 -2 -1 0 1 2 3 4 5 **B)** -5 -2 1 4 **C)** -10 -6 4 20 **D)** -5 -4 3 16 **E)** -5 -6 4 20 for(int i=-5, T=1; i<=5; i=i+3, T++) out.print(i\*T + " ");

Question 13 What is the output of the code segment to the right? int M = 6 + 10 & 4 + 10 << 2;**D)** 15 **B)** 12 **A)** 10 **C)** 14 **E)** 16 out.print(M); Question 14 out.print(Long.SIZE/Short.SIZE); What is the output of the code segment shown on the right? out.print(Integer.SIZE/Byte.SIZE); **A)** 22 **B)** 24 **C)** 42 **D)** 44 **E)** 84 Question 15 What is output by the code segment shown on the right? String Heat; Heat = "5 1 2 9 2 6 7 4 1 7"; Scanner Sc = new Scanner(Heat); **B)** 8 int T = Sc.nextInt();**C)** 10 for (int x=0;  $x \le T$ ; x++) **D)** 16 Sc.next(); T += Sc.nextInt() + Sc.nextInt(); **E)** 20 out.print(T); Question 16 int G = 0; What is the output of the code segment shown on the right? for (int A=-3; A<=3; A++) for (int B=0; B <= 100; B += 10) **C)** 70 **D)** 77 **A)** 60 **B)** 66 **E)** 84 G++; out.print(G); Question 17 String Plasma = "QWERTYUIOP"; What is the output of the code segment shown on the right? int R = 0; **A)** 25 **B)** 30 **C)** 35 **D)** 40 **E)** 45 for (int x=0; x<Plasma.length()-1; x++) char One =Plasma.charAt(x); char Two =Plasma.charAt(x+1); if (One<Two) R = R + 5;} out.print(R); Question 18 What is the output of the code segment shown on the right? int A = 20; **A)** 42 **B)** 47 **C)** 48 **D)** 49 **E)** 53 int B = (A>16) ? 21:15; int C = (A>B) ? 7:12; out.print(A + B + C);

```
Question 19
 What is the output of the code segment shown on the right?
A) 109
B) 124
C) 129
D) 144
E) 154
                                                int[]Speed = {4,1,4,1,4,1};
                                                int[]Velocity = {5,10,15,20,25,30,35,40};
                                                int Texas = Speed[0];
                                                for(int power: Speed)
                                                Texas += Velocity[power];
                                                out.print(Texas);
Question 20
 In the code to the right, what is output on line #1? 
A) 70 B) 85 C) 100 D) 110 E) 120
                                                public static int dr(int A, int B)
                                                 {
                                                 if (A < B)
                                                 return dr(A+2,B+1) + A*B;
                                                 return A*10;
                                                 }
                                                 // Client Code
                                                 out.print(dr(12,7)); // line #1
                                                 out.print(dr(4,6)); // line #2
                                                 out.print(dr(1,6)); // line #3
Question 21
In the code to the right, what is output on line #2? 
 A) 132 B) 137 C) 146 D) 148 E) 157
Question 22
In the code to the right, what is output on line #3? 
A) 220 B) 270 C) 310 D) 330 E) 350
Question 23
What is the output of the code segment shown on the right?
 A) SITYO
 B) RSITY
 C) RSIT
 D) SITY
 E) ITYO
                                                String St = "UNIVERSITYOFTEXAS";
                                                int T = St.length();
                                                St = St.substring(T/4,3*T/4);
                                                St = St.substring(1,St.length()-1);
                                                St = St.substring(1,St.length()-1);
                                                out.print(St);
Question 24
Which could possibly be the output of the code segment shown 
on the right? Four options are not possible. Only one is possible.
A) 25 B) 75 C) 125 D) 175 E) 225
                                                int A = (int)(Math.random()*5 + 10);
                                                int B = (int)(Math.random()*10 + 3);
                                                int C = (int)(Math.random()*2 + 6);
                                                out.print(A * C + B);
```

## **Question 25** In the code to the right, what is output on line #1? **A)** 46 **B)** 52 **C)** 62 **D)** 64 **E)** 68 public static int Red(int Number) { Number = Number%10\*10 + Number/10; return Number; } public static int White(int Number) { Number = (int)(0.1\* Number + 0.5)\*10; return Number; } public static int Blue(int Number) { Number = (int)(Math.sqrt(Number)); return Number; } // Client Code out.print(Red(64)); // Line #1 out.print(White(Blue(399))); // Line #2 out.print(Blue(Red(19))); // Line #3 **Question 26** In the code to the right, what is output on line #2? **A)** 10 **B)** 14 **C)** 15 **D)** 16 **E)** 20 **Question 27** In the code to the right, what is output on line #3? **A)** 5 **B)** 6 **C)** 7 **D)** 8 **E)** 9 **Question 28** In the code to the right, what is output on line #1? **A)** 5 **B)** 6 **C)** 7 **D)** 8 **E)** 9 PriorityQueue<Integer> T; T = new PriorityQueue<Integer>(); int x =-3; while (x < 100) { T.add(x); x = -2 \* x; } out.println(T.size()); //Line #1 out.println(T.peek()); //Line #2 for(int y=1; y<=5; y++) T.remove(); out.println(T.peek()); //Line #3 **Question 29** In the code to the right, what is output on line #2? **A)** -192 **B)** =96 **C)** -48 **D)** -24 **E)** -12 **Question 30** IIn the code to the right, what is output on line #3? **A)** -3 **B)** 6 **C)** 12 **D)** 24 **E)** 48 **Question 31** What is the output of the code segment shown on the right? **A)** 2 **B)** 4 **C)** 8 **D)** 16 **E)** 32 int A = 48; int B = 32; int C = 0; for(int x = 1; x<=1000; x++) if (A%x==0 && B%x==0) C = x; out.print(C); **Question 32** How many ones? **A)** 10 **B)** 11 **C)** 12 **D)** 13 **E)** 14 <sup>215</sup> = 32768 How many ones are in the binary representation of the base ten number 32764?

## **Question 33**

What is the output of the code segment shown on the right?

- **A)** 120 **B)** 124 **C)** 128 **D)** 130 **E)** 136
- out.print(Integer.parseInt("B4",12));

#### **Question 34**

In the client code to the right, what is output on line #1?

- **A)** 63
  - **B)** 56
  - **C)** 49
  - **D)** 42
  - **E)** 35

### **Question 35**

In the client code to the right, what is output on line #2?

- **A)** 8
  - **B)** 12
  - **C)** 20
  - **D)** 40
  - **E)** 48

## **Question 36**

In the client code to the right, what is output on line #3?

- **A)** 38
- **B)** 40
- **C)** 42
- **D)** 44
- **E)** 46

```
public class Football
 {
 private int TD;
 private int FG;
 private int XP;
 public Football(int A, int B)
 {
 TD = A;
 FG = B;
 XP = A;
 }
 public int getScore()
 {
 if (TD > FG)
 return TD * 8 + XP;
 return FG * 5;
 }
 public int getFun()
 {
 if (TD != FG)
 return TD * 3 - FG;
 return XP * 10;
 }
}
 //Client code
 Football Bob = new Football(7,3);
 Football Meg = new Football(4,4);
 int A = Bob.getScore();
 int B = Bob.getFun();
 int C = Meg.getScore();
 int D = Meg.getFun();
 out.println(A); //Line #1
 out.println(D); //Line #2
 out.println(C + B); //Line #3
```

| Question 37<br>What is the output of the code segment shown on the right?<br>A) 9 3<br>B) 9 5<br>C) 9 8<br>D) 8 5<br>E) 8 3                                                                                                                                                                                                                        | int R=8; int S=5; int T=9; int U=3;<br>R = Math.max(R,S);<br>S = Math.min(R,S);<br>T = Math.min(U,T);<br>U = Math.max(U,T);<br>R = Math.max(R,T);<br>S = Math.min(U,T);<br>out.print(R + " " + S); |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Question 38<br>What is the output of the code segment shown on the right?<br>A) -4<br>B) -2<br>C) -1<br>D) 1<br>E) 2                                                                                                                                                                                                                               | String One = "Earl";<br>String Two = "Campbell";<br>out.print(One.compareTo(Two));                                                                                                                 |
| Question 39<br>Imagine you have an empty binary search tree. First, you add<br>the five vowels into the tree, one at a time in this order<br>(A,E,I,O,U). Next, you add to the tree the remaining consonants<br>in alphabetical order, starting with B and ending with Z.<br>How many leafs would the tree have?<br>Write the number in blank #39. |                                                                                                                                                                                                    |
| Question 40<br>Evaluate the postfix expression to the right.                                                                                                                                                                                                                                                                                       | 9 7 5 + 3 / 2 -<br>4 1 + + *                                                                                                                                                                       |

**Write the number in blank #40.**

# **★ANSWER KEY – CONFIDENTIAL★**

# **UIL COMPUTER SCIENCE – 2024 District**

Questions (+6 points for each correct answer, -2 points for each incorrect answer)

1) **D** 

11) **D** 

21) **C** 

31) **D** 

2) **A** 

12) **D** 

22) **D** 

32) **D** 

3) **D** 

13) **E** 

23) **D** 

33) **E** 

4) **A** 

14) **D** 

24) **B** 

34) **A** 

5) **A** 

15) **C** 

25) **A** 

35) **D** 

6) **B** 

16) **D** 

26) **E** 

36) **A** 

7) **B** 

17) **B** 

27) **E** 

37) **E** 

8) **D** 

18) **E** 

28) **C** 

38) **E** 

9) **D** 

19) **A** 

29) **A** 

\*39) 5

10) **C** 

20) **E** 

30) **D** 

\*40) 63

Note: Correct responses are based on Java SE Development Kit 20 (JDK 20) from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 20 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.

### Explanations:

| 1.      | D | Change everything to base 8 first.            |                                                                        |
|---------|---|-----------------------------------------------|------------------------------------------------------------------------|
|         |   | 1100112 becomes 638 and 6410<br>becomes 1008. |                                                                        |
|         |   | 638 times 1008<br>is 63008.                   |                                                                        |
| 2.      | A | 12 -<br>27 + 17 % 10 / 2                      |                                                                        |
|         |   | 12 -<br>27 + 7 / 2                            |                                                                        |
|         |   | 12 -<br>27 + 3                                |                                                                        |
|         |   | -15 + 3 = -12                                 |                                                                        |
| 3.      | D | int A = 14; int B = 16; int C = 9; int D = 9; |                                                                        |
|         |   | out.print(A % B);                             | Prints 14                                                              |
|         |   | out.print(B % C);                             | Prints 7                                                               |
|         |   | out.println(A / D);                           | Prints 1 then carriage return (next line)                              |
|         |   | out.print(C / D);                             | Prints 1                                                               |
|         |   | out.println(D % C);                           | Prints 0 then carriage return (next line)                              |
|         |   |                                               | out.println(A + B / C + D); Prints 24 then carriage return (next line) |
| 4.<br>A |   | String St3 = St2+St1.substring(0,3);          |                                                                        |
|         |   | St3 is "CITYKAN"                              |                                                                        |
|         |   | out.print(St3.charAt(5));                     |                                                                        |
|         |   | Character #5 is the A                         |                                                                        |
| 5.      | A | boolean A = true;                             | A is true                                                              |
|         |   | boolean B = !A;                               | B is false                                                             |
|         |   | boolean C = A    B;                           | C is true (Or needs at least 1 true)                                   |
|         |   | boolean D = B && C;                           | D is false (And need 2 trues)                                          |
|         |   | boolean E = A ^ D;                            | E is true (Xor needs exactly 1 true)                                   |
|         |   | out.print(E);                                 |                                                                        |
| 6.      | B | This adds the numbers 5, 7, and 9 to get 21.  |                                                                        |
| 7.      | B | double A = Math.floor(8.7);                   | A = 8.0                                                                |
|         |   | double B = Math.ceil(A -                      | = 8<br>B<br>0.1);                                                      |
|         |   | double C = Math.sqrt(A + B);                  | C = 4                                                                  |
|         |   | int D = (int) C;                              | 4<br>D<br>=                                                            |
|         |   | out.print(D);                                 |                                                                        |
| 8.      | D | int A = 5;                                    | A=5                                                                    |
|         |   | int B = A -<br>1;                             | B=4                                                                    |
|         |   | int C = B + 2;                                | C=6                                                                    |
|         |   | if (A > B)                                    | true                                                                   |
|         |   | C++;                                          | C=7                                                                    |
|         |   | if (C < A)                                    | false                                                                  |
|         |   | B++;                                          |                                                                        |
|         |   | if (B < C)                                    | true                                                                   |
|         |   | A++;                                          | A=6                                                                    |
|         |   | out.print(A + B + C);                         | 17                                                                     |
|         |   |                                               |                                                                        |
|         |   |                                               |                                                                        |
|         |   |                                               |                                                                        |
|         |   |                                               |                                                                        |
|         |   |                                               |                                                                        |

```
9. D int[] Stuff = {4,2,1,0,3};
              int A = Stuff[Stuff[2]]; A= Stuff[1] = 2
              int B = Stuff[Stuff[3]]; B= Stuff[0] = 4
              int C = Stuff[Stuff[0]]; C= Stuff[4] = 3
              out.print(A + B + C); 9
10. C elf[10] = 10 * 2 + 5 = 25 
              elf[20] = 20 * 2 + 5 = 45 
              70 is printed 
11. D Fred starts at [7,5,8,3,9,1,4,0,2}
              Fred.set(5,2); [7,5,8,3,9,2,4,0,2}
              Fred.add(4,6); [7,5,8,3,6,9,2,4,0,2}
               for (int x=1; x<=5; x++)
               Fred.remove(1); Remove the 5,8,3,6,9
               out.print(Fred); [7,2,4,0,2}
12. D for(int i=-5, T=1; i<=5; i=i+3, T++)
               out.print(i*T + " ");
              Pass #1 i = -5 T=1 i*T = -5 
              Pass #2 i = -2 T=2 i*T = -4 
              Pass #3 i = 1 T=3 i*T = 3 
              Pass #4 i = 4 T=4 i*T = 16 
13. E 6 + 10 & 4 + 10 << 2;
              16 & 4 + 10 << 2
              16 & 14 << 2
              16 & 56
              10000 & 111000 = 0010000 = 16
14. D out.print(Long.SIZE/Short.SIZE); 64/16 = 4
              out.print(Integer.SIZE/Byte.SIZE); 32/8 = 4
15. C Heat = "5 1 2 9 2 6 7 4 1 7";
               int T = Sc.nextInt();
              for (int x=0; x<=T; x++)
               Sc.next();
              T += Sc.nextInt() + Sc.nextInt();
                                                   T=5
                                                   skip 6 1,2,9,2,6,7 
                                                   Add 4 and 1 to T 
              out.print(T);
16. D int G = 0;
              for(int A=-3; A<=3; A++) 7 iterations
               for(int B=0; B<=100; B+=10) 11 iterations
               G++;
              out.print(G); 77
```

```
17. B String Plasma = "QWERTYUIOP";
                Traverses entire string. If letter X is before letter X+1 in the alphabet, it adds 5 to the 
                total. QW, ER, RT, TY, IO, OP = 6 times 5 = 30
18. E int A = 20; A is 20
                int B = (A>16) ? 21:15; B is 21 since A > 16
                int C = (A>B) ? 7:12; C is 12 since is not greater than B
                out.print(A + B + C); 53
19. A int[]Speed = {4,1,4,1,4,1};
                  int[]Velocity = {5,10,15,20,25,30,35,40};
                  int Texas = Speed[0];
                  for(int power: Speed)
                 Texas += Velocity[power];
                  out.print(Texas);
                  Texas = 4 + Velocity[4] + Velocity[1} + Velocity[4] + Velocity[1} + Velocity[4] + Velocity[1]
                 Texas = 4 + 25 + 10 + 25 + 10 + 25 + 10 = 109 
20. E public static int dr(int A, int B)
                  {
                  if (A < B)
                  return dr(A+2,B+1) + A*B;
                  return A*10;
                  }
                dr(12,7) = 12*10 = 120
21. C dr(4,6) = dr(6,7) + 24 = 122 + 24 = 146
                dr(6,7) = dr(8,8) + 42 = 80 + 42 = 122
                dr(8,8) = 80
22. D dr(1,6) = dr(3,7) + 6 = 324 + 6 = 330
                dr(3,7) = dr(5,8) + 21 = 303 + 21 = 324
                dr(5,8) = dr(7,9) + 40 = 263 + 40 = 303
                dr(7,9) = dr(9,10) + 63 = 200 + 63 = 263
                dr(9,10) = dr(11,11) + 90 = 110 + 90 = 200
                dr(11,11) = 110
23. D String St = "UNIVERSITYOFTEXAS";
                int T = St.length(); T=17
                St = St.substring(T/4,3*T/4); St.substring(4,12) = "ERSITYOF"
                St = St.substring(1,St.length()-1); "RSITYO"
                St = St.substring(1,St.length()-1); "SITY"
24. B A= [10,14]
                                                       B= [3,12]
                A = (int)(Math.random()*5 + 10); 
                B = (int)(Math.random()*10 + 3); 
                C = (int)(Math.random()*2 + 6); C= [6,7]
                Substituting minimum values, we get 10*6 + 3 = 63
                Substituting maximum values, we get 14*7 + 12 = 110
                Thus only values [63,110] may be printed.
```

| 25. | A  |                                                                                                                                                |  |
|-----|----|------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 26. | E  | Red takes a two-digit number and reverses the digits.                                                                                          |  |
| 27. | E  | White rounds a number to the nearest 10.                                                                                                       |  |
|     |    | Blue, takes a square root and chops off the decimal.                                                                                           |  |
|     |    | reverse digits = 46<br>out.print(Red(64));                                                                                                     |  |
|     |    | out.print(White(Blue(399))); square root chopped is 19, nearest 10 is 20                                                                       |  |
|     |    | reverse digits is 91, square root chopped is 9<br>out.print(Blue(Red(19)));                                                                    |  |
| 28. | C  | PriorityQueue <integer> T;</integer>                                                                                                           |  |
|     |    | T = new PriorityQueue <integer>();</integer>                                                                                                   |  |
|     |    | The numbers -3, 6, -12, 24, -48, 96, and -192 are added to a T.                                                                                |  |
|     |    | The size is 7.                                                                                                                                 |  |
|     |    | out.println(T.peek());<br>//Line #2                                                                                                            |  |
|     |    | for(int y=1; y<=5; y++)                                                                                                                        |  |
|     |    | T.remove();                                                                                                                                    |  |
|     |    | out.println(T.peek());<br>//Line #3                                                                                                            |  |
| 29. | A  | When we peek, we see the item in the front -<br>always the smallest item.                                                                      |  |
|     |    | We see -192                                                                                                                                    |  |
| 30. | D  |                                                                                                                                                |  |
|     |    | The loop zaps the first item 5 times -<br>always the smallest of the remaining items.                                                          |  |
|     |    | Thus -192, -48, -12, -3, and 6 are removed.                                                                                                    |  |
|     |    | Now, when we peek, we see the 24.                                                                                                              |  |
| 31. | D  | Although the loop iterates a ridiculous number of times, this finds the greatest common factor                                                 |  |
|     |    | of 48 and 32 … 16                                                                                                                              |  |
| 32. | D  | 16 or 24 is 10000 in binary. Subtract 4 and you get 1100<br>(2 ones)<br>32 or 25 is 100000 in binary. Subtract 4 and you get 11100<br>(3 ones) |  |
|     |    | 64 or 26 is 1000000 in binary. Subtract 4 and you get 111100 (4 ones)                                                                          |  |
|     |    | 215 minus 4 should have 13 ones.                                                                                                               |  |
| 33. | E  | B412 = 13610                                                                                                                                   |  |
| 34. | A  | Since 7>3 Bob.getScore() will be 7*8+7 = 63                                                                                                    |  |
| 35. | D  | Since 4==4 Meg.getFun() will be 4*10 = 40                                                                                                      |  |
| 36. | A  | Since 7!=3 Bob.getFun() will be 7*3-3 = 18                                                                                                     |  |
|     |    | Since 4 is not greater than 4 Meg.getScore() will be 4*5 = 20                                                                                  |  |
|     |    | 18+20 = 38                                                                                                                                     |  |
| 37. | E  | int R=8; int S=5; int T=9; int U=3;                                                                                                            |  |
|     |    | R = Math.max(R,S);<br>R=8                                                                                                                      |  |
|     |    | S = Math.min(R,S);<br>S=5                                                                                                                      |  |
|     |    | T = Math.min(U,T);<br>T=3                                                                                                                      |  |
|     |    | U = Math.max(U,T);<br>U=3                                                                                                                      |  |
|     |    | R = Math.max(R,T);<br>R=8                                                                                                                      |  |
|     |    | S = Math.min(U,T);<br>S=3                                                                                                                      |  |
|     |    | out.print(R + " " + S);<br>8 3                                                                                                                 |  |
| 38. | E  | "Earl".compareTo("Campbell") focuses on the ASCII values if the E and the C.                                                                   |  |
|     |    | E is two greater than C                                                                                                                        |  |
| 39. | 5  | D, H, T, N, and Z are all leafs (leaves?)                                                                                                      |  |
| 40. | 63 | 9 7 5 +<br>3 / 2 -<br>4 1 + + *                                                                                                                |  |
|     |    | 9 12 3 /<br>2 -<br>4 1 + + *                                                                                                                   |  |
|     |    | 9 4 2 -<br>4 1 + + *                                                                                                                           |  |
|     |    |                                                                                                                                                |  |
|     |    | 9 2 4 1 +<br>+ *                                                                                                                               |  |
|     |    | 9 2 5 +<br>*                                                                                                                                   |  |
|     |    | 9 7 *<br>= 63                                                                                                                                  |  |
|     |    |                                                                                                                                                |  |