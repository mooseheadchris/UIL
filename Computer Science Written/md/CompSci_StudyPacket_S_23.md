# **UIL COMPUTER SCIENCE WRITTEN TEST – 2023 STATE**

**Note:** Correct responses are based on **Java SE Development Kit 17 (JDK 17)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 17 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

## **Question 1i** If the values of the five numbers were converted to a common base and sorted, which one would be in the middle - larger than two numbers and smaller than the other two? **A)** 11011101<sup>2</sup> **B)** 265<sup>8</sup> **C)** 180<sup>10</sup> **D)** B9<sup>16</sup> **E)** 3333<sup>4</sup> **Question 2uesti** What is the output of the code segment to the right? **A)** -3 **B)** 20 **C)** 21 **D)** 53 **E)** 9 out.print(23 + 37 / 7 % 2 - 24 % 5); **Question 3** What is the output of the code segment to the right? **A)** 68-13.60-c **B)** 68-13.00-c **C)** 68-13.60-D **D)** 68-13.00-D **E)** 54.40-D int May = 68; double State = May / 5; String St ="%d-%.2f-%c"; out.printf(St, May, State, May); **Question 4** What is the output of the code segment to the right? **A)** INAS **B)** STXA **C)** USAS **D)** TIXA **E)** INXA String One = "TEXAS"; String Two = "AUSTIN"; int A = Two.indexOf("T"); int B = One.indexOf("S"); String Three = One.substring(A); String Four = Two.substring(B); out.print(Four+Three); **Question 5** What is the output of the code segment to the right? **A)** true **B)** false int A = 4; int B = 7; int C = 2; boolean D = (A>C) && (B<A); boolean E = (A + B == 10)||(A >= C\*2); boolean F = D ^ E; out.print(F); **Question 6** What is the output of the code segment to the right? **A)** 11 **B)** 12 **C)** 13 **D)** 14 **E)** 15 int H = 5; int J = (int)(Math.pow(H,3)); int L = (int)(Math.sqrt(J)); out.print(L); **Question 7** What is the output of the code segment to the right? **A)** 50 **B)** 52 **C)** 54 **D)** 56 **E)** 58 int A = 10; int B = 25; int Z = A + B % A \* A - B / A; out.print(Z);

```
Question 8
What is the output of the code segment to the right?
A) 35
B) 45
C) 55
D) 65
E) 75
                                                int AA = 20;
                                                int BB = 15;
                                                int CC = 10;
                                                if (AA - BB > CC / 2)
                                                  AA += CC;
                                                if (BB % CC == 0)
                                                  AA += CC;
                                                else
                                                  AA += BB;
                                                if (AA % CC == 5)
                                                  AA += CC;
                                                else if (AA > 100)
                                                        AA -= 100;
                                                out.print(AA);
Question 9
What is the output of the code segment to the right?
A) 11121314151
B) 2345
C) 14
D) 1021324354
E) 111213141
                                                for(int x = 1; x <= 50; x += 10)
                                                   out.print(x / 10 * 10 + x % 10 );
Question 10
What is the output of the code segment to the right?
A) 14 B) 18 C) 21 D) 23 E) 30
                                                int[] Miller = {5,1,2,9,2,6,7,4,1,7};
                                                int F = Miller[Miller.length-1];
                                                for(int x=0; x<Miller.length; x++)
                                                  if (Miller[x]%2==0)
                                                    F += Miller[x];
                                                out.print(F);
Question 11
What is output by the code segment to the right?
A) EAG B) ECG C) FBF D) FDJ E) BDF
                                                String St = "AB CD EF GH IJ";
                                                St += St;
                                                Scanner Sc = new Scanner(St);
                                                for(int x = 1; x <= 3; x++)
                                                {
                                                  Sc.next();
                                                  Sc.next();
                                                  out.print(Sc.next().substring(1));
                                                }
Question 12
What is the output of the code segment to the right?
A) 201 B) 209 C) 219 D) 221 E) 229
                                               int G = 0;
                                                for (int x=10; x<=50; x++)
                                                  G += (int)(Math.sqrt(x)+0.5);
                                                out.print(G);
```

#### **Question 13** What is the output of the code segment to the right? **A)** 7 **B)** 12 **C)** 15 **D)** 21 **E)** 23 int R = 20; int Y = R >> 2 ^ 2 + R & 11; out.print(Y); **Question 14** What is the output of the code segment shown on the right? **A)** 2 **B)** 4 **C)** 6 **D)** 8 **E)** 12 int K = Integer.SIZE; int L = Double.SIZE; int M = Byte.SIZE; out.println(K / M + L / K); **Question 15** What is output by the code segment to the right? **A)** [10, 20, 30, 40, 50] **B)** [50, 40, 30, 20, 10] **C)** [10, 10, 20, 20, 30] **D)** [50, 50, 40, 40, 30] **E)** [1, 0, 2, 0, 3] ArrayList<Integer> soup; soup = new ArrayList<Integer>(); for(int x = 1; x<=5; x++) { soup.add(x); soup.add(0,x\*10); soup.remove(soup.size()-1); } out.print(soup); **Question 16** What is the output of the code segment shown on the right? **A)** 100 **B)** 121 **C)** 144 **D)** 169 **E)** 625 int N = 25; int z=0; for(int x=1; x<=N; x+=2) z +=x; out.print(z); **Question 17** What is the output of the code segment shown on the right? **A)** 75 **B)** 80 **C)** 84 **D)** 100 **E)** 105 int N=0; String St = ""; for(int x=0; x<=20; x++) { St = Integer.toBinaryString(x); N += St.length(); } out.print(N); **Question 18** What is the output of the code segment shown on the right? **A)** 498 **B)** 992 **C)** 1000 **D)** 1024 **E)** 2000 int N = 1000; for (int x=1; x<=5; x++) N = N>>1; for (int x=1; x<=5; x++) N = N<<1; out.print(N);

