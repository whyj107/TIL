import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score , recall_score , confusion_matrix

def get_clf_eval(y_test , pred):
    confusion = confusion_matrix( y_test, pred)
    accuracy = accuracy_score(y_test , pred)
    precision = precision_score(y_test , pred)
    recall = recall_score(y_test , pred)
    print('오차 행렬')
    print(confusion)
    print('정확도: {0:.4f}, 정밀도: {1:.4f}, 재현율: {2:.4f}'.format(accuracy , precision ,recall))
# LogisticRegression
from sklearn.linear_model import LogisticRegression

def Logistic_(x_train, y_train, x_test, y_test):
    lr_clf = LogisticRegression()
    lr_clf.fit(x_train, y_train)
    lr_pred = lr_clf.predict(x_test)
    get_clf_eval(y_test, lr_pred)
# DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier

def DecisionTree_(x_train, y_train, x_test, y_test):
    dt_clf = DecisionTreeClassifier(random_state=11)
    dt_clf.fit(x_train , y_train)
    dt_pred = dt_clf.predict(x_test)
    get_clf_eval(y_test, dt_pred)
# RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

def RandomForest_(x_train, y_train, x_test, y_test):
    rf_clf = RandomForestClassifier(random_state=11)
    rf_clf.fit(x_train , y_train)
    rf_pred = rf_clf.predict(x_test)
    get_clf_eval(y_test, rf_pred)
