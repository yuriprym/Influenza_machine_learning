import DNA_calculators as dna
import itertools
import sys
### variable ####
#No Global
###


class method():
    #def __init__(self):

    def read_file(self,filename):
    # this should allow us to read in a file and output the result that we want
        ####variables
        head_seqs={}
        header=[]
        seqs=[]
        gene=""
        ###
        with open(filename) as f:
            #we are reading in the file
#the next few lines are used to obtain both the header of the file and then the seq of the file as well 
            fh= f.readlines()
# we are reading file line by line
            for line in fh:
#this is returning the fileheader and then appending it by line
                if(line[0] == ('>')):
                    header.append(line)
#this is 
                    if len(gene) != 0:
                        seqs.append(gene)
                        gene= ''
                else:
                    gene += line.strip()
        seqs.append(gene)

        strainprofiles={}
        for i in range(0,len(seqs)):
            strainprofiles[header[i]]=dna.fullProfile(seqs[i])

        return strainprofiles








def main():
    mthd= method()
    name =sys.argv[1]
    seqdata=mthd.read_file(name)
    print seqdata

main()
