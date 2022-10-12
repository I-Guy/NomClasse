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

"""
def heatmap(file):
    try:
        os.mkdir("HEATOMAP")
    except OSError as error:
        print(error)
    df = 
    
"""
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
GO = Button(fenetre , text = "Gene ontology" , command = fenetre.quit)
de = Button(fenetre , text= "Differential Expression" , command = fenetre.quit )
heatomap = Button(fenetre, text = "Heatmap" , command = fenetre.quit)
exit=Button(fenetre, text="Fermer", command=fenetre.quit)

GO.pack()
de.pack()
heatomap.pack()
exit.pack()
fenetre.mainloop()