#### **Question 19**

What is the output of the code segment shown on the right?

- **A)** AB BC CD DE EF FG GH
- **B)** AB BC GH FG EF DE CD
- **C)** GH FG AB BC EF DE CD
- **D)** GH AB BC CD DE EF FG
- **E)** GH FG AB BC CD DE EF

```
String[]VV = {"AB","BC","CD","DE","EF","FG","GH"};
for(int x=VV.length-1;x>=2;x--)
 {
   String Closet = VV[x];
   VV[x] = VV[x-2];
   VV[x-2] = Closet;
 }
for(int x=0; x<VV.length; x++)
  out.print(VV[x]+ " ");
```

### **Question 20**

In the code segment to the right, what is the output of line 1?

- **A)** 50 **B)** 60 **C)** 70 **D)** 80 **E)** 90

### **Question 21**

In the code segment to the right, what is the output of line 2?

- **A)** 50 **B)** 60 **C)** 61 **D)** 62 **E)** 70

#### **Question 22**

In the code segment to the right, what is the output of line 3?

- **A)** 50 **B)** 61 **C)** 69 **D)** 70 **E)** 71

```
public class Rockford
{
   private int A;
   private int B;
   private int C;
   public Rockford(int D)
   {
      A = D;
      B = D++;
      C = --D;
   }
   public int getOne()
   {
      return A * 5;
   }
   public int getTwo()
   {
      return getOne() + B;
   }
   public int getThree()
   {
      return getTwo() + C;
   }
}
//////////////////////////////////
// Client code
Rockford Jim = new Rockford(10);
System.out.println(Jim.getOne()); //Line 1
System.out.println(Jim.getTwo()); //Line 2
System.out.println(Jim.getThree());//Line 3
```

#### **Question 23**

What is the output of the code segment shown on the right?

- **A)** 4 **B)** 6 **C)** 8 **D)** 10 **E)** 12
- String St = "BEAR OWL DOG CAT LION "; St += "ZEBRA RAT PIG TIGER GORILLA"; int N = 0; Scanner Sue = new Scanner(St); while(Sue.hasNext()) { Sue.next(); String A = Sue.next(); if(A.matches("..O.")) N++; if(A.matches("[A-C].\*")) N++; if(A.matches("..G")) N++; if(A.matches(".\*R.\*")) N++; } out.print(N);

#### **Question 24**

In the code segment to the right, what is the output of line 1?

- **A)** 2 **B)** 3 **C)** 6 **D)** 10 **E)** 14

### **Question 25**

In the code segment to the right, what is the output of line 2?

- **A)** 2 **B)** 3 **C)** 6 **D)** 10 **E)** 14

## **Question 26**

In the code segment to the right, what is the output of line 3?

- **A)** 2 **B)** 3 **C)** 6 **D)** 10 **E)** 14

```
HashSet<Integer>HS;
HS =new HashSet<Integer>();
int[]Nums = {8,0,6,3,5,2,4,3,6,3};
int[]More = {5,1,2,6,5,3,1,4,6,4};
for(int x=0; x<Nums.length; x++)
  HS.add(Nums[x]);
for(int x=0; x<More.length; x++)
  HS.add(More[x]);
TreeMap<String,Integer>Tree;
Tree = new TreeMap<String,Integer>();
Tree.put("BIG",0);
Tree.put("SMALL",0);
Tree.put("STRANGE",0);
for (int Bob: HS)
  {
    int A = Tree.get("BIG");
    int B = Tree.get("SMALL");
    int C = Tree.get("STRANGE");
    if (Bob>5)
       Tree.put("BIG",A+1);
    else
       Tree.put("SMALL",B+1);
    if (Bob%2==1)
       Tree.put("STRANGE",C+1);
   }
out.println(Tree.get("BIG")); //Line 1
out.println(Tree.get("SMALL")); //Line 2
out.println(Tree.get("STRANGE"));//Line 3
```

#### **Question 27** Find the value of Go(33). **A)** 3 **B)** 6 **C)** 33 **D)** 36 **E)** 39 public static int Go(int N) { int A = N / 10; int B = N % 10; if (A==B) return N; if (A > B) return A + Go(N+2); return B + Go(N+3); } **Question 28** FFind the value of Go(20). **A)** 14 **B)** 18 **C)** 20 **D)** 22 **E)** 24 **Question 29** Find the value of Go(1). **A)** 11 **B)** 55 **C)** 76 **D)** 114 **E)** 132 **Question 30** List the operators to the right in order from highest precedence to lowest precedence ? **A)** I II III **B)** III II I **C)** II I III D) I III II **E)** II III I I % II ^ III >> **Question 31** In the code to the right, what is output by line #1? **A)** 22 **B)** 24 **C)** 25 **D)** 27 **E)** 28 public static int Find(int nums[], int L, int R, int T) { int middle = (L + R)/2; int C = 0; while(L <= R) { C++; if (nums[middle] < T ) L = middle + 1; else if(nums[middle] > T) R = middle -1; else return middle + C; middle = (L + R)/2; } return -1; } //////////////////////////////////////////////// /// Client Code int[]nums = {1,2,2,2,2,4,6,7,7,7,9,10,11,11,11,23,34,45,45,45,56}; out.print(Find(nums,0,20,56)); // Line 1 out.print(Find(nums,0,20,45)); // Line 2 out.print(Find(nums,0,20,2)); // Line 3 **Question 32** In the code to the right, what is output by line #2? **A)** 20 **B)** 21 **C)** 22 **D)** 23 **E)** 24 **Question 33** In the code to the right, what is output by line #3? **A)** 2 **B)** 3 **C)** 4 **D)** 5 **E)** 6

