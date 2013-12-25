import numpy as np
from sklearn import preprocessing
from split_data import split_data
from svm import svm_data

def read_file(file_name):
# Function for read lines from file and then create list with parameters
    res=[]
    for line in file_name:
        temp=line.split(' ')
        first=temp[1]
        second=temp[2].rstrip()
        temp=[float(first),float(second)]
        res.append(temp)
    return res

def scale(ref,alt):
#Fuction for scaling parameters
    ref_scale=preprocessing.scale(ref)
    alt_scale=preprocessing.scale(alt)
    return ref_scale,alt_scale

if __name__=="__main__":
    #Open the files for reference and alternative splicing
    file1=open("ref_final.txt",'r')
    file2=open("alt_final.txt",'r')

    #Open results files for reference and alternative splicing
    ref_res=open('ref_scale.txt','w')
    alt_res=open('alt_scale.txt','w')

    #Create lists with splicing events
    ref=read_file(file1)
    alt=read_file(file2)

    #Create numpy arrays for lists with splicing arrays
    ref=np.array(ref)
    alt=np.array(alt)

    #Scale arrays (for each value subtract mean and then divide by SD)
    ref_scale,alt_scale=scale(ref,alt)
    #Writing results
    X_train,X_test=split_data(ref)
    y_pred_train,y_pred_test=svm_data(ref_scale,alt_scale)
    for i in y_pred_train:
        ref_res.write(str(i)+"\n")
    for j in y_pred_test:
        alt_res.write(str(j)+"\n")
    ref_res.close()
    alt_res.close()
