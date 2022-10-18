__author__ = "Ilango Guy"
__version__ = "0.0.1"
__licence__ = "CEPR"
__doc__ = "Window for proteomic analysis"


#import deseq2
import pandas as pd
import deseq2
import re
import os
from pathlib import Path
from tkinter import *
from tkinter.filedialog import *
import plotly.express as px
import dash_bio
import plotly.graph_objects as go
from scipy.stats import ttest_ind

def rundesq2(design , count):
    list_name = []
    df = pd.read_csv(count, sep=";")

    for i in df:
        list_name.append(i)
    df2 = pd.DataFrame(index=list_name)
    df3 = np.log2(df)


    deseq2.py_DESeq2(path_to_data.get() , path_to_design.get() ,design_formula.get(), gene_column=__id__.get() )
    with open(design ,"r") as desig:
        for line in desig:
            sline = line.strip().split("-")

            df2[sline[0]] = df.loc[df['cdt'] == sline[0], ].mean()
            df2[sline[1]] = df.loc[df["cdt"] == sline[1] , ].mean()
            df2['{sline[0]}_vs_{sline[1]}'] = np.log2(df[sline[0]]/df[sline[1]])
            df2['pval of {sline[0]}_vs_{sline[1]}'] = ttest_ind(df3.loc[df['cdt'] == sline[0], ],df3.loc[df["cdt"] == sline[1]])
            df2.to_csv("DE.csv")




def get_data_frame():
    filename = askopenfilename(title="Find text file", filetypes=[('txt files', '.txt'),('csv files' ,'.csv') ,('tsv files','.tsv'), ('all files', '.*')])
    path_to_data.set(filename)
fenetre = Tk()

window_label = Label(fenetre, text="Differential expression analysis")
window_label.pack()

# Frame
Frame_count = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame_count.pack(side=LEFT, padx=30, pady=30)

Frame_design = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame_design.pack(side=LEFT, padx=30, pady=60)

Frame_formula= Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame_formula.pack(side=LEFT, padx=30, pady=90)

Frame_id = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame_id.pack(side=LEFT, padx=30, pady=120)


#In Frame_count
path_count = Label(Frame_count, text="Select count matrix")
path_count.pack()
path_to_data = StringVar()
path_to_data.set("Path_to_the_D")
path_t = Entry(Frame_count, textvariable=path_to_data, width=30)
path_t.pack()
path_button = Button(Frame_count , text = 'Get count matrix' , command = get_data_frame)
path_button.pack()

#In Frame_design
path_design = Label(Frame_design, text="Select design matrix")
path_design.pack()
path_to_design = StringVar()
path_to_design.set("Path_to_the_D")
path_tt = Entry(Frame_design, textvariable=path_to_design, width=30)
path_tt.pack()
path_button_design = Button(Frame_design , text = 'Get design matrix' , command = get_data_frame)
path_button_design.pack()

#In Frame_formula
formula = Label(Frame_formula, text="Select design matrix")
formula.pack()
design_formula = StringVar()
design_formula.set("~ Design Formula")
formula_tt = Entry(Frame_formula, textvariable=design_formula, width=30)
formula_tt.pack()


#In Frame_ID
_id_ = Label(Frame_id, text="Select gene id")
_id_.pack()
__id__ = StringVar()
__id__.set("Gene ID")
formula_id = Entry(Frame_id, textvariable=__id__, width=30)
formula_id.pack()

run = Button(fenetre, text = "Run", command = rundesq2)
exit=Button(fenetre, text="Fermer", command=fenetre.quit)

run.pack()
exit.pack()
fenetre.mainloop()