#### **Question 34**

What is the output of the code segment shown on the right?

- **A)** 0
- **B)** 7
- **C)** 14
- **D)** 21
- **E)** 28

## **Question 35**

Assume that class One from problem #34 exists. Now assume that class Two to the right extends class one . Which five lines of the client code to the right will cause a compiler error?

- **A)** 4 11 14 15 16
- **B)** 4 11 12 14 16
- **C)** 4 12 14 15 16
- **D)** 6 7 11 12 13
- **E)** 6 7 10 13 16

```
public class One
 {
   private int A;
   public int B;
   public One(int Z)
    {
      A = Z;
      B = Z & (Z - 1);
    }
   public int getA()
   {
     return A ^ (A - 1);
   }
   public int getB()
   {
     return B & (B - 1);
   }
}
///////////////////////////////////////////
// Client Code
   One Uno = new One(7);
   One Dos = new One(12);
   out.print(Uno.getB()*Dos.getA());
 public class Two extends One
 {
```

```
private int A;
   private int E;
   public Two(int H, int G)
   {
     super(H*G);
     A = H;
     E = G;
   }
   public int getB()
   {
      return B;
   }
   public int getC()
   {
     return E;
   }
 }
//////////////////////////////////////////////
Possible Client Code
One Alpha = new One(12); // Line 1
One Beta = new Two(3,4); // Line 2
Two Gamma = new Two(12,16);// Line 3
Two Delta = new One(20); // Line 4
out.println(Alpha.getA()); // Line 5
out.println(Beta.getA()); // Line 6
out.println(Gamma.getA()); // Line 7
out.println(Alpha.getB()); // Line 8
out.println(Beta.getB()); // Line 9
out.println(Gamma.getB()); // Line 10
out.println(Alpha.getC()); // Line 11
out.println(Beta.getC()); // Line 12
out.println(Gamma.getC()); // Line 13
out.println(Gamma.A); // Line 14
out.println(Gamma.B); // Line 15
out.println(Gamma.E); // Line 16
```

## **Question 36** What is the output of the code segment shown on the right? **A)** 1 **B)** 2 **C)** 3 **D)** 4 **E)** 5 String A = new String("Apple"); String B = new String("Banana"); String C = new String("Banana"); String D = new String("Apple"); String E = A; A = B; int N = 0; if(A==B) N++; if(B==C) N++; if(C==D) N++; if(E==A) N++; if (A.equals(C)) N++; if (B.equals(D)) N++; if (C.equals(E)) N++; if (D.equals(B)) N++; out.print(N); **Question 37** What is the output of the code segment shown on the right? **A)** 5 **B)** 10 **C)** 15 **D)** 20 **E)** 25 int[][] Box = new int[5][5]; for(int x=1; x<Box.length; x++) for(int y=1; y<Box[0].length; y++) Box[x][y]=Box[x-1][y-1]+x\*y; out.print(Box[4][3]); **Question 38** What is the output of the code segment shown on the right? **A)** 24 **B)** 25 **C)** 26 **D)** 27 **E)** 28 int N = 16; for(int x=28; x>=21; x--) N ^= x; out.print(N); **Question 39** Evaluate the prefix expression to the right. Write the value in the blank reserved for #39. **+ / \* 3 4 - 17 \* 5 3 / + 6 6 3 Question 40** In the code to the right, we are conducting a Boolean Algebra test. What number will be output by the code? Write the value in the blank reserved for #40. int N=0; for(int A = 0; A<=1; A++) for(int B = 0; B<=1; B++) for(int C = 0; C<=1; C++) for(int D = 0; D<=1; D++) { boolean AA = (A==1); boolean BB = (B==1); boolean CC = (C==1); boolean DD = (D==1); boolean One = (AA&&BB)||(CC&&DD); boolean Two = (AA||BB)&&(CC||DD); if(One==Two) N++; } out.println(N);

![](_page_8_Picture_0.jpeg)

# **UIL COMPUTER SCIENCE – 2023 STATE**

**Questions** (+6 points for each correct answer, -2 points for each incorrect answer)

| 1) | D   | B   | C   |
|----|-----|-----|-----|
| D  | 11) | 21) | 31) |

8) B 18) B 28) E 38) A

5) A 15) B 25) C 35) B

6) A 16) D 26) B 36) B

7) E 17) A 27) C 37) D

2) B 12) C 22) D 32) B

3) D 13) A 23) A 33) E

4) A 14) C 24) A 34) E

9) E 19) E 29) D \*39) 10

10) C 20) A 30) D \*40) 10

**Note:** Correct responses are based on **Java SE Development Kit 17 (JDK 17)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 17 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

*<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.*

# **Explanations:**

