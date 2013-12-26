from sklearn import svm

def svm_data(X_train,X_test):
    for kernel_type in ['rbf']:
        print(kernel_type)
        clf = svm.OneClassSVM(nu=0.01, kernel='rbf', gamma=0.1)
        print('learning the model...')
        clf.fit(X_train)
        print('done')
        print('Predict class in train')
        y_pred_X_train = clf.predict(X_train)
        print('Done')
        print('Predict class in test')
        y_pred_X_test = clf.predict(X_test)
        print('Done')
        n_error_X_train = float(y_pred_X_train[y_pred_X_train == -1].size)/y_pred_X_train.size*100
        n_error_X_test = float(y_pred_X_test[y_pred_X_test == -1].size)/y_pred_X_test.size*100
        print n_error_X_train
        print n_error_X_test
    return (y_pred_X_train,y_pred_X_test)
