from phylogen import * 


filename = "Input_Mainz.txt"
alleles, trees = read_input(filename)

clades = trees[0].find_clades()

acc=["LPS119","LPS150","LPS168","LPS189"]
current=acc.pop(0)

ptrees = prune_trees(trees,acc)


phylo_str = Phylonet_input(ptrees,alleles,current,4,1)

print(phylo_str)

#print(header)





