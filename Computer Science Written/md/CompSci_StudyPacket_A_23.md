# **UIL COMPUTER SCIENCE WRITTEN TEST – 2023 INVITATIONAL A**

**Note:** Correct responses are based on **Java SE Development Kit 17 (JDK 17)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 17 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

| Question 1i                       | Which of the following decimal numbers has the largest base 10 value? |                |                                                                       |                                   |
|-----------------------------------|-----------------------------------------------------------------------|----------------|-----------------------------------------------------------------------|-----------------------------------|
| A) 1001012                        | B) 568                                                                | C) 2616        | D) 467                                                                | E) 1A12                           |
| Question 2uesti                   |                                                                       |                |                                                                       |                                   |
|                                   | What is the output of the code segment to the right?                  |                | out.print(15 + 5 / 4 + 1);                                            |                                   |
| A)<br>B) 4<br>1                   | C) 6<br>D) 17                                                         | E) 17.25       |                                                                       |                                   |
| Question 3                        |                                                                       |                |                                                                       |                                   |
| A) OneTwo<br>ThreeFour<br>Five    | What is the output of the code segment to the right?                  |                |                                                                       |                                   |
| B) One<br>TwoThree<br>FourFive    |                                                                       |                | out.print("One");<br>out.println("Two");<br>out.print("Three");       |                                   |
| C) One<br>TwoThreeFour<br>Five    |                                                                       |                | out.println("Four");<br>out.print("Five");                            |                                   |
| D) OneTwo<br>ThreeFourFive        |                                                                       |                |                                                                       |                                   |
| E) OneTwo<br>Three<br>FourFive    |                                                                       |                |                                                                       |                                   |
| Question 4<br>A) niv<br>B) i      | What is the output of the code segment to the right?<br>C) iv         | D) ive<br>E) v | String str = "University";                                            | out.print(str.substring(2,3));    |
| Question 5<br>A) true<br>B) false | What is the output of the code segment to the right?                  |                | boolean M = true;<br>boolean N = false;<br>out.print(M    true && N); |                                   |
| Question 6                        |                                                                       |                |                                                                       |                                   |
|                                   | What is the output of the code segment to the right?                  |                |                                                                       | out.print((int)Math.floor(5.85)); |
| A)<br>B)<br>4.0                   | C) 5.0<br>D)<br>6                                                     | E)<br>5<br>6   |                                                                       |                                   |
| Question 7                        |                                                                       |                | int x = 7;                                                            |                                   |
|                                   | What is the output of the code segment to the right?                  |                | int y = 8;                                                            |                                   |
| A)<br>78<br>B)                    | 67.5<br>C) 67<br>D)                                                   | 92<br>E)<br>70 | double a = 2.0;                                                       |                                   |
|                                   |                                                                       |                | out.print(x / a + y * y);                                             |                                   |

```
Question 8
What is the output of the code segment to the right?
A) MRVVRM
B) VRM
C) RVRM
D) VVRM
E) V
                                               int R = 7;
                                               int V = 9;
                                               int W = V - R;
                                               if(R > V)
                                                  out.print("M");
                                               if(2 + R < V)
                                                  out.print("R");
                                               else
                                                  out.print("V");
                                               if(W + R == V)
                                                  out.print("VRM");
Question 9
What is the output of the code segment to the right?
A) 1 2 3 4 5 6 7 8 9
B) 1 3 5 7 9
C) 1 4 9 16 25 36 49 64 81
D) 1 4 9
E) 1 9 25 49 81
                                                for(int x = 1; x < 10; x=x+2)
                                                   out.print(x*x + " ");
Question 10
What is the output of the code segment to the right?
A) 26 B) 4 C) 221 D) 33 E) 85
                                                int[] stuff = {2,17,3,13,5,11,7};
                                                out.print(stuff[1]*stuff[4]);
Question 11
What is output by the code segment to the right?
  A) MICH
  B) MII
  C) MICHI
  D) CHGAN
  E) MICHIGAN
                                               Scanner t = new Scanner("MI CH I GAN");
                                               t.next();
                                               String st = t.next();
                                               t.next();
                                               st += t.next();
                                               out.print(st);
Question 12
What is the output of the code segment to the right?
A) 100 B) 400 C) 210 D) 110 E) 81
                                               int h = 0;
                                               for(int i = 1; i <= 20; i = i + 2)
                                                    h += i;
                                               out.print(h);
Question 13
What is the output of the code segment to the right?
A) 40 B) 46 C) 20 D) 10 E) 80
                                                int a = 10, b = 4, c = 4;
                                                out.print(a << 2 + b >> 1 + ++c);
```

