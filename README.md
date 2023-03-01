Authors: ILANGO Guy 

Version : 0.0.3  

Draw : Cezard Adeline

Affiliation: Research Center for Respiratory Diseases (France)

Credit : CEPR ILANGO G., CEPR CEZARD A.



-----------------------------------------------
Insert a cool name here
-----------------------------------------------

NomClasse is made for all kind of analysis. It just need a formated table to process it. 

Features : - PCA (2d , 3d ) 
           - Differential expression analysis (DE)
           - Heatmap
           - VolcanoPlot
           - Gene ontology
           
This tools can only be used with a GUI

------------------------------------------------
Prerequisite
------------------------------------------------
- python 3.7
- tkinter
- numpy
- diffexpr
- goatools
- mygene
- plotly
- sklearn
- pandas
- rpy2

-------------------------------------------------
How to use
-------------------------------------------------

You have to load your count matrix with sample as column and gene as rows. You have to precise all replicate (ex  : A_1,A_2,A_3,B_1,B_2,B_3)
Then you can just click on the DE button, this will create automatically your design matrix. And output a DE.csv containing fold change and pvalue. 
The DE button use diffexpr which is a python implementation of DesEQ2. 

Volcano : You have to load count matrix and design matrix , then just click on volcano plot.




