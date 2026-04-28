# **UIL COMPUTER SCIENCE WRITTEN TEST – 2023 INVITATIONAL B**

**Note:** Correct responses are based on **Java SE Development Kit 17 (JDK 17)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 17 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

| Question 1i                                       |                                                                              |                 |                                                                                        |           |
|---------------------------------------------------|------------------------------------------------------------------------------|-----------------|----------------------------------------------------------------------------------------|-----------|
| What is the sum of 100101112<br>A)<br>141016      | and 101000112?<br>B) DA16                                                    | C) 13A16        | D) 19A16                                                                               | E) 131016 |
| Question 2uesti                                   |                                                                              |                 |                                                                                        |           |
|                                                   | What is the output of the code segment to the right?                         |                 | out.print(1 + 29 % 10 / 4 + 3);                                                        |           |
| A) 3<br>4<br>B)                                   | C) 5<br>D) 6                                                                 | E) 6.25         |                                                                                        |           |
| Question 3                                        |                                                                              |                 |                                                                                        |           |
| A) Blue<br>Red<br>GreenYellow<br>PurpleOrange     | What is the output of the code segment to the right?                         |                 |                                                                                        |           |
| B) Blue<br>Red<br>Green<br>Yellow<br>PurpleOrange |                                                                              |                 | out.print("Blue\nRed\nGreen");<br>out.print("Yellow\nPurple");<br>out.print("Orange"); |           |
| C) Blue<br>Red<br>Green<br>YellowPurple<br>Orange |                                                                              |                 |                                                                                        |           |
| D) BlueRed                                        | GreenYellowPurpleOrange                                                      |                 |                                                                                        |           |
| E) Blue<br>Red<br>GreenYellowPurple<br>Orange     |                                                                              |                 |                                                                                        |           |
| Question 4<br>A) 1<br>2<br>B)                     | What is the output of the code segment to the right?<br>C) 7<br>D) 8         | E) 9            | String str = "Scholastic";<br>out.print(str.indexOf("c",2));                           |           |
| Question 5<br>A) true<br>B) false                 | What is the output of the code segment to the right?                         |                 | boolean A = true;<br>boolean B = !A;<br>out.print(!A && (A    B) ^ B);                 |           |
| Question 6<br>5<br>A)<br>B)                       | What is the output of the code segment to the right?<br>5.0<br>6<br>C)<br>D) | 6.0<br>15<br>E) | double M = Math.sqrt(31);<br>out.print((int)Math.floor(M));                            |           |

```
Question 7
 What is the output of the code segment to the right? 
 A) 6.4 B) 3.2 C) 6.2 D) 6.0 E) 6
                                                double T = 2.2;
                                                double A = 8 * 4 / 10 + 1 + T ;
                                                out.print(A);
Question 8
 What is the output of the code segment to the right?
 A) B
 B) BCDEF
 C) BCDEFG
 D) F
 E) FG
                                                int Q = 20 % 7;
                                                switch (Q)
                                                {
                                                case 1:out.print("A");
                                                case 2:out.print("B");
                                                case 3:out.print("C");
                                                case 4:out.print("D");
                                                case 5:out.print("E");
                                                case 6:out.print("F");
                                                default:out.print("G"); 
                                                }
Question 9
 How many x's will be output of the code segment to the right?
 A) 4
 B) 5
 C) 6
 D) 7
 E) 12
                                                 for(int x = 50; x > 2; x = x / 2 + 1)
                                                out.print("x");
Question 10
 What is the output of the code segment to the right? 
 A) 49 B) 45 C) 41 D) 40 E) 36
                                                int[] four = {4,8,12,16,20,24,28};
                                                int[] five = {5,10,15,20,25,30,35};
                                                if (four.length<five.length)
                                                out.print(four[4]+five[5]);
                                                else
                                                out.print(four[5]+five[4]);
Question 11 
 What is output by the code segment to the right?
 A) 3684
 B) 12243648
 C) 361224
 D) 363648
 E) 3636
                                                String St = "12 24 36 48";
                                                Scanner go = new Scanner(St);
                                                out.print(go.nextInt() + go.nextInt());
                                                out.print(go.next() + go.next());
Question 12
 What is the output of the code segment to the right? 
 A) 113 B) 123 C) 73 D) 197 E) 63
                                                int sum = 0;
                                                for(int x = 1; x <= 50; x = x * 2 )
                                                     sum += x + 10;
                                                out.print(sum);
Question 13
 What is the output of the code segment to the right? 
 A) 11 B) 12 C) 13 D) 14 E) 15
                                                int a = 15, b = 12, c = 9 ;
                                                out.print(c ^ b | a - c & b ^ a);
Question 14
 What is the output of the code segment shown on the right?
 A) 0 B) 1 C) -1 D) 127 E) -129
                                                 out.println(Byte.MIN_VALUE + 127);
```