**Question 14** What is the output of the code segment shown on the right? **A)** 8 **B)** 16 **C)** 32 **D)** 4 **E)** 64 out.println(Integer.SIZE); **Question 15** What is output by the code segment to the right? **A)** [11, 22, 33, 44, 55, 66] **B)** [44, 55, 66] **C)** [11, 55, 66] **D)** [22, 55, 66] **E)** [22, 44, 66] ArrayList<Integer> list; list = new ArrayList<Integer>(); list.add(11); list.add(22); list.remove(1); list.add(33); list.add(44); list.remove(1); list.add(55); list.add(66); list.remove(1); out.println(list); **Question 16** What is the output of the code segment shown on the right? **A)** F **B)** G **C)** H **D)** I **E)** J String car = "FGHIJKLMNOPQRST"; int L = car.indexOf("KL"); out.println(car.charAt(L-1)); **Question 17** In the code segment to the right, which of the following numbers could NOT be printed? **A)** 22 **B)** 24 **C)** 26 **D)** 28 **E)** 30 int T = (int)(Math.random()\*7) + 22; System.out.print(T); **Question 18** What is the output of the code segment shown on the right? **A)** 15 **B)** 12 **C)** 4 **D)** 20 **E)** 7 out.print(12 & 7 + 8 ^ 11); **Question 19** What is the output of the code segment shown on the right? **A)** 1 **B)** 8 **C)** 7 **D)** 5 **E)** 0 int[][] w = {{5,1,2},{8,0,6},{7,1,3}}; out.print(w[2][1]);

In the code segment to the right, in line #1, if **<???>** was replaced by 2, what would the output be?

- **A)** 8 **B)** 7 **C)** 5 **D)** 3 **E)** 9

## **Question 21**

In the code segment to the right, in line #1, if **<???>** was replaced by 6, what would the output be?

- **A)** 8 **B)** 7 **C)** 5 **D)** 3 **E)** 9

# **Question 22**

In the code segment to the right, in line #1, if **<???>** was replaced by L-1, what would the code do to the list?

- **A)** It would set all values of the list to 8
- **B)** It would set all values of the list to 9
- **C)** It would sort the list
- **D)** It would delete all odd numbers from the list
- **E)** It would reverse the order of the numbers

```
int[]jenny = {8,6,7,5,3,0,9};
int box;
int L = jenny.length;
int N = <???>; // line #1
for(int x=1; x<=N; x++)
  for(int y=0; y<=L-2; y++)
    if (jenny[y] > jenny[y+1])
      {
        box = jenny[y];
        jenny[y] = jenny[y+1];
        jenny[y+1] = box;
      }
out.print(jenny[2]);
```

#### **Question 23**

What is the output of the code segment shown on the right?

- **A)** 2 **B)** B **C)** 10 **D)** D **E)** 34

```
int x = 2 << 5;
x++;
++x;
System.out.print((char) x);
```

#### **Question 24**

What is the output of the code segment shown on the right?

- **A)** -33
- **B)** -15
- **C)** 16
- **D)** 17
- **E)** -16

```
int A = 5;
 for(int x = 0; x < 10; x++)
   switch(x)
   {
      case 0: A++; break;
      case 1: A += 11;
      case 2: A = -A; break;
      case 3: A++; A++; break;
      case 4: A/=2;
      case 5: A*=2; break;
      case 6: A = -A; break;
      case 7: A++;
      case 8: A++; break;
    }
 out.print(A);
```

What is returned by the method call Go(2)

- **A)** 1 **B)** 2 **C)** 3 **D)** 4 **E)** 5

## **Question 26**

What is returned by the method call Go(3)

- **A)** 9 **B)** 12 **C)** 30 **D)** 15 **E)** 18

# **Question 27**

What is returned by the method call Go(33)

- **A)** 165 **B)** 163 **C)** 161 **D)** 159 **E)** 157

```
public static int Go(int x)
{
  if (x==0)
    return 10;
  if (x < 3)
    return x * 2;
  else
    return Go(x-1) + 5;
}
```

## **Question 28**

In the code to the right, what is output on line #1?

