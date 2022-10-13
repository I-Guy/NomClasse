from __future__ import print_function

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


def volcanoPlot():

    df = pd.read_csv(path_to_data.get(), sep=";")
    fig = go.Figure()
    features = []
    for i in df:
        features.append(i)
    for j in range(value.get()):
        trace1 = go.Scatter(
        x=df['log2_asp'],
        y=df['logpval_asp'],
        mode='markers',
        name='asp',
        hovertext=list(df['prot_asp'])
        )
    trace2 = go.Scatter(
    x=df['log2_pseudo'],
    y=df['logpval_pseudo'],
    mode='markers',
    name='pseudo',
    hovertext=list(df['prot_pseudo'])
    )


def goterm():
    from goatools.base import download_go_basic_obo
    obo_fname = download_go_basic_obo()
    from goatools.base import download_ncbi_associations
    fin_gene2go = download_ncbi_associations()
    from goatools.obo_parser import GODag

    obodag = GODag("go-basic.obo")

    from goatools.anno.genetogo_reader import Gene2GoReader
    objanno = Gene2GoReader(fin_gene2go, taxids=[10090])
    ns2assoc = objanno.get_ns2assc()

    for nspc, id2gos in ns2assoc.items():
        print("{NS} {N:,} annotated mouse genes".format(NS=nspc, N=len(id2gos)))
    from genes_ncbi_10090_proteincoding import GENEID2NT as GeneID2nt_mus
    print(len(GeneID2nt_mus))
    from goatools.goea.go_enrichment_ns import GOEnrichmentStudyNS

    goeaobj = GOEnrichmentStudyNS(
        GeneID2nt_mus.keys(),  # List of mouse protein-coding genes
        ns2assoc,  # geneid/GO associations
        obodag,  # Ontologies
        propagate_counts=False,
        alpha=0.05,  # default significance cut-off
        methods=['fdr_bh'])  # defult multipletest correction method
    import os
    geneid2symbol = {}
    # Get xlsx filename where data is stored
    ROOT = os.path.dirname(os.getcwd())  # go up 1 level from current working directory
    din_xlsx = os.path.join(ROOT, "goatools/test_data/nbt_3102/nbt.3102-S4_GeneIDs.xlsx")
    # Read data
    if os.path.isfile(din_xlsx):
        import xlrd
        book = xlrd.open_workbook(din_xlsx)
        pg = book.sheet_by_index(0)
        for r in range(pg.nrows):
            symbol, geneid, pval = [pg.cell_value(r, c) for c in range(pg.ncols)]
            if geneid:
                geneid2symbol[int(geneid)] = symbol
        print('{N} genes READ: {XLSX}'.format(N=len(geneid2symbol), XLSX=din_xlsx))
    else:
        raise RuntimeError('FILE NOT FOUND: {XLSX}'.format(XLSX=din_xlsx))
    # 'p_' means "pvalue". 'fdr_bh' is the multipletest method we are currently using.
    geneids_study = geneid2symbol.keys()
    goea_results_all = goeaobj.run_study(geneids_study)
    goea_results_sig = [r for r in goea_results_all if r.p_fdr_bh < 0.05]
    goeaobj.wr_xlsx("nbt3102.xlsx", goea_results_sig)
    goeaobj.wr_txt("nbt3102.txt", goea_results_sig)

    from goatools.godag_plot import plot_gos, plot_results, plot_goid2goobj

    plot_results("nbt3102_{NS}.png", goea_results_sig)




def run_de():
    os.system("python3 differential_expression.py")
def get_data_frame():
    filename = askopenfilename(title="Find text file", filetypes=[('txt files', '.txt'), ('all files', '.*')])
    path_to_data.set(filename)
fenetre = Tk()

window_label = Label(fenetre, text="Proteomics/Transcriptomics analysis")
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




GO = Button(fenetre , text = "Gene ontology" , command = goterm)
de = Button(fenetre , text= "Differential Expression" , command = run_de)
heatomap = Button(fenetre, text = "Heatmap" , command = heatmap)
volcoco = Button(fenetre, text ="Volcano" , command = volcanoPlot)
exit=Button(fenetre, text="Fermer", command=fenetre.quit)


GO.pack()
de.pack()
heatomap.pack()
volcoco.pack()
exit.pack()
fenetre.mainloop()



