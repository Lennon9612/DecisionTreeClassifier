from sklearn.tree\
import DecisionTreeClassifier, export_graphviz
from sklearn.model_selection import train_test_split

import pydot
import numpy as np
import pandas as pd
import collections
import os
from sklearn.metrics import accuracy_score

os.environ["PATH"] += os.pathsep + 'C:Program Files (x86)/Graphviz2.38/bin/'
dt = pd.read_csv("C:/Users/Lennon/Desktop/new/datamining2.csv", header=None)

print(type(dt))
X = dt.values [0:12669,0:300]
Y = dt.values [0:12669,300]
Y = Y.astype('int')

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, stratify = Y, random_state = 50 )
dTreeAll = DecisionTreeClassifier(random_state = 0)
dTreeAll.fit(X_train, y_train)

print("Train Set Score1 : {:.2f}".format(dTreeAll.score(X_train, y_train)))
print("Test Set Score1 : {:.2f}".format(dTreeAll.score(X_test, y_text)))

dTreeLimit = DecisionTreeClassifier(max_depth = 7, random_state = 0, min_samples_split = 50,
                                    min_impurity_split = 0.03, presort = True)
dTreeLimit.fit(X_train,y_train)

print("Train Set Score2 : {:.2f}".format(dTreeLimit.score(X_train, y_train)))
print("Test Set Score2 : {:.2f}".format(dTreeLimit.score(X_test, y_text)))

export_graphviz(dTreeLimit, out_file = "decisionTree1.dot", class_names = ["Value:0, Value=1"],
                feature_names = None, impurity = False, filled = True)

(graph,) = pydot.graph_from_dot_file('decisionTree1.dot', encoding = 'utf8')
print(dTreeLimit)
graph.write_png('decisionTree1.png')