| 1. | D | Convert all 5 to a common base…<br>I suggest base 8.                                                                                                           |  |  |  |  |
|----|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
|    |   |                                                                                                                                                                |  |  |  |  |
|    |   | A)11 011 1012<br>= 3358                                                                                                                                        |  |  |  |  |
|    |   | B) 2658<br>= 2658                                                                                                                                              |  |  |  |  |
|    |   | C)18010<br>= 2648                                                                                                                                              |  |  |  |  |
|    |   | D)B916<br>= 2718                                                                                                                                               |  |  |  |  |
|    |   | E)33334<br>= 3778                                                                                                                                              |  |  |  |  |
| 2. | B | 23<br>+<br>37<br>/<br>7<br>%<br>2<br>-<br>24<br>%<br>5                                                                                                         |  |  |  |  |
|    |   | 23<br>+<br>5<br>%2<br>-<br>24<br>%<br>5<br>23<br>+<br>1<br>-<br>24<br>%<br>5                                                                                   |  |  |  |  |
|    |   | 23<br>+<br>1<br>-<br>4                                                                                                                                         |  |  |  |  |
|    |   | 24<br>-<br>4                                                                                                                                                   |  |  |  |  |
|    |   | 20                                                                                                                                                             |  |  |  |  |
| 3. | D | int<br>May<br>=<br>68;<br>May<br>=<br>68                                                                                                                       |  |  |  |  |
|    |   | double<br>State<br>=<br>May<br>/<br>5;<br>State<br>=<br>13.00000                                                                                               |  |  |  |  |
|    |   | String<br>St<br>="%d-%.2f-%c";<br>Creates<br>the<br>format<br>integer-2-decimal<br>double-character<br>out.printf(St,<br>May,<br>State,<br>May);<br>68-13.00-D |  |  |  |  |
|    |   |                                                                                                                                                                |  |  |  |  |
| 4. | A | String<br>One<br>=<br>"TEXAS";                                                                                                                                 |  |  |  |  |
|    |   | String<br>Two<br>=<br>"AUSTIN";                                                                                                                                |  |  |  |  |
|    |   | int<br>A<br>=<br>Two.indexOf("T");<br>A=3<br>int<br>B<br>=<br>One.indexOf("S");<br>B=4                                                                         |  |  |  |  |
|    |   | String<br>Three<br>=<br>One.substring(A);<br>Three<br>=<br>"AS"                                                                                                |  |  |  |  |
|    |   | String<br>Four<br>=<br>Two.substring(B);<br>Four<br>=<br>"IN"                                                                                                  |  |  |  |  |
|    |   | out.print(Four+Three);<br>"INAS"                                                                                                                               |  |  |  |  |
| 5. | A | int<br>A<br>=<br>4;                                                                                                                                            |  |  |  |  |
|    |   | int<br>B<br>=<br>7;                                                                                                                                            |  |  |  |  |
|    |   | int<br>C<br>=<br>2;<br>boolean<br>D<br>=<br>(A>C)<br>&&<br>(B <a);<br>D<br/>=<br/>false</a);<br>                                                               |  |  |  |  |
|    |   | boolean<br>E<br>=<br>(A<br>+<br>B<br>==<br>10)  (A<br>>=<br>C*2);<br>E<br>=<br>true                                                                            |  |  |  |  |
|    |   | boolean<br>F<br>=<br>D<br>^<br>E;<br>XOR<br>F<br>=<br>true                                                                                                     |  |  |  |  |
|    |   | out.print(F);                                                                                                                                                  |  |  |  |  |
|    |   |                                                                                                                                                                |  |  |  |  |
| 6. | A | int<br>H<br>=<br>5;<br>int<br>J<br>=<br>(int)(Math.pow(H,3));<br>J<br>=<br>125                                                                                 |  |  |  |  |
|    |   | int<br>L<br>=<br>(int)(Math.sqrt(J));<br>L<br>=<br>(int)(11.18)<br>=<br>11                                                                                     |  |  |  |  |
|    |   | out.print(L);                                                                                                                                                  |  |  |  |  |
| 7. | E | int<br>A<br>=<br>10;                                                                                                                                           |  |  |  |  |
|    |   | int<br>B<br>=<br>25;                                                                                                                                           |  |  |  |  |
|    |   | int<br>Z<br>=<br>A<br>+<br>B<br>%<br>A<br>*<br>A<br>-<br>B<br>/<br>A;                                                                                          |  |  |  |  |
|    |   | 10<br>+<br>25<br>%<br>10<br>*<br>10<br>-<br>25<br>/<br>10<br>10<br>+<br>5<br>*<br>10<br>-<br>25<br>/<br>10                                                     |  |  |  |  |
|    |   | 10<br>+<br>50<br>-<br>25<br>/<br>10                                                                                                                            |  |  |  |  |
|    |   | 10<br>+<br>50<br>-<br>2                                                                                                                                        |  |  |  |  |
|    |   | 60<br>-<br>2<br>=<br>58                                                                                                                                        |  |  |  |  |
|    |   |                                                                                                                                                                |  |  |  |  |
|    |   |                                                                                                                                                                |  |  |  |  |
|    |   |                                                                                                                                                                |  |  |  |  |
|    |   |                                                                                                                                                                |  |  |  |  |

