import numpy as np
from .simple_mutation_operations import mutate_weight, mutate_connection, mutation_add_node, mutation_remove_node
from .hierarchical_genome_mutations_operations import mutation_hox_copy, mutation_hox_remove, mutation_hox_shuffle, mutation_hox_group
from .helper_functions import find_max_postive_int_in_nested_list, delete_empty_lists, compress_node_nr_difference
##################

def mutate_genome_with_hox(genome):
    """
    Mutates a genome in the form of a nested list where the leaf nodes are tuples representing 
    connectiosn between nodes and the weight between them.
    """

    # Find the largest node number in the genome
    max_node_nr = find_max_postive_int_in_nested_list(genome)

    # Generate a random variable to decide which mutation to perform
    random_variable = np.random.uniform(0,1,1)
    
    # Mutate the genome
    # Different mutation probabilities can be set here
    if random_variable < 0.2:
        # Simple mutation of weight between two nodes
        print("Mutated Weight")
        mutation = "Weigth"

        # Generate a random value to add to the weight
        mutation_value = np.random.normal(-0.1,0.1,1)
        
        # Mutate the genome
        genome = mutate_weight(genome, mutation_value)

    elif random_variable < 0.3:
        # Add or remove a node
        # To balance the probability of adding and removing a node, a random variable is generated
        # and if it is less than 0.5, a node is added, otherwise a node is removed
        random_variable = np.random.uniform(0,1,1)
        if random_variable < 0.5:
            print("Add Node")
            mutation = "Add Node"
            genome = mutation_add_node(genome, 0.5)

         
        else:
            if len(genome) > 2:
                print("Remove Node")
                mutation = "Remove Node"
                genome = mutation_remove_node(genome)
    
    elif random_variable < 0.5:
        # Mutate a connection between two nodes
        # i.e change which two nodes are connected
        print("Mutate Connection")
        mutation = "Change Connection"
        genome = mutate_connection(genome, max_node_nr)

    elif random_variable < 0.6:
        # Adds a connection between two nodes
        print("Add connection")
        mutation = "Add Connection"
        max_node_nr = find_max_postive_int_in_nested_list(genome)
        genome = mutate_connection(genome, max_node_nr)
    
    elif random_variable < 0.7:
        # Performs a HOX shuffle mutation
        # i.e shuffles the nested lists around the genome
        # Note: this does not change the structure of the graph the genome produces
        print(" Hox Shuffle")
        mutation = "Hox Shuffle"
        genome = mutation_hox_shuffle(genome, 0.2,0.2)
        
    elif random_variable < 0.8:
        # Performs a HOX group mutation
        # i.e groups parts of the genome together
        print("Hox group")
        mutation = "Hox Group"
        genome = mutation_hox_group(genome, 0.2, 0.2)
    else:
        # Performs a HOX copy or remove mutation
        # i.e copies or removes a sub part of the nested lists.
        # To balance the probability of copying and removing a node, a random variable is generated
        # and if it is less than 0.5,the copy mutation happens, otherwise the remove mutation happens
        
        # Random variable to decide which mutation to perform
        random_variable = np.random.uniform(0,1,1)

        # Mutation probabilities for the copy and remove mutations
        # changes the probability of which level the sub genome is copied or removed from
        mutation_probability = 0.2
        insertion_probability = 0.2
        if random_variable < 0.5:
            print("Hox copy")
            mutation = "Hox Copy"
            genome = mutation_hox_copy(genome, mutation_probability, insertion_probability)
        else:
            if len(genome) > 1:
                print("Hox remove")
                mutation = "Hox Remove"
                genome = mutation_hox_remove(genome, mutation_probability)
            else:
                print("Empty Genome")
                mutation = "Empty Genome"
        
    # Compress the node numbers in the genome
    # This is done such that the node numbers are consecutive integers
    # and such that the corresponding weight matrix doesn't become too large
    genome = compress_node_nr_difference(genome) 

    
    
    genome= delete_empty_lists(genome)

    
    return genome, mutation