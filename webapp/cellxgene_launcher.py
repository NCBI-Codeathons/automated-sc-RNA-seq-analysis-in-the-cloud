import subprocess
import os
# e.g., subprocess.call(['df', '-h'])

cwd = os.getcwd()

subprocess.run(['docker', 'run',
                '--mount', f'type=bind,source={cwd}/data/adata_small_test.h5ad,target=/input',
                '--mount', f'type=bind,source={cwd}/data/output/output_processed.h5ad,target=/output.h5ad',
                'czbiohub/sc-rna-seq-processing:0.0.2'],
               check=True)


subprocess.run(
    ['cellxgene', 'launch', 'data/output/output_processed.h5ad', '--open'])
