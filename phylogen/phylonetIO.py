from Bio import Phylo
import os

def create_header(ptrees):
    """ Creates the header of a phylonet output
        INPUT: 
         - ptrees : (list of tree objects) pruned trees
        OUTPUT: 
         - header: (string) contains the header of a Phylonet input.
    """
    tmp_file = "tmp.txt"
    header = ""
    header=header+"#NEXUS\n\nBEGIN TREES;\n\n"
    Phylo.write(ptrees,tmp_file,"newick",plain=True)
    ft = open(tmp_file,"r")
    ptree_str = ft.readlines()
    ft.close() 
    os.remove(tmp_file)
    for i in range(len(ptree_str)):
        header= header+"Tree g" +  "{0:07d}".format(i+1) + \
                " =\n"+ptree_str[i]
    header=header+"\nEND;"
    return(header)

def Phylonet_input(ptrees,accession,plevel,tree_repeats): 
   """ Generates Phylonet input
       INPUT: bla bla bla
       NOT FINISHED
       Tree repeats NOT implemented yet 
   """
   tree = ptrees[0]
   clades = get_clades_pattern(tree,accession) 
   permutates = my_permutator_major(clades)
   

