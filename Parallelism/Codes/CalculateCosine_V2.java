import java.io.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;
import java.util.concurrent.*;

public class CalculateCosine_V2
{
 static int MAX_TASKS;
 static int SIMULTANEOUS_TASKS;
 static int CATH_CLASS;
@SuppressWarnings("unchecked")
 public static void main(String[] args) throws Exception
  {
   if(args.length==3)
    {
     int processors = Runtime.getRuntime().availableProcessors();
     MAX_TASKS=Integer.parseInt(args[2])*processors;
     SIMULTANEOUS_TASKS = processors;
System.err.println("Processors found="+processors);
     int i=0, j=0, k=0, lines=0;
     double degrees_separation=Double.parseDouble(args[1]);
     String line="",clase="";
     String[] data = null;
     ArrayList rcc = null, rcc2=null;
     ArrayList rccs = new ArrayList(), pdbs = new ArrayList(), caths = new ArrayList();
     BufferedReader infile = new BufferedReader(new FileReader(args[0]));

     while((line=infile.readLine())!=null)
      {
       lines=lines+1;
       if(lines>1)
        {
         data = line.split(",");

         rcc = new ArrayList();
         pdbs.add(data[0]);
         caths.add(data[26]);
         for(i=1; i<27; i++) 
          {
           rcc.add(data[i]);
          }

         rccs.add(rcc);
        }
      }
     infile.close();

//     ExecutorService executor = Executors.newFixedThreadPool(SIMULTANEOUS_TASKS);
     ExecutorService executor = Executors.newFixedThreadPool(MAX_TASKS);
     CalculateRunner_V2 cr = null;
     System.out.println("PDB1,PDB2,Angle(degrees)");
     for(i=0; i<rccs.size()-1; i++)
      {
       rcc=(ArrayList)rccs.get(i);
       clase=(String)caths.get(i);
       for(j=i+1; j<rccs.size(); j++)
        {
         rcc2=(ArrayList)rccs.get(j);

         k=k+1;
         if(k>0 && k<=MAX_TASKS) 
          {
           cr = new CalculateRunner_V2((String)pdbs.get(i),(String)pdbs.get(j),(String)caths.get(i),(String)caths.get(j),rcc,rcc2,degrees_separation);
             executor.execute(cr);
//System.err.println(i+","+j+","+k);
           if(k==MAX_TASKS)
            {
             executor.awaitTermination(1,TimeUnit.MILLISECONDS);
//System.err.println(k+" threads finished");
             k=0;
            }
          }
        }
       executor.awaitTermination(1,TimeUnit.MILLISECONDS);
//System.err.println(k+" threads finished");
      }
     executor.shutdown();
     while(!executor.isTerminated()) {}
//System.err.println(k+" threads finished");
    }
   else
    {
     System.err.println("Usage:\njava CalculateCosineAndRatioBetweenRCCsDistributedArrayLists <infile> <degrees_separation> <max_tasks>");
     System.err.println("<infile> any file with RCC and CATH class; e.g., d5NoLatN0.csv.");
     System.err.println("<degrees_separation> is a double specifying the degrees separating the RCC to be considered; e.g., 5.");
     System.err.println("<max_tasks> is an integer that will multiple the number of processors foundn in the machine; e.g., 10.");
     System.err.println("The program will report for every pair of \"parallel\" RCCs compared their");
     System.err.println("cosine of their angle, norms and the ratio between their norms.");
     System.err.println("This is done using ArrayLists, recurrent distrubuted computing and reducing the number of comparison to only those pairs of RCC which degree of separation is < <degrees_separation> specified.");
     System.err.println("Note that the <max_tasks> allows the user to play with how many processes will run concurrently.");
     System.err.println("The output will be sent to the standard output in CSV format.");
     System.err.println("");
     System.err.println("");
    }
  }
}
