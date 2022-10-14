import numpy as np
import random 
#from treelib import Node, Tree

def find_unique_ints_in_nested_list(nested_list, out = {}):
    if type(nested_list) == int:
        return {nested_list} 
    else:
        s = {}
        for sub_list in nested_list:
            s.union(find_unique_ints_in_nested_list(sub_list))
        return s 

def delete_empty_lists(genome):
    if type(genome) == list:
        if len(genome) == 0:
            return True
        else:
            for sub_genome in genome:
                empty = delete_empty_lists(sub_genome)
                if empty == True:
                    genome.remove(sub_genome)
            return genome
            


def add_value_to_nested_list(nested_list, value):
    #print("i ", nested_list)
    if type(nested_list) == int:
        #print("D, ", nested_list)
        return nested_list + value
    elif type(nested_list) == float:
        return nested_list
    elif type(nested_list) == list:
        l = []
        for sub_list in nested_list:
            r = add_value_to_nested_list(sub_list, value)
            #print(r)
            l.append(r)
            #print(l)
        return l

def copy_hox_mutation_v1(genome, sub_genome):
    max_node_index = find_max_postive_int_in_nested_list(genome)
    sub_genome_copy = add_value_to_nested_list(sub_genome, max_node_index + 1)
    return sub_genome_copy
     

def transcribe_genome_to_connectivity_matrix(genome):
    
    largest_node_nr = find_max_postive_int_in_nested_list(genome)
    
    connectivity_matrix = np.zeros((largest_node_nr + 1, largest_node_nr + 1))
    #print(connectivity_matrix.shape)
    
    for gene in genome:
        out_node = gene[0]
        in_nodes = gene[1]
        for in_node in in_nodes:
            add_symmetric_connection(connectivity_matrix, 
                                    out_node, in_node)
    return connectivity_matrix
    
def add_symmetric_connection(connectivity_matrix, out_node, in_node):
    connectivity_matrix[[out_node, in_node], [in_node, out_node]] = 1
                        
    return connectivity_matrix

    
def find_max(nested_list):
    maximum = 0
    
    for l in nested_list:
        value = l[0]
        
        if maximum < value:
            maximum = value
        for value in l[1]:
            
            if maximum < value:
                maximum = value
    return maximum
                
def find_max_postive_int_in_nested_list(nested_list, maximum = 0):
    #print(type(nested_list), nested_list)
    if type(nested_list) == list:
        #print(nested_list)
        for sub_list in nested_list:
            sub_maximum = find_max_postive_int_in_nested_list(sub_list, maximum)
            if maximum < sub_maximum:
                maximum = sub_maximum
        return maximum 
    elif type(nested_list) == int:
        #print(nested_list)
        if nested_list > maximum:
            maximum = nested_list
        return maximum
    elif type(nested_list) == float:
        return maximum
    
def find_min_postive_int_in_nested_list(nested_list, minimum = float("inf")):
    if type(nested_list) == list:
        #print(nested_list)
        for sub_list in nested_list:
            sub_min = find_min_postive_int_in_nested_list(sub_list, minimum)
            if sub_min < minimum:
                minimum = sub_min
        return minimum 
    elif type(nested_list) == int:
        #print(nested_list)
        if nested_list < minimum:
            minimum = nested_list
        return minimum
    elif type(nested_list) == float:
        return minimum
    


def add_node_to_connectivity_matrix(connectivity_matrix, n_nodes_to_add):
    n_nodes = connectivity_matrix.shape[0]
    
    new_connectivity_matrix = np.zeros((n_nodes + n_nodes_to_add, n_nodes + n_nodes_to_add))
    new_connectivity_matrix[0:n_nodes,0:nodes] = connectivity_matrix
    
    return new_connectivity_matrix
    

def find_connection_genes(genome):
    if len(genome) == 0:
        del(genome)
        return 
    
    if type(genome[0]) == int and type(genome[1]) == int:
        gene = genome
        return gene
    else:
        genes = []
        for sub_genome in genome:
            gene = find_connection_genes(sub_genome)
            if type(gene[0]) == int and type(gene[1]) == int:
                genes.append(gene)
            else:
                genes.extend(gene)
        return genes

def transcribe_hierarchical_genome(genome):
    
    connection_genes = find_connection_genes(genome)
    max_node_nr = find_max_postive_int_in_nested_list(connection_genes)
    
    connectivity_matrix = np.zeros((max_node_nr + 1, max_node_nr + 1))
    
    for connection_gene in connection_genes:
        out_node = connection_gene[0]
        in_node = connection_gene[1]
        weight = connection_gene[2]
        
        connectivity_matrix[out_node, in_node] = weight
    return connectivity_matrix
    

