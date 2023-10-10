import random 
import numpy as np
from .helper_functions import find_max_postive_int_in_nested_list, add_value_to_int_in_nested_list, find_connection_genes, delete_empty_lists, compress_node_nr_difference


## HOX Mutations

def copy_hox_mutation_v2(genome, sub_genome):
    max_node_index = find_max_postive_int_in_nested_list(genome)
    #print(max_node_index)
    compressed_sub_genome = compress_node_nr_difference(sub_genome)
    #print(compressed_sub_genome)
    sub_genome_copy = add_value_to_int_in_nested_list(compressed_sub_genome, max_node_index + 1)
    #print(sub_genome_copy)
    return sub_genome_copy

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


def mutation_hox_remove(genome, mutation_probability):
    sub_genome_copy = False
    while sub_genome_copy == False:
        sub_genome_copy = select_and_copy_sub_genome(genome, genome, mutation_probability)
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
    


# HOX mutation Helper functions
############################################################################################################

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
    """
    Walks to a leaf gene and 
    """
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
    """
    insert sub_genome_copy into some random place of the genome
    First walks to some random leaf node, then moves back up the tree and inserts the sub_genome_copy and a random location
    """

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


    

    

