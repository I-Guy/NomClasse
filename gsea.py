from __future__ import print_function
from goatools.base import download_go_basic_obo
obo_fname = download_go_basic_obo()
from goatools.base import download_ncbi_associations
file_gene2go = download_ncbi_associations()
from goatools.obo_parser import GODag
obodag = GODag("go-basic.obo")
import pandas as pd
from goatools.anno.genetogo_reader import Gene2GoReader
import mygene
mg = mygene.MyGeneInfo()
objanno = Gene2GoReader(file_gene2go, taxids=[10090])
ns2assoc = objanno.get_ns2assc()
for nspc, id2gos in ns2assoc.items():
    print("{NS} {N:,} annotated mouse genes".format(NS=nspc, N=len(id2gos)))
from genes_ncbi_10090_proteincoding import GENEID2NT as GeneID2nt_mus
from goatools.goea.go_enrichment_ns import GOEnrichmentStudyNS


goeaobj = GOEnrichmentStudyNS(
        GeneID2nt_mus, # List of mouse protein-coding genes
        ns2assoc, # geneid/GO associations
        obodag, # Ontologies
        propagate_counts = False,
        alpha = 0.05, # default significance cut-off
        methods = ['fdr_bh'])


df = pd.read_csv("test.csv" , sep = ",")


print(df.columns)
print(df['symbol'])
xli = df['symbol'].to_list()
print(df['id'].to_list())
out = mg.querymany(xli, scopes='symbol', fields='entrezgene', species='mouse')
entrez_id = []

for i in out:
	#print(i)
	try:
		entrez_id.append(int(i["_id"]))
	except (KeyError , ValueError) as error:
		pass

geneids_study = entrez_id
goea_results_all = goeaobj.run_study(geneids_study)
goea_results_sig = [r for r in goea_results_all if r.p_fdr_bh < 0.05]
goeaobj.wr_xlsx("GO_up.xlsx", goea_results_sig)



