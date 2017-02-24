from Bio import Phylo
import warnings 
import os

from phylogen.Accession import * 
from phylogen.phylonet_utils import * 

class IPhylonet: 
   """ This class contains all the necessary information to 
       create a phylonet input. 
       ATRIBUTES: 
        - header: (string) contains the header of a Phylonet input.
   """
   def __init__(self, accession, known_alleles, trees_per_locus, splitting):
     self.trees_per_locus = trees_per_locus
     self.splitting = splitting
     self.header = self.__header__(accession)
     self.known_alleles = known_alleles
     self.MDC = self.__MDC__(accession)
     self.alleles_comb = self.__alleles_comb__(accession)

   def __header__(self, accession): 
     """ Creates the header of a phylonet input (self.header)
         INPUT: 
          - ptrees : (list of tree objects) pruned trees
     """
     tmp_file = "tmp.txt"
     header = ""
     header = header + "#NEXUS\n\nBEGIN TREES;\n\n"
     Phylo.write( accession.ptrees, tmp_file, "newick", plain = True)
     ft = open( tmp_file, "r")
     ptrees_str = ft.readlines()
     ft.close()  
     os.remove(tmp_file)
     for i in range(len(ptrees_str)):
         header = header + "Tree g" +  "{0:07d}".format( i + 1) + \
                 " =\n"+ptrees_str[i]
     header = header+"\nEND;"
     return header
 
   def __alleles_comb__(self, accession):
       Nt = len(accession.ptrees)
       alleles_comb = []
       # We could make an 
       for i in range(0, Nt, self.trees_per_locus):
            one_comb = get_allele_comb( accession.clades[i],accession.name, 
                           accession.ploidy, self.splitting)
            alleles_comb.append(one_comb)
       return alleles_comb

   def __MDC__(self,accession):
       Nt = len(accession.ptrees)
       MDC = []
       for i in range(1,Nt+1,self.trees_per_locus):
           indices = list(range(i,i + self.trees_per_locus)) 
           MDC.append(get_MDC_command(indices))
       return MDC

   def gen_input(self):
       """ Generates Phylonet input """
       phylo_str = self.header
       phylo_str = phylo_str + "\n\n\n\nBEGIN PhyloNet;\n\n"
       Ne = len(self.alleles_comb)
       for i in range(Ne):
         for comb in self.alleles_comb[i]:
             phylo_str = phylo_str + self.MDC[i]
             phylo_str = phylo_str + get_diploid_list(self.known_alleles,
                         comb)
       phylo_str = phylo_str + "\n\nEND;"
       return phylo_str

   def write_input(self,phylonet_input):
      f = open(phylonet_input,"w")
      f.write(self.gen_input())
      f.close()