```
Question 15
 What is output by the code segment to the right?
 A) [12, 10, 14, 16, 10]
 B) [10, 12, 10, 14, 16, 10] 
 C) [12, 12, 14, 16, 10]
 D) [10, 12, 12, 14, 16, 10]
 E) [10, 12, 14, 16, 10]
                                               ArrayList<Integer> messi;
                                               messi = new ArrayList<Integer>();
                                               messi.add(10);
                                               messi.add(12);
                                               messi.add(messi.get(1));
                                               messi.add(14);
                                               messi.remove(0);
                                               messi.add(16);
                                               messi.add(10);
                                               messi.add(0,messi.get(0)-2);
                                               out.println(messi);
Question 16
 What is the output of the code segment shown on the right?
 A) GJ B) IJ C) JB D) DE E) ED
                                               String D = "ABCDEFGHIJ";
                                               for(int x=1; x<=4; x++)
                                               D = D.substring(3)+D.substring(0,1);
                                               out.println(D);
Question 17
 What is the output of the code segment shown on the right?
 A) 169 B) 144 C) 121 D) 100 E) 81
                                              ArrayList<Integer>T;
                                              T = new ArrayList<Integer>();
                                              T.add(3);
                                              T.add(5);
                                              for (int x=2;x<=100;x++)
                                              {
                                              int N = T.get(x-2) + T.get(x-1);
                                              T.add(N);
                                              }
                                              out.print(T.get(8));
Question 18
 What is the output of the code segment shown on the right?
 A) 3 B) 6 C) 9 D) 12 E) 14
                                              String St = "";
                                              for(char ch = 'A'; ch<='C'; ch++)
                                              St += ch + St + ch;
                                              out.print(St.length()); 
Question 19
 What is the output of the code segment shown on the right?
 A) 3 B) 4 C) 5 D) 6 E) 7
                                              int[] G = {5,1,2,9,2,6,7,4,1,7};
                                              for(int x=1; x<=8; x++)
                                              G[x] = (G[x-1] + G[x+1])/2;
                                              out.println(G[5]);
```

```
Question 20
 In the code segment to the right, what is the output of line 1?
 A) 0 B) 1 C) 2 D) 3 E) 4
                                               int[]cool = {17,19,12,8,3};
                                               int[]list = new int[cool.length];
                                               for(int x=0;x<cool.length;x++)
                                                for(int y=x+1;y<cool.length;y++)
                                                if(cool[x]>=cool[y])
                                                list[x]++;
                                                else
                                                list[y]++;
                                               out.print(list[0]); //line 1
                                               out.print(list[4]); //line 2
Question 21
In the code segment to the right, what is the output of line 2?
 A) 0 B) 1 C) 2 D) 3 E) 4
Question 22
In the code segment to the right, if the first line:
int[]cool = {17,19,12,8,3}
was changed to 
int[]cool = {17,19,12,8,3,1,22,11,5,6}
What would be the final value of list[0]?
 A) 1 
 B) 3
 C) 5
 D) 7
 E) 9
Question 23
What is the output of the code segment shown on the right?
 A) CAB B) BAC C) 6 D) 216 E) 198
                                               String St = "CAB";
                                               int N = St.charAt(2);
                                               N += St.charAt(1);
                                               N += St.charAt(0);
                                               out.print(N);
Question 24
In the code on the right, how many *s will be printed?
 A) 770
 B) 28
 C) 800
 D) 700
 E) 880
                                               for(int A = 1; A <= 10; A++)
                                               for(int B = -5; B <= 5; B++) 
                                               for(int C = 8; C > 1; C--)
                                               out.print("*");
Question 25
What is returned by the method call Yes(5,2)
 A) 2 B) 5 C) 7 D) 10 E) 6 public static int Yes(int x, int y)
                                                {
                                                if (x>y)
                                                return x * y;
                                                if (x == y)
                                                return Yes(x+y,y+1);
                                                else
                                                return Yes(x+1,y-1) + 2;
                                                }
Question 26
 What is returned by the method call Yes(3,3)
 A) 9 B) 24 C) 6 D) 12 E) 18
Question 27
What is returned by the method call Yes(0,7)
 A) 20 B) 24 C) 26 D) 28 E) 30
```

