# AI Supervised Machine Learning
# Python SVM Classifications
# SVM = Support Vector Machine

from sklearn import svm

# Training Data
#---------------
# X contains 3 measurements of a person 
# Height (cm), Weight (kg), Shoesize (UK)
X = [ [170, 70, 10], [180, 80, 12], [170, 65, 8] , [160, 55, 7], [169, 68, 7.5], [195.5, 90, 10.5] ]
# Y labels the persons with a gender
# 0 : Male 1: Female
Y = [0, 0, 1, 1, 1, 0]

# Construct and Train the model
#------------------------------
clf = svm.SVC() # construct the model
clf.fit(X, Y) # train the model using X and Y

# Save the trained model to a file
from joblib import dump
dump(clf, 'AI_Programming/SVM/TrainedModels/svm_genderBasedOnMeasurements_model.joblib')
