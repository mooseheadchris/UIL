# **UIL COMPUTER SCIENCE WRITTEN TEST – 2023 REGION**

**Note:** Correct responses are based on **Java SE Development Kit 17 (JDK 17)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 17 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

| Question 1i                                                                                                            |                      |                                                                                                                                         |                                         |
|------------------------------------------------------------------------------------------------------------------------|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| Which of the below has a value different from the other four?<br>A)<br>101101012<br>B) 23114                           | C) 2658              | D) 18310                                                                                                                                | E) B516                                 |
| Question 2uesti                                                                                                        |                      |                                                                                                                                         |                                         |
| What is the output of the code segment to the right?                                                                   |                      |                                                                                                                                         | out.print(800 / 3 % 10 + 800 / 10 % 3); |
| A) 8<br>B) 1066<br>C) 52                                                                                               | D) 53<br>E) 9        |                                                                                                                                         |                                         |
| Question 3                                                                                                             |                      |                                                                                                                                         |                                         |
| What is the output of the code segment to the right?<br>A) \12.121212121212\\<br>nn12<br>B) \12.121212120000\\<br>nn12 |                      | double March = 12.12121212;<br>String St ="\\%.12f\\\\\nnn%d";<br>out.printf(St,March,(int)March);                                      |                                         |
| C) 12.12\\nnn12<br>D) \12.12\\<br>nn12                                                                                 |                      |                                                                                                                                         |                                         |
| E) \12.121212120000\\nn12                                                                                              |                      |                                                                                                                                         |                                         |
| Question 4<br>What is the output of the code segment to the right?<br>A) Com<br>B) omp<br>C) cie<br>Question 5         | D) nce<br>E) ute     | String Go = "ComputerScience";<br>String Fight = Go.substring(4);<br>String Win = Fight.substring(4);<br>out.print(Win.substring(1,4)); |                                         |
|                                                                                                                        |                      | boolean R = !false;<br>boolean S = R    false;                                                                                          |                                         |
| What is the output of the code segment to the right?                                                                   |                      | boolean T = R && S;                                                                                                                     |                                         |
| A) true<br>B) false                                                                                                    |                      | boolean U = S ^ T;<br>out.print(U);                                                                                                     |                                         |
| Question 6<br>What is the output of the code segment to the right?                                                     |                      | double M = Math.sqrt(80);                                                                                                               |                                         |
| A)<br>B)<br>C) 7<br>9<br>8                                                                                             | D)<br>E)<br>6<br>5   | out.print((int)Math.cbrt(M*M*M));                                                                                                       |                                         |
| Question 7<br>What is the output of the code segment to the right?                                                     |                      | int U = 240 % 100;<br>int I = U % 25;                                                                                                   |                                         |
| A)<br>5<br>B)<br>45<br>C) 50                                                                                           | D)<br>60<br>E)<br>75 | int L = I % 10;<br>out.print(U + I + L);                                                                                                |                                         |

```
Question 8
 What is the output of the code segment to the right?
 A) 10 2 4
 B) 11 10 11
 C) 10 10 10
 D) 11 10 10
 E) 10 10 11
                                                int D = 10;
                                                int R = 2;
                                                int P = 4;
                                                if (D + R > P)
                                                P = D;
                                                else
                                                D = P;
                                                if (D + P > R)
                                                R = D;
                                                else
                                                D = R;
                                                if (P + R > D)
                                                D++;
                                                else
                                                D--;
                                                out.print(D + " " + P + " " + R);
Question 9
 What is the output of the code segment to the right?
 A) 125
 B) 12514
 C) 14
 D) 5
 E) 8
                                                String St = "";
                                                for(int x = 1; x < 10; x = x * 3 - 1)
                                                St += x;
                                                out.println(St);
Question 10
 What is the output of the code segment to the right? 
 A) 32 B) 34 C) 35 D) 36 E) 38
                                                int[] perfect = new int[25];
                                                for(int x=0; x<24; x++)
                                                perfect[x] = x * x - 1;
                                                out.print(perfect[10] - perfect[8]); 
Question 11 
 What is output by the code segment to the right?
 A) 2 B) 6 C) 12 D) 20 E) 28
                                                String St = "Z 2 X 4 C 6 V 8 B 10";
                                                Scanner B = new Scanner(St);
                                                int Hello = 0;
                                                for(int x = 1; x <= 4; x++)
                                                {
                                                B.next();
                                                Hello += B.nextInt();
                                                }
                                                out.print(Hello);
Question 12
 What is the output of the code segment to the right? 
 A) 50 B) 25 C) 4 D) 33 E) 17
                                                int strange = 100;
                                                for(int x = 2; x <= 4; x++)
                                                strange /= x;
                                                out.print(strange);
Question 13
 What is the output of the code segment to the right? 
 A) 44
 B) 321
 C) 41
 D) 322
 E) 324
                                                int Q = 20; 
                                                out.print(Q << 2 + 2 ^ 3 >> 1);
```