- **A)** 12 **B)** 24 **C)** 36 **D)** 48 **E)** null

#### **Question 29**

In the code to the right, what is output on line #2?

- **A)** [12, 24, 48, 72]
- **B)** [12, 24, 72]
- **C)** [12, 24]
- **D)** [12, 36]
- **E)** [12, 36, 60]

## **Question 30**

IIn the code to the right, what is output on line #3?

- **A)** [36, 60, 72]
- **B)** [36, 72]
- **C)** [36]
- **D)** [36, 48, 60]
- **E)** [12, 36, 60, 72]

```
Stack<Integer> tall;
tall = new Stack<Integer>();
Stack<Integer> shorter;
shorter = new Stack<Integer>();
tall.push(12);
tall.push(24);
shorter.push(36);
tall.push(48);
out.println(shorter.peek());//line 1
tall.push(60);
shorter.push(tall.pop());
tall.push(72);
shorter.push(tall.peek());
tall.pop();
tall.pop();
out.println(tall); // line 2
```

out.println(shorter); // line 3

## **Question 31**

What is the output of the code segment shown on the right?

- **A)** 8 **B)** 9 **C)** 10 **D)** 11 **E)** 12
- int x = 8; for(x = 15; x>=12; x++) x = x - 3; out.print(x);

In the code to the right, how many class variables does the Dog class contain?

- **A)** 2 **B)** 3 **C)** 4 **D)** 1 **E)** 0

## **Question 33**

In the code to the right, what is the resulting output caused by line #1?

- **A)** 12
- **B)** 22
- **C)** 34
- **D)** 46
- **E)** 80

## **Question 34**

In the code to the right, what is the resulting output caused by line #2?

- **A)** 9
- **B)** 11
- **C)** 13
- **D)** 15
- **E)** 17

```
public void display()
 {
   A++;
   B +=A;
```

//client code

Dog R = new Dog();

Dog S = new Dog(7);

public class Dog

public Dog()

A = 11; B = A \* 2;

B = C;

public Dog(int C)

A = B - 4;;

{

}

{

}

}

private int A; private int B;

{

}

**Question 35**

What is the output of the code segment shown on the right?

- **A)** 770 **B)** 78 **C)** 66 **D)** 846 **E)** 902

```
int T = 0;
for(char x = 'A'; x <= 'L'; x++)
  T += x;
out.print(T);
```

R.display(); // line 1

S.display(); // line 2

out.println(A + B);

If the letters to the right were inserted into an initially empty binary search tree in the order shown, how many leaves would the resulting tree contain?

- **A)** 9 **B)** 10 **C)** 12 **D)** 1 **E)** 19

A B C D E F G H I J J I H G F E D C B A

#### **Question 37**

What is the output of the code segment shown on the right?

- **A)** 120 **B)** 24 **C)** 72 **D)** 504 **E)** 3024

```
int N = 123456789;
int C = 1;
do
{
   C *= N % 10;
   N /= 10;
}
while (N > 1000000);
out.println(C);
```

## **Question 38**

What is the output of the code segment shown on the right?

- **A)** 5 **B)** 7 **C)** 9 **D)** 0 **E)** 1021

```
int A = 5;
 int B = 7;
 int C = 9;
 int D = 0;
 for (int x = 1; x <= 1000; x++)
 {
   D = A;
   A = B;
   B = C;
   C = D;
 }
out.print(A);
```

| Question 39<br>After the code to the right is completed, what letter will be at<br>the front of the queue?               | add A<br>add B<br>add C<br>remove<br>remove<br>add D<br>add E<br>remove<br>add F<br>remove<br>add G<br>add H<br>add I<br>remove<br>remove<br>add J |
|--------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Question 40<br>Of the 8 possible ordered triplets (example 000), how many will<br>make the expression at the right true? | 𝐴<br>*<br>𝐵<br>(𝐴<br>+<br>𝐶)<br>*                                                                                                                  |

![](_page_8_Picture_0.jpeg)

| Questions (+6 points for each correct answer, -2 points for each incorrect answer) |  |
|------------------------------------------------------------------------------------|--|
|                                                                                    |  |

| 1 | В |
|---|---|
|   |   |

- 1) B 11) D 21) C 31) D
- 7) B 17) E 27) D 37) D

