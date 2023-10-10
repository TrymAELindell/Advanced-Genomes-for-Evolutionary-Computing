def compute_genome_depth(genome):
    """
    Find the longest path from the root node to a leaf node in a genome.
    """

    if type(genome[0]) == int and type(genome[1]) == int:
        return 1
    
    else:
        depth_list = []
        
        for sub_genome in genome:
            depth = compute_genome_depth(sub_genome)
            depth_list.append(depth)
        return max(depth_list) + 1