```
Question 14
 What is the output of the code segment shown on the right?
 A) 18 B) 16 C) 17 D) 14 E) 15
                                                out.println(Byte.MAX_VALUE/Byte.SIZE);
Question 15
 What is output by the code segment to the right?
 A) [10, 30, 50, 70, 90]
 B) [60, 70, 80, 90, 100] 
 C) [20, 40, 60, 80, 100]
 D) [20, 30, 40, 50, 60]
 E) [10, 20, 40, 50, 70]
                                               ArrayList<Integer> keys;
                                               keys = new ArrayList<Integer>();
                                               for(int x = 10; x<=100; x+=10)
                                                keys.add(x);
                                               for(int x = 1; x<= 5; x++)
                                                if (keys.get(x)%10 == 0) 
                                                keys.remove(x);
                                               out.print(keys);
Question 16
 What is the output of the code segment shown on the right?
 A) 60 B) 72 C) 66 D) 55 E) -66
                                                int z = 0;
                                                for(int x=1, y=-5; x<=12; x++, y++)
                                                 z = x * y;
                                                out.print(z);
Question 17
 What is the output of the code segment shown on the right?
 A) 60
 B) 50
 C) 70
 D) 40
 E) 90
                                                int N = 100;
                                                int A = 0;
                                                int B = 0;
                                                int C = 0;
                                                for(int x=1; x<=N; x++)
                                                {
                                                if (x%5==0) A++;
                                                if (x%2==0) B++;
                                                if (x%5==0 && x%2==0) C++;
                                                }
                                                System.out.print(A + B - C);
Question 18
 What is the output of the code segment shown on the right?
 A) 2.0 B) 2 C) 1.0 D) 1 E) 0
                                                out.print(Math.pow(64 ,1/6));
Question 19
 What is the output of the code segment shown on the right?
 A) BEMJALSAM
 B) BESOEMSAL
 C) BOBJENSAM
 D) BSJEAANNL
 E) BEMJAMSAL
                                                String[]L = {"BOB","JEN","SAM","PAM","MEL"};
                                                String St = "";
                                                for(int x=1;x<=3;x++)
                                                {
                                                St += L[x-1].substring(0,1);
                                                St += L[x].substring(1,2);
                                                St += L[x+1].substring(2,3);
                                                }
                                                out.print(St);
```

