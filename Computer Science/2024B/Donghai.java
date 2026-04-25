import java.io.FileNotFoundException;
import java.util.Scanner;
import java.io.File;

public class Donghai {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner shaggy = new Scanner(new File("C:\\VSCode\\donghai.dat"));
        
        int pp = shaggy.nextInt(); // number of paragraphs
        shaggy.nextLine();  
        for (int ii=0; ii<pp; ii++) {
            String paragraph = shaggy.nextLine();  // input paragraph
                
            //count total amount of each letter in paragraph
            int a = 0, b = 0, c = 0, d = 0, e = 0, f = 0, g = 0, h = 0, i = 0, j = 0, k = 0, l = 0, m = 0, n = 0, o = 0, p = 0, q = 0, r = 0, s = 0, t = 0, u = 0, v = 0, w = 0, x = 0, y = 0, z = 0;
            for (int jj=0; jj<paragraph.length(); jj++) {
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'a') a += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'b') b += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'c') c += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'd') d += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'e') e += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'f') f += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'g') g += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'h') h += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'i') i += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'j') j += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'k') k += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'l') l += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'm') m += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'n') n += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'o') o += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'p') p += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'q') q += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'r') r += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 's') s += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 't') t += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'u') u += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'v') v += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'w') w += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'x') x += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'y') y += 1;
                if (Character.toLowerCase(paragraph.charAt(jj)) == 'z') z += 1;
            }
            // print the amount of each letter with non-zero counts
            if (a != 0) System.out.println("A: " + a);
            if (b != 0) System.out.println("B: " + b);
            if (c != 0) System.out.println("C: " + c);
            if (d != 0) System.out.println("D: " + d);
            if (e != 0) System.out.println("E: " + e);
            if (f != 0) System.out.println("F: " + f);
            if (g != 0) System.out.println("G: " + g);
            if (h != 0) System.out.println("H: " + h);
            if (i != 0) System.out.println("I: " + i);
            if (j != 0) System.out.println("J: " + j);
            if (k != 0) System.out.println("K: " + k);
            if (l != 0) System.out.println("L: " + l);
            if (m != 0) System.out.println("M: " + m);
            if (n != 0) System.out.println("N: " + n);
            if (o != 0) System.out.println("O: " + o);
            if (p != 0) System.out.println("P: " + p);
            if (q != 0) System.out.println("Q: " + q);
            if (r != 0) System.out.println("R: " + r);
            if (s != 0) System.out.println("S: " + s);
            if (t != 0) System.out.println("T: " + t);
            if (u != 0) System.out.println("U: " + u);
            if (v != 0) System.out.println("V: " + v);
            if (w != 0) System.out.println("W: " + w);
            if (x != 0) System.out.println("X: " + x);
            if (y != 0) System.out.println("Y: " + y);
            if (z != 0) System.out.println("Z: " + z);
        
            System.out.println("==========");  
        }

        shaggy.close();
    }
}

