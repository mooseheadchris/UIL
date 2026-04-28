# **UIL COMPUTER SCIENCE WRITTEN TEST – 2026 DISTRICT**

**Note:** Correct responses are based on **Java SE Development Kit 22 (JDK 22)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

| Question 1                           |                                                                     |          |                                                         |
|--------------------------------------|---------------------------------------------------------------------|----------|---------------------------------------------------------|
|                                      | Which of the following is equivalent to the expression 4568 + 7118? |          |                                                         |
| A) 74510                             | B) 7448                                                             | C) 2E716 | D) 10111001112<br>E) 13678                              |
| Question 2                           |                                                                     |          |                                                         |
|                                      | What is output by the code to the right?                            |          | int a = 15;                                             |
| A) 10.5                              |                                                                     |          | int b = 4;<br>int c = 3;                                |
| B) 24                                |                                                                     |          |                                                         |
| C) 23.25                             |                                                                     |          | int result = a + b * c - a / b;                         |
| D) 23                                |                                                                     |          |                                                         |
| E) 25                                |                                                                     |          | out.println(result);                                    |
| Question 3                           |                                                                     |          |                                                         |
|                                      | What is output by the code to the right?                            |          |                                                         |
| A) Val: 5 and 3.50<br>Path: C:\\temp |                                                                     |          |                                                         |
| B) Val:                              |                                                                     |          | int x = 5;<br>double y = 3.5;                           |
| 5 and 3.5                            |                                                                     |          | out.print("Val: ");                                     |
| Path: C:\temp                        |                                                                     |          | out.printf("%d and %.1f\n", x, y);                      |
|                                      | C) Val: 5 and 3.5<br>Path: C:\temp                                  |          | out.println("Path: C:\\temp");                          |
| D) Val: 5 and 3.5<br>Path: C:\\temp  |                                                                     |          |                                                         |
| Question 4                           |                                                                     |          |                                                         |
|                                      | What is output by the code to the right?                            |          | String text = " Hello World ";                          |
| A) hexlo 5                           |                                                                     |          | String result = text.trim().toLowerCase()               |
| B) Hello World 11                    |                                                                     |          | .substring(0, 5).replace('l', 'x');                     |
| C) Hexxo 5                           |                                                                     |          | out.println(result + " " +<br>result.length());         |
| D) hexxo 5                           |                                                                     |          |                                                         |
| E) hello 5                           |                                                                     |          |                                                         |
| Question 5                           |                                                                     |          | boolean a = true;                                       |
|                                      | What is output by the code to the right?                            |          | boolean b = false;                                      |
| A) truetruefalsefalse                |                                                                     |          | boolean c = true;                                       |
| B) falsetruetruefalse                |                                                                     |          |                                                         |
| C) truetruetruefalse                 |                                                                     |          | boolean r1 = a && b    c;<br>boolean r2 = a    b && !c; |
| D) falsetruefalsefalse               |                                                                     |          | boolean r3 = a ^ c;                                     |
| E) falsefalsefalsefalse              |                                                                     |          | boolean r4 = !(a && c)    b;                            |
|                                      |                                                                     |          | out.println(r1 + "" + r2 + r3 + r4);                    |

What is output by the code to the right?

- **A)** 9267
- **B)** 8367
- **C)** 8377
- **D)** 826-7

# double a = Math.floor(8.9); double b = Math.ceil(2.1); long c = Math.round(6.4); int d = Math.abs(-7); out.println((int)a + "" + (int)b + c + d);

#### **Question 7**

What is output by the code to the right?

- **A)** 89 **B)** 88 **C)** 90 **D)** 91 **E)** 88

## **Question 8**

What is output by the code to the right?

- **A)** B
- **B)** B1
- **C)** B12
- **D)** C2
- **E)** A12

# int x = 7;

int y = 3; String result = "";

if (x > 5)

 if (y > 5) result = "A";

int a = 26 & 21 + 3; int b = 67 | 420 / 69;

a ^= b - 13 / 2; out.println(a);

else

result = "B";

