from Bio import Phylo
import warnings
from phylogen.tree_manip import *  
from phylogen.perm import *  
from phylogen.utils import *  
import os

def read_input(filename):
   """ Reads the input.
    INPUT: filename (str): name of the file we want to read in. 
           it contains N trees and a last line with a list 
           of species and alelles. 
    OUTPUT: a list with two elements 
       - alleles: string containing the last line of the input file
       - trees: list of tree objects (generated with Phyloparse) corresponding 
                to the trees contained in the inputfile.
   """
   # Open the file
   f = open(filename,"r")
   # Read file linewise
   tree_str = f.readlines()
   f.close()
   alleles = tree_str.pop()
   trees = list(Phylo.parse(tree_str,"newick"))
   return alleles,trees


def create_header(ptrees):
    """ Creates the header of a phylonet output
        INPUT: 
         - ptrees : (list of tree objects) pruned trees
        OUTPUT: 
         - header: (string) contains the header of a Phylonet input.
    """
    tmp_file = "tmp.txt"
    header = ""
    header = header + "#NEXUS\n\nBEGIN TREES;\n\n"
    Phylo.write(ptrees,tmp_file,"newick",plain=True)
    ft = open(tmp_file,"r")
    ptree_str = ft.readlines()
    ft.close() 
    os.remove(tmp_file)
    for i in range(len(ptree_str)):
        header = header+"Tree g" +  "{0:07d}".format(i+1) + \
                " =\n"+ptree_str[i]
    header = header+"\nEND;"
    return(header)

def Phylonet_input(ptrees,alleles,accession,plevel,tree_repeats): 
   """ Generates Phylonet input
       INPUT: bla bla bla
       NOT FINISHED
       Tree repeats NOT implemented yet 
       Florian mode, etc NOT implemented yet 
   """
   ret_str = create_header(ptrees)
   ret_str = ret_str + "\n\n\n\nBEGIN PhyloNet;\n\n"
   for i  in range(0,len(ptrees),tree_repeats):
       tree = ptrees[i]
       MDC_command = get_MDC_command(range(i+1,i+1+tree_repeats))
       # Obtaining alleles of accession
       clades = get_clades_pattern(tree,accession) 
       # Check the number of alleles vs the ploidity
       if (len(clades) <= plevel):   
           clades.extend(["empty"]*(plevel -len(clades)))
       else:
           raise NameError("Number of different alleles in "+ \
              accession + " exceeds the ploidity." )
       #print(clades)
       permutates = permutator_major(clades)
   #    print(MDC_command)
   #    print(str(len(permutates))+":" + csv_string(clades))
       for perm in permutates:
           dip_list = get_diploid_list(accession,alleles,perm)
           if(dip_list is not ""):
               ret_str = ret_str + MDC_command + dip_list
   ret_str = ret_str + "\n\nEND;"
   return(ret_str)



def get_MDC_command(indices):
  """ Returns a string with the format 
        Infer_ST_MDC(g000000i1, ... ,g000000in) -a
      INPUT: list of indices in the g's
  """
  tree_ids = get_tree_ids(indices)
  return("Infer_ST_MDC(" + csv_string(tree_ids) + ") -a\n")

def get_diploid_list(accession,alleles,perm):
   i = 0 
   d_i = 1
   dip_list = [trim_str(alleles,-1,"\n")]
   while ( i < len(perm) ):
       alleles = accession + "___" + "{0:02d}".format(d_i)\
               + ":" +  csv_string(perm[i:i+2])
       alleles = check_empty(alleles)
       dip_list.append(alleles)
       d_i = d_i + 1
       i = i + 2
   
   dip_list = [x for x in dip_list if x is not ""]
   if (len(dip_list)>1):
       dip_str = csv_string(dip_list,sep=";")
       return("<"+dip_str+">;\n")
   else:
       return("")



def check_empty(alleles):
   """Remove empty if appearing once
   and the whole string if appearing twice"""
   count = alleles.count("empty")
   if count > 1: 
       return ""
   elif count == 0: 
       return alleles
   else: 
       alleles = alleles.replace("empty,","")
       alleles = alleles.replace(",empty","")
   return alleles   
