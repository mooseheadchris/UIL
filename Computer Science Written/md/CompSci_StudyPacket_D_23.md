# **UIL COMPUTER SCIENCE WRITTEN TEST – 2023 DISTRICT**

**Note:** Correct responses are based on **Java SE Development Kit 17 (JDK 17)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 17 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

| Question 1i                                          |                                                                    |
|------------------------------------------------------|--------------------------------------------------------------------|
| What is the product of 710<br>and 1010112?           |                                                                    |
| A) 4558<br>B) 5458<br>C) 5448                        | D) 4548<br>E) 4458                                                 |
| Question 2uesti                                      |                                                                    |
| What is the output of the code segment to the right? | out.print(35 % 12 / 4 + 27 * 2 % 4);                               |
| A)<br>B) 4<br>C) 5<br>D) 6<br>E) 56<br>8             |                                                                    |
| Question 3                                           |                                                                    |
| What is the output of the code segment to the right? |                                                                    |
| A) 5.6                                               |                                                                    |
| Five                                                 |                                                                    |
| SixSeven<br>Eight                                    |                                                                    |
|                                                      |                                                                    |
| B) 5.6Five                                           | double A = 5.678;                                                  |
| SixSeven                                             | out.printf("%.1f\n",A);                                            |
| Eight                                                | out.print("Five\nSix");                                            |
| C) 5.7Five                                           | out.println("Seven\nEight");                                       |
| SixSeven                                             |                                                                    |
| Eight                                                |                                                                    |
|                                                      |                                                                    |
| D) 5.7<br>Five                                       |                                                                    |
| SixSevenEight                                        |                                                                    |
|                                                      |                                                                    |
| E) 5.7                                               |                                                                    |
| Five                                                 |                                                                    |
| SixSeven<br>Eight                                    |                                                                    |
| Question 4                                           | String str = "University";                                         |
| What is the output of the code segment to the right? | String yes = str.substring(3,7);                                   |
| A) 0<br>B) 2<br>C) 3<br>D) 7<br>E) -1                | out.print(yes.indexOf("i"));                                       |
| Question 5                                           |                                                                    |
| What is the output of the code segment to the right? | boolean<br>A<br>=<br>!true;                                        |
| A) true                                              | boolean<br>B<br>=<br>!A;<br>boolean<br>C<br>=<br>A<br>&&<br>B;     |
|                                                      | out.print(A<br>^<br>B<br>^<br>C);                                  |
| B) false                                             |                                                                    |
| Question 6                                           |                                                                    |
| What is the output of the code segment to the right? | double H = Math.pow(5,2)-Math.pow(2,5);<br>out.print(Math.abs(H)); |
| A)<br>B)<br>C) -7<br>D)<br>E)<br>0<br>7<br>-7.0      | 7.0                                                                |

```
Question 7
What is the output of the code segment to the right?
A) 1 B) 1.0 C) 1.5 D) 1.75 E) 2.0
                                                 double U = 70 / 20;
                                                 double T = (U + U) / 4;
                                                 out.print(T);
Question 8
What is the output of the code segment to the right?
A) 3
B) 4
C) 5
D) 19
E) 25
                                                int T = 12;
                                                if (T > 10)
                                                    T = T - 3;
                                                if (T == 12)
                                                    T *= 2;
                                                else
                                                    T /= 2;
                                                if (T - 10 < 0)
                                                    T++;
                                                else
                                                    T--;
                                                out.print(T);
Question 9
What is the last number printed by the loop to the right?
A) 127
B) 128
C) 199
D) 200
E) 255
                                                  for(int x = 1; x < 200; x = x * 2 + 1)
                                                     out.println(x);
Question 10
What is the output of the code segment to the right?
A) 4 B) 7 C) 22 D) 25 E) 28
                                                  int[] ten = new int[10];
                                                  for(int x=0; x<10; x++)
                                                    ten[x] = x * 3 + 4;
                                                  out.print(ten[7]);
Question 11
What is output by the code segment to the right?
A) ABCDEFGH
B) BCGHJK
C) BCGHJKO
D) ADEFILMN
E) ADEFI
                                                String St = "A BC DEF GH I JK LMN O";
                                                Scanner B = new Scanner(St);
                                                for(int x=0; x<=2; x++)
                                                  {
                                                     B.next();
                                                     out.print(B.next());
                                                  }
Question 12
What is the output of the code segment to the right?
A) 0 B) 4 C) 6 D) 7 E) 55
                                                 int total = 0;
                                                 for(int x = -10; x <= 10; x++ )
                                                   if (x > -3 && x < 3)
                                                      total += x;
                                                 out.print(total);
```

