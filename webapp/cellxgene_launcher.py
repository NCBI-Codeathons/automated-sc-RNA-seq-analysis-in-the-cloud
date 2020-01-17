# TODO: This should be a called by a page in flask.

import subprocess
import os

cwd = os.getcwd()
prefix = f'type=bind,source={cwd}/data/'

subprocess.run(
    [
        'docker', 'run',
        '--mount', f'{prefix}adata_small_test.h5ad,target=/input',
        '--mount', f'{prefix}output/output_processed.h5ad,target=/output.h5ad',
        'czbiohub/sc-rna-seq-processing:0.0.2'
    ],
    check=True)

subprocess.run(
    ['cellxgene', 'launch', 'data/output/output_processed.h5ad', '--open']
)