#### **Question 28**

In the code to the right, what is output on line #1?

- **A)** 10 **B)** 12 **C)** 14 **D)** 16 **E)** 18

#### **Question 29**

In the code to the right, what is output on line #2?

- **A)** 10
- **B)** 12
- **C)** 14
- **D)** 16
- **E)** 18

#### **Question 30**

In the code to the right, what is output on line #3?

- **A)** [16, 18]
- **B)** [18, 12]
- **C)** [12, 16]
- **D)** [18, 14]
- **E)** [18, 16]

```
TreeMap<Character,Integer> Cup;
 Cup = new TreeMap<Character,Integer>();
 Stack<Integer> Bowl;
 Bowl = new Stack<Integer>();
 Cup.put('D',18);
 Cup.put('A',12);
 Cup.put('C',14);
 Cup.put('B',10);
 Cup.put('C',16);
 char x;
 for(x='D';x>='A';x--)
 Bowl.push(Cup.get(x));
 out.println(Bowl.pop()); // Line 1
 Bowl.pop();
 out.println(Cup.get('C'));// Line 2
```

out.println(Bowl); // Line 3

#### **Question 31**

What is the output of the code segment shown on the right?

- **A)** false false
- **B)** false true
- **C)** true false
- **D)** true true
- **E)** no output there is a compile error

```
 boolean A = false;
 boolean B = true;
 for (int x = 1; x<=12; x++)
 if(x*x%2==0)
 A = B;
 else
 B = !B;
 out.println(A + " " + B);
```

### **Question 32**

In the code to the right, what is output by line #1?

- **A)** 5
- **B)** 6
- **C)** 12
- **D)** 14
- **E)** 16

### **Question 33**

In the code to the right, what is output by line #2?

- **A)** 12
- **B)** 24
- **C)** 28
- **D)** 36
- **E)** 42

#### **Question 34**

In the code to the right, what is output by line #3?

- **A)** 20
- **B)** 40
- **C)** 54
- **D)** 60
- **E)** 72

```
public class Soccer
 {
 private int A;
 private int B;
 private int C;
 public Soccer(int x, int y, int z)
 {
 A = x;
 B = y;
 C = z;
 }
 public Soccer(int x, int y)
 {
 this(y, x, x+y); 
 }
 public Soccer(int x)
 {
 this(x, 2*x); 
 }
 public Soccer()
 {
 this(10); 
 }
 public int primetime()
 {
 return A+B+C;
 }
 }
 //client code
 Soccer R = new Soccer(1,2,3);
 out.println(R.primetime()); // #1 
 Soccer S = new Soccer(4,8);
 out.println(S.primetime()); // #2
 Soccer T = new Soccer();
 out.println(T.primetime()); // #3
```