```
Question 13
What is the output of the code segment to the right?
A) 2324696
B) 2324520
C) 2324588
D) 2224696
E) 2224624
                                                int W = 22;
                                                out.print(W++);
                                                out.print(++W);
                                                out.print(W>>2);
                                                out.print(W<<2);
Question 14
What is the output of the code segment shown on the right?
A) 8 B) 16 C) 32 D) 64 E) 128
                                                out.println(Integer.SIZE);
Question 15
What is output by the code segment to the right?
A) [11, 22, 33, 55]
B) [11, 55, 44, 22]
C) [55, 22, 33, 22]
D) [44, 22, 33, 11]
E) [44, 55, 11, 22]
                                                 ArrayList<Integer> eagle;
                                                eagle = new ArrayList<Integer>();
                                                eagle.add(11);
                                                eagle.add(0,22);
                                                eagle.add(33);
                                                eagle.add(0,44);
                                                eagle.add(eagle.get(1));
                                                eagle.set(1,55);
                                                eagle.remove(3);
                                                out.print(eagle);
Question 16
What is the output of the code segment shown on the right?
A) 120 B) 240 C) 250 D) 256 E) 480
                                                int E = 500;
                                                for(int x=1; x<=5; x++)
                                                   E /= 2;
                                                for(int x=1; x<=4; x++)
                                                   E *= 2;
                                                out.print(E);
Question 17
What is the output of the code segment shown on the right?
A) 2400
B) 2800
C) 3200
D) 3500
E) 1000000
                                                 int A = 0;
                                                 for(int x=1; x<=100; x++)
                                                   for(int y=1; y<=100; y*=2)
                                                      for(int z=1; z<=100; z*=3)
                                                         A++;
                                                 out.print(A);
Question 18
What is the output of the code segment shown on the right?
A) 25 B) 48 C) 77 D) 98 E) 129
                                               String St = "ABCDE";
                                                for (int x=1; x<=5; x++)
                                                  St = St + St.substring(1,St.length()-1);
                                                out.print(St.length());
```

#### **Question 19**

What is the output of the code segment shown on the right?

- **A)** 0 **B)** 6 **C)** 10 **D)** 13 **E)** 20

```
boolean[] F = new boolean[20];
F[1] = true;
for(int x=2; x<=19; x++)
  F[x] = F[x-1] ^ F[x-2];
int C = 0;
for (int x=0; x<=19; x++)
   if (F[x])
     C++;
out.print(C);
```

## **Question 20**

In the code segment to the right, what is the output of line 1?

- **A)** 70 **B)** 60 **C)** 50 **D)** 40 **E)** 30

### **Question 21**

In the code segment to the right, what is the output of line 2?

- **A)** 35 **B)** 36 **C)** 38 **D)** 42 **E)** 50

## **Question 22**

In the code segment to the right, what is the output of line 3?

- **A)** 4 **B)** 3 **C)** 2 **D)** 1 **E)** 0

```
public class GotIt
{
  private int A;
  private int B;
  private int C;
  public GotIt(int H)
  {
     A = H;
     B = H * 2;
     C = B * 2;
  }
  public GotIt()
  {
     A = 5;
     B = 11;
     C = 20;
  }
 public int SendIt()
 {
    return A + B + C;
 }
}
//////////////////////////////////
// Client code
GotIt Bob = new GotIt(10);
GotIt Ann = new GotIt();
GotIt Ted = new GotIt(0);
out.print(Bob.SendIt()); // Line 1
out.print(Ann.SendIt()); // Line 2
out.print(Ted.SendIt()); // Line 3
```

## **Question 23**

What is the output of the code segment shown on the right?

- **A)** 4 **B)** 24 **C)** 26 **D)** 27 **E)** 54

out.print(0b11011);

