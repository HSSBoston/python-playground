import emlearn, joblib
from sklearn.ensemble import RandomForestClassifier

features = ["10", "3", "77", "0.0", "87", "4"]

clf = joblib.load("dt.joblib")
y_predicted = clf.predict([features])
alertLevel = int(y_predicted[0])
print(alertLevel)

# Convert model using emlearn
cmodel = emlearn.convert(clf, method="inline")

# Save as loadable .csv file
path = "dt.csv"
cmodel.save(file=path, name="dt", format="csv")
print('Wrote model to', path)