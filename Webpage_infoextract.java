/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package webpage_infoextract;
import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.util.*;
/**
 *
 * @author Satanu
 */
public class Webpage_infoextract {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException, UnsupportedEncodingException, IOException {
        // TODO code application logic here
        String path1 = "C:\\Users\\Satanu\\json\\";
        String path2 = "C:\\Users\\Satanu\\actual_json\\";
        
        String start_tag = "{\"report\":{";
        String title_tag = "\"title\":";
        String source_tag = "\"source\":";
        String date_tag = "\"date\":";
        String content_tag = "\"content\":";
        
        String end_singletag = "}";
        String end_tag = "}\n}";
        
        String source = "";
        String title = "";
        String date="";
        String author = "";
        String content="";
        
        final FileNameExtensionFilter extensionFilter = new FileNameExtensionFilter("N/A","txt");//, whatever other extensions you want);
        final File file = new File(path1);
        for(File child : file.listFiles()) {
            if(extensionFilter.accept(child)) {
                Scanner sc = new Scanner(child);
                int counter = 0;
                while (sc.hasNextLine()){
                    String line = sc.nextLine();
                    line = line.trim();
                    if (counter == 0){
                        title = line.trim();
                    }
                    else if (counter > 0 ){
                        content += line.trim();
                    }
                    counter++;
                }
                //Path p = Paths.get(String(child));
                String f_name = child.getName();
                int index = f_name.indexOf(".txt");
                f_name = f_name.substring(0,index);
                
                Webpage_infoextract obj = new Webpage_infoextract();
                source = obj.sourceExtractor(f_name);
                
                System.out.println(f_name+"\t"+source);
                
                //String sWrite = start_tag+"\n"+title_tag+" \""+title+"\","+"\n"+content_tag+" \""+content+"\""+"\n"+end_tag;
                String sWrite = start_tag+"\n"+title_tag+" \""+title+"\","+"\n"+source_tag+" \""+source+"\","+"\n"+content_tag+" \""+content+"\""+"\n"+end_tag;        
                Writer out = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(path2+f_name+".json"), "UTF-8"));
                try {
                    out.write(sWrite);
                } finally {
                    out.close();
                }

            }
            
        }
        
        //System.out.println(title);
    }
    
    public String sourceExtractor(String n) throws FileNotFoundException{
        
        String file_name = "C:\\Users\\Satanu\\actual_link.txt";
        File f = new File(file_name);
        Scanner sc = new Scanner(f);
        int lineNum = 0;
        String source_name = "";
        while(sc.hasNextLine()){
            String line = sc.nextLine();
            String arr[] = line.split("\t");
            String match = lineNum+arr[0];
           
            if(n.equals(match)){
                //System.out.println(arr[1]);
                String source[] = arr[1].split("/");
                /*for(int i=0;i<source.length;i++){
                    System.out.println(source[i]);
                }*/
                source_name = source[2];
            }
            lineNum++;
        }
        
        return source_name;
    }
    
}