**Question 20** In the code segment to the right, what is the output of line 1?  **A)** 8 **B)** 7 **C)** 0 **D)** 10 **E)** 9 public class Alpha { private int A; public Alpha(int AA) { A = AA; } public int getA() { return A + 1; } } public class Beta extends Alpha { private int A; public Beta(int AA) { super(AA + 5); } public int getA() { return A; } } ////////////////////////////////// // Client code Alpha Amp = new Alpha(7); Beta Bob = new Beta(10); Alpha Art = new Alpha(Amp.getA()); System.out.println(Amp.getA()); // Line 1 System.out.println(Bob.getA()); // Line 2 System.out.println(Art.getA()); // Line 3 **Question 21** In the code segment to the right, what is the output of line 2?  **A)** 8 **B)** 7 **C)** 0 **D)** 10 **E)** 9 **Question 22** In the code segment to the right, what is the output of line 3?  **A)** 8 **B)** 7 **C)** 0 **D)** 10 **E)** 9 **Question 23** What is the output of the code segment shown on the right?  **A)** 1 **B)** 16 **C)** 31 **D)** 32 **E)** 63 out.print(31 ^ 32); **Question 24** What is the output of the code segment shown on the right?  **A)** 64 **B)** 32 **C)** 0 **D)** -32 **E)** -64 out.print('E' - 'T' + 't' - 'e'); **Question 25** In the code segment to the right, what is the output of line 1?  **A)** 1 **B)** 2 **C)** 4 **D)** 7 **E)** 9 PriorityQueue<Integer>PQ; PQ = new PriorityQueue();

#### **Question 26**

In the code segment to the right, what is the output of line 2?

- **A)** 1 **B)** 2 **C)** 4 **D)** 7 **E)** 9
- int[]List = {5,1,2,9,2,6,7,4,1,7}; for(int x=0; x<List.length; x++) PQ.add(List[x]);
- out.println(PQ.remove()); // line #1 PQ.remove(); out.println(PQ.peek()); // line #2

# out.println(PQ); // line #3 **Question <sup>27</sup>**

In the code segment to the right, what is the output of line 3?

- **A)** [2, 9, 2, 6, 7, 4, 1, 7]
- **B)** [2, 2, 4, 5, 6, 7, 7, 9]
- **C)** [9, 7, 7, 6, 5, 4, 2, 2]
- **D)** [2, 4, 2, 7, 5, 6, 7, 9]
- **E)** [4, 5, 6, 7, 7, 9]

#### **Question 28**

In the code to the right, what is output on line #1?

- **A)** E **B)** N **C)** M **D)** C **E)** S

### **Question 29**

In the code to the right, what is output on line #2?

- **A)** E **B)** N **C)** M **D)** C **E)** S

#### **Question 30**

In the code to the right, what is output on line #3?

- **A)** 6 **B)** 5 **C)** 4 **D)** 3 **E)** 2

Stack<Character>Bunch;

Bunch = new Stack<Character>();

String St = "COMPUTERSCIENCE"; for (int x=0; x<St.length(); x++) if(!Bunch.contains(St.charAt(x))) Bunch.push(St.charAt(x));

System.out.print(Bunch.peek()); //Line 1 for (int x=1; x<=8; x++) Bunch.pop(); System.out.print(Bunch.pop()); //Line 2

System.out.print(Bunch.size()); //Line 3

### **Question 31**

Solve the problem stated to the right.

- **A)** 16 seconds
- **B)** 32 seconds
- **C)** 64 seconds
- **D)** 409 seconds
- **E)** 1024 seconds

 **The Big O Notation for a sorting routine is O(n \* log2n). When we sort a list of 10,000 elements, the process takes 0.4 seconds. How long do we predict the same sort will work on a list of 320,000 numbers?**

