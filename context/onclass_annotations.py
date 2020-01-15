# Import OnClass and other libs
from OnClass.utils import *
from OnClass.OnClassModel import OnClassModel
from OnClass.other_datasets_utils import my_assemble, data_names_all, load_names

# Embed the cell ontology

OnClassModel = OnClassModel()
tp2emb, tp2i, i2tp = OnClassModel.EmbedCellTypes(dim=500,
    cell_type_network_file='./OnClass_data/cell_ontology/cl.ontology',
    use_pretrain='./OnClass_data/pretrain/tp2emb_500')


# Here, we used the pretrain cell type embedding file tp2emb_500

data_file = './raw_data/tabula-muris-senis-facs_cell_ontology.h5ad'
train_X, train_genes, train_Y = read_data(feature_file=data_file, tp2i = tp2i, AnnData_label='cell_ontology_class_reannotated')


# Used the trained model
OnClassModel.train(train_X, train_Y, tp2emb, train_genes, nhidden=[500], log_transform = True,
    use_pretrain = '../../../OnClass_data/pretrain/BilinearNN_50019')

# Predict the labels of cells in droplet cells. Scanorama is used autoamtically to correct batch effcts.:

data_file = '../../../OnClass_data/raw_data/tabula-muris-senis-facs_cell_ontology.h5ad' #same as the input
test_X, test_genes, test_Y = read_data(feature_file=data_file, tp2i = tp2i, AnnData_label='cell_ontology_class_reannotated')

test_label = OnClassModel.predict(test_X, test_genes,log_transform=False,correct_batch=True)
