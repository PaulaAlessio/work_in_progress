import copy, itertools
# FUNCTIONS!!!! 
def get_all_pairs(lst):
    """ Get pairs of elements in the 
        list in all possible ways. 
        INPUT: list of N elements 
        OUTPUT: list of list of lists containing the pairs
        Example: lst [0,1,2,3]
            res  = [ [[0,1], [2,3]],
                     [[0,2], [1,3]],
                     [[0,3], [1,2]]
        """
          
    result =[]
    L = len(lst)
    if (L%2) :
      raise NameError("Number of elements is odd. Aborting.")
    if  L  < 2:
        return [lst] 
    a = lst[0]
    for i in range(1,L):
        pair = [a,lst[i]]
        rest = get_all_pairs(lst[1:i]+lst[i+1:])
        for res in rest:
            result.append(copy.deepcopy([pair] + res))
    return result 

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


def csv_string(str_list,**kwargs):
    """ Obtains a csv string from a list of strings
        INPUT: 
         - str_list: (list of strings) input fields
         - **kwargs: optional:
            -- sep: (char) separator. , as default
            -- elem: (list) elements to be taken from str_list. all as default
    """
    sep = kwargs.get('sep', ',')
    elem = kwargs.get('elem',range(len(str_list)))
    csv_str = ""
    for i in elem: 
        csv_str = csv_str + str_list[i] + sep
    return (csv_str[:-1])
        



def get_allele_combinations(lst,accession,ploidity,splitting):
    """ Returns a string of allele combinations suitable for a
        Pylonet input file. 
        INPUT: 
           - lst: (list of strings) list of alelles to be considered.
           - accesssion: (str) name of the accession.
           - ploidity: (int) ploidy level.
           - splitting: (bool) True when Florian Mode, False otherwise.
        OUTPUT: 
           - out_list: list of strings containing allele combinations in  Phylonet format. 
    """
    out_lst =[]
    L = len(lst)
    # Add empty fields
    if ( ploidity > L ):
        comb = get_all_pairs(lst + [""]*(ploidity - L))
        rm_dbl_splitting(comb,splitting)
    elif (ploidity < L):
        raise NameError("Number of different alleles in "+ \
            accession + " exceeds the ploidity." )
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

###############################################################################
# Here, the code. You can add new entries and check them! I can maybe prepare a 
# unit test! 


acc = "LPS119"



a = ["LPS119_7_B20_1","LPS119_7_B20_2","LPS119_7_B20_3","LPS119_7_B20_4"]
print("-  List of alleles: ")
print(a)
ploidy_level = 4
splitting = True
print("-  Ploidy level = "+str(ploidy_level) + "\n-  Splitting = ",str(splitting))
lst = get_allele_combinations(a,acc,ploidy_level,splitting)
for comb in lst: 
    print(comb)


print("\n-------------------------------")
a = ["LPS119_7_B12_1","LPS119_7_B12_2"]
print("-  List of alleles: ")
print(a)
ploidy_level = 4
splitting = True
print("-  Ploidy level = "+str(ploidy_level) + "\n-  Splitting = ",str(splitting))
lst = get_allele_combinations(a,acc,ploidy_level,splitting)
for comb in lst: 
    print(comb)

print("\n-------------------------------")
a = ["LPS119_7_B12_1","LPS119_7_B12_2"]
print("-  List of alleles: ")
print(a)
ploidy_level = 4
splitting = False
print("-  Ploidy level = "+str(ploidy_level) + "\n-  Splitting = ",str(splitting))
lst = get_allele_combinations(a,acc,ploidy_level,splitting)
for comb in lst: 
    print(comb)

print("\n-------------------------------")
a = ["LPS119_7_B12_1","LPS119_7_B12_2"]
print("-  List of alleles: ")
print(a)
ploidy_level = 6
splitting = True
print("-  Ploidy level = "+str(ploidy_level) + "\n-  Splitting = ",str(splitting))
lst = get_allele_combinations(a,acc,ploidy_level,splitting)
for comb in lst: 
    print(comb)

print("\n-------------------------------")
a = ["LPS119_7_B12_1","LPS119_7_B12_2"]
print("-  List of alleles: ")
print(a)
ploidy_level = 6
splitting = False
print("-  Ploidy level = "+str(ploidy_level) + "\n-  Splitting = ",str(splitting))
lst = get_allele_combinations(a,acc,ploidy_level,splitting)
for comb in lst: 
    print(comb)

print("\n-------------------------------")
a = ["LPS119_7_B12_1","LPS119_7_B12_2","LPS119_7_B12_3"]
print("-  List of alleles: ")
print(a)
ploidy_level = 6
splitting = True
print("-  Ploidy level = "+str(ploidy_level) + "\n-  Splitting = ",str(splitting))
lst = get_allele_combinations(a,acc,ploidy_level,splitting)
for comb in lst: 
    print(comb)
#

#
print("\n-------------------------------")
a = ["LPS119_7_B12_1","LPS119_7_B12_2","LPS119_7_B12_3"]
print("-  List of alleles: ")
print(a)
ploidy_level = 6
splitting = False
print("-  Ploidy level = "+str(ploidy_level) + "\n-  Splitting = ",str(splitting))
lst = get_allele_combinations(a,acc,ploidy_level,splitting)
for comb in lst: 
    print(comb)
#
