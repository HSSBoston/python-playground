from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, StratifiedKFold, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
 
clf = RandomForestClassifier(max_depth=3, random_state=0)
    # n_estimators=10 by default
clf.fit(X_train, y_train)

print (clf.score(X_test, y_test))

# K分割交差検証
stratifiedkfold = StratifiedKFold(n_splits=10)  #K=10分割
scores = cross_val_score(clf, X, y, cv=stratifiedkfold)
print('Cross-Validation scores: {}'.format(scores))   # 各分割におけるスコア
print('Average score: {}'.format(np.mean(scores)))  # スコアの平均値

# 最初の決定木を可視化
# max_depthでどのくらいの深さまで表示させるかを調整
plot_tree(clf.estimators_[0], 
          feature_names=iris.feature_names,
          class_names=iris.target_names,
          fontsize=10,
          filled=True)
plt.show()
#           rounded=True, 
#           proportion=False, 
#           precision=2,
#           max_depth=2)
# plt.show()
