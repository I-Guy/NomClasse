__author__ = "Ilango Guy"
__version__ = "0.0.1"
__licence__ = "CEPR"
__doc__ = "Window for proteomic analysis"


"""
Library
"""

import pandas as pd
import argparse
import re
import os
from pathlib import Path
from tkinter import *
from tkinter.filedialog import *
import plotly.express as px
import dash_bio
import plotly.graph_objects as go

def heatmap():
    try:
        os.mkdir("HEATOMAP")
    except OSError as error:
        print(error)
    df = pd.read_csv(path_to_data.get() , sep =";")
    print(df)
    feature_name = []
    for i in df:
        feature_name.append(i)
    val_list = []
    for j in df[target_data.get()]:
        val_list.append(j)
    print(len(feature_name) , len(val_list))
    fig = px.imshow(df, labels=dict(x="ID", y="Protein", color='FoldChange'), y = val_list,
                    x=feature_name, width=700, height=2800)
    fig.update_xaxes(side='top')
    fig.write_html("heatmap.html")

"""
def volcanoPlot():
    df = pd.read_csv(path_to_data.get(), sep=";")
    fig = go.Figure()
    features = []
    for i in df:
        features.append(i)
    trace1 = go.Scatter(
    x=df2['log2_asp'],
    y=df2['logpval_asp'],
    mode='markers',
    name='asp',
    hovertext=list(df2['prot_asp'])
    )
    trace2 = go.Scatter(
    x=df3['log2_pseudo'],
    y=df3['logpval_pseudo'],
    mode='markers',
    name='pseudo',
    hovertext=list(df3['prot_pseudo'])
    )
"""
"""
def make_fc():
    df = pd.read_csv(path_to_data.get() ,sep =";")
    for i in
"""
"""
def diff_prot():
    deseq2.py_DESeq2(count_matrix, design_matrix, design_formula, gene_column='id')
"""

def run_de():
    os.system("python3 differential_expression.py")
def get_data_frame():
    filename = askopenfilename(title="Find text file", filetypes=[('txt files', '.txt'), ('all files', '.*')])
    path_to_data.set(filename)
fenetre = Tk()

window_label = Label(fenetre, text="Proteomics analysis")
window_label.pack()

# Frame
Frame_data = Frame(fenetre, borderwidth=2, relief=GROOVE)
Frame_data.pack(side=LEFT, padx=30, pady=30)

Frame_target = Frame(fenetre, borderwidth = 2 , relief = GROOVE)
Frame_target.pack(side=LEFT , padx=30 , pady = 60)


#In Frame_data
path_label = Label(Frame_data, text="Select dataframe")
path_label.pack()
path_to_data = StringVar()
path_to_data.set("Path_to_the_D")
path_t = Entry(Frame_data, textvariable=path_to_data, width=30)
path_t.pack()
path_button = Button(Frame_data , text = 'Get DataFrame' , command = get_data_frame)
path_button.pack()

#In Frame_target
target_label = Label(Frame_target, text="Select target feature")
target_label.pack()
target_data = StringVar()
target_data.set("write col names of features")
target_t = Entry(Frame_target, textvariable=target_data, width=30)
target_t.pack()



value = StringVar()
value.set("Number of condition")
entree = Entry(fenetre, textvariable=value, width=30)
entree.pack()



calc = Button(fenetre, text = "Calculate Fold Change" , command = fenetre.quit)
GO = Button(fenetre , text = "Gene ontology" , command = fenetre.quit)
de = Button(fenetre , text= "Differential Expression" , command = run_de)
heatomap = Button(fenetre, text = "Heatmap" , command = heatmap)
volcoco = Button(fenetre, text ="Volcano" , command = fenetre.quit)
exit=Button(fenetre, text="Fermer", command=fenetre.quit)

calc.pack()
GO.pack()
de.pack()
heatomap.pack()
volcoco.pack()
exit.pack()
fenetre.mainloop()



