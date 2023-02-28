import sys

import pandas as pd
import argparse
import re
import os
import numpy as np
from pandas.api.types import is_numeric_dtype
from pathlib import Path
from tkinter import *
from tkinter.filedialog import *
import plotly.express as px

import plotly.graph_objects as go
from sklearn.impute import SimpleImputer
from diffexpr.py_deseq import py_DESeq2


df = pd.read_table('/home/administrateur/PycharmProjects/NomClasse/diffexpr/test/data/ercc.tsv')
sample_df = pd.DataFrame({'samplename': df.columns}) \
        .query('samplename != "id"')\
        .assign(sample = lambda d: d.samplename.str.extract('([AB])_', expand=False)) \
        .assign(replicate = lambda d: d.samplename.str.extract('_([123])', expand=False)) 
sample_df.index = sample_df.samplename




dds = py_DESeq2(count_matrix = df,
               design_matrix = sample_df,
               design_formula = '~ replicate + sample',
               gene_column = 'id') # <- telling DESeq2 this should be the gene ID column
    
dds.run_deseq() 
dds.get_deseq_result(contrast = ['sample','B','A'])
res = dds.deseq_result 
res.head()

dds.normalized_count()

dds.comparison 

lfc_res = dds.lfcShrink(coef=4, method='apeglm')
print(type(lfc_res))
print(lfc_res)