else if (x > 3)

result = "C";

else

}

result = "D";

switch (result) { case "A":

case "B":

result += "1";

 case "C": result += "2";

break;

 default: result += "3";

out.println(result);

## **Question 9**

On which line of code to the right marked by comments should we place the following loop to center the output pyramid?

```
for(int j = 4; j > i; j--) { 
 out.print(" "); 
}
```

- **A)** line 1 **B)** line 2
- **C)** line 3 **D)** line 4

```
for (int i=1; i<=4;i++) { 
 //line 1 
 for (int k=1; k<=2*i-1;k++) { 
 //line 2 
 out.print("*"); 
 // line 3 
 } 
 // line 4 
 out.println(); 
}
```

#### **Question 10** What is output by the code to the right? **A)** 10 6 21 **B)** 6 4 15 **C)** 10 4 14 **D)** 10 4 19 int[] arr = {2, 4, 6, 8, 10}; arr[1] = arr[0] + arr[3]; arr[4] = arr[1] - arr[2]; int result = arr[1] + arr[4] + arr.length; out.println(arr[1] + " " + arr[4] + " " + result); **Question 11** Given a file "data.txt" containing the below data. What is output by the code to the right? Hello World 25 3.75 **A)** Hello 25 28 **B)** Hello World 25 28 **C)** Hello 25 29 **D)** World 25 28 Scanner file = new Scanner( new File("data.txt")); String word = file.next(); file.nextLine(); int num = file.nextInt(); double dec = file.nextDouble(); file.close(); out.println(word + " " + num + " " + (num + (int)dec)); **Question 12** What is output by the code to the right? **A)** 15 12 **B)** 12 15 **C)** 12 8 **D)** 20 15 **E)** 6 15 int[] nums = {3, 5, 2, 4, 6}; int sum = 0; int product = 1; for (int n : nums) { if (n % 2 == 0) { sum += n; } else { product \*= n; } } out.println(sum + " " + product); **Question 13** What is output by the code to the right? **A)** 12 3 5 1 **B)** 10 3 5 2 **C)** 13 3 5 1 **D)** 14 3 5 1 int a = 3; int b = 4; int c = 2; int result = a + ++b \* c-- - b % c; out.println(result + " " + a + " " + b + " " + c);

#### **Question 14**

Which of the following statements about Java primitive data types is TRUE?

- **A)** A byte can store values from -128 to 128.
- **B)** When a short with value 32767 is incremented, it becomes 32768.
- **C)** A long and a double both use 32 bits of memory.
- **D)** When a byte with value -128 is decremented, it becomes 127.
- **E)** An int can store any value that a long can store.

#### **Question 15** What is output by the code to the right? **A)** 15 3 **B)** 20 3 **C)** 15 4 **D)** 30 3 **E)** There is no output due to a runtime error. ArrayList<Integer> list = new ArrayList<>(); list.add(10); list.add(20); list.add(30); list.add(1, 15); list.remove(2); list.set(0, 5); out.println(list.get(1) + " " + list.size()); **Question 16** What is output by the code to the right given that the file a.txt does not exist? **A)** 23 **B)** 13 **C)** There is no output due to a compile error. **D)** There is output, followed by a runtime error. **E)** There is no output due to a runtime error. try { String i = "a.txt"; File f = new File(i); Scanner s = new Scanner(i); s.nextLine(); out.print(1); } catch (IOException e) { out.print(2); } finally { out.print(3); } **Question 17** What could replace **<1\*>** in the code to the right so that it will compile and run without error (removing items). **A)** pop **C)** poll **D)** A and B. **B)** remove LinkedHashSet<Integer> struct; struct = new LinkedHashSet<>(); struct.add(1); struct.add(2); struct.add(1); struct.add(189); struct.add(3); struct.**<1\*>**(2); struct.**<1\*>**(1); out.println(struct); //q18 out.println(struct.remove(0)); //q19 **Question 18** Assuming **<1\*>** is filled in correctly, what is output by the line marked //q18 code to the right? **A)** [1, 189, 3] **B)** [189, 3] **C)** Output cannot be determined until runtime **D)** There is no output due to a compile error. **E)** There is no output due to a runtime error. **Question 19** Assuming **<1\*>** is filled in correctly, what is output by the line marked //q19 code to the right? **A)** 189 **B)** true **C)** false **D)** There is no output due to a compile error **E)** There is no output due to a runtime error. **Question 20** Which of the lines in the code to the right first causes an error? **A)** //1 **B)** //2 **C)** //3 **D)** //4 **E)** None of the above lines cause any errors. double g = Math.ceil(6); //1 int i = Math.min(g, 2); //2 i = Math.round(g); //3 g = Math.log(i); //4 **E)** All of the above.