```
Question 32
 In the code to the right, what is output by line #1? 
 A) 20
 B) 40
 C) 25
 D) 30
 E) 10
                                                 TreeMap<Integer,Integer>Oak;
                                                 Oak= new TreeMap<Integer,Integer>();
                                                 for (int x=1; x<=10; x++)
                                                 Oak.put(x,x*2);
                                                 for (int y=10; y>=1; y-=2)
                                                 for (int x=20;x<=21;x++)
                                                 Oak.put(y,x);
                                                 out.println(Oak.size()); // Line #1 
                                                 out.println(Oak.get(10)); // Line #2
                                                 out.println(Oak.get(3)); // Line #3
Question 33
 In the code to the right, what is output by line #2?
 A) 10
 B) 5
 C) 20
 D) 21
 E) 6
Question 34
 In the code to the right, what is output by line #3?
 A) 7
 B) 21
 C) 20
 D) 3
 E) 6
Question 35
What is the output of the code segment shown on the right?
 A) 1 B) 4 C) 5 D) 6 E) 10

                                                 int[][]BP = new int[8][8];
                                                 BP[1][1] = 1;
                                                 for (int y = 2; y<=7; y++)
                                                 for (int x = 1; x<=7; x++)
                                                 BP[y][x]= BP[y-1][x]+BP[y-1][x-1];
                                                 out.print(BP[6][5]);
Question 36
What is the output of the code segment shown on the right?
 A) 7 B) 8 C) 24 D) 22 E) 23

                                                 int A = 16;
                                                 A += Math.sqrt(A-1);
                                                 A += Math.sqrt(A+1);
                                                 out.print(A);
Question 37
 What is the output of the code segment shown on the right?
 A) 1
 B) 2
 C) 3 
 D) 4
 E) 5
                                                 int C=0; 
                                                 String A = "R2-D2";
                                                 if(A.matches(".....")) C++;
                                                 if(A.matches(".2.2")) C++;
                                                 if(A.matches("[A-T]*")) C++;
                                                 if(A.matches("2.*")) C++;
                                                 if(A.matches(".*2")) C++;
                                                 if(A.matches(".*[0-9].*[0-9]")) C++;

                                                 out.print(C);
```

#### **Question 38** What is the output of the code segment shown on the right? **A)** ABCDE **B)** EDCBA **C)** ABCDEEDCBA **D)** ABCDEDCBA **E)** AABBCCDDEE String One = "ABCDE"; String Two = ""; for(int x=0; x<One.length(); x++) Two = One.substring(x,x+1) + Two; out.print(Two); **Question 39** There are 16 different combinations of A, B, C, and D in the code on the right. How many combinations would result in the value "true" being printed? boolean A = ???; boolean B = ???; boolean C = ???; boolean D = ???; out.print(A && B ^ C || D); **Question 40** Consider a binary tree with 1023 nodes. What is the greatest number of leaves that the tree could contain?

![](_page_7_Picture_0.jpeg)

# **UIL COMPUTER SCIENCE – 2023 REGION**

Questions (+6 points for each correct answer, -2 points for each incorrect answer)

| 1) D |  |
|------|--|
|------|--|

2) A

3) B

4) C

5) B

6) B

7) D

8) D

9) A

10) D

11) D

12) C

13) B

14) E

15) A

16) B

17) A

18) C

20) A

19) E

21) C

22) E

23) E

24) C

25) A

26) B

27) D

28) B

29) C

30) E

31) C

32) E

33) D

34) E

35) C

36) E

37) C

38) B

\*39) 10

\*40) 512

Note: Correct responses are based on Java SE Development Kit 17 (JDK 17) from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 17 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.

## **Explanations:**

