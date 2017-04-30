from sklearn.datasets import load_iris
iris = load_iris()
print iris.feature_names
print iris.target_names
print iris.data[0]
print iris.target[0]
for i in range(len(iris.target)):
    print ("Example %d: label %s, feature %s" % (i, iris.target[i], iris.data[i]))


#output:
#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
#['setosa' 'versicolor' 'virginica']
#[ 5.1  3.5  1.4  0.2]
# 0 means 'setosa'
