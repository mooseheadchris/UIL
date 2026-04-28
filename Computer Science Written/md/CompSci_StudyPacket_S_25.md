# **UIL COMPUTER SCIENCE WRITTEN TEST – 2025 STATE**

**Note:** Correct responses are based on **Java SE Development Kit 22 (JDK 22)** from Oracle, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used. **For all output statements, assume that the System class has been statically imported using: import static java.lang.System.\*;**

| Question 1                                                           |                                                                                             |  |
|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------|--|
| Which of the following is equivalent to the expression 28579 + 1325? |                                                                                             |  |
| A) 221010<br>B) 42308<br>C) 28149                                    | D) 333005<br>E) None are equivalent.                                                        |  |
| Question 2<br>What is output by the code to the right?               |                                                                                             |  |
| A) 16<br>B) 5<br>C) 38<br>D) 92                                      | out.print(243+34 / 21-9 * 21-17);                                                           |  |
| E) There is no output due to a compile error.                        |                                                                                             |  |
| Question 3                                                           |                                                                                             |  |
| What is output by the code to the right?                             | String s = "Yep";                                                                           |  |
| A) 1.2YEPZ<br>B) 1.2YepY                                             | int i = 89;                                                                                 |  |
| C) 1.3YEPY<br>D) 1.3YepZ                                             | double d = 1.25;                                                                            |  |
| E) There is no output due to a runtime error.                        | out.printf("%3\$.1f%1\$S%2\$c",s,i,d);                                                      |  |
| Question 4                                                           | String s = "CaptHanSolo";                                                                   |  |
| What is output by the code to the right?                             | String r = "CaptHandsome";                                                                  |  |
| A) -17<br>B) -1<br>C) 17<br>D) 1                                     | int i = s.compareTo(r);                                                                     |  |
| E) There is no output due to a compile error.                        | out.println(i);                                                                             |  |
| Question 5                                                           | boolean a = false;                                                                          |  |
| What is output by the code to the right?                             | boolean b = true;<br>a  = a ^ b & !b   a;<br>b ^= b ^ !a & a   !b;<br>out.print(a ^ b   a); |  |
| A) true                                                              |                                                                                             |  |
| B) false                                                             |                                                                                             |  |
| Question 6                                                           |                                                                                             |  |
| What is output by the code to the right?                             | double c = 4.5;<br>c = Math.nextAfter(c, -7);                                               |  |
| A) 4.00 4.00<br>B) 4.50 4.49                                         | String s = "" + c;                                                                          |  |
| C) 4.50 4.50<br>D) -3.50 -3.5                                        | s = s.substring(0, 4);                                                                      |  |
| E) There is no output due to a runtime error.                        | out.printf("%.2f %s",c,s);                                                                  |  |
| Question 7                                                           |                                                                                             |  |
| What is output by the code to the right?                             | int i = -7;                                                                                 |  |
| A) 12-7                                                              | if(i < 0   i++ > -10)<br>out.print(1);                                                      |  |
| B) 13-7                                                              | if(i > 0 && i < 10)                                                                         |  |
| C) 2-7                                                               | out.print(2);                                                                               |  |
| D) 13-6                                                              | else out.print(3);                                                                          |  |
| E) 3-6                                                               | out.print(i);                                                                               |  |
| Question 8                                                           | int i = 212;                                                                                |  |
| What is output by the code to the right?                             | i &= i - 7 << 4;                                                                            |  |
| A) 54<br>B) 63<br>C) 31<br>D) 22                                     | i %= i ^ 123 - 17;                                                                          |  |
| E) There is no output due to a runtime error.                        | out.print(i   13);                                                                          |  |

What is output by the line marked //q09 in the code to the right?

- **A)** [13, 13, 15, 19, 25]
- **B)** [8, 8, 10, 14, 20]
- **C)** [17, 15, 15, 17, 21]
- **D)** [12, 10, 10, 12, 16]
- **E)** There is no output due to a runtime error.

## **Question 10**

What is output by the line marked //q10 in the code to the right?

- **A)** [8, 6, 9, 3, 20]
- **B)** [8, 9, 8, 6, 20]
- **C)** [12, 8, 9, 5, 16]
- **D)** [8, 8, 9, 5, 20]
- **E)** There is no output due to a runtime error.

## **Question 11**

Which of the following could replace **<1\*>** for the code to the right to compile without error?

- **A)** IOException
- **B)** FileNotFoundException
- **C)** Exception
- **D)** Only A or C.
- **E)** Any of the above will work.

## **Question 12**

What is output by the code to the right?

- **A)** 4
- **B)** 104
- **C)** 15
- **D)** 105
- **E)** There is no output due to a compile error.

## **Question 13**

What is the order of precedence for the operators to the right?

- **A)** III, II, I, IV **B)** I, III, IV, II
- **C)** III, I, II, IV **D)** III, I, II, IV
- **E)** III, I, IV, II

