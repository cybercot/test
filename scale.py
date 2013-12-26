import numpy as np
from sklearn import preprocessing
from split_data import split_data
from svm import svm_data

def read_file(file_name):
    # Function for read lines from file and then create list with parameters
    res=[]
    for line in file_name:
        temp=line.split('	')
        first=temp[1]
        second=temp[2]
        forth=temp[3]
        fifth=temp[4]
        temp=[float(first),float(second),float(forth),float(fifth)]
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
  
    #Open files for results
    res1=open('ref_res.txt','w')
    res2=open('alt_res.txt','w')

    #Create lists with splicing events
    ref=read_file(file1)
    alt=read_file(file2)

    #Create numpy arrays for lists with splicing arrays
    ref=np.array(ref)
    alt=np.array(alt)

    #Scale arrays (for each value subtract mean and then divide by SD)
    ref_scale,alt_scale=scale(ref,alt)

    #Split data onto train and test sets
    X_train,X_test=split_data(ref_scale)

    #Perform SVM with different parameters for choose the bese one
    y_pred_X_train,y_pred_X_test=svm_data(ref_scale,alt_scale)

    #Writing results
    for i in y_pred_X_train:
         res1.write(str(i)+"\n")
    for j in y_pred_X_test:
         res2.write(str(j)+"\n")

    res1.close()
    res2.close()
