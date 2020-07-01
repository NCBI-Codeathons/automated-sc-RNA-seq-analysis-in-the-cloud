import subprocess
import os
# e.g., subprocess.call(['df', '-h'])

cwd = os.getcwd()
prefix = f'type=bind,source={cwd}/data/'


#subprocess.run(['/Users/angela.pisco/src/Using-Tabula-Muris-Senis-as-reference-for-a-semi-automated-sc-RNA-seq-analysis-workflow-in-the-cloud/docker-utils-annotations.sh'], check=True)

subprocess.run(
     [
         'docker', 'run',
         '--mount', f'{prefix}output/output_processed.h5ad,target=/input.h5ad',
         '--mount', f'{prefix}output/output_processed_annotated.h5ad,target=/output.h5ad',
         '--mount', f'{prefix}OnClass_data/data_used_for_training/tabula-muris-senis-facs_cell_ontology.h5ad,target=/data_file.h5ad',
         '--mount', f'{prefix}OnClass_data/OnClass_data_others/cell_ontology/cl.ontology,target=/cell_type_network_file.ontology',
         '--mount', f'{prefix}OnClass_data/cell_ontology/cl.obo,target=/cl.obo',
         '--mount', f'{prefix}OnClass_data/pretrain/,target=/pretrain',
         'czbiohub/sc-rna-seq-annotating:0.0.1'
     ],
     check = True)


subprocess.run(['cellxgene','launch', 'data/output/output_processed_annotated.h5ad', '--open', '--experimental-annotations'])
