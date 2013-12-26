from sklearn import cross_validation

def split_data(ref):
    X_train,X_test=cross_validation.train_test_split(ref,test_size=0.1,random_state=0)
    return X_train,X_test