- 2) D 12) A 22) C 32) E
- 3) A 13) D 23) B 33) D
- 4) B 14) C 24) A 34) D
- 5) A 15) C 25) D 35) D
- 6) D 16) E 26) A 36) B
- 8) D 18) E 28) C 38) B
- 9) E 19) A 29) C \*39) G
- 10) E 20) D 30) A \*40) 4

**Note:** Correct responses are based on **Java SE Development Kit 17 (JDK 17)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 12 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

*<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.*

## Explanations:

| 1.  | B | Convert<br>all<br>to<br>Base<br>10<br>and<br>then<br>compare.<br>1001012<br>=<br>3710<br>568<br>=<br>4610<br>2616<br>=<br>3810<br>467<br>=<br>3410<br>1A12<br>=<br>2210                                                                                                                                                                                                                 |  |
|-----|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
| 2.  | D | Use<br>order<br>of<br>operations.<br>Perform<br>integer<br>division<br>first,<br>then<br>add<br>left<br>to<br>right.<br>15<br>+<br>5<br>/<br>4<br>+<br>1<br>15<br>+<br>1<br>+<br>1<br>=<br>17                                                                                                                                                                                           |  |
| 3.  | A | A<br>new<br>line<br>is<br>invoked<br>after<br>each<br>println<br>statement<br>There<br>will<br>be<br>a<br>new<br>line<br>after<br>"Two"<br>and<br>after<br>"Four"                                                                                                                                                                                                                       |  |
| 4.  | B | str.substring(A,B)<br>This<br>will<br>return<br>a<br>string<br>of<br>characters<br>beginning<br>at<br>position<br>A<br>They<br>continue<br>up<br>to,<br>but<br>not<br>including<br>position<br>B.<br>str.substring(2,3)<br>will<br>therefore<br>only<br>contain<br>"i"                                                                                                                  |  |
| 5.  | A | M<br>  <br>true<br>&&<br>N<br>First,<br>evaluate<br>true<br>&&<br>N<br>which<br>is<br>true<br>&&<br>false<br>=<br>false<br>Now<br>evaluate<br>M<br>  <br>false<br>which<br>is<br>true<br>  <br>false<br>=<br>true                                                                                                                                                                       |  |
| 6.  | D | Math.floor(5.85)<br>returns<br>the<br>value<br>5.0<br>(int)<br>type<br>casts<br>that<br>value<br>as<br>an<br>integer<br>5                                                                                                                                                                                                                                                               |  |
| 7.  | B | In<br>the<br>expression<br>x<br>/<br>a<br>+<br>y<br>*<br>y<br>since<br>a<br>is<br>a<br>double,<br>x/a<br>will<br>yield<br>a<br>double<br>value<br>3.5<br>3.5<br>+<br>64<br>=<br>67.5                                                                                                                                                                                                    |  |
| 8.  | D | R<br>=<br>7<br>and<br>V<br>=9,<br>so<br>W<br>will<br>have<br>the<br>value<br>of<br>2<br>The<br>first<br>if<br>has<br>a<br>false<br>condition<br>and<br>will<br>cause<br>no<br>output<br>The<br>second<br>also<br>has<br>a<br>false<br>condition,<br>but<br>its<br>else<br>will<br>print<br>a<br>V<br>The<br>third<br>if<br>has<br>a<br>true<br>condition<br>and<br>will<br>print<br>VRM |  |
| 9.  | E | The<br>loop<br>would<br>print<br>1<br>3<br>5<br>7<br>9<br>if<br>it<br>was<br>out.print(x<br>+<br>"<br>")<br>Since<br>it<br>prints<br>x*x,<br>we<br>get<br>the<br>square<br>of<br>each<br>of<br>those<br>numbers.                                                                                                                                                                        |  |
| 10. | E | The<br>first<br>element<br>in<br>an<br>array<br>is<br>at<br>position<br>0.<br>We<br>are<br>multiplying<br>the<br>elements<br>in<br>positions<br>1<br>and<br>4<br>17<br>*<br>5<br>=<br>85                                                                                                                                                                                                |  |
| 11. | D | Each<br>of<br>the<br>four<br>t.next()<br>statements<br>access<br>a<br>different<br>String<br>within<br>the<br>Scanner<br>String.<br>The<br>second<br>one,<br>"CH",<br>is<br>the<br>initial<br>value<br>of<br>st.<br>The<br>fourth<br>one,<br>"GAN",<br>is<br>added<br>to<br>the<br>end<br>of<br>String<br>st.                                                                           |  |
| 12. | A | This<br>loop<br>finds<br>the<br>sum<br>of<br>all<br>odd<br>numbers<br>in<br>the<br>range<br>1<br>to<br>20<br>1+3+5+7+9+11+13+15+17+19<br>=<br>100<br>Fun<br>fact:<br>The<br>sum<br>of<br>all<br>consecutive<br>odd<br>numbers<br>starting<br>with<br>1<br>is<br>always<br>a<br>perfect<br>square.                                                                                       |  |
| 13. | D | a<br><<<br>2<br>+<br>b<br>>><br>1<br>+<br>++c<br>++c<br>a<br><<<br>2<br>+<br>b<br>>><br>1<br>+<br>a<br><<<br>2<br>+<br>b<br>>><br>1<br>+<br>5<br>2 + b<br>a<br><<<br>>><br>1<br>+<br>5<br>a<br><<<br>6<br>>><br>1<br>+<br>5<br>1 + 5<br>a<br><<<br>6<br>>><br>a<br><<<br>6<br>>><br>6<br>a << 6<br>>><br>6<br>640<br>>><br>6<br>10                                                      |  |
| 14. | C | SIZE<br>represents<br>the<br>number<br>of<br>bits<br>used<br>to<br>store<br>a<br>particular<br>data<br>type.<br>Integer.SIZE<br>is<br>32<br>Know<br>as<br>many<br>of<br>these<br>as<br>you<br>can.                                                                                                                                                                                      |  |

