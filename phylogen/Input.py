from Bio import Phylo

class Input: 
    def __init__(self,filename):
        self.filename = filename
        self.known_alleles, self.trees = self.__read_input__()

    def __read_input__(self):
       """ Reads the input.
        INPUT: filename (str): name of the file we want to read in. 
               it contains N trees and a last line with a list 
               of species and alelles. 
        OUTPUT: a list with two elements 
           - alleles: string containing the last line of the input file
           - trees: list of tree objects (Phylo.parse) corresponding 
                    to the trees contained in the inputfile.
       """
       # Open the file
       f = open(self.filename,"r")
       # Read file linewise
       tree_str = f.readlines()
       f.close()
       known_alleles = tree_str.pop()
       trees = list(Phylo.parse(tree_str,"newick"))
       return known_alleles, trees