```
8. B int AA = 20;
                     int BB = 15;
                     int CC = 10;
                     if (AA - BB > CC / 2) false!!!!
                      AA += CC;
                     if (BB % CC == 0) false!!! do the else
                      AA += CC;
                     else
                      AA += BB; AA is now 35
                     if (AA % CC == 5) true!!!
                      AA += CC; AA is now 45
                     else if (AA > 100)
                        AA -= 100;
                     out.print(AA);
9. E for(int x = 1; x <= 50; x += 10)
                      out.print(x / 10 * 10 + x % 10 );
                    Iteration 1: x is 1 1/10*10 + 1%10 = 0+1=1
                    Iteration 2: x is 11 11/10*10 + 11%10 = 10+1=11
                    Iteration 3: x is 21 21/10*10 + 11%10 = 20+1=21
                    Iteration 4: x is 31 31/10*10 + 11%10 = 30+1=31
                    Iteration 5: x is 41 41/10*10 + 11%10 = 40+1=41
10. C int[] Miller = {5,1,2,9,2,6,7,4,1,7};
                     int F = Miller[Miller.length-1];
                     for(int x=0; x<Miller.length; x++)
                      if (Miller[x]%2==0)
                       F += Miller[x];
                     out.print(F);
                    F = 7 before the loop begins
                    Then, we add all the even values to F
                    F = 21
11. D String St = "AB CD EF GH IJ";
                     St += St; St ="AB CD EF GH IJAB CD EF GH IJ";
                                                    Notice no space between IJ and AB
                    Scanner Sc = new Scanner(St);
                     for(int x = 1; x <= 3; x++) The loop skips 2 strings then processes the 3rd, three times.
                     {
                      Sc.next(); EF CD IJ
                      Sc.next(); Printing letter #1 in each gives us FDJ
                      out.print(Sc.next().substring(1));
                     }
```

| 12. | C                                                               | int<br>G<br>=<br>0;<br>41<br>iterations                                                                                   |
|-----|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
|     |                                                                 | for<br>(int<br>x=10;<br>x<=50;<br>x++)<br>10-12<br>Add<br>3<br>3*3<br>=<br>9                                              |
|     |                                                                 | G<br>+=<br>(int)(Math.sqrt(x)+0.5);<br>13-20<br>Add<br>4<br>8*4=32                                                        |
|     |                                                                 | out.print(G);<br>21-30<br>Add<br>5<br>10*5=50                                                                             |
|     |                                                                 | 31-42<br>Add<br>6<br>12*6=72                                                                                              |
|     |                                                                 | 43-50<br>Add<br>7<br>8*7=56                                                                                               |
| 13. | A                                                               | G<br>=<br>219<br>int<br>R<br>=<br>20;                                                                                     |
|     |                                                                 | int<br>Y<br>=<br>R<br>>><br>2<br>^<br>2<br>+<br>R<br>&<br>11;                                                             |
|     |                                                                 | out.print(Y);                                                                                                             |
|     |                                                                 |                                                                                                                           |
|     |                                                                 | Order<br>of<br>precedence:<br>+<br>>><br>&<br>^                                                                           |
|     |                                                                 | 20<br>>><br>2<br>^<br>2<br>+<br>20<br>&<br>11                                                                             |
|     |                                                                 | 20<br>>><br>2<br>^<br>22<br>&<br>11                                                                                       |
|     |                                                                 | 5<br>^<br>22<br>&<br>11                                                                                                   |
|     |                                                                 | 5<br>^<br>2                                                                                                               |
| 14. | C                                                               | 101<br>^<br>010<br>=<br>111<br>=<br>7                                                                                     |
|     |                                                                 | int<br>K<br>=<br>Integer.SIZE;<br>32                                                                                      |
|     |                                                                 | int<br>L<br>=<br>Double.SIZE;<br>64                                                                                       |
|     |                                                                 | int<br>M<br>=<br>Byte.SIZE;<br>8                                                                                          |
| 15. | B                                                               | out.println(K<br>/<br>M<br>+<br>L<br>/<br>K);<br>32/8<br>+<br>64/32<br>=<br>4+2<br>=<br>6                                 |
|     |                                                                 | ArrayList <integer><br/>soup;</integer>                                                                                   |
|     |                                                                 | soup<br>=<br>new<br>ArrayList <integer>();</integer>                                                                      |
|     |                                                                 | for(int<br>x<br>=<br>1;<br>x<=5;<br>x++)                                                                                  |
|     |                                                                 | {                                                                                                                         |
|     |                                                                 | soup.add(x);                                                                                                              |
|     |                                                                 | soup.add(0,x*10);                                                                                                         |
|     |                                                                 | soup.remove(soup.size()-1);<br>}                                                                                          |
|     |                                                                 | out.print(soup);                                                                                                          |
|     |                                                                 | Iteration<br>1:<br>[]<br>then<br>[1]<br>then<br>[10,<br>1]<br>then<br>[10]                                                |
|     |                                                                 | Iteration<br>2:<br>[10]<br>then<br>[10,2]<br>then<br>[20,10,<br>2]<br>then<br>[20,10]                                     |
|     |                                                                 | Iteration<br>3:<br>[20,10]<br>then<br>[20,10,3]<br>then<br>[30,20,10,<br>3]<br>then<br>[30,20,10]                         |
|     |                                                                 | Iteration<br>4:<br>[30,20,10]<br>then<br>[30,20,10,4]<br>then<br>[40,30,20,10,<br>4]<br>then<br>[40,30,20,10]             |
|     |                                                                 | Iteration<br>5:<br>[40,30,20,10]<br>then<br>[40,30,20,10,5]<br>then<br>[50,40,30,20,10,<br>5]<br>then<br>[50,40,30,20,10] |
| 16. | D                                                               | int<br>N<br>=<br>25;                                                                                                      |
|     |                                                                 | int<br>z=0;                                                                                                               |
|     |                                                                 | for(int<br>x=1;<br>x<=N;<br>x+=2)                                                                                         |
|     |                                                                 | z<br>+=x;                                                                                                                 |
|     |                                                                 | out.print(z);                                                                                                             |
|     | 2<br>Add<br>the<br>first<br>N<br>odds<br>and<br>you<br>get<br>N |                                                                                                                           |
|     |                                                                 | This<br>adds<br>the<br>first<br>13<br>odds<br>and<br>gets<br>169                                                          |
| 17  | A                                                               | This<br>adds<br>the<br>lengths<br>of<br>the<br>binary<br>strings<br>from<br>0<br>to<br>20.                                |
|     |                                                                 | 0,1<br>=<br>2                                                                                                             |
|     |                                                                 |                                                                                                                           |
|     |                                                                 | 10,11<br>=<br>4                                                                                                           |
|     |                                                                 | 100,101,110,111<br>=<br>12                                                                                                |
|     |                                                                 | 1000,1001,1010,1011,1100,1101,<br>1110,<br>1111<br>=<br>32                                                                |
|     |                                                                 | 10000,10001,10010,10011,10100<br>=<br>25                                                                                  |
|     |                                                                 | The<br>sum<br>of<br>the<br>lengths<br>is<br>75                                                                            |
|     |                                                                 |                                                                                                                           |
|     |                                                                 |                                                                                                                           |