| 1.  | D | Convert the 4 powers-of-two numbers to base 16.<br>101101012 = 1011 01012<br>which is B516      |
|-----|---|-------------------------------------------------------------------------------------------------|
|     |   | 23114 = 10 11 01 012 = 1011 01012 which also is B516                                            |
|     |   | 2658 = 010 110 1012 = 1011 01012 which also is B516                                             |
|     |   | Well, B516<br>is B516                                                                           |
|     |   | B516<br>= 11*16 + 5*1 = 18110                                                                   |
|     |   | So, the odd one out is 18310                                                                    |
| 2.  | A | Use order of operations.                                                                        |
|     |   | 800 / 3<br>% 10 + 800 / 10 % 3<br>266 % 10<br>+ 800 / 10 % 3                                    |
|     |   | 6 + 800 / 10<br>% 3                                                                             |
|     |   | 6 + 80 % 3                                                                                      |
|     |   | 6 + 2 = 8                                                                                       |
| 3.  | B | You will be printing 12.12121212 and 12 with the format defined by String St.                   |
|     |   | \\<br>gives us one \                                                                            |
|     |   | %.12f prints the double with 12 decimal places.<br>That gives us 12.121212120000                |
|     |   | \\\\<br>produces \\                                                                             |
|     |   | \n provides a new line.                                                                         |
|     |   | nn gives us, well nn                                                                            |
|     |   | %d formats 12                                                                                   |
|     |   | Thus…                                                                                           |
|     |   | \12.121212120000\\                                                                              |
| 4.  | C | nn12<br>Go = "ComputerScience"                                                                  |
|     |   | Fight = "uterScience"                                                                           |
|     |   | Win = "Science"                                                                                 |
|     |   | It prints "cie"                                                                                 |
| 5.  | B | R = true (!false)                                                                               |
|     |   | S = true (true    false)                                                                        |
|     |   | T = true (true && true)                                                                         |
|     |   | U = false (true ^ true)                                                                         |
| 6.  | B | M = 8.94                                                                                        |
|     |   | M*M*M will be a number greater than 512 but less than 729                                       |
|     |   | So the cube root is greater than 8 but less than 9.                                             |
| 7.  | D | (int) casts the number to 8<br>U = 40 (240%100)                                                 |
|     |   | I = 15 (40 % 25)                                                                                |
|     |   | L = 5 (15 % 10)                                                                                 |
|     |   | 40+15+5 = 60                                                                                    |
| 8.  | D | D=10 R=2 P=4                                                                                    |
|     |   | P becomes 10 since 10+2>4                                                                       |
|     |   | R becomes 10 since 10+10>2                                                                      |
|     |   | D becomes 11 since 10+10>10                                                                     |
| 9.  | A | It prints 11 10 10<br>The loop goes through the values 1, 2, and 5 before 14 stops the process. |
|     |   | Since St is a String, the values are concatenated onto the St producing "125"                   |
| 10. | D | perfect[10] is 99 (10*10-1)                                                                     |
|     |   | perfect[8] is 63 (8*8-1)                                                                        |
|     |   | 99-63 = 36                                                                                      |
| 11. | D | "Z 2 X 4 C 6 V 8 B 10"                                                                          |
|     |   | The loop iterates 4 times.                                                                      |
|     |   | Each time, it reads the String first and does nothing with it.                                  |
|     |   | It then reads the integer and adds it to Hello<br>2+4+6+8 = 20                                  |
|     |   |                                                                                                 |
|     |   |                                                                                                 |

| 12. | C | This divides 100 by 2 to get 50<br>Then it divides 50 by 3 to get 16<br>Then it divides 16 by 4 to get 4                                                                                                                                                                                                                                                                                                           |
|-----|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 13. | B | Follow the order of precedence…<br>Q<br><< 2 + 2 ^ 3 >> 1<br>20 << 2 + 2<br>^ 3 >> 1<br>20 << 4<br>^ 3 >> 1<br>320 ^ 3 >> 1<br>320 ^ 1 = 101000000 ^ 000000001 = 101000001 = 321                                                                                                                                                                                                                                   |
| 14. | E | Byte.MAX_VALUE = 127<br>Byte.SIZE = 8<br>127/8 = 15                                                                                                                                                                                                                                                                                                                                                                |
| 15. | A | After the first loop, keys begins<br>with [10,20,30,40,50,60,70,80,90,100]<br>In the second loop, we begin at position 1 and delete items that are evenly divisible by 10 (all of<br>the numbers in the list are evenly divisible by 10).<br>But, when we delete the 20, the items move back one position, so<br>we miss the 20 and delete<br>the 30 on the next step. This process continues.<br>[10,30,50,70,90] |
| 16. | B | In the loop, x begins at 1 and does 12 iterations reaching 12.<br>As x does its work, y starts at -5 and does the same 12 iterations stopping at 6.<br>The final printed z is the final x*y = 72                                                                                                                                                                                                                   |
| 17. | A | A counts the multiples of 5 in the range [1,100] which is 20.<br>B counts the multiples of 2 in the range [1,100] which is 50.<br>C counts the multiples of 10 in the range [1,100] which is 10.<br>20+50-10 = 60                                                                                                                                                                                                  |
| 18. | C | 1/6 = 0<br>64 to the 0 power is 1.<br>Math.pow() returns a double.<br>The answer is 1.0                                                                                                                                                                                                                                                                                                                            |
| 19. | E | In the first iteration of the loop,<br>St = "B" St = "BE" St = "BEM"<br>In the next iteration of the loop,<br>St = "BEMJ" St = "BEMJA" St = "BEMJAM"<br>In the next iteration of the loop,<br>St = "BEMJAMS" St = "BEMJAMSA" St = "BEMJAMSAL"                                                                                                                                                                      |
| 20. | A | Amp's A attribute is equal to 7.<br>Alpha's getA() returns A+1<br>8                                                                                                                                                                                                                                                                                                                                                |
| 21. | C | Bob's A attribute never changes from the default zero.<br>When the constructor is called, it sends the argument 15 up to Alpha and its constructor.<br>So, when we call Bob.getA() it returns a 0.                                                                                                                                                                                                                 |
| 22. | E | Art takes Amp.getA() which is 8, and sends it to the constructor to be used.<br>Art's A attribute is indeed 8, but Alpha's getA() returns A+1.<br>9                                                                                                                                                                                                                                                                |
| 23. | E | 31 ^ 32<br>011111 ^ 100000 = 111111 = 63 in base 10                                                                                                                                                                                                                                                                                                                                                                |
| 24. | C | If you know your ASCII values for the letters ('A' is 65 and 'a' is 97) you can do the arithmetic,<br>but…<br>The difference between 'E' and 'T' will be the same as 't' and 'e' with one being positive and the<br>other<br>negative.<br>So, the answer is 0.                                                                                                                                                     |
| 25. | A | A PriorityQueue is a Min-Heap, so when the first item is removed, it will be the smallest value in<br>the list.<br>That value is 1                                                                                                                                                                                                                                                                                 |
| 26. | B | Two items are removed from the Priority Queue.<br>So, the two 1's are gone.<br>When we peek(), we see the new smallest item, 2.                                                                                                                                                                                                                                                                                    |