What can replace **<1\*>** in the code to the right so that the wings instance variable is assigned value 2 and compiles without error?

**A)** static **B)** static final

**C)** final **D)** Nothing is required.

**E)** B or C. **F)** Any of the above.

#### **Question 22**

Which of the following describes the scope of the city instance variable in the Pigeon class?

**A)** More restrictive than private.

**B)** Less restrictive than private; more than protected.

**C)** Less restrictive than protected; more than public.

**D)** Less restrictive than public.

#### **Question 23**

What can replace **<2\*>** in the code to the right so that the fly() method returns value 2 and the Bird interface compiles without warning?

**A)** {return wings;} **B)** ;

**C)** {return 2;} **D)** A or C.

**E)** Any of the above.

#### **Question 24**

What can replace **<3\*>** in the code to the right so that the fly() method returns the value 2?

**A)** super.wings **B)** wings

**C)** 2 **D)** B or C.

**E)** Any of the above.

#### **Question 25**

Assuming **<1\*>**, **<2\*>**, and **<3\*>** are filled in correctly, what is output by the line marked //q27 in the code to the right, assuming any errors below line //q27 are commented out?

**A)** Caw!Caw!Caw!

**B)** Caw! NYC Caw! LA Caw!

**C)** Caw! NYC Caw! LA Caw! Miami

**D)** There is no output due to a compile error.

**E)** There is no output due to a runtime error.

#### **Question 26**

Assuming **<1\*>**, **<2\*>**, and **<3\*>** are filled in correctly, and any error from the previous question has been commented out, what is output by the line marked //q28 in the code to the right?

**A)** 0 0 0 **B)** 2 2 2

**C)** 2 0 0 **D)** 2 2 0

**E)** There is no output due to a compile error.

```
interface Bird { 
 <1*> int wings = 2; 
 public String call(); 
 private int fly() <2*>
} 
class Pigeon implements Bird { 
 String city; 
 public Pigeon(String c) { 
 city = c; 
 } 
 public String call() { 
 return "Caw! " + city; 
 } 
 public int fly() { 
 return <3*>; 
 } 
} 
////////////client code//////////// 
Pigeon p1 = new Pigeon("NYC"); 
Pigeon p2 = new Pigeon("LA"); 
Bird b1 = new Pigeon("Miami"); 
String o = p1.call(); 
o += " " + p2.call(); 
o += " " + b1.call(); 
out.println(o); //q27 
o = "" + p1.fly(); 
o += " " + p2.fly(); 
o += " " + b1.fly(); 
out.println(o); //q28
```

What is output if the following call is made to the function mystery to the right? mystery("AHs2");

- **A)** -102 **B)** 108

- **C)** 99 **D)** 117
- **E)** There is no output due to a runtime error.

#### **Question 28**

What is output if the following call is made to the function mystery to the right? mystery("K38knd38kOP1");

- **A)** 210 **B)** -183
- **C)** -237 **D)** -234
- **E)** There is no output due to a runtime error.

```
int mystery(String s) { 
  if (s.isEmpty()) 
  return 0; 
  char c = s.charAt(0); 
  s = s.substring(1); 
  if (Character.isUpperCase(c)) 
 return 3 * mystery(s); 
  if (Character.isDigit(c)) 
  return 5 + mystery(s); 
   if (c < 'l') 
 return -1 * mystery(s); 
  return 1 + 2 * mystery(s); 
}
```