# **Question 14**

What is output by the code to the right?

- **A)** 5
- **B)** 3
- **C)** 8
- **D)** 6
- **E)** There is no output due to a compile error.

```
int[][] mat = new int[3][5]; 
for(int r = 0; r < 3; r++) 
 for(int c = 4; c >= 0; c--) 
 mat[r][c] = 
 (r + 1) * 5 + (c - 1) * c - 2; 
out.println 
 (Arrays.toString(mat[2])); //q09 
for(int i = 0; i < 4; i ++) { 
 if(i != 3) { 
 mat[i][i] = mat[i][i + 1]; 
 mat[i][i]--; 
 } if(i != 0) { 
 mat[i - 1][i + 1] = 
 mat[i - 1][i - 1]; 
 mat[i - 1][i]++; 
 } 
 mat[0][i] += i; 
 mat[1][i] -= i; 
} 
out.println 
 (Arrays.toString(mat[1])); //q10
```

```
public void scan()throws <1*>{ 
 File f = new File("a.dat"); 
 Scanner sc = new Scanner(f); 
 sc.nextLine(); 
 out.print(sc.nextLine()); 
}
```

```
int i = 4; 
switch(5) { 
 case 4: i += 10; 
 case 2: i++; 
 break; 
 default: i += 100; 
} 
out.print(i);
```

```
I. == 
II. += 
III. <= 
IV. ?: (ternary)
```

```
int[] sizes = new int[] { 
 Double.BYTES, Float.BYTES, 
 Long.BYTES, Integer.BYTES, 
 Short.BYTES, Byte.BYTES 
}; 
Arrays.sort(sizes); 
out.print(sizes[0]+sizes[2]);
```

#### **Question 15** What is output by the code to the right? **A)** [Ironhide, RC, Bumblebee, RC, Optimus] **B)** [Ironhide, RC, RC, Optimus] **C)** [Ironhide, RC, Optimus] **D)** [Ironhide, Bumblebee, RC, Optimus] **E)** There is no output due to a runtime error. ArrayList<String> a; a = new ArrayList<String>(); a.add("Bumblebee"); a.add("Optimus"); a.add(1,"RC"); a.set(0, "Ironhide"); if(!a.contains(new String("RC"))) a.add(1, "RC"); out.println(a); **Question 16** What is output by the code to the right? **A)** true i **B)** false 0 **C)** false NaN **D)** true NaN **E)** There is no output due to a compile error. double x = 0, y = 0; x /= y--; y = Math.sqrt(y); out.print((y == x) + " "); out.println(y); **Question 17** What is output by the following client code? out.print(A.B.s); **A)** C **B)** D **C)** Output cannot be determined until runtime. **D)** There is no output due to a compile error. **E)** There is no output due to a runtime error. class A { static class B { static String s = "C"; } static TopLevel B = new TopLevel(); } class TopLevel { String s = "D"; } **Question 18** What is the asymptotic time complexity of the code to the right? **A)** log **B)** log **C)** - **D)** - **E)** - log PriorityQueue<Integer> pq; pq = new PriorityQueue<Integer> (Collections.reverseOrder()); for(int y = 0; y < N; y++) { double d = Math.random() \* 100; pq.add((int)(d)); } out.println(pq); **Question 19** Which data structure is demonstrated by the code to the right? **A)** Queue **B)** Min-Heap **C)** Linked List **D)** Max-Heap **E)** Stack **Question 20** What is output by the code to the right? **A)** true true **B)** true false **C)** false true **D)** false false **E)** There is no output due to a runtime error. String m1 = "(\\w+ ){2,7}"; String m2 = "([A-Z]?[a-z]\* ?)+"; String s = "One of a Kind"; out.print(s.matches(m1)); out.print(" "); out.print(s.matches(m2));

Which of the following could replace **<1\*>** in the client code to the right so that the resulting code produces a compile-time error?

- **A)** <T>
- **B)** <? extends T>
- **C)** <R>
- **D)** Nothing (leave the space blank)
- **E)** A or C

## **Question 22**

Suppose we were to implement the solution proposed in option A in question 21 in the code to the right. In addition, we replace all instances of Node with Node<T> (except for the occurrences of Node on the marked lines). Which of the following Java concepts is demonstrated by the resulting code?

- **A)** Hiding
- **B)** Overloading
- **C)** Overriding
- **D)** Encapsulation
- **E)** Abstraction

# **Question 23**

Suppose we were to implement the solution proposed in option C in question 21 in the code to the right. In addition, we replace all instances of Node with Node<R> (except for the occurrences of Node on the marked lines). Would this new code produce any warnings or errors?

