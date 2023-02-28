##TODO :: RIEN JAI FINI 




import sys

import pandas as pd
import argparse
import re
import os
import numpy as np
import pickle as pkl
from pandas.api.types import is_numeric_dtype
from pathlib import Path
from tkinter import *
from tkinter.filedialog import *
import plotly.express as px
import plotly.graph_objects as go
from sklearn.impute import SimpleImputer
from diffexpr.py_deseq import py_DESeq2
from scipy import stats
from sklearn.decomposition import PCA
df = pd.read_table("ercc.tsv" , sep ="\t")
id_list =  list(df["id"])
df=df.set_index("id")
df=df.T
design = pd.read_table("design.csv", sep = ",")
print(design)


print(df)
pval_dict = {}
for i in df:
	shapiro_test = stats.shapiro(df[i])	
	pval_dict[i] = shapiro_test.pvalue

print(pval_dict)
val_list= []
for j in df.columns:
		val_list.append(j)
X = df[val_list]

pca = PCA(n_components=2)
components = pca.fit_transform(X)
print(components)
fig = px.scatter(components, x=0, y=1, color = design["sample"].to_list())
fig.write_html("pca.html")
