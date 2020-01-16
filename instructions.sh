#!/usr/bin/env bash
set -o errexit
set -o pipefail

[ -e tabula-muris-senis-facs_cell_ontology.h5ad] ||#if script runs ok, don't download -- check how to do for directories

# Train dataset

[ -e ./data/adata_small_test.h5ad] || wget https://drive.google.com/file/d/1R09kuT6oxQjEFtB2UZbotsOP56u-aeT_/view?usp=sharing


# OnClass pretrained model
[ -e ./data/OnClass_data/pretrain/tp2emb_500X.npy] || wget https://files.figshare.com/21009027/pretrain.tar.gz -O - | tar -xz -C ./data/OnClass_data/
# Cell type embeddings, marker genes and 26-datasets
[ -e ./data/OnClass_data/OnClass_data_others/cell_ontology/cl.ontology.gz] || wget https://files.figshare.com/20157284/OnClass_data_others.tar.gz -O - | tar -xz -C ./data/OnClass_data/
# FACS cells used in the study
[ -e ./data/OnClass_data/data_used_for_training/tabula-muris-senis-facs_cell_ontology.h5ad] || wget https://files.figshare.com/20157215/tabula-muris-senis-facs_cell_ontology.h5ad -O ./data/OnClass_data/data_used_for_training/tabula-muris-senis-facs_cell_ontology.h5ad



build Dockerimage
run Dockerimage with the files we have pulled down
check output is what we want the output to be