#### **Question 29**

What is the intended purpose of method the method goodtime(int i, int j) to the right?

- **A)** Return the greatest common divisor of two numbers.
- **B)** Return the least common multiple of two numbers.
- **C)** Return the least prime number between the two.
- **D)** Return the greatest prime number between the two.
- **E)** Return the product of greatest factors of two numbers.

#### **Question 30**

What is output by the client code to the right?

- **A)** 1 1 **B)** 216 216
- **C)** 36 126 **D)** 6 1
- **E)** There is no output due to a runtime error.

# **Question 31**

What is output by the client code to the right?

- **A)** false false **B)** false true
- **C)** true false **D)** true true
- **E)** There is no output due to a compile error.

```
 if(i == 0 || j == 0) 
       return 0; 
    int s = Math.abs(i * j); 
    while(j != 0) { 
        int t = i % j; 
        i = j; 
        j = t; 
    } 
    return s / i; 
} 
////////////client code//////////// 
out.print(goodtime(12, 18)); 
out.print(" "); 
out.print(goodtime(14, 9));
```

int goodtime(int i, int j) {

String str = "BEEPbeepONtheSTREET"; String reg = "([A-Z]+[a-z]+)\*|((\\w\\w)+)+"; out.print(str.matches(reg) + " "); reg = "\\w\\D{10,17}...."; out.println(str.matches(reg));

### **Question 32**

What is output by the code to the right?

- **A)** TT **B)** TF
- **C)** FT **D)** FF
- **E)** There is no output due to a runtime error.

## **Question 33**

Which of the following ranges accurately describes the list of possible integers that rand can be?

- **A)** 5,18 **B)** 5,18
- **C)** 5,13 **D)** 5,13
- **E)** None of the above.

```
int a = 5; 
double b = 5.2; 
out.print((a >= b) ? 'T' : 'F'); 
out.println((b <= a) ? 'T' : 'F');
```

int rand = (Math.random() \* 13) + 5;

What is output by the line marked //Q34 in the code to the right?

- **A)** 1 **B)** 4 **C)** 5

[98, 99, 100, 97] abcd

- **D)** There is no output due to a runtime error as the byte[] entity does not implement hashCode(), which is required for all types that are stored in a HashSet.
- **E)** There is no output due to a compile time error as the byte arrays are being filled with char's, not byte's.

#### **Question 35**

Disregarding the output produced by the line marked //Q34 in the code to the right, what is output by the code to the right?

- **A)** [97, 98, 99, 100] **B)** abcd [100, 97, 98, 99] bcda [99, 100, 97, 98] cdab [97, 98, 99, 100] dabc
- **C)** [a, b, c, d] [b, c, d, a] [c, d, a, b] [d, a, b, c]
- **D)** It is impossible to know the output until runtime as the output will be dependent on the memory addresses of the arrays, since arrays use the identity hash code.
- **E)** It is impossible to know the output until runtime due to the nature of it being a HashSet and storing arrays; however, the output would have been a permutation of the lines from one of either option A, B, or C.
- **F)** There is still no output due to an error.

#### **Question 36**

Consider if uniques was instead storing char[]'s, each newly created array added to uniques was instead of type char[], and unique was of type char[] in the for loop. Then, what is output by the line marked //Q34 in the code to the right?

- **A)** 1 **B)** 4 **C)** 5
- **D)** There is no output due to a runtime error as the char[] entity does not implement hashCode(), which is required for all types that are stored in a HashSet.
- **E)** There is no output due to a compile time error.

#### **Question 37**

Using the same situation described by Question 36 above, and disregarding the output produced by the line marked //Q34, what is output by the code to the right?

- **A)** The same answer as **B)** The same answer as
- option A from question 35. option B from question 35.
- **C)** The same answer as **D)** The same answer as
  - option C from question 35. option D from question 35.
- **E)** The same answer as **F)** The same answer as
  - option E from question 35. option F from question 35.