| 15. | C | Here<br>is<br>the<br>progression<br>of<br>list.                                                                      |
|-----|---|----------------------------------------------------------------------------------------------------------------------|
|     |   | [<br>]                                                                                                               |
|     |   | [11]                                                                                                                 |
|     |   | [11,<br>22]                                                                                                          |
|     |   | [11]                                                                                                                 |
|     |   | [11,<br>33]<br>[11,<br>33,<br>44]                                                                                    |
|     |   | [11,<br>44]                                                                                                          |
|     |   | [11,<br>44,<br>55]                                                                                                   |
|     |   | [11,<br>44,<br>55,<br>66]                                                                                            |
|     |   | [11,<br>55,<br>66]                                                                                                   |
| 16. | E | The<br>index<br>of<br>"KL"<br>in<br>car<br>is<br>5                                                                   |
|     |   | The<br>problem<br>then<br>outputs<br>the<br>character<br>in<br>position<br>4                                         |
| 17. | E | (int)(Math.random()*7)<br>+<br>22<br>-<br>This<br>generates<br>numbers<br>included<br>in<br>the<br>following<br>set: |
|     |   | {22,23,24,25,26,27,28}<br>-<br>a<br>list<br>that<br>starts<br>with<br>22<br>and<br>has<br>7<br>elements.             |
|     |   | Therefore<br>30<br>cannot<br>be<br>generated.                                                                        |
| 18. | E | Order<br>of<br>precedence<br>tells<br>us<br>to<br>add<br>7+8<br>first                                                |
|     |   | Now<br>we<br>have<br>12<br>&<br>15<br>^<br>11                                                                        |
|     |   | Convert<br>all<br>to<br>binary.                                                                                      |
|     |   | 1100<br>&<br>1111<br>^<br>1011                                                                                       |
|     |   | AND<br>has<br>priority<br>over<br>XOR                                                                                |
|     |   | 1100<br>^<br>1011                                                                                                    |
|     |   | This<br>gives<br>us<br>0111<br>=<br>7                                                                                |
| 19. | A | w[2][1]<br>is<br>accessing<br>the<br>element<br>in<br>list<br>#2,<br>item<br>#1.                                     |
|     |   | Remember<br>that<br>lists<br>and<br>items<br>are<br>numbered<br>starting<br>with<br>0                                |
|     |   | So,<br>1<br>is<br>the<br>answer.                                                                                     |
| 20. | D | This<br>is<br>the<br>code<br>for<br>a<br>version<br>of<br>the<br>bubble<br>sort.                                     |
|     |   | 8<br>6<br>7<br>5<br>3<br>0<br>9<br>-<br>original<br>list                                                             |
|     |   | 6<br>7<br>5<br>3<br>0<br>8<br>9<br>-<br>after<br>1st<br>pass<br>through<br>the<br>list                               |
|     |   | 6<br>5<br>3<br>0<br>7<br>8<br>9<br>-<br>after<br>2nd<br>pass<br>through<br>the<br>list                               |
|     |   | Item<br>#2<br>is<br>3                                                                                                |
| 21. | C | This<br>is<br>the<br>code<br>for<br>a<br>version<br>of<br>the<br>bubble<br>sort.                                     |
|     |   | 8<br>6<br>7<br>5<br>3<br>0<br>9<br>-<br>original<br>list                                                             |
|     |   | 6<br>7<br>5<br>3<br>0<br>8<br>9<br>-<br>after<br>1st<br>pass<br>through<br>the<br>list                               |
|     |   | 6<br>5<br>3<br>0<br>7<br>8<br>9<br>-<br>after<br>2nd<br>pass<br>through<br>the<br>list                               |
|     |   | 5<br>3<br>0<br>6<br>7<br>8<br>9<br>-<br>after<br>3rd<br>pass<br>through<br>the<br>list                               |
|     |   | 3<br>0<br>5<br>6<br>7<br>8<br>9<br>-<br>after<br>4th<br>pass<br>through<br>the<br>list                               |
|     |   | 0<br>3<br>5<br>6<br>7<br>8<br>9<br>-<br>after<br>5th<br>pass<br>through<br>the<br>list                               |
|     |   | 0<br>3<br>5<br>6<br>7<br>8<br>9<br>-<br>after<br>6th<br>pass<br>through<br>the<br>list                               |
|     |   | Item<br>#2<br>is<br>35                                                                                               |
| 22. | C | This<br>is<br>a<br>version<br>of<br>the<br>bubble<br>sort.                                                           |
| 23. | B | 2<br><<<br>5<br>performs<br>a<br>bitwise<br>left<br>shift<br>5                                                       |
|     |   | This<br>sets<br>x<br>=<br>64                                                                                         |
|     |   | Each<br>of<br>the<br>next<br>two<br>lines<br>add<br>one<br>to<br>x<br>giving<br>us<br>66                             |
|     |   | The<br>output<br>typecasts<br>66<br>as<br>a<br>character<br>=<br>B                                                   |
| 24. | A | A=5                                                                                                                  |
|     |   | Loop<br>iterations                                                                                                   |
|     |   | x=0<br>A<br>=<br>6                                                                                                   |
|     |   | x=1<br>A<br>=<br>17<br>then<br>A<br>=<br>-17                                                                         |
|     |   | x=2<br>A<br>=<br>17                                                                                                  |
|     |   | x=3<br>A<br>=<br>18<br>then<br>A<br>=<br>19                                                                          |
|     |   | x=4<br>A<br>=<br>9<br>then<br>A<br>=<br>18                                                                           |
|     |   | x=5<br>A<br>=<br>36                                                                                                  |
|     |   | x=6<br>A<br>=<br>-36                                                                                                 |
|     |   | x=7<br>A<br>=<br>-35<br>then<br>A<br>=<br>-34                                                                        |
|     |   | x=8<br>A=-33                                                                                                         |
|     |   | x=9<br>No<br>Change                                                                                                  |
| 25. | D | Go(2)<br>does<br>not<br>recurse.                                                                                     |
|     |   | The<br>second<br>if<br>returns<br>us<br>a<br>value<br>of<br>4                                                        |

