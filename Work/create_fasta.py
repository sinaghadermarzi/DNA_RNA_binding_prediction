ofile = open("sequences.fasta","w")
ifile = open("sequences.csv")

line = ifile.readline()
i = 1
while line:
    ofile.write('>'+str(i)+'\n')
    ofile.write(line)
    i+=1
    line = ifile.readline()


    # line_cols = line.split()
    # value = (float(line_cols[2]))
    # if value < 0:
    #     print 'ERROR!'
    # res_list.append(str(value))
    # # res_list.append(line_cols[2])
    # # use realine() to read next line
    # line = f.readline()
ofile.close()
ifile.close()