def recursively_add_nodes(tree, lst, node_ids, parent):
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
            

def draw_tree(lst):
    
    tree = Tree()
    node_ids = [1]
    tree.create_node("",node_ids[-1])
    
    recursively_add_nodes(tree, lst, node_ids, node_ids[-1])

    tree.show()

def find_unique_ints_in_nested_list(nested_list):
    if len(nested_list) == 0:
        del (nested_list)
        return set()
    #print(nested_list)
    #if len(nested_list) < 2:
        #ToDo: Figure out what's wrong here, how come it goes to the empty set?
    #    return set()
    if type(nested_list[0]) == int and type(nested_list[1]) == int:
        nodes = nested_list[:2]
        #print(nodes)
        return set(nodes)
    else:
        nodes = set()
        
        for sub_list in nested_list:
            sub_nodes = find_unique_ints_in_nested_list(sub_list)
            #print(sub_nodes, nodes)
            nodes = nodes.union(sub_nodes)
            #print(nodes)
        return nodes
    
def swap_values_in_nested_list(nested_list, translator):
    if type(nested_list) == int:
        return translator[nested_list]

    elif type(nested_list) == float:
        return nested_list 
        
    elif type(nested_list):
        l = []
        for sub_list in nested_list:
            r = swap_values_in_nested_list(sub_list, translator)
            l.append(r)
        return l

def compress_node_nr_difference(genome):
    maximum = find_max_postive_int_in_nested_list(genome)
    minimum = find_min_postive_int_in_nested_list(genome)
    #print(maximum, minimum)
    
    current_node_values = find_unique_ints_in_nested_list(genome)
    current_node_values = list(current_node_values)
    target_node_values = list(range((maximum - minimum)+1))
    
    translator = {}
    for i, c_node in enumerate(current_node_values):
        
        translator[c_node] = target_node_values[i]
    
    compressed_genome = swap_values_in_nested_list(genome, translator)
    return compressed_genome

def compute_genome_depth(genome):
    if type(genome[0]) == int and type(genome[1]) == int:
        return 1
    
    else:
        depth_list = []
        
        for sub_genome in genome:
            depth = compute_genome_depth(sub_genome)
            depth_list.append(depth)
        return max(depth_list) + 1
    

### Mutations
def mutate_weight(genome, mutation_value):
    if type(genome[0]) == int and type(genome[1]) == int:
        genome[2] += mutation_value
        genome[2] = float(genome[2])
        return genome
    else:
        target_sub_genome = random.choice(genome)
        mutate_weight(target_sub_genome, mutation_value)
    return genome



def add_node(genome, max_node_nr, mutation_probability):
    '''
    This should go through a single random path to the leaf node of the genome
    and then walk back up again with some probability of a mutation happening at each
    backwards step. This is done to make the probability of mutating higher at the lower levels
    than the higher
    
    '''
    if type(genome[0]) == int and type(genome[1]) == int:
        return False
    
    
    target_sub_genome = random.choice(genome)
    mutated = add_node(target_sub_genome, max_node_nr, mutation_probability)
    
    if mutated == False:
        random_variable = np.random.uniform(0,1,1)
        if random_variable < mutation_probability:
            # to do: make bi directional by 50-50 prob
            out_node = random.choice(range(max_node_nr))
            new_node_connection = [out_node, max_node_nr + 1, float(np.random.uniform(-0.1,0.1,1)[0])]
            genome.append(new_node_connection)
            return genome
        else:
            return False
    else:
        return genome
    
def remove_node(genome):
    
    if genome is not None and type(genome[0]) == int and type(genome[1]) == int :
        return True
    
    target_sub_genome = random.choice(genome)
    leaf_node = remove_node(target_sub_genome)
    if leaf_node == True:
        genome.remove(target_sub_genome)
        if len(genome) == 0:
            return True
    return genome

def add_connection(genome, max_node_nr, mutation_probability):
    if type(genome[0]) == int and type(genome[1]) == int:
        return False
    
    
    target_sub_genome = random.choice(genome)
    mutated = add_node(target_sub_genome, max_node_nr, mutation_probability)
    
    if mutated == False:
        random_variable = np.random.uniform(0,1,1)
        if random_variable < mutation_probability:
            # to do: make bi directional by 50-50 prob
            out_node = random.choice(range(max_node_nr))
            in_node = random.choice(range(max_node_nr))
            new_node_connection = [out_node, in_node, float(np.random.uniform(-0.1,0.1,1)[0])]
            genome.append(new_node_connection)
            return genome
        else:
            return False
    else:
        return genome