```
Question 24
What is the output of the code segment shown on the right?
 A) 19 B) 21 C) 30 D) 32 E) false
                                                 int A = 32;
                                                 int B = 21;
                                                 out.print(A < B ? B : A - 2);
Question 25
What is returned by the method call Wow("GO")?
 A) GO
 B) XGOX
 C) UIL
 D) XUILX
 E) XX
                                                public static String Wow(String W)
                                                  {
                                                     if (W.length()<3)
                                                       return "UIL";
                                                     else if (W.length()==3)
                                                       return "X" + W + "X";
                                                     else if (W.length()>6)
                                                       return Wow(W.substring(1,4));
                                                     else
                                                       return Wow(W.substring(1));
                                                  }
Question 26
What is returned by the method call Wow("STOP")?
 A) STOP
 B) XSTOX
 C) STO
 D) XTOPX
 E) XOX
Question 27
What is returned by the method call Wow("COMPUTER")?
 A) XCOMX
 B) XOMPX
 C) XMPUX
 D) XPUTX
 E) XUTEX
Question 28
In the code to the right, what is output on line #1?
 A) 10 B) 9 C) 8 D) 7 E) 6
                                                Stack<Integer>Bob;
                                                Bob = new Stack<Integer>();
                                                for (int x=6; x<=10; x++)
                                                  Bob.push(x);
                                                out.print(Bob.peek()); //Line 1
                                                for (int x=11; x<=13; x++)
                                                  Bob.pop();
                                                out.print(Bob.pop()); //Line 2
                                                for (int x=14; x<=20; x++)
                                                  Bob.push(x);
                                                out.print(Bob.size()); //Line 3
Question 29
In the code to the right, what is output on line #2?
 A) 13 B) 11 C) 9 D) 7 E) 6
Question 30
In the code to the right, what is output on line #3?
 A) 20 B) 6 C) 15 D) 7 E) 8
```

#### Question 31

What is the output of the code segment shown on the right?

- A) 10 seconds
- B) 24 seconds
- c) 25 seconds
- D) 48 seconds
- E) 50 seconds

The Big O Notation for a sorting routine is O(n²). When we sort a list of 3000 numbers, the process takes 2 seconds. How long do we predict the same sort will work on a list of 15,000 numbers?

### Question 32

In the code to the right, what is output by line #1?

- **A)** 2
- **B)** 4
- **C)** 6
- **D)** 8
- **E)** 10

#### Question 33

In the code to the right, what is output by line #2?

- **A)** 1
- **B)** 3
- **C)** 5
- **D)** 7
- **E)** 9

#### Question 34

In the code to the right, what is output by line #3?

- **A)** 0
- **B)** 1
- **C)** 2
- **D)** 3
- **E)** 4

```
ArrayList<String>Words;
Words = new ArrayList<String>();
Words.add("MILK");
Words.add("EGGS");
Words.add("BUTTER");
Words.add("OLEO");
Words.add("APPLE");
Words.add("PIE");
Words.add("STRAWBERRIES");
Words.add("BANANA");
Words.add("YOGURT");
Words.add("HAM");
int A = 0;
int B = 0;
int C = 0;
for(String T:Words)
  if(T.contains("A"))
    A++;
for(String T:Words)
  if(T.indexOf("T") == -1)
    B++;
for(String T:Words)
  if(T.matches("..E.*"))
    C++;
out.print(A);
                // Line 1
out.print(B);
                 // Line 2
out.print(C); // Line 3
```

## **Question 35** What is the output of the code segment shown on the right? **A)** 125 **B)** 152 **C)** 215 **D)** 251 **E)** 521 int L = 512; int M = L / 100; int N = (L - M \* 100) / 10; int R = L % 10; int U = R\*100 + M\*10 + N; out.print(U); **Question 36** What is the output of the code segment shown on the right? **A)** 0 **B)** 9 **C)** 16 **D)** 22 **E)** 25 int A = 9; int B = 16; int C = 25; out.print(A ^ B ^ C); **Question 37** What is the output of the code segment shown on the right? **A)** 9 **B)** 11 **C)** 13 **D)** 15 **E)** 17 String A = new String("HORSE"); String B = new String("PIG"); String C = A; A = B; B = C; int AL = A.length(); int BL = B.length(); int CL = C.length(); out.print(AL+BL+CL); **Question 38** What is the output of the code segment shown on the right? **A)** 22A37BA12 **B)** 22A2710B77 **C)** 22A2710BA12 **D)** 22A2710BA12 **E)** 22A37BAB int A = 10; int B = 12; int C = 27; out.print(A+B+"A"+C+A+"B"+('A'+B)); **Question 39** Evaluate the postfix expression to the right. Write your answer in the answer blank for #39. **3 4 + 5 \* 20 - 5 / 4 ^ Question 40** Create the binary search tree using the letters in the word to the right. After building the tree, determine how many leaf nodes the tree contains. **T R A M P O L I N E**

![](_page_7_Picture_0.jpeg)

# **UIL COMPUTER SCIENCE – 2023 DISTRICT**

**Questions** (+6 points for each correct answer, -2 points for each incorrect answer)

