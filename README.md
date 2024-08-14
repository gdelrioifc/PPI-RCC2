# PPI-RCC2
<h3>Supplementary Material for "Residue Cluster Classes in Protein-Protein Interactions" in "Aggregates &amp; Clusters of Amino Acids. Properties and biochemical consequences", edited by Vladimir Uversky y Munishwar Nath Gupta (CRC Press).</h3>

In this site you will find the training and testing datasets used to evaluate 3 different models previously reported by our group to efficiently classify protein-protein interactions (PPI) <a href="https://pubmed.ncbi.nlm.nih.gov/32640745/">(1)</a>.

The training sets are included in the <a href="https://github.com/gdelrioifc/PPI-RCC2/tree/main/Training">Training</a> directory. The testing sets are included in the <a href="https://github.com/gdelrioifc/PPI-RCC2/tree/main/Testing">Testing</a> directory. Both sets are included in the ARFF file format useable by <a href="https://ml.cms.waikato.ac.nz/weka/">Weka</a>.

The Weka models trained to predict PPI are included in <a href="https://github.com/gdelrioifc/PPI-RCC2/tree/main/Models">Models</a> directory. These files are in a binary format readable by Weka.

To use this model, you want want to install <a href="https://waikato.github.io/weka-wiki/downloading_weka/">Weka jar</a> file in your computer, then type the following command in your console:

java -cp <weka-jar>:. weka.classifiers.meta.AutoWEKAClassifier -T <arff_file> -l <weka_model>

where <weka-jar> corresponds with the full path to the weka.jar file located in your computer, <arff_file> is any of the files in the Testing dir or any other similar file and <weka_model> is any of the weka models reported in the Models directory.

The directory <a href="https://github.com/gdelrioifc/PPI-RCC2/tree/main/Parallelism">Parallelism</a> contains the data (RCC vectors) and codes used to evaluate the parallelism/semi-parallelism observed in 4 different datasets, including: Full_DB, Experimental_DB, AlphaFold_DB and Random_DB. Please review the original work for a full desciption of these datasets.