| B | This<br>does<br>1000>>5<br>followed<br>by<br>a<br><<5<br>1000,500,250,125,62,<br>31<br>31,<br>62,<br>124,<br>248,<br>496,<br>992           |  |  |  |
|---|--------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|
| E | "AB","BC","CD","DE","EF","FG","GH"                                                                                                         |  |  |  |
|   | Starting at the last element, this routine swaps the element x with element x-2.                                                           |  |  |  |
|   | This continues until =2.                                                                                                                   |  |  |  |
|   | x=6 "AB","BC","CD","DE","GH","FG","EF"                                                                                                     |  |  |  |
|   | x=5 "AB","BC","CD","FG","GH","DE","EF"                                                                                                     |  |  |  |
|   | x=4 "AB","BC","GH","FG","CD","DE","EF"                                                                                                     |  |  |  |
|   | x=3 "AB","FG","GH","BC","CD","DE","EF"                                                                                                     |  |  |  |
|   | x=2 "GH","FG","AB","BC","CD","DE","EF"                                                                                                     |  |  |  |
| A | Rockford Jim = new Rockford(10);                                                                                                           |  |  |  |
|   | When the constructor is called, A, B, and C are all initialized to 10.                                                                     |  |  |  |
|   | getOne() returns a 50                                                                                                                      |  |  |  |
| B | getTwo()<br>returns<br>getOne()<br>+<br>10<br>=<br>60                                                                                      |  |  |  |
| D | getThree()<br>returns<br>getTwo()<br>+<br>10<br>=<br>70                                                                                    |  |  |  |
|   | "BEAR OWL DOG CAT LION ZEBRA RAT PIG TIGER GORILLA"                                                                                        |  |  |  |
|   | The<br>loop<br>tests<br>these<br>values<br>for<br>A:<br>"OWL CAT ZEBRA PIG GORILLA"                                                        |  |  |  |
|   | if(A.matches("O."))<br>N++;<br>no matches                                                                                                  |  |  |  |
|   | if(A.matches("[A-C].*"))<br>N++;<br>CAT                                                                                                    |  |  |  |
|   | if(A.matches("G"))<br>N++;<br>PIG                                                                                                          |  |  |  |
|   |                                                                                                                                            |  |  |  |
|   | if(A.matches(".*R.*"))<br>N++;<br>ZEBRA GORILLA<br>4<br>matches                                                                            |  |  |  |
|   | The<br>HashSet<br>HS<br>takes<br>on<br>these<br>values<br>{0,1,2,3,4,5,6,8}<br>in<br>some<br>order.<br>Sets<br>cannot<br>have<br>duplicate |  |  |  |
|   | values.                                                                                                                                    |  |  |  |
|   | A<br>TreeMap<br>is<br>set<br>up<br>using<br>the<br>Strings<br>BIG,<br>SMALL,<br>and<br>STRANGE.                                            |  |  |  |
|   | BIG<br>numbers:<br>Those<br>in<br>HS<br>that<br>are<br>greater<br>than<br>5<br>2<br>is<br>the<br>answer<br>here.                           |  |  |  |
|   | SMALL<br>numbers:<br>Those<br>in<br>HS<br>that<br>are<br>not<br>greater<br>than<br>5                                                       |  |  |  |
|   | 6<br>is<br>the<br>answer<br>here.                                                                                                          |  |  |  |
| B | STRANGE<br>numbers:<br>Those<br>in<br>HS<br>that<br>are<br>odd                                                                             |  |  |  |
|   | 3<br>is<br>the<br>answer<br>here.                                                                                                          |  |  |  |
|   | go(33)<br>=<br>33<br>go(20)<br>=<br>2<br>+<br>go(22)<br>=<br>24                                                                            |  |  |  |
|   | go(22)<br>=<br>22                                                                                                                          |  |  |  |
| D | go(1)<br>=<br>1<br>+<br>go(4)<br>=<br>114                                                                                                  |  |  |  |
|   | go(4)<br>=<br>4<br>+<br>go(7)<br>=<br>113                                                                                                  |  |  |  |
|   | go(7)<br>=<br>7<br>+<br>go(10)<br>=<br>109                                                                                                 |  |  |  |
|   | go(10)<br>=<br>1<br>+<br>go<br>(12)<br>=<br>102<br>go(12)<br>=<br>2<br>+<br>go(15)<br>=<br>101                                             |  |  |  |
|   | go(15)<br>=<br>5<br>+<br>go(18)<br>=<br>99                                                                                                 |  |  |  |
|   | go(18)<br>=<br>8<br>+<br>go<br>(21)<br>=<br>94                                                                                             |  |  |  |
|   | go(21)<br>=<br>2<br>+<br>go(23)<br>=<br>86                                                                                                 |  |  |  |
|   | go(23)<br>=<br>3<br>+<br>go(26)<br>=<br>84<br>go(26)<br>=<br>6<br>+<br>go(29)<br>=<br>81                                                   |  |  |  |
|   | go(29)<br>=<br>9<br>+<br>go(32)<br>=<br>75                                                                                                 |  |  |  |
|   | go(32)<br>=<br>3<br>+<br>go(34)<br>=<br>66                                                                                                 |  |  |  |
|   | go(34)<br>=<br>4<br>+<br>go(37)<br>=<br>63                                                                                                 |  |  |  |
|   | go(37)<br>=<br>7<br>+<br>go(40)<br>=<br>59                                                                                                 |  |  |  |
|   | go(40)<br>=<br>4<br>+<br>go(42)<br>=<br>52<br>go(42)<br>=<br>4<br>+<br>go(44)<br>=<br>48                                                   |  |  |  |
|   | go(44)<br>=<br>44                                                                                                                          |  |  |  |
|   | A<br>A<br>C<br>C<br>E                                                                                                                      |  |  |  |