- **A)** The code would demonstrate the same concept as in Question 22 and not result in an error.
- **B)** The code would not demonstrate the same concept as in Question 22 but would result in an error.
- **C)** The code would demonstrate the same concept as in Question 22 and result in an error.
- **D)** The code would not demonstrate the same concept as in Question 22 and not result in an error, but would not work as intended.
- **E)** The code would not demonstrate the same concept as in Question 22 and not result in an error, and would work as intended.

## **Question 24**

The class DataStructure in the code to the right is a partial implementation of what well-known data structure?

- **A)** Dequeue
- **B)** AVL Tree
- **C)** Stack
- **D)** Min-Heap
- **E)** Queue

```
class DataStructure<T> { 
 private class Node<1*> { // EXCEPT THIS LINE 
 public T data; 
 public Node next, prev; 
 public Node(T data) { // EXCEPT THIS LINE 
 this.data = data; 
 } 
 } 
 private Node head, tail; 
 private int size; 
 public DataStructure() { 
 head = tail = null; 
 size = 0; 
 } 
 public void addFront(T data) { 
 Node newNode = new Node(data); 
 if (head == null) { 
 tail = newNode; 
 } else { 
 newNode.next = head; 
 head.prev = newNode; 
 } 
 head = newNode; 
 size++; 
 } 
 public void addBack(T data) { 
 Node newNode = new Node(data); 
 if (tail == null) { 
 head = newNode; 
 } else { 
 newNode.prev = tail; 
 tail.next = newNode; 
 } 
 tail = newNode; 
 size++; 
 } 
 public T removeFront() { 
 if (head == null) { 
 return null; 
 } 
 T data = head.data; 
 head = head.next; 
 if (head == null) { 
 tail = null; 
 } else { 
 head.prev = null; 
 } 
 size--; 
 return data; 
 } 
 public T removeBack() { 
 if (tail == null) { 
 return null; 
 } 
 T data = tail.data; 
 tail = tail.prev; 
 if (tail == null) { 
 head = null; 
 } else { 
 tail.next = null; 
 } 
 size--; 
 return data; 
 }
```

}

Using the undirected graph to the right, what would be the length of its minimum spanning tree?

- **A)** 27
- **B)** 33
- **C)** 35
- **D)** 43
- **E)** 50

## Question 26

Which of the following algorithms can be used to calculate the length of the minimum spanning tree for the graph to the right?

- A) Kruskal's Algorithm
- B) Floyd-Warshall Algorithm
- C) Ford–Fulkerson Algorithm
- D) Prim's Algorithm
- E) Both A and B.
- F) Both A and C.
- G) Both A and D.

# Question 27

Among the different variants of the algorithm, which of the following is equivalent to the best-known asymptotic time complexity of Kruskal's Algorithm?

- A)  $\mathcal{O}(V \log V)$
- B)  $\mathcal{O}(E \log V)$

C)  $\mathcal{O}(E)$ 

- D)  $\mathcal{O}(V^2)$
- E) None of the above.

![](_page_4_Figure_23.jpeg)

What is the shortest cost path in the graph to the right between nodes A and E?

- **A)** 17
- **B)** 21
- **C)** 25
- **D)** 27
- **E)** 33

![](_page_4_Figure_30.jpeg)

Which of the following boolean expressions, when evaluated over all permutations of true and false, is equivalent to the truth table to the right?

- **A)** !C || !B && (!A || C)
- **B)** (!A && !B && !C) || A
- **C)** (!A && C) || (A && B)
- **D)** (A && !C) || (!A && !B)
- **E)** More than one of the above.

|   | • |   |        |
|---|---|---|--------|
| Α | В | С | Output |
| F | F | F | Т      |
| F | F | Т | Т      |
| F | Τ | F | F      |
| F | Τ | Т | F      |
| Τ | F | F | Т      |
| Τ | F | Т | F      |
| Т | Т | F | Т      |
|   |   |   |        |

9

10

2

11

# Question 30

What is the value of the expression to the right?

**A)** 1024

**B)** 2048

**C)** 2047

- **D)** 8192
- E) None of the above.

 $2^{23} = 8388608$ 

F

Τ

Τ

Find the value of  $8388608 \gg 10$ 

