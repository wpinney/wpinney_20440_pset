import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os

def example_plotter(data_sets, num_file):
    '''This function is not particularly generalizable
    and is has been designed around a specific data set
    data_sets: a list of pandas dataframes loaded from
    RNA_seq experiments, must contain a "counts" column
    of how many transcripts were present, a "gene number"
    column mapping each gene to a single number 
    1...number of total genes, each frame must have the 
    same number of genes analyzed.
    num_file: number of dataframes to plot

    Returns: plotted data
    '''
    color_list = sns.color_palette("rocket") #color scheme

    for i,c in zip(range(num_files),color_list):
        #generating scatter plot
        ax = sns.scatterplot(data=transcript_counts[i], x='gene_order',
        y='counts',color=c,alpha=0.5,marker='.',
        edgecolor=c,label="mTec ID {}".format(i+36))

        #axis settings for 
        ax.set_xlabel("Gene")
        ax.set_ylabel("Transcript Count Number")
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.set_xlim(left = 0, right = num_genes)
        ax.set_ylim(bottom = 0)
        ax.set_xticks([],minor = False)
        ax.set_yticks([10000,20000,30000])
        ax.set_yticklabels(['10k','20k','30k'])
        ax.set_title('Example mTEC scRNASeq Data')
        ax.legend(loc ='upper right', bbox_to_anchor=(1.04,1)) 
    path_p = os.path.realpath(os.path.join(os.path.dirname(__file__), '..',
        'figures','example_plot.png'))
    plt.savefig(path_p, dpi=300)
    plt.show() 



num_files = 5 #number of files to analyze
loaded_data = [0]*num_files #empty list for data to be added

#extracting all data from each rna_seq file
for i in range(num_files):  
    #creates data frame from each rna_seq file
    path_i = os.path.realpath(os.path.join(os.path.dirname(__file__), '..',
        'processed_raw_data', 'transcripts_srx6743{}-1.txt'.format(36+i)))
    loaded_data[i] = pd.read_csv(path_i,sep='\t')


#Once RNAseq data has been loaded, wish to extract only
#the most important information
transcript_counts = [0]*num_files 
num_genes = len(loaded_data[0]["counts"]) 
gene_order = np.linspace(1,num_genes,num_genes)

#This iterates through the loaded data and defines new
#pandas DataFrames with only the most important info
for i in range(num_files):
    if len(loaded_data[i]["counts"]) == num_genes:
        #check to make sure each analysis contains correct
        #number of genes
        transcript_counts[i] = \
            pd.DataFrame({"mapped_id":loaded_data[i]["mapped_id"], 
            "counts":loaded_data[i]["counts"],
            "gene_order":gene_order,
            "Transcript ID": 36*i})
    else:
        #if gene numbers are inconsistent
        raise("Value Error: Gene Number Conflict")

#Creating example plot for a small number of mTec datasets
example_plotter(loaded_data,num_files)

########################################################################