| 30. | D | %<br>>><br>^                                                                                                                 |  |  |  |  |
|-----|---|------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|
| 31. | C | {1,2,2,2,2,4,6,7,7,7,9,10,11,11,11,23,34,45,45,45,56}                                                                        |  |  |  |  |
|     |   | This is the code for a binary search, which will be performed on the sorted list.                                            |  |  |  |  |
|     |   | When a target is found, it returns the index of the "found" target + how many "visits" it took to find it.                   |  |  |  |  |
|     |   | To find the 56, we visit the 10th item, the 9. (Visit 1)                                                                     |  |  |  |  |
|     |   | Then we visit the 15th item, the 23 (Visit 2)                                                                                |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |
|     |   | Then we visit the 18th item, the 45. (Visit 3)                                                                               |  |  |  |  |
|     |   | Then we visit the 19th item, another 45. (Visit 4)                                                                           |  |  |  |  |
|     |   | Then we find the 56 at position 20. (Visit 5)                                                                                |  |  |  |  |
|     |   | 20 + 5 = 25                                                                                                                  |  |  |  |  |
| 32. | B | To find the 45, we visit the 10th item, the 9. (Visit 1)                                                                     |  |  |  |  |
|     |   | Then we visit the 15th item, the 23 (Visit 2)                                                                                |  |  |  |  |
|     |   | Then we visit the 18th item, the 45. (Visit 3)                                                                               |  |  |  |  |
|     |   | 18 + 3 = 21                                                                                                                  |  |  |  |  |
| 33. | E | To find the 45, we visit the 10th item, the 9. (Visit 1)                                                                     |  |  |  |  |
|     |   | Then we visit the 4th item, the 2.                                                                                           |  |  |  |  |
|     |   | Then we visit the 1st item, another 2.                                                                                       |  |  |  |  |
|     |   | Then we find the target at position 0.                                                                                       |  |  |  |  |
| 34. | E | One Uno = new One(7);                                                                                                        |  |  |  |  |
|     |   | A = 7<br>B = 7 ^ 6 (111^110) = 1                                                                                             |  |  |  |  |
|     |   | Uno.getB() = 6 & 5 (110 & 101) = 4                                                                                           |  |  |  |  |
|     |   | One Dos = new One(12);                                                                                                       |  |  |  |  |
|     |   | A = 12 B = 12^11 (1100 ^ 1011) = 7                                                                                           |  |  |  |  |
|     |   | Dos.getA() = 12 ^ 11 (1100^1011) = 7                                                                                         |  |  |  |  |
|     |   | out.print(Uno.getB()*Dos.getA());<br>4 * 7 = 28                                                                              |  |  |  |  |
| 35. | B | Two Delta = new One(20);<br>// Line 4                                                                                        |  |  |  |  |
|     |   | Two is-a One, not vice versa. Thus, this declaration is invalid.                                                             |  |  |  |  |
|     |   | out.println(Alpha.getC()); // Line 11                                                                                        |  |  |  |  |
|     |   | class One does not have a getC() method                                                                                      |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |
|     |   | out.println(Beta.getC());<br>// Line 12<br>This error occurs at compilation time, class One does not contain a getC() method |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |
|     |   | out.println(Gamma.A);<br>// Line 14                                                                                          |  |  |  |  |
|     |   | A is a private instance variable which cannot be accessed in this manor.                                                     |  |  |  |  |
|     |   | out.println(Gamma.E);<br>// Line 16                                                                                          |  |  |  |  |
|     |   | E is a private instance variable which cannot be accessed in this manor.                                                     |  |  |  |  |
| 36. | B | if(A==B)<br>N++;<br>true<br>because<br>A<br>and<br>B<br>now<br>represent<br>the<br>same<br>object.                           |  |  |  |  |
|     |   | if(B==C)<br>N++;<br>false                                                                                                    |  |  |  |  |
|     |   | if(C==D)<br>N++;<br>false                                                                                                    |  |  |  |  |
|     |   | if(E==A)<br>N++;<br>false                                                                                                    |  |  |  |  |
|     |   | if<br>(A.equals(C))<br>N++;<br>true<br>because<br>A<br>now<br>contains<br>the<br>String<br>"Banana"                          |  |  |  |  |
|     |   | if<br>(B.equals(D))<br>N++;<br>false                                                                                         |  |  |  |  |
|     |   | if<br>(C.equals(E))<br>N++;<br>false                                                                                         |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |
|     |   | if<br>(D.equals(B))<br>N++;<br>false                                                                                         |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |
|     |   |                                                                                                                              |  |  |  |  |

