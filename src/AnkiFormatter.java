import java.util.Scanner;

import java.io.PrintStream;
import java.io.File;

public class AnkiFormatter{

   private static final short index_POS = 0;
   private static final short index_KANJI = 1;
   private static final short index_FURIGANA = 2;
   private static final short index_ENGLISH = 3;
   private static final char HT = (char)(9);
   
   private static String rawIn, splitIn[];
   private static String formattedString;
   private static Scanner in;
   private static PrintStream out;

   private static String out_string = "./formattedOut.txt";

   public static void main(String arg[]){

      //read file, skip tag lines
      try{
         in = new Scanner(new File("rawIn.txt"));
         out = new PrintStream(new File(out_string));
      }
      catch(Exception E){}
      
      out.println("#deck:Japanese::日本語 - the everything deck");
      out.println("#notetype:Japanese-75658");
      while(in.hasNext()){
         //skip # lines
         rawIn = in.nextLine().trim();
         if("#".equals(rawIn.charAt(0) + "")){
            System.out.println("SKIPPED ANKI FORMAT LINE");
            print(rawIn);
            continue;
         }
         //read entry, format it, save twice to formatted output
         splitIn = rawIn.split(HT + "");
         
         formattedString = splitIn[index_KANJI]+ HT + HT + splitIn[index_FURIGANA] + HT 
            + splitIn[index_ENGLISH] + HT + HT + splitIn[index_POS];
         
         print(formattedString);

         if(!splitIn[index_FURIGANA].equals("")){
            formattedString = splitIn[index_FURIGANA]+ HT + HT + splitIn[index_KANJI] + HT 
               + splitIn[index_ENGLISH] + HT + HT + splitIn[index_POS];
            
            print(formattedString);
         }
      }   
      // Run the Python Script to import the new cards
      String[] envArr = {"python","AnkiImporter.py", out_string};
      try{
         Runtime.getRuntime().exec(envArr);
      }
      catch(Exception E){
         System.out.println("Had some kind of error.");
      }
   }
   
   private static void print(String s){
      out.println(s);
      System.out.println(s);
   }

}