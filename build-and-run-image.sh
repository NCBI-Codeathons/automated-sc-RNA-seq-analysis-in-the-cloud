#!/usr/bin/env bash
set -o errexit
set -o pipefail

NAME=czbiohub/sc-rna-seq-processing:0.0.2

# to create a new container
docker build ./context/ --tag $NAME

# push to dockerhub
echo "if ready to push run 'docker push $NAME' "
# docker push $NAME

# run inside the container
docker run \
    --mount type=bind,source=$PWD/data/adata_small_test.h5ad,target=/input \
    --mount type=bind,source=$PWD/data/output/adata_small_test_processed.h5ad,target=/output.h5ad \
    $NAME
