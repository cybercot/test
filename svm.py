import numpy as np
import pylab as pl
import matplotlib.font_manager
from sklearn import svm

def svm_data(ref,alt):
    clf = svm.OneClassSVM(nu=0.01, kernel="rbf", gamma=0)
    clf.fit(ref)
    y_pred_ref = clf.predict(ref)
    y_pred_alt = clf.predict(alt)
    n_error_ref = y_pred_ref[y_pred_ref == -1].size
    n_error_alt = y_pred_alt[y_pred_alt == -1].size
    print n_error_ref
    print n_error_alt
    return (y_pred_ref,y_pred_alt)
