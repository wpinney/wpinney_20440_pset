README
###########################################################################
OVERVIEW:
This repository provides data and code to run an example comparison of
Single Cell RNA Sequencing on Mouse Thymic Epithelial Cells.

The output figure plots the number of transcripts per gene of five mouse
Thymic Epithelial Cells.

DATA :
DATA SOURCE:
The source for all data in this repository is:

Sansom SN, Shikama-Dorn N, Zhanybekova S, Nusspaumer G et al. Population
and single-cell genomics reveal the Aire dependency, relief from 
Polycomb silencing, and distribution of self-antigen expression in thymic 
epithelia. Genome Res 2014 Dec;24(12:1918-31.) PMID: 25224068

Data was retrieved from the NCBI Gene Expression Omnibus (GEO) Database:

Edgar R, Domrachev M, Lash AE.Gene Expression Omnibus: NCBI gene
expression and hybridization array data repositoryNucleic Acids Res. 2002
Jan 1;30(1):207-10 

The study in question has accession number: GSE60297
In particular, this repository contains five files from this data set, the
GEO/SRA accessionnumbers for these files is as follows:

(1) GSM1470411 / SRX674336

(2) GSM1470412 / SRX674337

(3) GSM1470413 / SRX674338

(4) GSM1470414 / SRX674339

(5) GSM1470415 / SRX674340

Data was downloaded in .fastq format from the 
NCBI Sequence Read Archive (SRA)
https://trace.ncbi.nlm.nih.gov/Traces/sra/sra.cgi?view=software 
Sequence Read Archive Team

DATA PREPROCESSING:
Raw files were manually edited to remove two ‘/n’ empty lines at the end
of each fastq file

DATA PROCESSING:
Data was processed using the RNA Detector Software:

La Ferlita A, Alaimo S, Di Bella S, Martorana E, Laliotis GI, Bertoni F
Cascione L, Tsichlis PN, Ferro A, Bosotti R, Pulvirenti A. 
RNAdetector: a free user-friendly stand-alone and cloud-based
system for RNA-Seq data analysis. BMC Bioinformatics. 2021 Jun 3;22(1
:298. doi: 10.1186/s12859-021-04211-7.

RNA Detector requires Docker to work: https://www.docker.com/

Assembly of RNA Sequence reads, and counting of transcript number was done
according to standard methods in the RNA Dectector software using the 
mouse mm10 reference sequencep resent in this package.

FOLDER STRUCTURE

assembled_raw_data: 
Contains .txt files output from the assembly of sequencing data by RNA
Detector, files are named according to the SRA accession number for the
raw data.

scripts:
Contains the example_figure.py script used to generate an example figure 
based on this RNA Seq Data. The output, js a scatter plot showing expression 
levels of each gene in the analysis from the five single cell data sets 
included as data.

figures:
Contains a .png containing the figure output from example_figures.py

INSTALLATION:
This code was tested with the following software packages and version:
RNA DETECTOR v 0.0.4

RNA DETECTOR CONTAINER v 0.0.3

DOCKER DESKTOP 4.5.0

matplotlib==3.5.0

numpy==1.20.3

seaborn==0.11.2

pandas==1.4.1