| Question 35<br>What is the output of the code segment shown on the right?<br>0<br>1<br>7<br>17<br>64<br>A)<br>B)<br>C)<br>D)<br>E)   | int B = 127;<br>B = B >> 5;                                   |  |  |  |
|--------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|--|--|--|
|                                                                                                                                      | B = B << 4;                                                   |  |  |  |
|                                                                                                                                      | B = B + 8;                                                    |  |  |  |
|                                                                                                                                      | B = B >> 3;                                                   |  |  |  |
|                                                                                                                                      | out.println(B);                                               |  |  |  |
| Question 36                                                                                                                          |                                                               |  |  |  |
| What is the output of the code segment shown on the right?                                                                           | String St = "UNIVERSITY";                                     |  |  |  |
| UNI<br>NIV<br>NI<br>SIT<br>SI<br>A)<br>B)<br>C)<br>D)<br>E)                                                                          | int L = St.indexOf("I");<br>out.print(St.substring(L-1,L+1)); |  |  |  |
|                                                                                                                                      |                                                               |  |  |  |
| Question 37                                                                                                                          |                                                               |  |  |  |
| What is the output of the code segment shown on the right?                                                                           | int[]Pogo = {22,33,11,66,44};                                 |  |  |  |
| 44 66 11 33 22<br>A)                                                                                                                 | int x = 10;                                                   |  |  |  |
| B)<br>44 44 44 44 44                                                                                                                 | int y = 4;                                                    |  |  |  |
| 22 22 22 22 22<br>C)                                                                                                                 | for(x = 0;x<=4;x++)<br>{                                      |  |  |  |
| 22 33 11 66 44<br>D)                                                                                                                 | Pogo[x]=Pogo[y];                                              |  |  |  |
| 44 66 11 66 44<br>E)                                                                                                                 | Pogo[y]=Pogo[x];                                              |  |  |  |
|                                                                                                                                      | y;                                                            |  |  |  |
|                                                                                                                                      | }                                                             |  |  |  |
|                                                                                                                                      | for(int i = 0; i<=4; i++)                                     |  |  |  |
|                                                                                                                                      | out.print(Pogo[i]+" ");                                       |  |  |  |
|                                                                                                                                      |                                                               |  |  |  |
| Question 38                                                                                                                          | int A = 50;                                                   |  |  |  |
| What is the output of the code segment shown on the right?                                                                           | int B = 65;                                                   |  |  |  |
| 5<br>50<br>65<br>500<br>650<br>A)<br>B)<br>C)<br>D)<br>E)                                                                            | int F = -1;                                                   |  |  |  |
|                                                                                                                                      | for (int x=1; x<=A; x++)                                      |  |  |  |
|                                                                                                                                      | if(A%x==0 && B%x==0)                                          |  |  |  |
|                                                                                                                                      | F = x;                                                        |  |  |  |
|                                                                                                                                      | out.print(A * B / F);                                         |  |  |  |
| Question 39                                                                                                                          |                                                               |  |  |  |
| Evaluate the prefix expression to the right. Write your answer in                                                                    |                                                               |  |  |  |
| the answer blank for #39.                                                                                                            | + * / -<br>90 20 10 3 7                                       |  |  |  |
|                                                                                                                                      |                                                               |  |  |  |
| Question 40                                                                                                                          |                                                               |  |  |  |
| To the right, we have begun to list all the 6-digit binary numbers                                                                   | 000000, 000001, 000010, 000011                                |  |  |  |
| from 000000 to 111111. So far, we have listed only 8 of them. If<br>we were to list all 64 of these 6-digit binary numbers, how many |                                                               |  |  |  |
| 000100, 000101, 000110, 000111<br>"ones" would be written? So far, we have written 12 "ones"                                         |                                                               |  |  |  |
|                                                                                                                                      |                                                               |  |  |  |

![](_page_7_Picture_0.jpeg)

## **UIL COMPUTER SCIENCE – 2023 INVITATIONAL B**

Questions (+6 points for each correct answer, -2 points for each incorrect answer)

| 1)  | С | 11) | D | 21) | Α | 31)  | D   |
|-----|---|-----|---|-----|---|------|-----|
| 2)  | D | 12) | В | 22) | D | 32)  | В   |
| 3)  | Α | 13) | E | 23) | Е | 33)  | В   |
| 4)  | E | 14) | С | 24) | Α | 34)  | D   |
| 5)  | В | 15) | D | 25) | D | 35)  | С   |
| 6)  | A | 16) | Α | 26) | В | 36)  | С   |
| 7)  | С | 17) | В | 27) | А | 37)  | E   |
| 8)  | E | 18) | E | 28) | В | 38)  | E   |
| 9)  | С | 19) | D | 29) | D | *39) | 28  |
| 10) | A | 20) | D | 30) | E | *40) | 192 |

Note: Correct responses are based on Java SE Development Kit 17 (JDK 17) from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 17 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.

### **Explanations:**