```
HashSet<byte[]> uniques = 
       new HashSet<byte[]>(); 
uniques.add(new byte[] { 
        'a', 'b', 'c', 'd' 
}); 
uniques.add(new byte[] { 
        'b', 'c', 'd', 'a' 
}); 
uniques.add(new byte[] { 
        'c', 'd', 'a', 'b' 
}); 
uniques.add(new byte[] { 
        'd', 'a', 'b', 'c' 
}); 
uniques.add(new byte[] { 
        'a', 'b', 'c', 'd' 
}); 
out.println(uniques.size()); //Q34 
for (byte[] unique : uniques) { 
    out.println(unique); 
}
```

#### **Question 38** What is output by the code to the right? **A)** T1T1T1T1T1T1T1T1T1T1T2T2T2T2T2T2T2T2T2T2 **B)** T2T2T2T2T2T2T2T2T2T2T1T1T1T1T1T1T1T1T1T1 **C)** T1T2T1T2T1T2T1T2T1T2T1T2T1T2T1T2T1T2T1T2 **D)** T2T1T2T1T2T1T2T1T2T1T2T1T2T1T2T1T2T1T2T1 **E)** It is impossible to determine the output until runtime. **F)** There is no output due to an error. final Lock lock = new ReentrantLock(); StringBuilder sb = new StringBuilder(); Thread t1 = new Thread(() -> { for (int i = 0; i < 10; i++) { lock.lock(); sb.append("T1"); lock.unlock(); } }); Thread t2 = new Thread(() -> { for (int i = 0; i < 10; i++) { lock.lock(); sb.append("T2"); lock.unlock(); } }); t1.start(); t2.start(); try { t1.join(); t2.join(); } catch (InterruptedException e) { e.printStackTrace(); } out.println(sb); **Question 39** What is the *height* of the Binary Search Tree (BST) of integers resulting from inserting the elements to the right in order? Write your answer in the blank provided on your answer sheet for this question. First: 59 | 56 | 42 | 16 | 72 | 83 | 77 **Question 40** What is the *maximum width* of the Binary Search Tree (BST) of

integers resulting from inserting the elements to the right in order? Write your answer in the blank provided on your

answer sheet for this question.

 | 58 v 32 Last: 73

# ★**ANSWER KEY – CONFIDENTIAL**★

# **UIL COMPUTER SCIENCE – 2025-2026 DISTRICT**

**Questions** (+6 points for each correct answer, -2 points for each incorrect answer)

1) E 11) A 21) F 31) B

2) B 12) B 22) B 32) D

3) C 13) C 23) D 33) E

4) D 14) D 24) D 34) C

5) A 15) A 25) C 35) D

6) B 16) A 26) E 36) C

7) A 17) B 27) D 37) E

8) C 18) B 28) C 38) E

9) A 19) C 29) B \*

39) 4

10) D 20) B 30) C \*

40) 12

**Note:** Correct responses are based on **Java SE Development Kit 22 (JDK 22)** from Sun Microsystems, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

Explanations:

*<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.*