| 27.<br>D | After two removals, we now want to see what the list looks like.                                    |
|----------|-----------------------------------------------------------------------------------------------------|
|          | It is important to learn the algorithm used when deleting from a Priority Queue.                    |
|          | Here is the evolution of the list.                                                                  |
|          | [1, 1, 2, 2, 5, 6, 7, 9, 4, 7] -<br>This is the original Priority Queue.                            |
|          | [1, 2, 2, 4, 5, 6, 7, 9, 7]<br>-<br>The Priority Queue after the first item is removed              |
|          | [2, 4, 2, 7, 5, 6, 7, 9]<br>-<br>The Priority Queue after the second item is removed                |
|          | But in desperation, there are ways to narrow it down.                                               |
|          | The first element must be the smallest, so C and E are out.                                         |
|          | Choice A would be nearly impossible, because at this point the largest value, 9, should not be      |
|          | on row one of the tree.                                                                             |
|          | Choice B is possible, but very unlikely, since the<br>list of 8 items is sorted.                    |
|          | D is the answer and would have been the best guess.                                                 |
|          | But, learn the algorithm. It is very cool and will take you only ten minutes of practice.           |
| 28.<br>B | In this problem, the only letters allowed to be pushed on the Stack are items not already on the    |
|          | Stack. It allows no duplicates.                                                                     |
|          | So, the initial Stack from bottom to top is: C O M P U T E R S I N.                                 |
|          | When we peek(), we see the N.                                                                       |
| 29.<br>C | The Stack is C O M P U T E R S I N                                                                  |
|          | The loop pops the 8 items on the top, leaving us with C O M.                                        |
|          | When we pop() the next item, it is M.                                                               |
| 30.<br>E | After all of this, the Stack is C O.                                                                |
|          | The size() is 2                                                                                     |
| 31.<br>C | O(n * log2n)                                                                                        |
|          | This is the Big O notation for routines like the Quick Sort.                                        |
|          | It generally involves routines where there is a linear iteration and within it a process of cutting |
|          | things in half.                                                                                     |
|          | In this problem, we must have to do the arithmetic.                                                 |
| n = 32   |                                                                                                     |
|          | This is determined by seeing how many times larger the second list is than the original list.       |
|          | Plugging into th formula: 32 * log232                                                               |
|          |                                                                                                     |
|          | log232 = 5                                                                                          |
|          | 32 * log232 = 160                                                                                   |
|          | Now take 160 times the original time 0.4 and we get 64.                                             |
| 32.<br>E | The first loop creates the following relationships.                                                 |
| 1 -> 2   |                                                                                                     |
| 2 -> 4   |                                                                                                     |
| 3 -> 6   |                                                                                                     |
| 4 -> 8   |                                                                                                     |
| 5 -> 10  |                                                                                                     |
| 6 -> 12  |                                                                                                     |
| 7 -> 14  |                                                                                                     |
| 8 -> 16  |                                                                                                     |
| 9 -> 18  |                                                                                                     |
| 10 -> 20 |                                                                                                     |
|          | The nested loops reassign 10 of the mappings first to values of 20, then to values of 21.           |
| 1 -> 2   |                                                                                                     |
| 2 -> 21  |                                                                                                     |
| 3 -> 6   |                                                                                                     |
| 4 -> 21  |                                                                                                     |
| 5 -> 10  |                                                                                                     |
| 6 -> 21  |                                                                                                     |
| 7 -> 14  |                                                                                                     |
| 8 -> 21  |                                                                                                     |
|          |                                                                                                     |
| 9 -> 18  |                                                                                                     |
| 10 -> 21 |                                                                                                     |
|          | The size is 10                                                                                      |
| 33.<br>D | Looking at the explanation of #32, Oak.get(10) = 21                                                 |
| 34.<br>E | Looking at the explanation of #32, Oak.get(3) = 6                                                   |

