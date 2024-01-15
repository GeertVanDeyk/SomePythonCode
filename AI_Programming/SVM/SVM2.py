# AI Supervised Machine Learning
# Python SVM Classifications
# SVM = Support Vector Machine

from sklearn import svm, datasets
iris = datasets.load_iris()

# Take the first two features : Sepal length and Sepal Width
X = iris.data[ : , :2 ]
Y = iris.target 
print(Y)

clf = svm.SVC() # construct the model
clf.fit(X, Y) # train the model using X and Y

# The trained model now can make predictions p
p = clf.predict([[5.4, 3.2]]) # !!! Note the double [[]] - this is an array of an array of measurements

# report results - a dict is used as to make the result more readable
flower = {0 : "Setosa", 1 : "Versicolour", 2 : "Virginica"}
for idx, f in enumerate(p):
    print (str(idx) + " :: " + flower[f])

