import numpy as np
from .helper_functions import find_max_postive_int_in_nested_list, find_connection_genes



def transcribe_hierarchical_genome_to_weight_matrix(genome):
    """
    Transcribes the genome to a weight matrix.
    """
    
    # Finds all connection genes in the genome
    # i.e all genes that connect two nodes and the weight between them
    connection_genes = find_connection_genes(genome)

    # Finds the largest node number to determine size of weight matrix
    max_node_nr = find_max_postive_int_in_nested_list(connection_genes)
    
    # Initialize weight matrix
    weight_matrix = np.zeros((max_node_nr + 1, max_node_nr + 1))
    
    # Add the weights to the weight matrix
    for connection_gene in connection_genes:

        out_node = connection_gene[0]
        in_node = connection_gene[1]
        weight = connection_gene[2]
        
        weight_matrix[out_node, in_node] = weight


    return weight_matrix