| 1.  | C | Convert all to Base 16 and then add.                                                                                            |
|-----|---|---------------------------------------------------------------------------------------------------------------------------------|
|     |   | 100101112<br>= 9716                                                                                                             |
|     |   | 101000112<br>= A316                                                                                                             |
|     |   | 7 + 3 = 10 which would be an A                                                                                                  |
|     |   | 9 + A (10) = 19 which is 13 (3 carry the 1)                                                                                     |
|     |   | 9716<br>+ A316<br>= 13A16                                                                                                       |
| 2.  | D | Use order of operations.                                                                                                        |
|     |   | Perform integer modulus first.                                                                                                  |
|     |   | 1 + 29 % 10 / 4 + 3<br>1 + 9 / 4 + 3                                                                                            |
|     |   | Next do integer division.                                                                                                       |
|     |   | 1 + 2 + 3                                                                                                                       |
|     |   | Now add left to right.                                                                                                          |
|     |   | 1 + 2 + 3 = 6                                                                                                                   |
| 3.  | A | Since there are only print statements, new lines will only be invoked at the \n new line escape                                 |
| 4.  | E | character. So new lines will occur after Blue, Red, and Yellow<br>str.indexOf("c",2)                                            |
|     |   | This will find the position of "c" if you start looking at position 2. Therefore it "misses" the first                          |
|     |   | "c" and finds the "c" in position 9                                                                                             |
| 5.  | B | A is true. B is "not A" meaning B is false.                                                                                     |
|     |   | Now.                                                                                                                            |
|     |   | !A && (A    B) ^ B                                                                                                              |
|     |   | First, substitute all the values                                                                                                |
|     |   | !true && (true    false) ^ false                                                                                                |
|     |   | Next, evaluate !true                                                                                                            |
|     |   | false && (true    false) ^ false                                                                                                |
|     |   | Now, do the parenthesis                                                                                                         |
|     |   | false && true ^ false                                                                                                           |
|     |   | Next is "xor"                                                                                                                   |
|     |   | false && true<br>Using and                                                                                                      |
|     |   | false is the final answer                                                                                                       |
|     |   |                                                                                                                                 |
|     |   |                                                                                                                                 |
|     |   |                                                                                                                                 |
| 6.  | A | Math.sqrt(31) returns a value greater than 5.0 but less than 6.0                                                                |
|     |   | Math.floor() will round that value down to 5.0                                                                                  |
|     |   | (int) type casts that value as an integer 5                                                                                     |
| 7.  | C | Even though A is a double, the evaluation begins with integer operations.<br>8*4 is 32, then 32/10 is 3 using integer division. |
|     |   | Next add 1 (another integer) to get 4 before a double is finally introduced giving us 6.2                                       |
| 8.  | E | 20 % 7 is 6                                                                                                                     |
|     |   | So case "6" is invoked.                                                                                                         |
|     |   | Because there are no break statements, the output will begin with F and keep doing all the                                      |
|     |   | inputs through the end of the switch statement.                                                                                 |
| 9.  | C | x = x / 2 + 1<br>The values of x in the iterations would be:                                                                    |
|     |   | 50 26 14 8 5 3 then the value 2 would stop the process, but not print a 7th x.                                                  |
| 10. | A | The two arrays are the same length, so the else is invoked.                                                                     |
|     |   | Remember the first element in an array has an index of 0.                                                                       |
|     |   | four[5] is 24 five[4] is 25                                                                                                     |
|     |   | The sum is 49                                                                                                                   |
|     |   |                                                                                                                                 |
|     |   |                                                                                                                                 |

