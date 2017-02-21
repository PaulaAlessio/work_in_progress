import warnings
# Counts lines of a file 
def count_lines(filename):
    ret = 0 
    with open(filename) as f: 
         for _ in f: 
            ret = ret +1  
    return ret

# Trims character char in position pos from string
def trim_str(string,pos,char):
    if(string[pos]==char):
#        warnings.warn("Removing "+char+" form position"+str(pos))
        if(pos+1==0): 
            return(string[:pos])
        else:
            return(string[:pos]+string[(pos+1):])
    return(string)  



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
        

def get_tree_ids(list_str):
    """ Returns a list of g000000i tree names """
    res = []
    for elem in list_str:
        res.append("g"+"{0:07d}".format(elem))
    return res





