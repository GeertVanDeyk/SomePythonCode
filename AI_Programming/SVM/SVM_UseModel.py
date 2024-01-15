# AI Supervised Machine Learning
# Python SVM Classifications
# SVM = Support Vector Machine

import joblib
# Load the trained model from the file
clf = joblib.load('AI_Programming/SVM/TrainedModels/svm_genderBasedOnMeasurements_model.joblib')

print("Hi,")
print("I will ask you some questions about your measurements.")
print("Based on those I will then predict whether you are male or female.")
Height = input("What is your height in cm?")
Weight = input("What is your weight in kg?")
ShoeSize = input("What is your shoesize (UK size)?")

# use the model to make predictions p on new data
p = clf.predict([[Height, Weight, ShoeSize]]) # !!! Note the double [[]] - this is an array of an array of measurements

# report results - a dict is used as to make the result more readable
gender = {0 : "Male", 1 : "Female"}
for idx, g in enumerate(p):
    print (str(idx) + " :: " + gender[g])

