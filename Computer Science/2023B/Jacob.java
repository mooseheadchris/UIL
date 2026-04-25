import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Jacob {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scrappydoo = new Scanner(new File("2023B\\jacob.dat"));
        int cases = scrappydoo.nextInt();
        double sum = 0;
        for (int i=0; i<cases; i++){
            int iter = scrappydoo.nextInt();
            for (int j=0; j<iter; j++){
                sum += 4.0/(2+2*j)/(2*j+3)/(2*j+4)*Math.pow(-1,j);
            }
            double pi = 3.0+sum;
            String print = String.format("%.13f", pi);

            
        System.out.println(print);
        sum = 0;
        }

        
    }
    
}