def mutation_remove_node(genome):
    remove_node(genome)
    return genome

def mutation_add_connection(genome, mutation_probability):
    mutated = False
    max_node_nr = find_max_postive_int_in_nested_list(genome)
    
    while mutated == False:
        mutated = add_connection(genome, max_node_nr, mutation_probability)
    
    return mutated
 
def mutation_add_node(genome, mutation_probability):
    
    mutated = False
    max_node_nr = find_max_postive_int_in_nested_list(genome)
    
    while mutated == False:
        mutated = add_node(genome, max_node_nr, mutation_probability)
    
    return mutated


def mutate_connection(genome, max_node_nr):
    if type(genome[0]) == int and type(genome[1]) == int:
        random_variable = np.random.uniform(0,1,1)
        if random_variable < 0.5:
            # ToDo: should it be max node nr + 1? Otherwise it can't connect to the largest node nr
            genome[0] = random.choice(range(max_node_nr + 1))
        else:
            genome[1] = random.choice(range(max_node_nr + 1))
        return genome
    else:
        target_sub_genome = random.choice(genome)
        mutate_connection(target_sub_genome, max_node_nr)
        
    return genome
        

## HOX
def copy_hox_mutation_v2(genome, sub_genome):
    max_node_index = find_max_postive_int_in_nested_list(genome)
    #print(max_node_index)
    compressed_sub_genome = compress_node_nr_difference(sub_genome)
    #print(compressed_sub_genome)
    sub_genome_copy = add_value_to_nested_list(compressed_sub_genome, max_node_index + 1)
    #print(sub_genome_copy)
    return sub_genome_copy
    
def select_and_copy_sub_genome(genome, sub_genome, mutation_probability):
    #print("Copy ", sub_genome)
    #if len(sub_genome) == 0:
    #    del sub_genome
    #    return False
    if type(sub_genome[0]) == int and type(sub_genome[1]) == int:
        return False
    else:
        target_sub_genome = random.choice(sub_genome)
        mutated = select_and_copy_sub_genome(genome, target_sub_genome, mutation_probability)
    
    #print(mutated)
    if mutated == False:
        random_variable = np.random.uniform(0,1,1)
        if random_variable < mutation_probability:
            sub_genome_copy = copy_hox_mutation_v2(genome, sub_genome)
            return sub_genome_copy
        else:
            return False
    else:
        return mutated

def select_and_move_sub_genome(genome, sub_genome, mutation_probability):
    #print("Move ", sub_genome)
    #if len(sub_genome) == 0:
    #    del (sub_genome)
    #    return False
    if type(sub_genome[0]) == int and type(sub_genome[1]) == int:
        return False
    else:
        index = random.choice(range(len(sub_genome)))
        target_sub_genome = sub_genome[index]
        mutated = select_and_move_sub_genome(genome, target_sub_genome, mutation_probability)
        if len(sub_genome[index]) == 0:
            del sub_genome[index]
    
    #print(mutated)
    if mutated == False:
        random_variable = np.random.uniform(0,1,1)
        if random_variable < mutation_probability:
            #print("Mutation ")
            #print(sub_genome)
            
            sub_sub_genome = random.choice(sub_genome)
            sub_genome.remove(sub_sub_genome)
            if len(sub_genome) == 0:
                del(sub_genome)
                #print("sub_genome deleted")
                   
            
            return sub_sub_genome
        else:
            return False
    else:
        return mutated
    
def insert_sub_genome(genome, sub_genome_copy, insertion_probability):
    #print("insert ", genome)
    if type(genome[0]) == int and type(genome[1]) == int:
        return False
    else:
        target_sub_genome = random.choice(genome)
        mutated = insert_sub_genome(target_sub_genome, sub_genome_copy, insertion_probability)
    
    if mutated == False:
        random_variable = np.random.uniform(0,1,1)
        if random_variable < insertion_probability:
            genome.append(sub_genome_copy)
            return True
        else:
            return False
    return True

def mutation_hox_remove(genome, mutation_probability):
    sub_genome_copy = False
    while sub_genome_copy == False:
        sub_genome_copy = select_and_copy_sub_genome(genome, genome, mutation_probability)
    return genome
    
