import copy, itertools

# Chunk a list into pairs in all possible ways.
# Input: list
# Output: list of lists with the possible pairs (ordered in 
# every list) without repetition
def permutator_major(lst):
    result =[]
    L = len(lst)
    if (L%2) :
      raise NameError("Number of elements is odd. Aborting.")
    if len(lst) < 2:
        return [lst]
    a = lst[0]
    for i in range(1,L):
        pair = [a,lst[i]]
        rest = my_permutator_major(lst[1:i]+lst[i+1:])
        for res in rest: 
            result.append( pair + res )
    # Remove possible doubles 
    for i in range(len(result)-1,-1,-1):
        if result[i] in result[0:i]:
           result.pop(i) 
    return result 




# Join n lists of strings in all possible ways. 
# Input: list of lists of strings with the same number of elements. 
# Ouput: list  of lists with all possible concatenations.
def permutator_minor(lst):
    N = len(lst)
    first=lst[0]
    L = len(first)
    P = L
    for l in range(1,L):
       P = l * P
    Nt = P**(N-1)
    result = [ first ]*Nt
    i = 1
    for element in lst[1:]:
        perm = itertools.permutations(element)
        pe = 0
        for p in perm: 
           for j in range(int(Nt/P)):
                   index =  i*pe + j%i + int(j/i) *P*i
                   result[index] =\
                     [a + b for a, b in zip(result[index], p)]
           pe = pe + 1
        i = i * P
    return(result)




################################################################
####################### MARKUS FUNCTIONS  ######################
################################################################


# Permutation function for deductive search, outer part
def permutator_minimus(trees,ploidy):
    back_list=[]
    for i_tree in range(0,int(ploidy/2)):
        back_list.append([i_tree])
    for i_trees in range(1, trees):
        internal_list=[]
        work_list=copy.deepcopy(back_list)
        for i_allele in range(0,int(ploidy/2)):
            for i_work in range(0,len(work_list)):
                internal_list.append(work_list[i_work]+[i_allele])
        back_list=internal_list
    return (back_list)

# Permutation function for deductive search, inner part
def permutator_maximus(inlist):
    ploidy_count=len(inlist[0])*2
    tree_count=len(inlist)
    pop_map=permutator_minimus(tree_count, ploidy_count)
##    print(pop_map)
    final_list=[]
    for diploid_map in range (0,len(pop_map)):
        work_copy=copy.deepcopy(inlist)
        temp_list=[]
        for diploid in range (0,len(pop_map[diploid_map])):
            temp_list.append(work_copy[diploid].pop(pop_map[diploid_map][diploid]))
##        print(temp_list)
        final_list.append([work_copy, temp_list])
    if len(final_list[0][0][0])is 1:
        print("   Deduction to diploid successfull.")
        final_list=final_list[0:int((len(final_list)/2))]
##        print ("List length:", len(final_list),"\nFinal List:\n",final_list)
    return (final_list)
