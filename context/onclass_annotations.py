# Import OnClass and other libs
from OnClass.utils import *
from OnClass.OnClassModel import OnClassModel
from OnClass.other_datasets_utils import my_assemble, data_names_all, load_names

# Embed the cell ontology

OnClassModel = OnClassModel()
tp2emb, tp2i, i2tp = OnClassModel.EmbedCellTypes(dim=500,
    cell_type_network_file='../data/OnClass_data/OnClass_data_others/cell_ontology/cl.ontology',
    use_pretrain='../data/OnClass_data/pretrain/tp2emb_500')

# Here, we used the pretrain cell type embedding file tp2emb_500

data_file = '../data/OnClass_data/data_used_for_training/tabula-muris-senis-facs_cell_ontology.h5ad' #same as the input
train_X, train_genes, train_Y = read_data(feature_file=data_file, tp2i = tp2i, AnnData_label='cell_ontology_class_reannotated')

# Load the new dataset. Scanorama is used autoamtically to correct batch effcts.:
data_file = '../data/adata_small_test.h5ad'
test_X, test_genes, test_Y = read_data(feature_file=data_file, tp2i = tp2i, AnnData_label='cell_ontology_id')

# Predict the labels of cells in droplet cells. Scanorama is used autoamtically to correct batch effcts.:
# currently only running on tensor flow 1; working on the fix for tensor flow 2