| 11. | D | St = "12 24 36 48";                                                                                                                     |  |  |  |
|-----|---|-----------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
|     |   | The Scanner go accesses the String St.<br>The first two go.nextInt() calls treat the inputs as integers and thus adds 12 + 24 to get 36 |  |  |  |
|     |   | The next two go.next() calls treat the inputs as Strings and thus adds "36"+"48" = "3648"                                               |  |  |  |
|     |   | So, we get 363648 as the output                                                                                                         |  |  |  |
| 12. | B | The loop itself runs through the values 1 2 4 8 16 32.                                                                                  |  |  |  |
|     |   | The accumulator adds these values one by one.                                                                                           |  |  |  |
|     |   | That gets a total of 63                                                                                                                 |  |  |  |
|     |   | But with every iteration, 10 more is added, for a total of 60.                                                                          |  |  |  |
|     |   | The output is 63 + 60 = 123                                                                                                             |  |  |  |
| 13. | E | a = 15, b = 12, c = 9 ;                                                                                                                 |  |  |  |
|     |   | a=1111 b=1100 c=1010                                                                                                                    |  |  |  |
|     |   | c ^ b   a -<br>c & b ^ a                                                                                                                |  |  |  |
|     |   | 9 ^ 12   15 -<br>9 & 12 ^ 15                                                                                                            |  |  |  |
|     |   | 9 ^ 12   15 -<br>9<br>& 12 ^ 15<br>(first, subtract)                                                                                    |  |  |  |
|     |   | 9 ^ 12   6 & 12 ^ 15<br>(now it is bit-wise time)                                                                                       |  |  |  |
|     |   | 1001 ^ 1100   0110 & 1100 ^ 1111                                                                                                        |  |  |  |
|     |   | 1001 ^ 1100   0110 & 1100<br>^ 1111 (do and)                                                                                            |  |  |  |
|     |   | 1001 ^ 1100   0100 ^ 1111                                                                                                               |  |  |  |
|     |   | 1001 ^ 1100<br>  0100 ^ 1111<br>(do leftmost xor)                                                                                       |  |  |  |
|     |   | 0101   0100 ^ 1111                                                                                                                      |  |  |  |
|     |   | 0101   0100 ^ 1111<br>(do other xor)                                                                                                    |  |  |  |
|     |   | 0101   1011<br>(finish with the or)                                                                                                     |  |  |  |
|     |   | 1111 = 15                                                                                                                               |  |  |  |
| 14. | C | Byte values range from -128 to 127                                                                                                      |  |  |  |
|     |   | Byte_MIN_VALUE = -128                                                                                                                   |  |  |  |
|     |   | -128 + 127 = -1                                                                                                                         |  |  |  |
| 15. | D | Here is the progression of messi.                                                                                                       |  |  |  |
|     |   | [ ]                                                                                                                                     |  |  |  |
|     |   | [10]                                                                                                                                    |  |  |  |
|     |   | [10,12]<br>[10,12,12]                                                                                                                   |  |  |  |
|     |   | [10,12,12,14]                                                                                                                           |  |  |  |
|     |   | [12,12,14]                                                                                                                              |  |  |  |
|     |   | [12,12,14,16]                                                                                                                           |  |  |  |
|     |   | [12,12,14,16,10]                                                                                                                        |  |  |  |
|     |   | [10,12,12,14,16,10]                                                                                                                     |  |  |  |
| 16. | A | In each iteration, the string loses the first three letters, but that first letter is saved as it moves to                              |  |  |  |
|     |   | the end.<br>There are 4 iterations.                                                                                                     |  |  |  |
|     |   | (0) ABCDEFGHIJ                                                                                                                          |  |  |  |
|     |   | (1) DEFGHIJA                                                                                                                            |  |  |  |
|     |   | (2) GHIJAD                                                                                                                              |  |  |  |
|     |   | (3) JADG                                                                                                                                |  |  |  |
|     |   | (4) GJ                                                                                                                                  |  |  |  |
| 17. | B | This is a Fibonacci algorithm starting with a 3 and a 5.                                                                                |  |  |  |
|     |   | Each new element is the sum of the previous two elements.<br>3 5 8 13 21 34 55 89 144 233 377                                           |  |  |  |
|     |   | The code prints element #8                                                                                                              |  |  |  |
| 18. | E | The loop iterates 3 times. For A, B, then C.                                                                                            |  |  |  |
|     |   | A: St becomes "AA"                                                                                                                      |  |  |  |
|     |   | B: St becomes AABAAB                                                                                                                    |  |  |  |
|     |   | C: St becomes AABAABCAABAABC                                                                                                            |  |  |  |
|     |   |                                                                                                                                         |  |  |  |
|     |   | The length is 14                                                                                                                        |  |  |  |
|     |   |                                                                                                                                         |  |  |  |
|     |   |                                                                                                                                         |  |  |  |