```
/* Use the code below to answer question 31 through 36 */
final class Character { 
 final int hp; 
 final String name; 
 final double basicAttackDamage; 
 final double secondaryAttackDamage; 
 final double primaryAbilityDamage; 
 final double secondaryAbilityHeal; 
 final double ultimateAbilityDamage; 
 final int basicAttackCoolDownMillis; 
 final int secondaryAttackCoolDownMillis; 
 final int primaryAbilityCoolDownMillis; 
 final int secondaryAbilityCoolDownMillis; 
 final int ultimateAbilityCoolDownMillis; 
 final double ultimateChargeRate; 
 final double ultimateChargePerDamage; 
 public Character(CharacterThing thing) { 
 this.hp = thing.hp; 
 this.name = thing.name; 
 this.basicAttackDamage = thing.basicAttackDamage; 
 this.secondaryAttackDamage = thing.secondaryAttackDamage; 
 this.primaryAbilityDamage = thing.primaryAbilityDamage; 
 this.secondaryAbilityHeal = thing.secondaryAbilityHeal; 
 this.ultimateAbilityDamage = thing.ultimateAbilityDamage; 
 this.basicAttackCoolDownMillis = thing.basicAttackCoolDownMillis; 
 this.secondaryAttackCoolDownMillis = thing.secondaryAttackCoolDownMillis; 
 this.primaryAbilityCoolDownMillis = thing.primaryAbilityCoolDownMillis; 
 this.secondaryAbilityCoolDownMillis = thing.secondaryAbilityCoolDownMillis; 
 this.ultimateAbilityCoolDownMillis = thing.ultimateAbilityCoolDownMillis; 
 this.ultimateChargeRate = thing.ultimateChargeRate; 
 this.ultimateChargePerDamage = thing.ultimateChargePerDamage; 
 } 
 @Override 
 public String toString() { 
 Field[] fields = this.getClass().getDeclaredFields(); 
 StringBuilder res = new StringBuilder(); 
 for (Field field : fields) { 
 try { 
 res.append((field.get(this)) != null ? field.getName() + " = " + 
 field.get(this).toString() + "\n" : ""); 
 } catch (Exception ignored) {} 
 } 
 return res.toString().trim(); 
 } 
 static class CharacterThing { 
 private int hp; 
 private String name; 
 private double basicAttackDamage; 
 private double secondaryAttackDamage; 
 private double primaryAbilityDamage; 
 private double secondaryAbilityHeal; 
 private double ultimateAbilityDamage; 
 private int basicAttackCoolDownMillis; 
 private int secondaryAttackCoolDownMillis; 
 private int primaryAbilityCoolDownMillis; 
 private int secondaryAbilityCoolDownMillis;
 private int ultimateAbilityCoolDownMillis; 
 private double ultimateChargeRate; 
 private double ultimateChargePerDamage; 
                       /* Continued on Next Page */
```

```
 static { 
 out.println("You sure can."); 
 } 
 { 
 this.name = "Good Luck"; 
 out.println("Wait... you can do this?"); 
 } 
 public static CharacterThing thingy() { 
 return new CharacterThing(); 
 } 
 <2*> CharacterThing() {} 
 public CharacterThing hp(int hp) { 
 this.hp = hp; 
 return this; 
 } 
 public CharacterThing name(String name) { 
 this.name = name; 
 return this; 
 } 
 public CharacterThing basicAttackDamage(double basicAttackDamage) { 
 this.basicAttackDamage = basicAttackDamage; 
 return this; 
 } 
 public CharacterThing secondaryAttackDamage(double secondaryAttackDamage) { 
 this.secondaryAttackDamage = secondaryAttackDamage; 
 return this; 
 } 
 public CharacterThing primaryAbilityDamage(double primaryAbilityDamage) { 
 this.primaryAbilityDamage = primaryAbilityDamage; 
 return this; 
 } 
 public CharacterThing secondaryAbilityHeal(double secondaryAbilityHeal) { 
 this.secondaryAbilityHeal = secondaryAbilityHeal; 
 return this; 
 } 
 public CharacterThing ultimateAbilityDamage(double ultimateAbilityDamage) { 
 this.ultimateAbilityDamage = ultimateAbilityDamage; 
 return this; 
 } 
 public CharacterThing basicAttackCoolDownMillis(int basicAttackCoolDownMillis) { 
 this.basicAttackCoolDownMillis = basicAttackCoolDownMillis; 
 return this; 
 } 
 public CharacterThing secondaryAttackCoolDownMillis(int secondaryAttackCoolDownMillis) { 
 this.secondaryAttackCoolDownMillis = secondaryAttackCoolDownMillis; 
 return this; 
 } 
 public CharacterThing primaryAbilityCoolDownMillis(int primaryAbilityCoolDownMillis) { 
 this.primaryAbilityCoolDownMillis = primaryAbilityCoolDownMillis; 
 return this; 
 }
```

