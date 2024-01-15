# AI Supervised Machine Learning
# Python SVM Classifications
# SVM = Support Vector Machine

from sklearn import svm



# X contains 3 measurements of a person 
# Height (cm), Weight (kg), Shoesize (UK)
X = [ [170, 70, 10], [180, 80, 12], [170, 65, 8] , [160, 55, 7], [169, 68, 7.5], [195.5, 90, 10.5] ]
# Y labels the persons with a gender
# 0 : Male 1: Female
Y = [0, 0, 1, 1, 1, 0]

clf = svm.SVC() # construct the model
clf.fit(X, Y) # train the model using X and Y

# The trained model now can make predictions p
p = clf.predict([[180, 80, 13.5], [160, 60, 7] ]) # !!! Note the double [[]] - this is an array of an array of measurements

# report results - a dict is used as to make the result more readable
gender = {0 : "Male", 1 : "Female"}
for idx, g in enumerate(p):
    print (str(idx) + " :: " + gender[g])

