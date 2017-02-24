from Bio import Phylo
import copy

def get_clades_pattern(tree,tags):
    """ Gets clades of a tree that contain at least one of the prefixes in tags
     INPUT: 
      - tree: (tree object) tree to be inspected,
      - tags: (list of strings/strings) that contains the prefixes to be found
     OUTPUT: 
      - clades: (list of strings) clades containing the prefixes in tags
    """ 
    clades = [] 
    # Convert tags to a list if it wasn't
    if (not isinstance(tags,list)):
        tags_lst = [tags]
    else:
        tags_lst = tags

    for clade in tree.find_clades():
        if(clade.name):
            for prefix in tags_lst:
                if (clade.name.startswith(prefix)):
                    clades.append(clade.name)
    return(clades)



def prune_one_tree(tree,prune_tags):
    """ Prunes a tree: gets rid of leaves whose prefix is contained in prune_tag
     INPUT: 
      - tree : (tree object) tree to be pruned,
      - prune_tag: (list of strings) contains the accesssions we want to prune.
     OUTPUT: 
      - pruned_tree: (tree objects) pruned trees.
    """
    pruned_tree = copy.deepcopy(tree)
    clades = get_clades_pattern(tree,prune_tags)
    for clade in clades: 
        pruned_tree.prune(name=clade)
    return(pruned_tree) 


def prune_trees(trees,prune_tags):
    """ Prunes a list of trees: gets rid of leaves whose prefix 
     is contained in prune_tags
     INPUT: 
     - trees : (list of tree objects) trees to be pruned,
     - prune_tags: (list of strings) contains the accesssions we want to prune.
     OUTPUT: 
     - pruned tree: (list of tree objects) pruned trees.
    """
    pruned_trees = []
    for tree in trees:
        pruned_trees.append(prune_one_tree(tree,prune_tags))
    return(pruned_trees)


       