```
 public CharacterThing secondaryAbilityCoolDownMillis(int secondaryAbilityCoolDownMillis) { 
 this.secondaryAbilityCoolDownMillis = secondaryAbilityCoolDownMillis; 
 return this; 
 } 
 public CharacterThing ultimateAbilityCoolDownMillis(int ultimateAbilityCoolDownMillis) { 
 this.ultimateAbilityCoolDownMillis = ultimateAbilityCoolDownMillis; 
 return this; 
 } 
 public CharacterThing ultimateChargeRate(double ultimateChargeRate) { 
 this.ultimateChargeRate = ultimateChargeRate; 
 return this; 
 } 
 public CharacterThing ultimateChargePerDamage(double ultimateChargePerDamage) { 
 this.ultimateChargePerDamage = ultimateChargePerDamage; 
 return this; 
 } 
 public Character thing() { 
 return new Character(<1*>); 
 } 
 } 
} 
////////////////////////////////////////// client code ////////////////////////////////////////// 
Character character_1 = Character.CharacterThing.thingy() 
 .hp(76_67_77) 
 .name("Terry") 
 .basicAttackDamage(212) 
 .secondaryAttackDamage(131) 
 .primaryAbilityDamage(1413.14) 
 .secondaryAbilityHeal(1512.74) 
 .basicAttackCoolDownMillis(300) 
 .primaryAbilityCoolDownMillis(2500) 
 .secondaryAttackCoolDownMillis(1000) 
 .secondaryAbilityCoolDownMillis(4750) 
 .ultimateAbilityDamage(9999) 
 .ultimateAbilityCoolDownMillis(9000) 
 .ultimateChargeRate(0.015) 
 .ultimateChargePerDamage(0.045) 
 .thing(); 
Character character_2 = new Character.CharacterThing() 
 .hp(10_000) 
 .ultimateAbilityDamage(7231) 
 .basicAttackDamage(149) 
 .secondaryAttackDamage(342) 
 .thing(); 
out.println(character_1); // line 1 
out.println(character_2); // line 2
```

The CharacterThing class in the source code above demonstrates which of the following design patterns?

- **A)** Singleton
- **B)** Object Pool
- **C)** Builder
- **D)** Prototype
- **E)** Factory Method

Which of the following concepts is utilized in the client code to the right?

- **A)** Overriding
- **B)** Overloading
- **C)** Abstraction
- **D)** Method Chaining
- **E)** Encapsulation

```
Character character_2 = new 
 Character.CharacterThing() 
 .hp(212_212) 
 .name("Stacey") 
 .ultimateAbilityDamage(7231) 
 .basicAttackDamage(212) 
 .secondaryAttackDamage(342) 
 .thing();
```

## **Question 33**

Which of the following could replace **<1\*>** in the code above to ensure objects are created with the provided values?

- **A)** null
- **B)** CharacterThing.thingy()
- **C)** this
- **D)** Nothing is required.
- **E)** More than one of the above.

# **Question 34**

Which of the following could replace **<2\*>** in the code above to ensure all client code runs successfully in the following question?

- **A)** protected
- **B)** public
- **C)** void
- **D)** Nothing is required.
- **E)** More than one of the above.

Assuming any errors in the client code above have been corrected, what is output to the console when the code marked //line 1 has finished executing?

- **A)** You sure can. **B)** Wait... you can do this? Wait... you can do this? You sure can. hp = 766777 hp = 766777 name = Terry name = Good Luck basicAttackDamage = 212.0 basicAttackDamage = 212.0 secondaryAttackDamage = 131.0 secondaryAttackDamage = 131.0 primaryAbilityDamage = 1413.14 primaryAbilityDamage = 1413.14 secondaryAbilityHeal = 1512.74 secondaryAbilityHeal = 1512.74 ultimateAbilityDamage = 9999.0 ultimateAbilityDamage = 9999.0 basicAttackCoolDownMillis = 300 basicAttackCoolDownMillis = 300 secondaryAttackCoolDownMillis = 1000 secondaryAttackCoolDownMillis = 1000 primaryAbilityCoolDownMillis = 2500 primaryAbilityCoolDownMillis = 2500 secondaryAbilityCoolDownMillis = 4750 secondaryAbilityCoolDownMillis = 4750 ultimateAbilityCoolDownMillis = 9000 ultimateAbilityCoolDownMillis = 9000 ultimateChargeRate = 0.015 ultimateChargeRate = 0.015 ultimateChargePerDamage = 0.045 ultimateChargePerDamage = 0.045
- **C)** Wait... you can do this? **D)** You sure can. Wait... you can do this? Wait... you can do this? You sure can. Wait... you can do this? hp = 766777 hp = 766777 name = Good Luck name = Terry basicAttackDamage = 212.0 basicAttackDamage = 212.0 secondaryAttackDamage = 131.0 secondaryAttackDamage = 131.0 primaryAbilityDamage = 1413.14 primaryAbilityDamage = 1413.14 secondaryAbilityHeal = 1512.74 secondaryAbilityHeal = 1512.74 ultimateAbilityDamage = 9999.0 ultimateAbilityDamage = 9999.0 basicAttackCoolDownMillis = 300 basicAttackCoolDownMillis = 300 secondaryAttackCoolDownMillis = 1000 secondaryAttackCoolDownMillis = 1000 primaryAbilityCoolDownMillis = 2500 primaryAbilityCoolDownMillis = 2500 secondaryAbilityCoolDownMillis = 4750 secondaryAbilityCoolDownMillis = 4750 ultimateAbilityCoolDownMillis = 9000 ultimateAbilityCoolDownMillis = 9000 ultimateChargeRate = 0.015 ultimateChargeRate = 0.015 ultimateChargePerDamage = 0.045 ultimateChargePerDamage = 0.045

