import csv
import sys



def sliding_window(seq,sw_size,num_th,ref_set):
    length = len(seq)
    temp =0
    count=0

    for i in range(0,sw_size):
        if seq[i] in ref_set:
            temp+=1
    for i in range(0,length-sw_size):
        if seq[i] in ref_set:
            temp-=1
        if seq[i+sw_size] in ref_set:
            temp+=1
        if temp>=num_th:
            count+=1
    norm_count = float(count)/float(length)
    return norm_count


def fractions(seq,aa):
    num =seq.count(aa)
    frac = float(num)/float(len(seq))
    return frac



def R_sw_3_h_2(seq):
    return sliding_window(seq,3,2,'R')

def K_sw_3_h_2(seq):
    return sliding_window(seq,3,2,'K')

def RorK_sw_3_h_2(seq):
    return sliding_window(seq,3,2,'RK')

def R_sw_5_h_2(seq):
    return sliding_window(seq,5,2,'R')

def K_sw_5_h_2(seq):
    return sliding_window(seq,5,2,'K')

def RorK_sw_5_h_2(seq):
    return sliding_window(seq,5,2,'RK')




def R_sw_2_h_2(seq):
    return sliding_window(seq,2,2,'R')

def K_sw_2_h_2(seq):
    return sliding_window(seq,2,2,'K')

def RorK_sw_2_h_2(seq):
    return sliding_window(seq,2,2,'RK')







def D_sw_5_h_2(seq):
    return sliding_window(seq,5,2,'D')

def E_sw_5_h_2(seq):
    return sliding_window(seq,5,2,'E')

def DorE_sw_5_h_2(seq):
    return sliding_window(seq,5,2,'DE')


def D_sw_10_h_2(seq):
    return sliding_window(seq,10,2,'D')

def E_sw_10_h_2(seq):
    return sliding_window(seq,10,2,'E')

def DorE_sw_10_h_2(seq):
    return sliding_window(seq,10,2,'DE')

def out_of_range(seq):
    ref_set = 'ARNDCEQGHILKMFPSTWYV'
    res = 0
    for ch in seq:
    	if ref_set.count(ch)==0:
    		res = 1
    return res
			




def length(seq):
    return len(seq)












def frac_D(seq):
    return fractions(seq,'D')
def frac_E(seq):
    return fractions(seq,'E')





def frac_R(seq):
    return fractions(seq,'R')
def frac_K(seq):
    return fractions(seq,'K')

features_to_compute =[
    R_sw_3_h_2,
    K_sw_3_h_2,
    RorK_sw_3_h_2,
    R_sw_5_h_2,
    K_sw_5_h_2,
    RorK_sw_5_h_2,
    R_sw_2_h_2,
    K_sw_2_h_2,
    RorK_sw_2_h_2,
    D_sw_10_h_2,
    E_sw_5_h_2,
    DorE_sw_10_h_2,
    length,
    frac_R,
    frac_K,
    frac_D,
    frac_E,
    out_of_range
]






seq_data_file_name = 'seq_train.csv'
with open(seq_data_file_name) as csvfile , open(seq_data_file_name+'_features.csv','wb') as out_csv:
        reader = csv.DictReader(csvfile)
        field_names = reader.fieldnames
        for f in features_to_compute:
            field_names = field_names + [f.func_name]
        writer = csv.DictWriter(out_csv, field_names)
        writer.writeheader()
        for row in reader:
            out_row = row
            seq = row['Sequence']
            for f in features_to_compute:
                feature = f(seq)
                out_row[f.func_name] = str(feature)
            writer.writerow(out_row)










