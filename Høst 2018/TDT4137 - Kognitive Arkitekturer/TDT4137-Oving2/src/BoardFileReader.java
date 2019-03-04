import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class BoardFileReader {

    //This file reads the board textfiles and return them as nested ArrayLists.
    public static ArrayList<ArrayList<String>> read() throws IOException {
        ArrayList<ArrayList<String>> board = new ArrayList<ArrayList<String>>();
        File file = new File("/C:\\Users\\Erling\\Desktop\\36\\TDT4137-Oving2\\src\\boards\\board-2-4.txt");
        java.io.FileReader fr = new java.io.FileReader(file);
        BufferedReader br = new BufferedReader(fr);
        String line;
        int counter = 0;
        while ((line = br.readLine()) != null) {
            board.add(new ArrayList<String>());
            for (int i = 0; i < line.split("").length; i++) {
                board.get(counter).add(line.split("")[i]);
            }
            counter += 1;

        }
        br.close();
        fr.close();

        return board;
    }
}