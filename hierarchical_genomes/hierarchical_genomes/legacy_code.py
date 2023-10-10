

def add_node_to_connectivity_matrix(connectivity_matrix, n_nodes_to_add):
    n_nodes = connectivity_matrix.shape[0]
    
    new_connectivity_matrix = np.zeros((n_nodes + n_nodes_to_add, n_nodes + n_nodes_to_add))
    new_connectivity_matrix[0:n_nodes,0:nodes] = connectivity_matrix
    
    return new_connectivity_matrix




def transcribe_genome_to_connectivity_matrix(genome):
    """
    Transcribes a genome to a connectivity matrix.
    Note: does not translate weight values, only which node is connected to which node
    """

    # Finds largest node number to determine size of connectivity matrix
    largest_node_nr = find_max_postive_int_in_nested_list(genome)
    
    # Initialize connectivity matrix
    connectivity_matrix = np.zeros((largest_node_nr + 1, largest_node_nr + 1))
    
    
    for gene in genome:
        out_node = gene[0]
        in_nodes = gene[1]
        for in_node in in_nodes:
            add_symmetric_connection(connectivity_matrix, 
                                    out_node, in_node)
    return connectivity_matrix


def find_max(nested_list):
    """
    Finds maximum value in a nested list.
    ToDo: make this separate functions for floats and ints
    """
    maximum = 0
    
    for l in nested_list:
        value = l[0]
        
        if maximum < value:
            maximum = value
        for value in l[1]:
            
            if maximum < value:
                maximum = value
    return maximum


def draw_tree(lst):
    
    tree = Tree()
    node_ids = [1]
    tree.create_node("",node_ids[-1])
    
    recursively_add_nodes(tree, lst, node_ids, node_ids[-1])

    tree.show()

def recursively_add_nodes(tree, lst, node_ids, parent):
    """
    
    """
    if type(lst[0]) == int and type(lst[1]) == int:
        node_id = node_ids[-1] + 1
        node_ids.append(node_id)
        tree.create_node(str(lst), node_id, parent = parent)
        
    else:
        for sub_list in lst:
            node_id = node_ids[-1] + 1
            node_ids.append(node_id)
            tree.create_node("o",node_id, parent = parent)
            recursively_add_nodes(tree, sub_list, node_ids, node_id)
            


def copy_hox_mutation_v1(genome, sub_genome):
    max_node_index = find_max_postive_int_in_nested_list(genome)
    sub_genome_copy = add_value_to_int_in_nested_list(sub_genome, max_node_index + 1)
    return sub_genome_copy