| 1) | Α |
|----|---|
|    |   |

7) C 17) D 27) B 37) C

8) C 18) D 28) A 38) B

4) E 14) C 24) C 34) C

5) A 15) E 25) C 35) D

6) E 16) B 26) D 36) A

9) A 19) D 29) D \*39) 81

10) D 20) A 30) E \*40) 2

1) A 11) B 21) B 31) E

2) B 12) A 22) E 32) B

3) E 13) D 23) D 33) D

**Note:** Correct responses are based on **Java SE Development Kit 17 (JDK 17)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 17 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

*<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.*

# **Explanations:**

| 1. | A | Convert<br>the<br>base<br>two<br>number<br>to<br>base<br>10.                                                                                                                                                                                                                                                                                                                                                          |
|----|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|    |   | 1010112<br>=<br>4310                                                                                                                                                                                                                                                                                                                                                                                                  |
|    |   | 4310<br>*<br>710<br>=<br>30110                                                                                                                                                                                                                                                                                                                                                                                        |
|    |   | 30110<br>=<br>4558                                                                                                                                                                                                                                                                                                                                                                                                    |
|    |   | (4<br>*<br>64)<br>+<br>(5<br>*<br>8)<br>+<br>(5<br>*<br>1)<br>=<br>256<br>+<br>40<br>+<br>5<br>=<br>301                                                                                                                                                                                                                                                                                                               |
|    |   | Actually,<br>a<br>cooler<br>solution<br>is<br>to<br>convert<br>the<br>binary<br>number<br>to<br>octal<br>and<br>do<br>the<br>arithmetic<br>there.<br>If<br>you<br>learn<br>this<br>method,<br>there<br>are<br>fewer<br>chances<br>to<br>make<br>conversion<br>errors.                                                                                                                                                 |
| 2. | B | Use<br>order<br>of<br>operations.<br>35<br>%<br>12<br>/<br>4<br>+<br>27<br>*<br>2<br>%<br>4<br>Perform<br>integer<br>modulus<br>first.<br>11<br>/<br>4<br>+<br>27<br>*<br>2<br>%<br>4                                                                                                                                                                                                                                 |
|    |   | Next<br>do<br>integer<br>division.<br>2<br>+<br>27<br>*<br>2<br>%<br>4<br>Now,<br>multiply.<br>2<br>+<br>54<br>%<br>4                                                                                                                                                                                                                                                                                                 |
|    |   | Again<br>with<br>the<br>integer<br>modulus.<br>2<br>+<br>2<br>2<br>+<br>2<br>=<br>4                                                                                                                                                                                                                                                                                                                                   |
| 3. | E | out.printf("%.1f\n",A);<br>This<br>prints<br>A<br>formatted<br>with<br>one<br>decimal<br>place<br>(rounded)<br>followed<br>by<br>a<br>carriage<br>return<br>out.print("Five\nSix");                                                                                                                                                                                                                                   |
|    |   | On<br>the<br>next<br>line,<br>this<br>prints<br>"Five"<br>on<br>the<br>next<br>line,<br>then<br>"Six"<br>on<br>the<br>following<br>line<br>because<br>of<br>the<br>"\n"<br>out.println("Seven\nEight");<br>This<br>prints<br>"Seven"<br>next<br>to<br>"Six."<br>The<br>\n<br>sends<br>"Eight<br>"<br>to<br>the<br>last<br>line.                                                                                       |
| 4. | E | yes.substring(3,7)<br>is<br>"vers"<br>(starts<br>at<br>position<br>3<br>and<br>stops<br>before<br>position<br>7)<br>So,<br>there<br>is<br>no<br>"i"<br>in<br>yes<br>giving<br>us<br>a<br>value<br>of<br>-1<br>Cool<br>hint,<br>when<br>you<br>spot<br>a<br>substring<br>with<br>2<br>arguments,<br>subtract<br>the<br>numbers.<br>This<br>will<br>tell<br>you<br>how<br>many<br>characters<br>will<br>be<br>returned. |
| 5. | A | A<br>is<br>not<br>true,<br>or<br>false.<br>B<br>is<br>not<br>A,<br>or<br>true                                                                                                                                                                                                                                                                                                                                         |
|    |   | A<br>&&<br>B<br>is<br>false<br>(two<br>trues<br>are<br>needed)<br>So,<br>C<br>is<br>false.<br>A<br>^<br>B<br>^<br>C<br>becomes<br>false<br>^<br>true<br>^<br>false                                                                                                                                                                                                                                                    |
|    |   | Work<br>left<br>to<br>right<br>keeping<br>in<br>mind<br>that<br>^<br>needs<br>a<br>true<br>and<br>a<br>false<br>to<br>be<br>true.<br>false<br>^<br>true<br>^<br>false                                                                                                                                                                                                                                                 |
|    |   | true<br>^<br>false<br>=<br>true                                                                                                                                                                                                                                                                                                                                                                                       |
| 6. | E | Math.pow(5,2)<br>returns<br>25.0<br>Math.pow(2,5)<br>returns<br>32.0<br>25.0<br>-<br>32.0<br>is<br>-7.0<br>Math.abs(-7.0)<br>returns<br>the<br>absolute<br>value<br>of<br>-7.0<br>which<br>is<br>7.0                                                                                                                                                                                                                  |
| 7. | C | The<br>key<br>to<br>the<br>problem<br>is<br>that<br>U<br>has<br>the<br>value<br>of<br>3.0.<br>70/20<br>performs<br>integer<br>division,<br>then<br>the<br>value<br>is<br>handed<br>to<br>U<br>as<br>a<br>double<br>(3.0<br>+<br>3.0)<br>is<br>6.0<br>6.0<br>/<br>4<br>is<br>1.5<br>as<br>real<br>number<br>division<br>takes<br>place                                                                                 |
| 8. | C | The<br>first<br>if<br>is<br>true<br>so<br>T<br>becomes<br>9<br>Since<br>T<br>is<br>9<br>now,<br>the<br>second<br>if<br>is<br>false,<br>the<br>else<br>makes<br>T<br>the<br>value<br>of<br>4.<br>Now<br>T<br>is<br>4,<br>so<br>the<br>final<br>if<br>is<br>true<br>causing<br>one<br>to<br>be<br>added<br>to<br>T.<br>T<br>finishes<br>the<br>adventure<br>at<br>5.                                                    |
| 9. | A | x<br>=<br>x*/<br>2<br>+<br>1<br>The<br>values<br>of<br>x<br>that<br>would<br>be<br>printed<br>are:<br>1<br>3<br>7<br>15<br>31<br>63<br>127                                                                                                                                                                                                                                                                            |

