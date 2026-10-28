# Experiment 14: Underfitting and Overfitting
# Install: pip install scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

for depth in [1, 3, None]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    print("Depth:", depth,
          "Train:", round(accuracy_score(y_train, model.predict(X_train)), 2),
          "Test:", round(accuracy_score(y_test, model.predict(X_test)), 2))
