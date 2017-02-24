### ESCRIBIR ALGO AQUI
from phylogen.utils import * 
from phylogen.combinatorics import * 

def get_MDC_command(indices):
  """ Returns a string with the format 
        Infer_ST_MDC(g000000i1, ... ,g000000in) -a
      INPUT: list of indices in the g's
  """
  tree_ids = get_tree_ids(indices)
  return("Infer_ST_MDC(" + csv_string(tree_ids) + ") -a\n")

def rm_dbl_splitting(all_pairs,splitting):
    """ Treating alelles combinations in the case where 
        there are empty fields (this happens when the number 
        of alelles available is smaller than the ploidity). 
        If splitting is set to True, remove the cases in which 
        there is an ancestor getting two alleles and another 0.
        INPUT:  
           - all_pairs: list of lists of 2-elem list. Output of get_all_pairs
           - splitting: true or false
        all_pairs is being modified. 
        """ 
    # Remove doubles
    for i in range(len(all_pairs)-1,-1,-1):
        if all_pairs[i] in all_pairs[0:i]:
            all_pairs.pop(i)
#    print("Longitud de all_pairs: " +  str(len(all_pairs)))
    # handle empty fields
    for i in range(len(all_pairs) -1, -1, -1):
        empty = False
        pair = False
       # print(all_pairs[i])
        for j in range(len(all_pairs[i])-1,-1,-1):
            if ((all_pairs[i][j][0] == "") and (all_pairs[i][j][1] == "")):
                emtpy = True
                all_pairs[i].pop(j)
            elif all_pairs[i][j][1] is "":
                all_pairs[i][j].pop(1)
            elif all_pairs[i][j][0] is "":
                all_pairs[i][j].pop(0)
            else:
                pair = True
        if (empty and pair and splitting):
            all_pairs.pop(i)


  
def get_allele_comb(lst,accession,ploidy,splitting):
  """ Returns a string of allele combinations suitable for a
      Pylonet input file. 
      INPUT: 
         - lst: (list of strings) list of alelles to be considered.
         - accesssion: (str) name of the accession.
         - ploidy: (int) ploidy level.
         - splitting: (bool) True when Florian Mode, False otherwise.
      OUTPUT: 
         - out_list: list of strings containing allele combinations in  Phylonet format. 
  """
  out_lst =[]
  L = len(lst)
  # Add empty fields
  if ( ploidy > L ):
      comb = get_all_pairs(lst + [""]*(ploidy - L))
      rm_dbl_splitting(comb,splitting)
  elif (ploidy < L):
      raise NameError("Number of different alleles in "+ \
          accession + " exceeds the ploidy." )
  else:
      comb = get_all_pairs(lst)
  for  pairs in comb:
      i = 1
      alleles = []
      for pair in pairs:
          alleles.append(accession + "___" + "{0:02d}".format(i)\
              + ":" + csv_string(pair))
          i = i + 1
      out_lst.append(csv_string(alleles,sep = ";"))
  return out_lst

def get_diploid_list(known,comb):
    dip_str = trim_str(known,-1,"\n")
    dip_str = dip_str + ";" + comb
    return("<" + dip_str + ">;\n")