| 26. | A | Go(3)<br>recurses                                                                                                                                                                                                                                                                             |
|-----|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     |   | Go(3)<br>=<br>Go(2)<br>+<br>5<br>Go(2)<br>=<br>4                                                                                                                                                                                                                                              |
|     |   | So,<br>Go(3)<br>is<br>9                                                                                                                                                                                                                                                                       |
| 27. | D | Go(33)<br>recurses                                                                                                                                                                                                                                                                            |
|     |   | Go(33)<br>=<br>Go(32)<br>+<br>5                                                                                                                                                                                                                                                               |
|     |   | Go(32)<br>=<br>Go(31)<br>+<br>5                                                                                                                                                                                                                                                               |
|     |   | Go(31)<br>=<br>Go(30)<br>+<br>5                                                                                                                                                                                                                                                               |
|     |   | continues<br>Go(3)<br>=<br>Go(2)<br>+<br>5                                                                                                                                                                                                                                                    |
|     |   | Go(2)<br>=<br>4                                                                                                                                                                                                                                                                               |
|     |   | 5<br>is<br>added<br>with<br>each<br>call.                                                                                                                                                                                                                                                     |
|     |   | There<br>are<br>31<br>calls<br>from<br>33<br>to<br>3                                                                                                                                                                                                                                          |
|     |   | So,<br>4<br>+<br>31(5)<br>=<br>159                                                                                                                                                                                                                                                            |
| 28. | C | At<br>this<br>point,<br>shorter<br>has<br>only<br>one<br>value                                                                                                                                                                                                                                |
| 29. | C | When<br>we<br>print<br>shorter.peek()<br>it<br>prints<br>36<br>Here<br>is<br>the<br>evolution<br>of<br>tall                                                                                                                                                                                   |
|     |   | [<br>]                                                                                                                                                                                                                                                                                        |
|     |   | [12]                                                                                                                                                                                                                                                                                          |
|     |   | [12,<br>24]                                                                                                                                                                                                                                                                                   |
|     |   | [12,<br>24,<br>48]                                                                                                                                                                                                                                                                            |
|     |   | [12,<br>24,<br>48,<br>60]                                                                                                                                                                                                                                                                     |
|     |   | [12,<br>24,<br>48]<br>[12,<br>24,<br>48,<br>72]                                                                                                                                                                                                                                               |
|     |   | [12,<br>24,<br>48]                                                                                                                                                                                                                                                                            |
|     |   | [12,<br>24]                                                                                                                                                                                                                                                                                   |
| 30. | A | Here<br>is<br>the<br>evolution<br>of<br>shorter                                                                                                                                                                                                                                               |
|     |   | [<br>]                                                                                                                                                                                                                                                                                        |
|     |   | [36]<br>[36,<br>60]                                                                                                                                                                                                                                                                           |
|     |   | [36,<br>60,<br>72]                                                                                                                                                                                                                                                                            |
| 31. | D | Here<br>is<br>the<br>step-by-step<br>evolution<br>of<br>x                                                                                                                                                                                                                                     |
|     |   | x<br>=<br>8                                                                                                                                                                                                                                                                                   |
|     |   | x<br>=<br>15                                                                                                                                                                                                                                                                                  |
|     |   | Is<br>(x>=12)?<br>Yes<br>x<br>=<br>12                                                                                                                                                                                                                                                         |
|     |   | x<br>=<br>13                                                                                                                                                                                                                                                                                  |
|     |   | Is<br>(x>=12)?<br>Yes                                                                                                                                                                                                                                                                         |
|     |   | x<br>=<br>10                                                                                                                                                                                                                                                                                  |
|     |   | x<br>=<br>11                                                                                                                                                                                                                                                                                  |
|     |   | Is<br>(x>=12)?<br>No                                                                                                                                                                                                                                                                          |
| 32. | E | Print<br>11<br>The<br>Dog<br>class<br>has<br>no<br>class<br>variables,<br>both<br>A<br>and<br>B<br>are<br>instance<br>variables.                                                                                                                                                              |
|     |   | The<br>key<br>word<br>to<br>look<br>for<br>on<br>class<br>variables<br>is<br>"static"                                                                                                                                                                                                         |
| 33. | D | Doing<br>a<br>little<br>algebra,<br>one<br>can<br>see<br>that<br>the<br>display<br>method<br>will<br>output<br>2A<br>+<br>B<br>+<br>2                                                                                                                                                         |
|     |   | For<br>R,<br>A=11<br>and<br>B<br>=<br>22                                                                                                                                                                                                                                                      |
|     |   | 2(11)<br>+<br>22<br>+<br>2<br>=<br>46                                                                                                                                                                                                                                                         |
| 34. | D | Doing<br>a<br>little<br>algebra,<br>one<br>can<br>see<br>that<br>the<br>display<br>method<br>will<br>output<br>2A<br>+<br>B<br>+<br>2                                                                                                                                                         |
|     |   | For<br>S,<br>A=3<br>and<br>B<br>=<br>7<br>2(3)<br>+<br>7<br>+<br>2<br>=<br>15                                                                                                                                                                                                                 |
| 35. | D | The<br>loop<br>goes<br>through<br>all<br>the<br>letters<br>A<br>-<br>J<br>and<br>takes<br>a<br>sum<br>of<br>the<br>ASCII<br>values.<br>Thus,<br>it<br>add<br>the                                                                                                                              |
|     |   | numbers<br>65<br>through<br>76<br>getting<br>a<br>sum<br>of<br>846.                                                                                                                                                                                                                           |
| 36. | B | As<br>the<br>tree<br>is<br>created,<br>each<br>new<br>node<br>is<br>a<br>leaf<br>that<br>becomes<br>the<br>right<br>child<br>of<br>the<br>bottom-most                                                                                                                                         |
|     |   | node<br>which<br>loses<br>its<br>"leaf<br>status".<br>So<br>after<br>the<br>first<br>10<br>nodes,<br>there<br>is<br>only<br>one<br>leaf.                                                                                                                                                      |
|     |   | Then<br>as<br>the<br>next<br>ten<br>nodes<br>are<br>added,<br>the<br>first<br>is<br>added<br>to<br>the<br>left<br>of<br>the<br>J<br>leaf,<br>but<br>the<br>next                                                                                                                               |
| 37. | D | nine<br>are<br>added<br>to<br>the<br>left<br>of<br>nodes<br>that<br>are<br>not<br>leafs.<br>Thus,<br>we<br>will<br>have<br>10<br>leafs.<br>With<br>each<br>iteration<br>of<br>the<br>loop,<br>C<br>is<br>multiplied<br>by<br>the<br>ones<br>digit.<br>N<br>is<br>then<br>divided<br>by<br>10, |
|     |   | removing<br>the<br>ones<br>digit.<br>This<br>will<br>stop<br>after<br>three<br>iterations.                                                                                                                                                                                                    |
|     |   | 9<br>*<br>8<br>*<br>7<br>=<br>504                                                                                                                                                                                                                                                             |
|     |   |                                                                                                                                                                                                                                                                                               |

