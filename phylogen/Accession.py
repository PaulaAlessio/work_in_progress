from Bio import Phylo
from phylogen.tree_manip import * 

""" En esta funcion codificamos una accession
    Como input necesitamos, por ejemplo
      - Nombre:  "LPS119"
      - ploidy: 4
      - trees: arboles para analizar (obtenidos a partir de la clase Input)
      - prune_tags: Lista de los nombres de los otros accessions que vamos a podar
           ["LPS150","LPS168","LPS189"]
"""
class Accession: 
    def  __init__(self, accession, ploidy, trees, prune_tags):
        self.name = accession
        self.ploidy = ploidy
        self.trees = trees
        self.ptrees = self.__get_pruned_trees__(prune_tags)
        self.clades = self.__get_clades__()

    def __get_pruned_trees__(self, prune_tags):
        return prune_trees(self.trees, prune_tags)

    def __get_clades__(self):
        """ En esta funcion estamos obteniendo los 
            alelos que luego vamos a recombinar y 
            que acabaran en el Phylonet input.
            Escribes esto un poco m'as seriamente?
        """
        clades = []
        for ptree in self.ptrees:
            clades.append(get_clades_pattern(ptree,self.name))
        return clades