| 10. | D | The<br>array<br>called<br>ten<br>begins<br>with<br>the<br>following<br>values:<br>{0,0,0,0,0,0,0,0,0,0}.                                                                                                                                                                                        |
|-----|---|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     |   | With<br>each<br>iteration<br>of<br>x<br>in<br>the<br>loop,<br>the<br>xth<br>position<br>takes<br>on<br>the<br>value<br>of<br>3x<br>+<br>4.                                                                                                                                                      |
|     |   | The<br>array<br>becomes:<br>{4,7,10,13,16,19,22,25,28,31}                                                                                                                                                                                                                                       |
|     |   | Therefor<br>ten[7]<br>is<br>25                                                                                                                                                                                                                                                                  |
| 11. | B | St<br>=<br>"A<br>BC<br>DEF<br>GH<br>I<br>JK<br>LMN<br>O";                                                                                                                                                                                                                                       |
|     |   | The<br>Scanner<br>called<br>B<br>accesses<br>the<br>String<br>St.                                                                                                                                                                                                                               |
|     |   | Inside<br>the<br>loop,<br>the<br>first<br>B.next()<br>skips<br>a<br>value.                                                                                                                                                                                                                      |
|     |   | The<br>print<br>statement<br>prints<br>the<br>next.                                                                                                                                                                                                                                             |
|     |   | The<br>loop<br>iterates<br>three<br>times<br>giving<br>us<br>BC,GH,<br>and<br>JK                                                                                                                                                                                                                |
|     |   | So,<br>we<br>get<br>BCGHJK<br>as<br>the<br>output                                                                                                                                                                                                                                               |
| 12. | A | The<br>loop<br>runs<br>through<br>the<br>values<br>-10<br>-9<br>-8<br>-7<br>-6<br>-5<br>-4<br>-3<br>-2<br>-1<br>0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>If<br>an<br>x<br>is<br>larger<br>than<br>-3<br>and<br>smaller<br>than<br>3,<br>it<br>is<br>added<br>to<br>the<br>total. |
|     |   | -2<br>-1<br>0<br>1<br>and<br>2<br>are<br>added<br>to<br>that<br>total.                                                                                                                                                                                                                          |
|     |   | The<br>sum<br>is<br>zero.                                                                                                                                                                                                                                                                       |
| 13. | D | The<br>first<br>print<br>statement<br>prints<br>22,<br>then<br>adds<br>one<br>to<br>W.                                                                                                                                                                                                          |
|     |   | The<br>next,<br>adds<br>one<br>more,<br>then<br>prints<br>24.                                                                                                                                                                                                                                   |
|     |   | The<br>next,<br>uses<br>integer<br>division<br>twice,<br>printing<br>the<br>value<br>6.                                                                                                                                                                                                         |
|     |   | W<br>does<br>not<br>change.<br>It<br>is<br>still<br>24.                                                                                                                                                                                                                                         |
|     |   | The<br>last,<br>doubles<br>the<br>value<br>24<br>twice,<br>printing<br>96.                                                                                                                                                                                                                      |
| 14. | C | In<br>Java,<br>32<br>bits<br>(4<br>bytes)<br>are<br>used<br>to<br>store<br>integer<br>data                                                                                                                                                                                                      |
| 15. | E | Here<br>is<br>the<br>progression<br>of<br>eagle.                                                                                                                                                                                                                                                |
|     |   | [<br>]                                                                                                                                                                                                                                                                                          |
|     |   | [11]<br>[22,11]                                                                                                                                                                                                                                                                                 |
|     |   | [22,11,33]                                                                                                                                                                                                                                                                                      |
|     |   | [44,22,11,33]                                                                                                                                                                                                                                                                                   |
|     |   | [44,22,11,33,22]                                                                                                                                                                                                                                                                                |
|     |   | [44,55,11,33,22]                                                                                                                                                                                                                                                                                |
|     |   | [44,55,11,22]                                                                                                                                                                                                                                                                                   |
| 16. | B | E<br>begins<br>at<br>500.                                                                                                                                                                                                                                                                       |
|     |   | It<br>then<br>undergoes<br>being<br>divided<br>by<br>2<br>five<br>consecutive<br>times,                                                                                                                                                                                                         |
|     |   | 500<br>-<br>250<br>-<br>125<br>-<br>62<br>-<br>31<br>-<br>15                                                                                                                                                                                                                                    |
|     |   | Then,<br>starting<br>at<br>15,<br>we<br>double<br>it<br>four<br>times.<br>15<br>-<br>30<br>-<br>60<br>-<br>120<br>-<br>240                                                                                                                                                                      |
| 17. | D | Be<br>careful<br>on<br>this<br>one.<br>It<br>is<br>easy<br>to<br>"underestimate"<br>the<br>y<br>and<br>the<br>z<br>loops.                                                                                                                                                                       |
|     |   | The<br>x<br>loop<br>iterates<br>100<br>times<br>-<br>no<br>problem.                                                                                                                                                                                                                             |
|     |   | The<br>y<br>loop<br>iterates<br>7<br>times<br>-<br>1,2,4,8,16,32,64                                                                                                                                                                                                                             |
|     |   | The<br>z<br>loop<br>iterates<br>5<br>times<br>-<br>1,3,9,27,81                                                                                                                                                                                                                                  |
|     |   | 100*7*5<br>=<br>3500                                                                                                                                                                                                                                                                            |
| 18. | D | The<br>value<br>of<br>St<br>does<br>not<br>matter,<br>only<br>the<br>length.                                                                                                                                                                                                                    |
|     |   | With<br>each<br>iteration,<br>we<br>add<br>St.length()-2<br>characters<br>to<br>St.                                                                                                                                                                                                             |
|     |   | 0<br>-<br>length<br>is<br>5                                                                                                                                                                                                                                                                     |
|     |   | 1<br>-<br>length<br>is<br>8<br>(5+3)                                                                                                                                                                                                                                                            |
|     |   | 2<br>-<br>length<br>is<br>14<br>(8<br>+<br>6)                                                                                                                                                                                                                                                   |
|     |   | 3<br>-<br>length<br>is<br>26<br>(14<br>+<br>12)                                                                                                                                                                                                                                                 |
|     |   | 4<br>-<br>length<br>is<br>50<br>(26<br>+<br>24)<br>5<br>-<br>length<br>is<br>98<br>(50<br>+<br>48)                                                                                                                                                                                              |
| 19. | D | For<br>purposes<br>of<br>brevity,<br>I<br>will<br>use<br>0<br>for<br>false<br>and<br>1<br>for<br>true.                                                                                                                                                                                          |
|     |   | [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]<br>=<br>original<br>array                                                                                                                                                                                                                             |
|     |   | Then<br>we<br>set<br>F[1]<br>=<br>true.                                                                                                                                                                                                                                                         |
|     |   | [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                                                                                                                                                                                                                                                       |
|     |   | In<br>the<br>loop,<br>to<br>get<br>the<br>value<br>of<br>F[2],<br>do<br>F[0]<br>^<br>F[1]<br>=<br>false<br>^<br>true<br>=<br>true                                                                                                                                                               |
|     |   | [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                                                                                                                                                                                                                                                       |
|     |   | In<br>the<br>loop,<br>to<br>get<br>the<br>value<br>of<br>F[3],<br>do<br>F[1]<br>^<br>F[2]<br>=<br>true<br>^<br>true<br>=<br>false                                                                                                                                                               |
|     |   | [0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                                                                                                                                                                                                                                                       |
|     |   | In<br>the<br>loop,<br>to<br>get<br>the<br>value<br>of<br>F[4],<br>do<br>F[2]<br>^<br>F[3]<br>=<br>true<br>^<br>false<br>=<br>true                                                                                                                                                               |
|     |   | [0,1,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]                                                                                                                                                                                                                                                       |
|     |   | Watch<br>the<br>cool<br>pattern<br>emerge<br>as<br>you<br>trace<br>until<br>the<br>end.                                                                                                                                                                                                         |
|     |   | [0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1]<br>There<br>are<br>13<br>trues.                                                                                                                                                                                                                       |

|     |          | 1                                                                                                                   |
|-----|----------|---------------------------------------------------------------------------------------------------------------------|
| 20. | Α        | Bob uses the one-parameter constructor.                                                                             |
|     |          | 10 is sent in, assigning these values: A=10, B=20, C=40                                                             |
|     |          | SendIt returns the sum of the three 70                                                                              |
| 21. | В        | Ted uses the zero-parameter constructor.                                                                            |
|     |          | It assigns these values: A=5, B=11, C=20                                                                            |
| 00  |          | SendIt returns the sum of the three 36                                                                              |
| 22. | E        | Ann uses the one-parameter constructor.                                                                             |
|     |          | 0 is sent in, assigning these values: A=0, B=0, C=0 SendIt returns the sum of the three 0                           |
| 23. | D        | This takes the binary number 11011 and prints the base 10 value.                                                    |
| 23. |          | That value is 27 (16+8+2+1)                                                                                         |
| 24. | С        | A is not less than B, so the statement will print A-2, which is 30.                                                 |
| 25. | C        | Wow("GO") with a length of 2, goes straight to the first if and returns "UIL"                                       |
| 26. | D        | Wow("STOP") with a length of 4, goes to the last return                                                             |
| 20. |          | Wow("STOP") = Wow("TOP")                                                                                            |
|     |          | Then, with length of 3, the second return is invoked giving us "XTOPX"                                              |
| 27. | В        | Wow("COMPUTER") has a length greater than 6.                                                                        |
|     |          | Wow("COMPUTER") = Wow("OMP")                                                                                        |
|     |          | Then, with length of 3, the second return is invoked giving us "XOMPX"                                              |
| 28. | Α        | At the time of Line 1, Bob is [6,7,8,9,10]                                                                          |
|     |          | Bob.peek() returns the value of the top item 10                                                                     |
| 29. | D        | The second loop pops three items to give us [6,7]                                                                   |
|     |          | Then, on line 2 we print and pop.                                                                                   |
|     | ļ        | That item is the 7.                                                                                                 |
| 30. | E        | Moving onward, we have [6]                                                                                          |
|     |          | The last loop pushes 7 more numbers onto the stack giving us [6,14,15,16,17,18,19,20]                               |
|     | <u> </u> | The final stack size is 8.                                                                                          |
| 31. | E        | First, look at the size of the original list and the size of the second list.                                       |
|     |          | Here we see that the first list has 3000 items and the second list has 15,000.                                      |
|     |          | The second list is 5 times as big.                                                                                  |
|     |          | 5 will be our n.                                                                                                    |
|     |          | The Big O is $O(n^2)$ .                                                                                             |
|     |          | Plugging in 5 for n gives us 25.                                                                                    |
|     |          | Theoretically, it should take the process 25 times as long.                                                         |
|     |          | The original took 2 seconds.                                                                                        |
|     |          | 50 seconds is our answer.                                                                                           |
| 32. | В        | Words.add("MILK");                                                                                                  |
|     |          | Words.add("EGGS");                                                                                                  |
|     |          | Words.add("BUTTER");                                                                                                |
|     |          |                                                                                                                     |
|     |          | Words.add("OLEO");                                                                                                  |
|     |          | Words.add("APPLE");                                                                                                 |
|     |          | Words.add("PIE");                                                                                                   |
|     |          | <pre>Words.add("STRAWBERRIES");</pre>                                                                               |
|     |          | Words.add("BANANA");                                                                                                |
|     |          | Words.add("YOGURT");                                                                                                |
|     |          |                                                                                                                     |
|     |          | Words.add("HAM");                                                                                                   |
|     |          | This counts the words in the list that contain at least one "A"  4 = APPLE, STRAWBERRIES, BANANA, HAM               |
| 33. | D        | This counts the words in the list that do not contain at least one "T" 7 = All but BUTTER, STRAWBERRIES, and YOGURT |
| 34. | С        | This counts the words in the list that have an E in String position 2.                                              |
| J   |          | There may be 0 or more characters of any type after the E.                                                          |
|     |          | 2 = PIE, OLEO                                                                                                       |
|     |          |                                                                                                                     |
|     |          |                                                                                                                     |
|     |          |                                                                                                                     |

| 35. | D  | I<br>have<br>a<br>feeling<br>the<br>programmer<br>had<br>hopes<br>of<br>reversing<br>the<br>integer,<br>but<br>messed<br>up<br>along<br>the<br>way.<br>M<br>=<br>512<br>/<br>100<br>=<br>5<br>N<br>=<br>(512<br>-<br>500)<br>/<br>10<br>=1<br>R<br>=<br>512<br>%<br>10<br>=<br>2<br>OK.<br>The<br>digits<br>are<br>separated.<br>But,<br>the<br>U<br>formula<br>does<br>something<br>odd.<br>R<br>=<br>2*100<br>+<br>5*10<br>+<br>1<br>=<br>251                                                                                                 |
|-----|----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 36. | A  | First,<br>convert<br>each<br>number<br>to<br>binary.<br>A<br>=<br>01001<br>B<br>=<br>10000<br>C<br>=<br>11001<br>Notice<br>that<br>we<br>added<br>a<br>leading<br>zero<br>to<br>A<br>so<br>that<br>all<br>numbers<br>would<br>be<br>5<br>bits<br>long.<br>01001<br>^<br>10000<br>^<br>11001<br>Work<br>left<br>to<br>right.<br>01001<br>^<br>10000<br>=<br>11001<br>Hmm.<br>11001<br>^<br>11001<br>=<br>00000<br>=<br>0                                                                                                                         |
| 37. | C  | Step<br>by<br>step<br>A<br>=<br>"HORSE"<br>B<br>=<br>"PIG"<br>C<br>=<br>"HORSE"<br>A<br>=<br>"PIG"<br>B<br>=<br>"HORSE"<br>We<br>end<br>up<br>with<br>2<br>HORSEs<br>and<br>1<br>PIG.<br>The<br>sum<br>of<br>the<br>lengths<br>is<br>13.                                                                                                                                                                                                                                                                                                        |
| 38. | B  | int A = 10;<br>int B = 12;<br>int C = 27;<br>out.print(A+B+"A"+C+A+"B"+('A'+B));<br>Note:<br>'A'<br>+<br>B<br>will<br>have<br>a<br>value<br>of<br>77.<br>The<br>ASCII<br>code<br>for<br>'A"<br>is<br>65.<br>We<br>will<br>add<br>A+B<br>at<br>the<br>beginning<br>because<br>it<br>comes<br>before<br>any<br>mention<br>of<br>Strings.<br>We<br>will<br>not<br>use<br>arithmetic<br>to<br>add<br>C<br>and<br>A<br>since<br>it<br>is<br>embedded<br>in<br>the<br>Strings.<br>22<br>A<br>27<br>10<br>B<br>77<br>22A2710B77<br>is<br>the<br>output |
| 39. | 81 | 3<br>4<br>+<br>5<br>*<br>20<br>-<br>5<br>/<br>4<br>^<br>7<br>5<br>*<br>20<br>-<br>5<br>/<br>4<br>^<br>35<br>20<br>-<br>5<br>/<br>4<br>^<br>15<br>5<br>/<br>4<br>^<br>3<br>4<br>^<br>81                                                                                                                                                                                                                                                                                                                                                          |
| 40. | 2  | After<br>building<br>the<br>binary<br>search<br>tree,<br>only<br>the<br>E<br>and<br>the<br>N<br>have<br>no<br>"children."                                                                                                                                                                                                                                                                                                                                                                                                                       |