def mutation_hox_copy(genome, mutation_probability, insertion_probability):
    sub_genome_copy = False
    inserted = False
    
    genome_connection_genes = find_connection_genes(genome)
    
    while sub_genome_copy == False:
        sub_genome_copy = select_and_copy_sub_genome(genome, genome, mutation_probability)
    
    #print(sub_genome_copy)
    while inserted == False:
        inserted = insert_sub_genome(genome, sub_genome_copy, insertion_probability)
        
    sub_genome_copy_connection_genes = find_connection_genes(sub_genome_copy)
    
    c1 = random.choice(genome_connection_genes)
    c2 = random.choice(sub_genome_copy_connection_genes)
    #print("connections ", c1, c2)
    node_1 = random.choice(c1[:2])
    node_2 = random.choice(c2[:2])
    #print("nodes ", node_1, node_2)
    
    new_connection = [node_1, node_2, float(np.random.uniform(-0.1,0.1,1)[0])]
    genome.append(new_connection)
    
    return genome
    
def mutation_hox_shuffle(genome, mutation_probability, insertion_probability):
    sub_genome_copy = False
    inserted = False
    while sub_genome_copy == False:
        sub_genome_copy = select_and_move_sub_genome(genome, genome, mutation_probability)
    
    print(sub_genome_copy)
    while inserted == False:
        inserted = insert_sub_genome(genome, sub_genome_copy, insertion_probability)
    
    return genome


def mutation_hox_group(genome, mutation_probability, insertion_probability):
    
    sub_genome_1 = False
    while sub_genome_1 == False:
        sub_genome_1 = select_and_move_sub_genome(genome, genome, mutation_probability)
    
    sub_genome_2 = sub_genome_1
    
    genome = delete_empty_lists(genome)
    while sub_genome_1 == sub_genome_2:
        sub_genome_2_temp = False
        while sub_genome_2_temp == False:
            sub_genome_2_temp = select_and_move_sub_genome(genome, genome, mutation_probability)
        sub_genome_2 = sub_genome_2_temp
    
        
    grouped_genome = [sub_genome_1, sub_genome_2]
    
    inserted = False
    while inserted == False:
        inserted = insert_sub_genome(genome, grouped_genome, insertion_probability)
        
    return genome
    

##################

def mutate_genome_with_hox(genome):


    #node_biases = genome[1]
    connection_genome = genome
    max_node_nr = find_max_postive_int_in_nested_list(connection_genome)

    random_variable = np.random.uniform(0,1,1)
    
    
    if random_variable < 0.2:
        print("Mutated Weight")
        mutation_value = np.random.normal(-0.1,0.1,1)
        connection_genome = mutate_weight(connection_genome, mutation_value)

    elif random_variable < 0.3:
        random_variable = np.random.uniform(0,1,1)
        if random_variable < 0.5:
            print("Add Node")
            connection_genome = mutation_add_node(connection_genome, 0.5)
         
        else:
            if len(connection_genome) > 2:
                print("Remove Node")
                connection_genome = mutation_remove_node(connection_genome)
    
    elif random_variable < 0.5:
        print("Mutate Connection")
        connection_genome = mutate_connection(connection_genome, max_node_nr)

    elif random_variable < 0.6:
        print("Add connection")
        max_node_nr = find_max_postive_int_in_nested_list(connection_genome)
        connection_genome = mutate_connection(connection_genome, max_node_nr)
    
    elif random_variable < 0.7:
        print(" Hox Shuffle")
        connection_genome = mutation_hox_shuffle(connection_genome, 0.2,0.2)
        
    elif random_variable < 0.8:
        print("Hox group")
        connection_genome = mutation_hox_group(connection_genome, 0.2, 0.2)
    else:
        
        random_variable = np.random.uniform(0,1,1)
        mutation_probability = 0.2
        insertion_probability = 0.2
        if random_variable < 0.5:
            print("Hox copy")
            connection_genome = mutation_hox_copy(connection_genome, mutation_probability, insertion_probability)
        else:
            if len(connection_genome) > 1:
                print("Hox remove")
                connection_genome = mutation_hox_remove(connection_genome, mutation_probability)
        
    connection_genome = compress_node_nr_difference(connection_genome) 

    new_max_node_nr = find_max_postive_int_in_nested_list(connection_genome)
    
    connection_genome= delete_empty_lists(connection_genome)

    
    return connection_genome