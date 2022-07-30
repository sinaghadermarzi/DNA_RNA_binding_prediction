import csv
import sys

DNA_file_addr = 'DNA-bindingProteins.txt'
RNA_file_addr = 'RNA-bindingProteins.txt'


DNAs = []
RNAs = []


DNA_file = open(DNA_file_addr)

line = DNA_file.readline()
while line:
    if line[0]== '>':
        line = DNA_file.readline()
        line = line.rstrip('\n')
        DNAs.append(line)
    line = DNA_file.readline()
DNA_file.close()

RNA_file = open(RNA_file_addr)
line = RNA_file.readline()
while line:
    if line[0] == '>':
        line = RNA_file.readline()
        line = line.rstrip('\n')
        RNAs.append(line)
    line = RNA_file.readline()
RNA_file.close()


set_RNAs = set(RNAs)
set_DNAs = set(DNAs)

set_DRNAonly = set_RNAs & set_DNAs

set_DNAonly = set_DNAs-set_DRNAonly
set_RNAonly = set_RNAs-set_DRNAonly




DRNA_only_file_addr ='DRNA.csv'
DNA_only_file_addr ='DNA.csv'
RNA_only_file_addr ='RNA.csv'


DNA_only_file_addr ='DNA.csv'
DNA_only_file = open(DNA_only_file_addr,'w')
for s in set_DNAonly:
    DNA_only_file.write(s+'\n')
DNA_only_file.close()



RNA_only_file_addr ='RNA.csv'
RNA_only_file = open(RNA_only_file_addr,'w')
for s in set_RNAonly:
    RNA_only_file.write(s+'\n')
RNA_only_file.close()


DRNA_only_file_addr ='DRNA.csv'
DRNA_only_file = open(DRNA_only_file_addr,'w')
for s in set_DRNAonly:
    DRNA_only_file.write(s+'\n')
DRNA_only_file.close()


old = []
old_file = open("seq.csv_features.csv")
line = old_file.readline()
while line:
    line = line.rstrip('\n')
    lineitems = line.split(',')
    old.append(lineitems[0])
    line = old_file.readline()


old_set = set(old)












set_DRNAonly_new = set_DRNAonly - old_set
set_DNAonly_new = set_DNAonly - old_set
set_RNAonly_new = set_RNAonly - old_set





DNA_only_file_addr ='DNA_new.csv'
DNA_only_file = open(DNA_only_file_addr,'w')
for s in set_DNAonly_new:
    DNA_only_file.write(s+'\n')
DNA_only_file.close()



RNA_only_file_addr ='RNA_new.csv'
RNA_only_file = open(RNA_only_file_addr,'w')
for s in set_RNAonly_new:
    RNA_only_file.write(s+'\n')
RNA_only_file.close()


DRNA_only_file_addr ='DRNA_new.csv'
DRNA_only_file = open(DRNA_only_file_addr,'w')
for s in set_DRNAonly_new:
    DRNA_only_file.write(s+'\n')
DRNA_only_file.close()