| 38. | B | With<br>each<br>pass<br>through<br>the<br>loop,<br>the<br>values<br>of<br>A,<br>B,<br>and<br>C<br>rotate<br>amongst<br>themselves<br>with<br>D<br>serving<br>as<br>a<br>helper.<br>A=5<br>B=7<br>C=9<br>Original<br>List<br>A=7<br>B=9<br>C=5<br>After<br>Pass<br>#1<br>A=9<br>B=5<br>C=7<br>After<br>Pass<br>#2<br>A=5<br>B=7<br>C=9<br>After<br>Pass<br>#3<br>After<br>every<br>3<br>passes,<br>the<br>numbers<br>are<br>back<br>in<br>the<br>original<br>order.<br>After<br>999<br>passes,<br>they<br>are<br>in<br>the<br>original<br>order.<br>After<br>one<br>more<br>pass,<br>A=7<br>B=9<br>C=5                                                    |
|-----|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 39. | G | Here<br>is<br>the<br>evolution<br>of<br>the<br>queue:<br>[A]<br>[A,<br>B]<br>[A,<br>B,<br>C]<br>[B,<br>C]<br>[C]<br>[C,<br>D]<br>[C,<br>D,<br>E]<br>[D,<br>E]<br>[D,<br>E,<br>F]<br>[E,<br>F]<br>[E,<br>F,<br>G]<br>[E,<br>F,<br>G,<br>H]<br>[E,<br>F,<br>G,<br>H,<br>I]<br>[F,<br>G,<br>H,<br>I]<br>[G,<br>H,<br>I]<br>[G,<br>H,<br>I,<br>J]                                                                                                                                                                                                                                                                                                            |
| 40. | 4 | Using<br>DeMorgan's<br>Law<br>on<br>the<br>first<br>part<br>of<br>the<br>expression,<br>then<br>finding<br>the<br>"product"<br>of<br>the<br>binomials<br>is<br>a<br>good<br>route<br>to<br>take.<br>But,<br>we<br>can<br>always<br>just<br>inspect<br>the<br>two<br>terms.<br>Since<br>there<br>is<br>an<br>AND<br>statement,<br>both<br>parts<br>must<br>be<br>true.<br>- A<br>and<br>B<br>cannot<br>both<br>be<br>true<br>(This<br>eliminates<br>110<br>and<br>111)<br>𝐴 * 𝐵<br>Either<br>A<br>or<br>C<br>has<br>to<br>be<br>true.<br>(This<br>eliminates<br>000<br>and<br>010)<br>Four<br>combinations<br>work:<br>000,<br>010,<br>110,<br>and<br>111 |