| 1.  | E | = 302. 711<br>= 457. 302<br>456<br>+ 457<br>= 759<br>= 1367                                         |
|-----|---|-----------------------------------------------------------------------------------------------------|
| 2.  | B | Simple order of operations.                                                                         |
| 3.  | C | Simple printing with escape sequences and printf.                                                   |
| 4.  | D | trim() removes leading/trailing spaces. toLowerCase() makes the string lowercase.                   |
|     |   | Substring makes the string "hello". replace() replaces all occurrences of the first character       |
|     |   | with the second, making the string "hexxo". The string is 5 characters long.                        |
| 5.  | A | Simple boolean logic.                                                                               |
| 6.  | B | Math.floor(8.9) → 8.0 (rounds down to nearest integer)                                              |
|     |   | Math.ceil(2.1) → 3.0 (rounds up to nearest integer)                                                 |
|     |   | Math.round(6.4) → 6 (rounds to nearest, 0.4 rounds down)                                            |
|     |   | Math.abs(-7) → 7 (absolute value)                                                                   |
| 7.  | A | Order of operations.                                                                                |
| 8.  | C | First, the if-else chain: x > 5 is true (7 > 5), so we enter the inner if. y > 5 is false           |
|     |   | (3 > 5), so result = "B".                                                                           |
|     |   | Then, the switch: result is "B", matching case "B". It assigns result += "1" making it              |
|     |   | "B1". There's no break, so fall-through occurs to case "C", which assigns                           |
|     |   | result += "2" making it "B12". The break then exits the switch.                                     |
| 9.  | A | The spaces need to be printed before the star in order to center the higher levels of the pyramid   |
|     |   | with the bottom level.                                                                              |
| 10. | D | arr[1] becomes 2 + 8 = 10, then arr[4] becomes 10 - 6 = 4, and result is                            |
|     |   | 10 + 4 + 5 = 19.                                                                                    |
| 11. | A | file.next() reads "Hello", file.nextLine() consumes the rest of line one                            |
|     |   | (" World"), file.nextInt() reads 25, file.nextDouble() reads 3.75, and                              |
|     |   | (int)dec truncates to 3, so num + (int)dec = 25 + 3 = 28.                                           |
| 12. | B | Even numbers (2,<br>4, 6) are added to sum giving 2<br>+ 4+ 6 = 12, odd numbers (3,<br>5) are       |
|     |   | multiplied into product giving 1<br>⋅ 3 ⋅ 5 = 15.                                                   |
| 13. | C | ++b increments b to 5 and uses 5, c uses 2 then decrements c to 1, b % c uses current               |
|     |   | values 5 % 1 = 0, then 5 * 2 = 10, and finally 3 + 10 - 0 = 13.                                     |
| 14. | D | When a byte at its minimum value -128 is decremented, it underflows and wraps to the                |
|     |   | maximum value 127; A is false because byte ranges from -128 to 127 (not 128); B is false            |
|     |   | because 32767 wraps to -32768; C is false because both long and double use 64 bits; E is            |
|     |   | false because long is 64 bits and can store larger values than the 32-bit int.                      |
| 15. | A | Starting with [10, 20, 30], add(1, 15) inserts at index 1 giving [10, 15, 20, 30],                  |
|     |   | remove(2) removes index 2 giving [10, 15, 30], set(0, 5) replaces index 0 giving                    |
|     |   | [5, 15, 30], so get(1) returns 15 and size() returns 3.                                             |
| 16. | A | An IOException is thrown since the file does not exist, so we enter the catch block and             |
|     |   | then before terminating, enter the finally block.                                                   |
| 17. | B | Only remove will work for a LinkedHashSet                                                           |
| 18. | B | LinkedHashSet will stay in the same order as added, and remove will take out the                    |
|     |   | occurrence of the integer given (also there are no duplicates in a set, so only one instance of 1). |
| 19. | C | The LinkedHashSet remove method will return false if nothing is removed, but true if                |
|     |   | something is removed.                                                                               |
| 20. | B | Math.min(double, double) returns a double, there is no version for                                  |
|     |   | Math.min(double, int). //3 also causes an error, Math.round(double) returns a                       |
|     |   | long, but //2 happens first.                                                                        |
| 21. | F | Instance variables in an interface default as static and final, so you can define these or          |
|     |   | not.                                                                                                |
| 22. | B | Default scope for instance variable is package-protected, which is less restrictive than            |
|     |   | private, but more restrictive than protected.                                                       |
| 23. | D | A method marked private in an interface must be initialized, but since wings is a final             |
|     |   | variable with value 2, we can send that or the constant 2 as our return.                            |
| 24. | D | super.wings causes an error, but wings can be accessed regularly, and it is equal to                |
|     |   | constant<br>2, so either can be returned.                                                           |

