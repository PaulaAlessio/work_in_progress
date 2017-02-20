from phylogen import * 


filename = "Input_Mainz.txt"
alleles, trees = read_input(filename)

clades = trees[0].find_clades()

acc=["LPS119","LPS150","LPS168","LPS189"]
acc.pop(0)

p_trees = prune_trees(trees,acc)

header = create_header(p_trees)

print(header)