| 19. | D | [5,1,2,9,2,6,7,4,1,7] = original array                                                         |
|-----|---|------------------------------------------------------------------------------------------------|
|     |   | Loop goes from 1 to 8. Watch the array change.                                                 |
|     |   | 1 -<br>[5,3,2,9,2,6,7,4,1,7]                                                                   |
|     |   | 2 -<br>[5,3,6,9,2,6,7,4,1,7]                                                                   |
|     |   | 3 -<br>[5,3,6,4,2,6,7,4,1,7]                                                                   |
|     |   | 4 -<br>[5,3,6,4,5,6,7,4,1,7]                                                                   |
|     |   | 5 -<br>[5,3,6,4,5,6,7,4,1,7]                                                                   |
|     |   | 6 -<br>[5,3,6,4,5,6,5,4,1,7]                                                                   |
|     |   | 7 -<br>[5,3,6,4,5,6,5,3,1,7]                                                                   |
|     |   | 8 -<br>[5,3,6,4,5,6,5,3,5,7]                                                                   |
|     |   | Element #5 is a 6                                                                              |
| 20. | D | This is a portion of a sort routine called the "flag-tag" or "Supreme Court" sort.             |
|     |   | The elements in the list array represent the indices of the where each corresponding cool item |
|     |   | should be in a sorted array.                                                                   |
|     |   | 17 is greater than 3 other values in the cool: 12, 8, and 3                                    |
| 21. | A | 3 is greater than 0 other values in cool                                                       |
| 22. | D | 17 is larger than 7 items 12,8,3,1,11,5,6                                                      |
|     |   |                                                                                                |
| 23. | E | This adds the ASCII codes of 'A', 'B', and 'C'                                                 |
|     |   | It is nice to know that the ASCII Code for 'A" is 65 and 'a' is 97.                            |
|     |   | Here we add 65+66+67 = 198                                                                     |
| 24. | A | The A loop iterates 10 times.                                                                  |
|     |   | For each iteration of the A loop, the B loop iterates 11 times.                                |
|     |   | For each iteration of the B loop, the C loop iterates 7 times.                                 |
|     |   | 10 * 11 * 7 = 770                                                                              |
| 25. | D | Yes(5,2) goes straight to the stopping state condition.                                        |
|     |   | 5 * 2 = 10                                                                                     |
| 26. | B | Yes (3,3) first goes to the middle option.                                                     |
|     |   | Yes(3,3) = Yes(6,4)                                                                            |
|     |   | Yes(6,4) = 24                                                                                  |
| 27. | A | Yes(0,7) = Yes(1,6) + 2                                                                        |
|     |   | Yes(1,6) = Yes(2,5) + 2                                                                        |
|     |   | Yes(2,5) = Yes(3,4) + 2                                                                        |
|     |   | Yes(3,4) = Yes(4,3) + 2                                                                        |
|     |   | Yes(4,3) = 12                                                                                  |
|     |   | 12 + 2 + 2+ 2+ 2 = 20                                                                          |
| 28. | B | After the 5 Cup.put() lines, we have:                                                          |
|     |   | 'A' = 12 'B'=10 'C'=16 'D' = 18                                                                |
|     |   |                                                                                                |
|     |   | These are pushed onto the Bowl stack in reverse order with 18 being on the bottom.             |
|     |   | At this point the stack is [18,16,10,12]                                                       |
|     |   | The first pop removes the 12                                                                   |
| 29. | D | Continuing from #28                                                                            |
|     |   | Cup.get('C') gives us 16                                                                       |
| 30. | E | Continuing from #28                                                                            |
|     |   | Cup is now [18,16,10]                                                                          |
|     |   | 10 is popped.                                                                                  |
|     |   | Cup is now [18,16]                                                                             |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |
|     |   |                                                                                                |

