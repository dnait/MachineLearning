import numpy as np
import pydotplus as pydotplus
from sklearn.datasets import load_iris
from sklearn import tree


iris = load_iris()
#The first setosa is 0, the first versicolor is 50 and so on
test_idx = [0, 50, 100]

#Training data is to removing three entries from the data and target variables
#Training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#Testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

print test_target   #[0 1 2]
print clf.predict(test_data)   #[0 1 2]


#viz code
from IPython.display import Image
dot_data = tree.export_graphviz(clf, out_file=None,
                         feature_names=iris.feature_names,
                         class_names=iris.target_names,
                         filled=True, rounded=True,
                         special_characters=True)
graph = pydotplus.graph_from_dot_data(dot_data)
Image(graph.create_png())