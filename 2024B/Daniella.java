import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Daniella {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scrappydoo = new Scanner(new File("C:\\VSCode\\daniella.dat"));

        int n = scrappydoo.nextInt();  // number of test cases
        for (int i=0; i<n; i++) {
            String word = scrappydoo.next();  // input word
            int k = scrappydoo.nextInt();  // number of splits

            // split the word and add a hyphen after every k letters except the last one
            for (int j=0; j<word.length(); j+=k) {
                if (j+k < word.length()) {
                    System.out.print(word.substring(j, j+k) + "-");
                } else {
                    System.out.print(word.substring(j));
                }
            }
            System.out.println();
        }
        scrappydoo.close();
    }

}