from phylogen import * 

# Variables (we still have to implement the input file and so on..)
filename = "Input_Mainz.txt"
prune_tags=["LPS150","LPS168","LPS189"]
accession = "LPS119"
ploidy = 4
splitting = True
trees_per_locus = 1

# Opens inputfile and reads it
data = Input(filename)

# Generate an instance of Accession for LPS119 (see attributes in Accession.py) 
LPS119 = Accession(accession, ploidy, data.trees, prune_tags)

# Instance of IPhylonet. Contains necessary into to generate a Phylonet input
Phylo_LPS119 = IPhylonet(LPS119,data.known_alleles,trees_per_locus,splitting)

# Write phylonet input
Phylo_LPS119.write_input("LPS119_1.nex")

