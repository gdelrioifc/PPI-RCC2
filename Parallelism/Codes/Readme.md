<h3>This directory contains the codes used to calculate the angles between pairs of <i>RCC</i></h3>
<p>The pairs of <i>RCC</i> used are included in the directories <a href="https://github.com/gdelrioifc/PPI-RCC2/tree/main/Parallelism/Interacting">Interacting</a> and <a href="https://github.com/gdelrioifc/PPI-RCC2/tree/main/Parallelism/NonInteracting">Non interacting</a>.</p>

<p>To compile the Java files (extension .java), plese type in your console:</p>
<p>javac CalculateCosine_V2.java</p>
<p>That will generate 2 extra files with extension .class. To execute it, type in your console:</p>
<p>java CalculateCosine_V2</p>
<p>That would print out in your console the instructions to run it.</p>
<p>Please note you have to have installed Java Run Environment (JRE v8 or lower) in your computer.</p>

<p>For the Python files (extension .py and .sh), those must be executed in the following order:</p>
<table border=1>
<th>Program name</th><th>Description</th>
<tr>
  <td>p0_dirGen0.sh</td>
  <td>This bash script creates directories and compiles two java programs</td>
</tr>
<tr>
  <td>p1_interacting.py</td>
  <td>This python script reads the complexes file and writes a list of proteins with at least 1 interaction. Also calculates the average value for each one of the 26 components, and its standard deviation. Also calculates the sum of all 26 components for each vector in the list of proteins</td>
</tr>
<tr>
  <td>p2_sampleGenerator.py</td>
  <td>This python script takes the list of proteins and generates a given number of samples with certain number of items at the same time calculates the sum and average values for each component for all the vectors in the sample. By default the variable 'interact_case' is set to False. If 'interact_case' is set to True, this program will print a list of known interactions, but with a set of randomly generated corresponding vectors. Only works after running p3_generator with the 'interact_case' set to True</td>
</tr>
<tr>
  <td>p3_generator.py</td>
  <td>This python script simulates vectors for each sample taking into account the sum and average values. By default the variable 'interact_case' is set to False. If 'interact_case' is set to True, this program generate N samples but only for one set of sums and averages. This configuration will generate a set of random vectors corresponding to those with a known interaction, and should be used before p2_sampleGenerator.py with 'interact_case' set to True</td>
</tr>
<tr>
  <td>p4_runAngles.py</td>
  <td>This python script calculates the angles between all the non interacting proteins</td>
</tr>
<tr>
  <td>p5_runAngles.sh</td>
  <td>This bash script is needed to calculate the angle between all the proteins in a huge database like FullPDB</td>
</tr>
<tr>
  <td>p6_anglesInComplexes.py</td>
  <td>This python script calculates the angles between the interacting proteins, and between its corresponding random vectors</td>
</tr>
<tr>
  <td>p7_atLeast.py</td>
  <td>This python script counts the proteins with at least 1 parallel, in particular for angles gotten with p5_runAngles.sh</td>
</tr>
</table>
<p>Please note you need to have installed Python v3 on your computer.</p>