**E)** There is no output due to an error

Assuming any errors in the client code above have been corrected, what is output to the console when the code marked //line 2 has finished executing, ignoring all output by previous lines?

- A) hp = 10000
   name = Good Luck
   basicAttackDamage = 149.0
   secondaryAttackDamage = 342.0
   ultimateAbilityDamage = 7231.0
- C) Wait... you can do this? You sure can. hp = 10000name = Good LuckbasicAttackDamage = 149.0 secondaryAttackDamage = 342.0 primaryAbilityDamage = 1413.14 secondaryAbilityHeal = 1512.74 ultimateAbilityDamage = 7231.0 basicAttackCoolDownMillis = 300 secondaryAttackCoolDownMillis = 1000 primaryAbilityCoolDownMillis = 2500 secondaryAbilityCoolDownMillis = 4750 ultimateAbilityCoolDownMillis = 9000 ultimateChargeRate = 0.015 ultimateChargePerDamage = 0.045
- E) hp = 10000
   name = Good Luck
   basicAttackDamage = 149.0
   secondaryAttackDamage = 342.0
   primaryAbilityDamage = 0.0
   secondaryAbilityHeal = 0.0
   ultimateAbilityDamage = 7231.0
   basicAttackCoolDownMillis = 0
   secondaryAttackCoolDownMillis = 0
   primaryAbilityCoolDownMillis = 0
   secondaryAbilityCoolDownMillis = 0
   ultimateAbilityCoolDownMillis = 0
   ultimateChargeRate = 0.0
   ultimateChargePerDamage = 0.0

```
B) You sure can.
  Wait... you can do this?
  hp = 10000
  name = Good Luck
  basicAttackDamage = 149.0
  secondaryAttackDamage = 342.0
  ultimateAbilityDamage = 7231.0
```

- D) You sure can. Wait... you can do this? hp = 10000name = nullbasicAttackDamage = 149.0 secondaryAttackDamage = 342.0 primaryAbilityDamage = 0.0 secondaryAbilityHeal = 0.0 ultimateAbilityDamage = 7231.0 basicAttackCoolDownMillis = 0 secondaryAttackCoolDownMillis = 0 primaryAbilityCoolDownMillis = 0 secondaryAbilityCoolDownMillis = 0 ultimateAbilityCoolDownMillis = 0 ultimateChargeRate = 0.0 ultimateChargePerDamage = 0.0
- F) hp = 10000
  name = null
  basicAttackDamage = 149.0
  secondaryAttackDamage = 342.0
  primaryAbilityDamage = 0.0
  secondaryAbilityHeal = 0.0\nultimateAbilityDamage = 7231.0
  basicAttackCoolDownMillis = 0
  secondaryAttackCoolDownMillis = 0
  primaryAbilityCoolDownMillis = 0
  secondaryAbilityCoolDownMillis = 0\nultimateAbilityCoolDownMillis = 0\nultimateChargeRate = 0.0\nultimateChargePerDamage = 0.0

# Question 37

Which of the following statements is not true about protected methods?

- A) They can be accessed from within the class it was defined in.
- B) They can be accessed from a different class within same package as the protected method.
- C) They can be accessed from any subclass of the class it's contained in, within the same package as the protected method.
- D) They can be accessed from any subclass of the class it's contained in, from a different package than the protected method.
- E) None of the above.

## Question 38

Which of the following pairings does not properly match the data structure in question to the worst-case asymptotic time complexity of the operation on that structure?

- A) O(1) random access using an Array.
- C)  $O(\log n)$  search using a Tree Set
- **E)**  $O(\log n)$  search using a Binary Search Tree

- **B)**  $\mathcal{O}(1)$  find min using a Min-Heap
- **D)**  $\mathcal{O}(1)$  search using a Hash Set.

Consider a series of four (potentially identical) binary search trees created from 20 arbitrary, but distinct (no duplicate) values. Let the first tree be created such that the width of the tree is maximized. We will denote the width of that tree as max. Let the second tree be created such that the width of the tree is minimized. We will denote the width of that tree as min. Let the third tree be created such that the height of the tree is maximized. We will denote the height of that tree as ℎmax. Let the fourth tree be created such that the height of the tree is minimized. We will denote the height of that tree as ℎmin. Your answer should be these four values separated by commas in the order of max, min, ℎmax, ℎmin. When calculating the height or width of the tree, assume that the number of edges are being counted, and not the number of vertices.

### **Question 40**

Consider the adjacency matrix representation of the graph to the right. How many times does the value "0" appear in the adjacency matrix?

![](_page_11_Picture_4.jpeg)

![](_page_12_Picture_0.jpeg)

# **UIL COMPUTER SCIENCE – 2024-2025 STATE**