| 25. | C | The method works as intended for all 3 instances, returning "Caw! " followed by the given city<br>name from instantiation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 26. | E | Since the fly() method is private within the interface, and b1 is instantiated with<br>Bird class in the eyes of the compiler, the fly() method is out of scope and causes a compile<br>error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| 27. | D | Recursive Tracing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 28. | C | Recursive Tracing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 29. | B | The goodtime() function finds the LCM of the two numbers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 30. | C | The LCM of 12<br>and 18 is 36 (12<br>⋅ 3 = 18 ⋅ 2 = 36), and the LCM of 14 and 9 is 126 (no common<br>factors to work from, 14<br>⋅ 9 = 126)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 31. | B | The first pattern will match either the group of one or more uppercase sequences directly<br>followed by one or more lowercase sequences, any number of times (the whole group), or the<br>group of a string of an even number of word characters, but at least 2, so it does not match. The<br>second pattern will match a string made up of any word character, followed by between 10-17<br>non digit characters, followed by 4 characters (can be any single characters), so it does match.                                                                                                                                                                                                                                                                                                                          |
| 32. | D | Integers get promoted to doubles in this situation, meaning that the comparison becomes<br>5.0 >= 5.2, which is false. Note that the order in which a and b appear does not influence<br>how the promotion occurs. Thus, both comparisons are false, and 'F' is printed twice on the<br>same line.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 33. | E | Note that the line assigning a value to rand does not compile. This is because<br>Math.random() returns a type of double, and needs to be explicitly casted down to an<br>integer before it can be stored in rand (of type int).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 34. | C | Regardless of what array is stored in a HashSet, the value of hashCode() is dependent on<br>the memory address rather than the value being stored. Since five arrays are dynamically<br>allocated via the new keyword, despite two of the arrays storing the same literal values, they will<br>each point to unique memory addresses, and thus there are five elements in the HashSet.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| 35. | D | Objects that don't have an overwritten toString() method print the name of the object,<br>followed by the character '@' followed by the hex representation of their hashCode() value.<br>Arrays are prefaced by one '[' character for each dimension of the array. Lastly, the JVM has<br>special class names encoded for each of the primitive data types since they themselves are not<br>classes. In the case of a byte, this is the character 'B'. In the case of a char, this is the<br>character 'C'.                                                                                                                                                                                                                                                                                                              |
| 36. | C | Even though the data type has changed here, the same rule from question 34 applies.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| 37. | E | The output will actually be a permutation of option choice B from question 35. Note that<br>out.println() has an implementation for println(byte[] arr) which instead prints<br>the String representation of the byte array. This, however, does not change the fact that the<br>order which these lines appear in is not known until runtime due to the rules regarding array's<br>toString() implementation.                                                                                                                                                                                                                                                                                                                                                                                                           |
| 38. | E | A common use of a Lock (also known as a mutex which is short for mutual exclusion) is used to<br>ensure that no two processes which use a shared resource modify said shared resource at the<br>same time. Without some additional techniques, it does not, however, determine the order in<br>which said processes access the shared resource. In this case, it is impossible to determine what<br>order the "T1"s and "T2"s will occur in. Rather, we just know that some permutation of ten<br>"T1"s and ten "T2"s will be printed. Thus "T1T2T2T1T2T2T2T1…" is also a valid output that<br>can be generated by this program. This behavior can be more easily observed by instead<br>changing the loop bound from 10 to something like 100 as this is largely dependent on CPU<br>scheduling and instruction cycles. |

| 39. | 4  | The nodes when inserted in the order specified result in the following BST:                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-----|----|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|     |    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|     |    | The height of a binary tree is the number of edges on the longest path from the root node to the<br>deepest leaf node. Here that value is 4                                                                                                                                                                                                                                                                                                                                                                                                          |
| 40. | 12 | The nodes when inserted in the order specified result in the BST shown above. The maximum<br>width of a binary tree is the maximum of the widths of all levels of the binary tree. The width of<br>a level of a binary tree is the number of nodes between the leftmost and rightmost non-null<br>nodes, inclusive of any null nodes (empty spots) in between. Here, this occurs on the level which<br>contains nodes 32 and 73, which is represented as [32, null, null, null, null,<br>null, null, null, null, null, null, 77] which has width 12. |