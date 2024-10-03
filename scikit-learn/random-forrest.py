from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
 
clf = RandomForestClassifier(max_depth=3, random_state=0)
    # n_estimators=10 by default
clf.fit(X_train, y_train)

print (clf.score(X_test, y_test))

stratifiedkfold = StratifiedKFold(n_splits=10)  #K=10分割
scores = cross_val_score(clf, X, y, cv=stratifiedkfold)
print('Cross-Validation scores: {}'.format(scores))   # 各分割におけるスコア
print('Average score: {}'.format(np.mean(scores)))  # スコアの平均値
