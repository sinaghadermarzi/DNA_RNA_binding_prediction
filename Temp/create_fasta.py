ofile = open("sequences.fasta","w")
ifile = open("sequences_training.csv")
lfile = open("labels.csv","w")


line = ifile.readline()
i = 1
while line:
    res =  line.find('X')
    if res != -1:
        print 'ERROR'
#    eline = line.replace('X','A')
 #   res =  eline.find('X')
    else:
        if i %80 ==1:
            linespl = line.split(',')
            lfile.write(str(i)+','+linespl[1])
            ofile.write('>' + str(i) + '\n')
            ofile.write(linespl[0]+'\n')
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