| 37. | D  |                  |                      | left of the place plus the product of the row and column.          |             | Starting with position 1,1 and moving Left to Right down the matrix, each cell will be the cell up and to the |
|-----|----|------------------|----------------------|--------------------------------------------------------------------|-------------|---------------------------------------------------------------------------------------------------------------|
|     |    |                  |                      |                                                                    |             |                                                                                                               |
|     |    | 0<br>0<br>0<br>1 | 0<br>0<br>2<br>3     | 0<br>4                                                             |             |                                                                                                               |
|     |    | 0<br>2           | 5<br>8<br>11         |                                                                    |             |                                                                                                               |
|     |    | 0<br>3           | 8<br>14<br>20        |                                                                    |             |                                                                                                               |
|     |    | 0<br>4           | 20<br>11             | 30                                                                 |             |                                                                                                               |
|     |    |                  | Box[4][3] = 20       |                                                                    |             | (and so does Box[3][4]) See the pattern emerging?                                                             |
| 38. | A  |                  |                      | 16 ^ 28 = 10000 ^ 11100 = 01100<br>12 ^ 27 = 01100 ^ 11011 = 10111 |             |                                                                                                               |
|     |    |                  |                      | 23 ^ 26 = 10111 ^ 11010 = 01101                                    |             |                                                                                                               |
|     |    |                  |                      | 13 ^ 25 = 01101 ^ 11001 = 10100                                    |             |                                                                                                               |
|     |    |                  |                      | 20 ^ 24 = 10100 ^ 11000 = 01100                                    |             |                                                                                                               |
|     |    |                  |                      | 12 ^ 23 = 01100 ^ 10111 = 11011                                    |             |                                                                                                               |
|     |    |                  |                      | 27 ^ 22 = 11011 ^ 10110 = 01101                                    |             |                                                                                                               |
|     |    |                  |                      | 16 ^ 21 = 01101 ^ 10101 = 11000 = 24                               |             |                                                                                                               |
| 39. | 10 | +<br>/           | *<br>3<br>4<br>-     | 17<br>*<br>5<br>3<br>/<br>+                                        | 6<br>6<br>3 |                                                                                                               |
|     |    | +<br>/           | *<br>3<br>4<br>-     | 17<br>*<br>5<br>3<br>/<br>12                                       | 3           |                                                                                                               |
|     |    | +<br>/           | *<br>3<br>4<br>-     | 17<br>*<br>5<br>3<br>4                                             |             |                                                                                                               |
|     |    | +<br>/           | *<br>3<br>4<br>-     | 17<br>15<br>4                                                      |             |                                                                                                               |
|     |    | +<br>/           | *<br>3<br>4<br>2     | 4                                                                  |             |                                                                                                               |
|     |    | +<br>/           | 12<br>2<br>4         |                                                                    |             |                                                                                                               |
|     |    | +<br>6           | 4<br>=<br>10         |                                                                    |             |                                                                                                               |
| 40. | 10 | A<br>truth       | table<br>would<br>be | apropos                                                            |             |                                                                                                               |
|     |    | ABCD             | AB + CD              | (A + B) * (C + D)                                                  |             |                                                                                                               |
|     |    | 0000             | 0                    | 0                                                                  | same        | 1                                                                                                             |
|     |    | 0001             | 0                    | 0                                                                  | same        | 2                                                                                                             |
|     |    | 0010             | 0                    | 0                                                                  | same        | 3                                                                                                             |
|     |    | 0011             | 1                    | 0                                                                  |             |                                                                                                               |
|     |    | 0100             | 0                    | 0                                                                  | same        | 4                                                                                                             |
|     |    | 0101             | 0                    | 1                                                                  |             |                                                                                                               |
|     |    | 0110             | 0                    | 1                                                                  |             |                                                                                                               |
|     |    | 0111             | 1                    | 1                                                                  | same        | 5                                                                                                             |
|     |    | 1000             | 0                    | 0                                                                  | same        | 6                                                                                                             |
|     |    | 1001             | 0                    | 1                                                                  |             |                                                                                                               |
|     |    | 1010             | 0                    | 1                                                                  |             |                                                                                                               |
|     |    | 1011             | 1                    | 1                                                                  | same        | 7                                                                                                             |
|     |    | 1100             | 1                    | 0                                                                  |             |                                                                                                               |
|     |    | 1101             | 1                    | 1                                                                  | same        | 8                                                                                                             |
|     |    | 1110             | 1                    | 1                                                                  | same        | 9                                                                                                             |
|     |    | 1111             | 1                    | 1                                                                  | same        | 10                                                                                                            |
|     |    |                  |                      |                                                                    |             |                                                                                                               |