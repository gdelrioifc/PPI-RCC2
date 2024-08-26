import java.util.*;

class CalculateRunner_V2 implements Runnable
 {
  double degrees_separation;
  String pdb1, pdb2, cath1, cath2;
  ArrayList rcc1, rcc2;

  public CalculateRunner_V2(String p1, String p2, String c1, String c2, ArrayList r1, ArrayList r2, double ds)
   {
    pdb1=p1;
    pdb2=p2;
    cath1=c1;
    cath2=c2;

    rcc1=r1;
    rcc2=r2;

    degrees_separation=ds;
   }
  
  public double calculateNorm(ArrayList rcc, int inicio, int ultimo) throws Exception
   {
    double result = 0.0;

    double p=0.0, sumSqr=0.0;
    int i=0;
    for (i=inicio; i<ultimo; i++)
     {
      p=Double.parseDouble((String)rcc.get(i));

      sumSqr=Math.pow(p,2.0);

      result=result+sumSqr;
     }

    result = Math.sqrt(result);

    return result;
   }// end calculateNorm
 
  public String getCosine() throws Exception
   {
    String result = "";

    double degrees=0.0;
    double MT=0.0;
    double v1=0.0, v2=0.0, v3=0.0, v4=0.0, v5=0.0, v6=0.0, v7=0.0, v8=0.0, v9=0.0, v10=0.0, v11=0.0, v12=0.0, v13=0.0, v14=0.0, v15=0.0, v16=0.0, v17=0.0, v18=0.0, v19=0.0, v20=0.0, v21=0.0, v22=0.0, v23=0.0, v24=0.0, v25=0.0, v26=0.0;
    double w1=0.0, w2=0.0, w3=0.0, w4=0.0, w5=0.0, w6=0.0, w7=0.0, w8=0.0, w9=0.0, w10=0.0, w11=0.0, w12=0.0, w13=0.0, w14=0.0, w15=0.0, w16=0.0, w17=0.0, w18=0.0, w19=0.0, w20=0.0, w21=0.0, w22=0.0, w23=0.0, w24=0.0, w25=0.0, w26=0.0;
    double vw=0.0, vsqr=0.0, wsqr=0.0, rccS1=0.0, rccS2=0.0;

    v1=Double.parseDouble((String)rcc1.get(0));
    v2=Double.parseDouble((String)rcc1.get(1));
    v3=Double.parseDouble((String)rcc1.get(2));
    v4=Double.parseDouble((String)rcc1.get(3));
    v5=Double.parseDouble((String)rcc1.get(4));
    v6=Double.parseDouble((String)rcc1.get(5));
    v7=Double.parseDouble((String)rcc1.get(6));
    v8=Double.parseDouble((String)rcc1.get(7));
    v9=Double.parseDouble((String)rcc1.get(8));
    v10=Double.parseDouble((String)rcc1.get(9));
    v11=Double.parseDouble((String)rcc1.get(10));
    v12=Double.parseDouble((String)rcc1.get(11));
    v13=Double.parseDouble((String)rcc1.get(12));
    v14=Double.parseDouble((String)rcc1.get(13));
    v15=Double.parseDouble((String)rcc1.get(14));
    v16=Double.parseDouble((String)rcc1.get(15));
    v17=Double.parseDouble((String)rcc1.get(16));
    v18=Double.parseDouble((String)rcc1.get(17));
    v19=Double.parseDouble((String)rcc1.get(18));
    v20=Double.parseDouble((String)rcc1.get(19));
    v21=Double.parseDouble((String)rcc1.get(20));
    v22=Double.parseDouble((String)rcc1.get(21));
    v23=Double.parseDouble((String)rcc1.get(22));
    v24=Double.parseDouble((String)rcc1.get(23));
    v25=Double.parseDouble((String)rcc1.get(24));
    v26=Double.parseDouble((String)rcc1.get(25));
    w1=Double.parseDouble((String)rcc2.get(0));
    w2=Double.parseDouble((String)rcc2.get(1));
    w3=Double.parseDouble((String)rcc2.get(2));
    w4=Double.parseDouble((String)rcc2.get(3));
    w5=Double.parseDouble((String)rcc2.get(4));
    w6=Double.parseDouble((String)rcc2.get(5));
    w7=Double.parseDouble((String)rcc2.get(6));
    w8=Double.parseDouble((String)rcc2.get(7));
    w9=Double.parseDouble((String)rcc2.get(8));
    w10=Double.parseDouble((String)rcc2.get(9));
    w11=Double.parseDouble((String)rcc2.get(10));
    w12=Double.parseDouble((String)rcc2.get(11));
    w13=Double.parseDouble((String)rcc2.get(12));
    w14=Double.parseDouble((String)rcc2.get(13));
    w15=Double.parseDouble((String)rcc2.get(14));
    w16=Double.parseDouble((String)rcc2.get(15));
    w17=Double.parseDouble((String)rcc2.get(16));
    w18=Double.parseDouble((String)rcc2.get(17));
    w19=Double.parseDouble((String)rcc2.get(18));
    w20=Double.parseDouble((String)rcc2.get(19));
    w21=Double.parseDouble((String)rcc2.get(20));
    w22=Double.parseDouble((String)rcc2.get(21));
    w23=Double.parseDouble((String)rcc2.get(22));
    w24=Double.parseDouble((String)rcc2.get(23));
    w25=Double.parseDouble((String)rcc2.get(24));
    w26=Double.parseDouble((String)rcc2.get(25));
    vw=(v1*w1)+(v2*w2)+(v3*w3)+(v4*w4)+(v5*w5)+(v6*w6)+(v7*w7)+(v8*w8)+(v9*w9)+(v10*w10)+(v11*w11)+(v12*w12)+(v13*w13)+(v14*w14)+(v15*w15)+(v16*w16)+(v17*w17)+(v18*w18)+(v19*w19)+(v20*w20)+(v21*w21)+(v22*w22)+(v23*w23)+(v24*w24)+(v25*w25)+(v26*w26);
    vsqr=(v1*v1)+(v2*v2)+(v3*v3)+(v4*v4)+(v5*v5)+(v6*v6)+(v7*v7)+(v8*v8)+(v9*v9)+(v10*v10)+(v11*v11)+(v12*v12)+(v13*v13)+(v14*v14)+(v15*v15)+(v16*v16)+(v17*v17)+(v18*v18)+(v19*v19)+(v20*v20)+(v21*v21)+(v22*v22)+(v23*v23)+(v24*v24)+(v25*v25)+(v26*v26);
    wsqr=(w1*w1)+(w2*w2)+(w3*w3)+(w4*w4)+(w5*w5)+(w6*w6)+(w7*w7)+(w8*w8)+(w9*w9)+(w10*w10)+(w11*w11)+(w12*w12)+(w13*w13)+(w14*w14)+(w15*w15)+(w16*w16)+(w17*w17)+(w18*w18)+(w19*w19)+(w20*w20)+(w21*w21)+(w22*w22)+(w23*w23)+(w24*w24)+(w25*w25)+(w26*w26);

    if(vsqr==0.0) MT=-1.0;
    if(wsqr==0.0) MT=-1.0;
    if(vsqr!=0.0 && wsqr!=0.0) MT=(vw)/Math.sqrt(vsqr*wsqr);

		degrees=(180.0/Math.PI)*Math.acos(MT);

    if(degrees<degrees_separation)
     {
      result=""+(180.0/Math.PI)*Math.acos(MT);

      rccS1=Math.sqrt(vsqr);
      rccS2=Math.sqrt(wsqr);
      if(rccS1>=rccS2)
       {
        if(rccS2==0.0) vw=-1.0;
        else vw=rccS1/rccS2;
       }
      else
       {
        if(rccS1==0.0) vw=-1.0;
        else vw=rccS2/rccS1;
       }
      result=result;
     }
    return result;
   }// end getCosine

  public void run()
   {
    try
     {
      String result=getCosine();
      if(!result.equals("")) System.out.println(pdb1+","+pdb2+","+result);
     }
    catch(Exception e)
     {
      System.err.println("CalculateRunner_V2.run error: "+e.getMessage());
     }
   }
 }
