import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def run_logistic_demo(seed: int = 0):
    X, y = make_classification(
        n_samples=400, n_features=6, n_informative=4, random_state=seed
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=seed
    )
    clf = LogisticRegression(max_iter=200)
    clf.fit(X_train, y_train)
    acc = accuracy_score(y_test, clf.predict(X_test))
    return {"accuracy": float(acc), "n_train": len(X_train)}
