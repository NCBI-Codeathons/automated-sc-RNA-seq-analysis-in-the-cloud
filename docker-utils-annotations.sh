#!/usr/bin/env bash
set -o errexit
set -o pipefail

NAME=czbiohub/sc-rna-seq-processing:0.0.2

# to create a new container
docker build ./context_annotations/ --tag $NAME

# push to dockerhub
echo "if ready to push run 'docker push $NAME' "
# docker push $NAME

# run inside the container
echo "previous file will be re-written"
touch $PWD/data/output/output_processed_annotated.h5ad;
docker run \
  --mount type=bind,source=$PWD/data/output/output_processed.h5ad,target=/input \
  --mount type=bind,source=$PWD/data/output/output_processed_annotated.h5ad,target=/output.h5ad \
  --mount type=bind,source=,target=$PWD/data/OnClass_data/data_used_for_training/tabula-muris-senis-facs_cell_ontology.h5ad ,target=data_file.h5ad \
  --mount type=bind,source=,target=$PWD/data/OnClass_data/OnClass_data_others/cell_ontology/cl.ontology ,target= \
  --mount type=bind,source=,target=$PWD/data/OnClass_data/pretrain/tp2emb_500 ,target=pretrain_model_prefix \
  --mount type=bind,source=,target=$PWD/data/OnClass_data/cell_ontology/cl.obo ,target= /cl.obo\
  $NAME