**Questions** (+6 points for each correct answer, -2 points for each incorrect answer)

1) B 11) E 21) B 31) C

2) C 12) B 22) A 32) D

3) C 13) E 23) B 33) C

4) A 14) A 24) A 34) E

5) B 15) C 25) C 35) D

6) B 16) C 26) G 36) E

7) D 17) B 27) B 37) E

8) C 18) A 28) B 38) E

9) A 19) D 29) D \*

39) 9,1,19,4

10) D 20) C 30) D \*

40) 86

**Note:** Correct responses are based on **Java SE Development Kit 22 (JDK 22)** from Sun Microsystems, Inc. All provided code segments are intended to be syntactically correct, unless otherwise stated (e.g., "error" is an answer choice) and any necessary Java SE 22 Standard Packages have been imported. Ignore any typographical errors and assume any undefined variables are defined as used.

*<sup>\*</sup> See "Explanation" section below for alternate, acceptable answers.*

# Explanations:

| 1.  | B | Basic base conversion problem.                                                                       |  |
|-----|---|------------------------------------------------------------------------------------------------------|--|
| 2.  | C | Basic order of operations problem.                                                                   |  |
| 3.  | C | %c will output a character with the ASCII value given. The number before the \$ in a printf          |  |
|     |   | term denotes which of the following objects will be output by the term, it is 1-indexed.             |  |
| 4.  | A | String's compareTo method will return the ASCII difference between the first two                     |  |
|     |   | characters that are different between the two Strings.                                               |  |
| 5.  | B | Simple boolean solving.                                                                              |  |
| 6.  | B | Math.nextAfter(a, b) will return the closest number to a in the direction of b (either               |  |
|     |   | positive or negative), so 4.49999999999… in this case.                                               |  |
| 7.  | D | Double boolean operators (  , &&), will short-circuit (if the first value is false for an &&, the    |  |
|     |   | second will not be evaluated because it is impossible for the expression to be true. Similar for     |  |
|     |   | the first value of a    expression being true). Single boolean operators do not so this.             |  |
| 8.  | C | Order of operations with Java expressions.                                                           |  |
| 9.  | A | Matrix Tracing.                                                                                      |  |
| 10. | D | Matrix Tracing.                                                                                      |  |
| 11. | E | Only a FileNotFoundException is required, but FileNotFoundException extends                          |  |
|     |   | IOException which extends Exception, so any of the 3 will work.                                      |  |
| 12. | B | Literals are allowed in switches, but since none of the cases are true only the default statement    |  |
|     |   | will execute.                                                                                        |  |
| 13. | E | Java Order of Precedence.                                                                            |  |
| 14. | A | After sorting: [1, 2, 4, 4, 8, 8], bytes is simply size divided by 8, and then it will be            |  |
|     |   | sorted. Then 1 and 4 will be chosen from positions 0 and 2.                                          |  |
| 15. | C | Simple ArrayList tracing, an ArrayList of Strings contains() method will use                         |  |
|     |   | .equals() to compare, not == so the actual content will be compared, not the memory                  |  |
|     |   | addresses.                                                                                           |  |
| 16. | C | NaN is never equal to NaN, and both values will be NaN once the operations are complete.             |  |
| 17. | B | Instance variables take precedence over inner classes with the same name.                            |  |
| 18. | A | The runtime of adding to a max-heap is<br>log , and it is being done  times.                         |  |
| 19. | D | Java's PriorityQueue utilizes a min-heap ordinarily, but because it is initialized with the          |  |
|     |   | Collections.reverseOrder() object, it is actually implementing a max-heap in this case.              |  |
| 20. | C | First String<br>m1 will match 2-7 words followed by a space, the String<br>s does not end with a     |  |
|     |   | space. Second String<br>m2 will match one or more instances of a capital letter followed by 0 or     |  |
|     |   | more lowercase letter followed by 0 or 1 spaces, which matches.                                      |  |
| 21. | B | The notation of extends T is a common pattern to be used when creating an instance of                |  |
|     |   | data structure that all extend a certain class T, but not within the definition of a class.          |  |
| 22. | A | Doing this will create a compile-time warning. The exact warning is as follows:                      |  |
|     |   | "The type parameter T is hiding the type T"                                                          |  |
|     |   | While also a compile-timer error produced by many IDEs, Java officially identifies this issue        |  |
|     |   | known as Type Hiding, which occurs when a class is re-defined within a more specific scope, thus     |  |
|     |   | hiding the existence of the class defined in the earlier scope.                                      |  |
| 23. | B | Doing this will create multiple compile-time errors. The first of these reveals the real issue. The  |  |
|     |   | exact wording of the first error is as follows:                                                      |  |
|     |   |                                                                                                      |  |
|     |   | "R cannot be resolved to a type"                                                                     |  |
|     |   | Note that R is defined within the localized scope of the Node class. Thus, the DataStructure         |  |
|     |   | class does not know of its existence since it was not defined within that scope or a higher scope.   |  |
|     |   | Note that this is unique from the issue of type hiding, as the type of R is simply not accessible to |  |
|     |   | the outside class due to issues with scope.                                                          |  |
| 24. | A | The DataStructure class is an implementation of a Dequeue which can be described as a                |  |
|     |   | combination of a Stack and a Queue. Namely, an<br>1 insertion and removal operation from             |  |
|     |   | the front of the structure (Queue-like) and the back of the structure (Stack-like).                  |  |

