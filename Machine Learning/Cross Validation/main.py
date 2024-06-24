from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, StratifiedKFold, LeaveOneOut, LeavePOut, ShuffleSplit, cross_val_score

# Load dataset
X, y = load_iris(return_X_y=True)

# Decision Tree classifier
clf = DecisionTreeClassifier(random_state=42)

# K-Fold Cross-Validation
k_folds = KFold(n_splits=5)
k_fold_scores = cross_val_score(clf, X, y, cv=k_folds)
print("K-Fold Cross Validation Scores:")
print(k_fold_scores)
print("Average CV Score:", k_fold_scores.mean())
print("Number of CV Scores used in Average:", len(k_fold_scores))
print()

# Stratified K-Fold Cross-Validation
sk_folds = StratifiedKFold(n_splits=5)
stratified_scores = cross_val_score(clf, X, y, cv=sk_folds)
print("Stratified K-Fold Cross Validation Scores:")
print(stratified_scores)
print("Average CV Score:", stratified_scores.mean())
print("Number of CV Scores used in Average:", len(stratified_scores))
print()

# Leave-One-Out (LOO) Cross-Validation
loo = LeaveOneOut()
loo_scores = cross_val_score(clf, X, y, cv=loo)
print("Leave-One-Out Cross Validation Scores:")
print(loo_scores)
print("Average CV Score:", loo_scores.mean())
print("Number of CV Scores used in Average:", len(loo_scores))
print()

# Leave-P-Out (LPO) Cross-Validation
lpo = LeavePOut(p=2)
lpo_scores = cross_val_score(clf, X, y, cv=lpo)
print("Leave-P-Out Cross Validation Scores:")
print(lpo_scores)
print("Average CV Score:", lpo_scores.mean())
print("Number of CV Scores used in Average:", len(lpo_scores))
print()

# Shuffle Split Cross-Validation
ss = ShuffleSplit(train_size=0.6, test_size=0.3, n_splits=5)
shuffle_split_scores = cross_val_score(clf, X, y, cv=ss)
print("Shuffle Split Cross Validation Scores:")
print(shuffle_split_scores)
print("Average CV Score:", shuffle_split_scores.mean())
print("Number of CV Scores used in Average:", len(shuffle_split_scores))
