import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;

public class Billy {
    public static void main(String[] args) throws FileNotFoundException {
       
        Scanner scoobydoo = new Scanner(new File("C:\\VSCode\\InvB\\billy.dat"));

        double win,loss, max = 0;
        String team, max_team = "";
                
            for (int i = 0; i < 8; i++) {
                team = scoobydoo.nextLine();
                //System.out.print(team);
                win = scoobydoo.nextDouble();
                //System.out.print(win);
                loss = scoobydoo.nextDouble();
                //System.out.println(loss);
                if (win / (win + loss) > max) {
                    max = win / (win + loss);
                    max_team = team;
                }
                //System.out.println(max_team);
                scoobydoo.nextLine();
            }
            
            System.out.println(max_team);
            
            scoobydoo.close();
    }
}