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
        warnings.warn("Removing "+char+" form position"+str(pos))
        if(pos+1==0): 
            return(string[:pos])
        else:
            return(string[:pos]+string[(pos+1):])
    return(string)  