| 31. | D | The loop will test the numbers 1,4,9,16,25,36,49,64,81,100,121,144          |
|-----|---|-----------------------------------------------------------------------------|
|     |   | Notice that the alternate from odd to even                                  |
|     |   | A = false, B=true.                                                          |
|     |   | if even, A takes on B's value                                               |
|     |   | if odd, B's value flips                                                     |
|     |   | 1 odd<br>-<br>now B=false                                                   |
|     |   | 4 even<br>-<br>now A=false                                                  |
|     |   | 9 odd<br>-<br>now B=true                                                    |
|     |   | 16 even<br>-<br>now A=true                                                  |
|     |   | 25 odd<br>-<br>now B=false                                                  |
|     |   | 36 even<br>-<br>now A=false                                                 |
|     |   | 49 odd<br>-<br>now B=true                                                   |
|     |   | 64 even<br>-<br>now A=true                                                  |
|     |   | 81 odd<br>-<br>now B=false                                                  |
|     |   | 100 even -<br>now A=false                                                   |
|     |   | 121 odd<br>-<br>now B=true                                                  |
|     |   | 144 even -<br>now A=true                                                    |
| 32. | B | R utilizes the 3-parameter constructor sending in 1,2,3                     |
|     |   | A=1 B=2 C=3 primetime returns 1+2+3 = 6                                     |
| 33. | B | S utilizes the 2-parameter constructor sending in 4,8                       |
|     |   | It then calls the 3-parameter constructor sending in 8,4,12                 |
|     |   | A=8 B=4 C=12 primetime returns 8+4+12 = 24                                  |
| 34. | D | T utilizes the 0-parameter constructor                                      |
|     |   | It then calls the 1-parameter constructor sending in 10                     |
|     |   | Then it calls the 2-parameter constructor sending in 10,20                  |
|     |   | It then calls the 3-parameter constructor sending in 20,10,30               |
|     |   | A=20 B=10 C=30 primetime returns 20+10+30 = 60                              |
| 35. | C | B = 127 (1111111)                                                           |
|     |   | Each right shift >>divides by 2 using integer division                      |
|     |   | Each left shift << multiplies by 2                                          |
|     |   | B >> 5 (right shift 5) divides 127/32 = 3 (11)                              |
|     |   | B<< 4 (left shift 4) multiples 3 * 16 = 48 (110000)                         |
|     |   | B + 8 Now add 8<br>48+8 = 56<br>(111000)                                    |
|     |   | B >>3 (right shift 3) divides by 8 56/8 = 7 (111)                           |
| 36. | C | St = "UNIVERSITY"                                                           |
|     |   | L will have a value of 2, the location of the first "I"                     |
|     |   | St.substring(1,3) is "NI"                                                   |
| 37. | E | The original values are [22,33,11,66,44]                                    |
|     |   | The loop iterates 5 times.                                                  |
|     |   | Pogo[0] becomes Pogo[4] [44,33,11,66,44]                                    |
|     |   | The next line has no effect Pogo[4] = Pogo[0] since they are already equal. |
|     |   | The second iteration makes Pogo[1] = Pogo[3]<br>[22,66,11,66,44]            |
|     |   | Again the next line has no effect.                                          |
|     |   | In fact, no other changes are made because:                                 |
|     |   | Pogo[2] = Pogo[2] causes no change.                                         |
|     |   | Pogo[3] = Pogo[1] causes no change.                                         |
|     |   | Pogo[4] = Pogo[0] causes no change.                                         |
| 38. | E | The loop is designed to find the greatest common factor of 50 and 65        |
|     |   | Thus F = 5                                                                  |
|     |   | Now doing 50 * 65 / 5 you get 650                                           |
|     |   | This is a good way to get the least common multiple since                   |
|     |   | A * B = GCF(A,B) * LCM(A,B)                                                 |
|     |   |                                                                             |
|     |   |                                                                             |
|     |   |                                                                             |
|     |   |                                                                             |
|     |   |                                                                             |
|     |   |                                                                             |
|     |   |                                                                             |
|     |   |                                                                             |

| 39. | 28  | + * / - 90 20 10 3 7<br>+ * / 70 10 3 7<br>+ * /<br>70 10 3 7<br>+ * 7 3 7<br>+ 21 7<br>28                                                                                                                 |
|-----|-----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 40. | 192 | If we listed all 64 binary numbers from 000000 to 111111, we would be listing 384 digits (64*6).<br>If it is a complete list, there would be half zeros and half ones.<br>Thus, we would have 192 of each. |