| 25. | C | Consider the following cover of edges that is a minimum spanning tree:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |  |
|-----|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|     |   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |  |
|     |   | There are multiple minimum spanning trees for this graph, but this one has a length of 35.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |
| 26. | G | Both Prim's and Kruskal's algorithms are algorithms for calculating the minimum spanning tree of<br>a graph.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |
| 27. | B | <br>Since  <br>  =<br><br>, we can note that<br>=<br><br>log 	. This is the time complexity for<br>log<br>Kruskal's algorithm.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  |
| 28. | B | The shortest path is either<br>or !"#<br>, both of which are of cost 21.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |  |
| 29. | D | Simple boolean table/expression evaluation/comparison                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |  |
| 30. | D | ≫<br>%&' ≡<br>&  ≡<br>Note that 8388608<br>≫ 10 ≡ 2<br>10 ≡ 2<br>2<br>8192                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  |
| 31. | C | This is a classic example of the Builder design pattern                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |  |
| 32. | D | This is a classic example of Method Chaining                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  |
| 33. | C | The this<br>keyword is the only option that keeps functionality. Option A compiles but leads to a<br>runtime exception, and option B compiles and executes but results in an empty object being<br>created every time with only default values.                                                                                                                                                                                                                                                                                                                                                     |  |
| 34. | E | Because of the client code marked //line2, the constructor must be reachable from the client<br>code which is assumed to be in the same package. This means that answer choices A, B, and C all<br>work.                                                                                                                                                                                                                                                                                                                                                                                            |  |
| 35. | D | Because both objects are created before being printed, the static block and setup block both<br>execute before the code marked //line1 is executed. Then the object prints with the values<br>set when creating the object.                                                                                                                                                                                                                                                                                                                                                                         |  |
| 36. | E | Since both objects have already been created and printed as part of the previous line, the output<br>here is only the object. The object prints all declared variables, and unassigned variables print<br>the primitive default values. name is set as part of the initializer block that was executed when<br>the object was created.                                                                                                                                                                                                                                                              |  |
| 37. | E | Protected methods, instance variables, constructors, and classes can be accessed by entities with<br>the following scopes: anything (i) within the same class (ii) within a subclass contained in the<br>same package (iii) within a class contained in the same package (iv) within a subclass contained<br>within a different package. The only situation that an entity cannot access a protected member is<br>if it is from a different class (not subclass) in a different package. The four options A through D<br>are equivalent to (i) through (iv), thus, the answer is none of the above. |  |
| 38. | E | While it is true that search in a binary search tree is Ω<br>log  (i.e., best case), it is not true that it<br>is<br>log  (i.e., worst case). Binary search trees have an<br>search operation since, in the<br>worst case, a binary search tree can effectively be a linked list.                                                                                                                                                                                                                                                                                                                   |  |

| 39. | 9,1,19,4 | Note that using the values 1 through 20 is a valid set of 20 arbitrary and distinct values. Any<br>other set of 20 values can be mapped to the values 1 through 20 based on their lexicographical<br>order. Therefore, we will assume that the values are 1 through 20 for the sake of creating<br>concrete examples of the four trees. Consider the following set of trees:                                    |  |
|-----|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--|
|     |          |                                                                                                                                                                                                                                                                                                                                                                                                                 |  |
|     |          |                                                                                                                                                                                                                                                                                                                                                                                                                 |  |
|     |          |                                                                                                                                                                                                                                                                                                                                                                                                                 |  |
|     |          | In general, ℎmin occurs when the tree is complete. That said, in this case, the proposed tree also<br>works. For max, we can note that a complete tree here only has a width of 8 while the tree<br>proposed has a width of 9. Note that attempting to increase this width would require a 21th                                                                                                                 |  |
|     |          | node. For the min and ℎmax cases, these both happen when the tree is effectively a linked list.                                                                                                                                                                                                                                                                                                                 |  |
| 40. | 86       | <br>An adjacency matrix for  	  vertices requires  	 <br>space to represent the edges<br>. Since we have<br>10, we know that the adjacency matrix will take up 10 =<br> 	  =<br>100 numbers (either a 1 for an<br>edge being present, or a 0 for an edge not being present). There are a total of 14 edges present,<br>so 14 of the 100 values will be a 1. This leaves 100<br>− 14 = 86 values that will be 0. |  |