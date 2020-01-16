# Automated scRNA-seq Analysis in the Cloud 

The goal of this project is to build a semi-automated sc-RNA-seq analysis workflow in the cloud. *Tabula Muris Senis* will be used as the reference database for the annotations.

## What is Tabula Muris Senis?

Per the the Chan Zuckerberg Biohub website, “Tabula Muris is a compendium of single cell transcriptome data from the model organism Mus musculus, containing nearly 100,000 cells from 20 organs and tissues. The data allow for direct and controlled comparison of gene expression in cell types shared between tissues, such as immune cells from distinct anatomical locations.” More information on Tabula Muris Senis can be found [here](https://tabula-muris.ds.czbiohub.org).

## Visual:

![TMS2](TMS2.pdf)

## Workflow:

1. **Input gene counts and metadata .h5ad**  
    1. Preprocessing  
2. **Process data using Scanpy**  
    1. Minimum number of reads  
    2. Minimum number of genes  
    3. Minimum number of cells  
3. **Visualization**  
      1. Utilizing CZ Biohub cellxgene tool - <https://tabula-muris-senis.ds.czbiohub.org/all/scVI-UMAP/>  
4. **Annotations**  
     1. Label Propagation  
    2. SCVI & OnClass

  
  ## Where is the data?
  - **Tabula Muris**
    - [site](https://tabula-muris.ds.czbiohub.org/)
    - [github](https://github.com/czbiohub/tabula-muris)
    - [data (figshare)](https://figshare.com/projects/Tabula_Muris_Transcriptomic_characterization_of_20_organs_and_tissues_from_Mus_musculus_at_single_cell_resolution/27733)
    - [Single-cell transcriptomics of 20 mouse organs creates a *Tabula Muris* (Nature)](https://www.nature.com/articles/s41586-018-0590-4)
  - **Tabula Muris Senis**
    - [site](https://tabula-muris-senis.ds.czbiohub.org/)
    - [github](https://github.com/czbiohub/tabula-muris-senis)
    - [raw data (s3)](https://s3.console.aws.amazon.com/s3/buckets/czb-tabula-muris-senis/)
    - [processed data (figshare)](https://figshare.com/projects/Tabula_Muris_Senis/64982)
    - [A Single Cell Transcriptomic Atlas Characterizes Aging Tissues in the Mouse (BioRxiv)](https://www.biorxiv.org/content/10.1101/661728v2)

