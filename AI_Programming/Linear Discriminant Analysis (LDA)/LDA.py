#Naive Bayes on the Iris dataset
from sklearn.datasets import load_iris
from sklearn.datasets import make_classification
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
X, y = make_classification( n_samples=1000, n_features=4, n_informative=2, n_redundant=0,shuffle=False)
print(X)
clf = LinearDiscriminantAnalysis
clf.fit(X,y)
p = clf.predict([[5.0, 3.4, 1.5, 0.4]])

flower = {0 : "Setosa", 1 : "Versicolour", 2 : "Virginica"}
for idx, f in enumerate(p):
    print (str(idx) + " :: " + flower[f])
    
   