| 35. | C   | This algorithm generates the values of Pascal's triangle.<br>Formatting would print a prettier picture, but we are focusing on Row 6<br>0 0 0 0 0 0 0 0<br>0 1 0 0 0 0 0 0<br>0 1 1 0 0 0 0 0<br>0 1 2 1 0 0 0 0<br>0 1 3 3 1 0 0 0<br>0 1 4 6 4 1 0 0<br>0 1 5 10 10 5 1 0<br>0 1 6 15 20 15 6 1<br>Row 6<br>0 1 5 10 10 5 1 0<br>We want element 5 in that row = 5                                                                                                                                                                                                                |  |
|-----|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 36. | E   | A = 16<br>Math.sqrt(15) is a little less than 4.<br>=+ type casts the expression on the right.<br>We add 3 to A making it 19.<br>Math.sqrt(20) is more than 4, but less than 5<br>Again with the type casting.<br>We add 4 more to A to give us 23.                                                                                                                                                                                                                                                                                                                                 |  |
| 37. | C   | The 1st, 5th, and 6th if statements evaluate to true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |
| 38. | B   | This is a classic method of reversing a String.<br>Two = Two + One.substring(x,x+1) would produce the original String.<br>But, reversing the two expressions on the right gives us a reversal.<br>Two = One.substring(x,x+1) + Two                                                                                                                                                                                                                                                                                                                                                  |  |
| 39. | 10  | Here is the truth table for the problem:<br>The order of operations will be ^ &&   <br>0000 = 0<br>0001 = 1<br>0010 = 0<br>0011 = 1<br>0100 = 0<br>0101 = 1<br>0110 = 0<br>0111 = 1<br>1000 = 0<br>1001 = 1<br>1010 = 1<br>1011 = 1<br>1100 = 1<br>1101 = 1<br>1110 = 0<br>1111 = 1<br>If D is true, the expression is true because of the placement of the "or."<br>That gives us 8 answers.<br>If D is false, the expression is true if A is true and B and C are opposites.<br>That gives us 1010 and 1100.<br>So, there are 10 combinations that will make the expression true. |  |
| 40. | 512 | The perfect scenario for most leaves (leafs?) would be a perfectly balanced 10 level binary tree<br>with 511 interior nodes and 512 nodes on the bottommost level. All 512 would be leaves.                                                                                                                                                                                                                                                                                                                                                                                         |  |