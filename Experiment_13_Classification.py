# Experiment 13: Decision Tree, Naive Bayes and KNN
# Install: pip install scikit-learn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

models = [DecisionTreeClassifier(), GaussianNB(),
          KNeighborsClassifier(n_neighbors=3)]

for model in models:
    model.fit(X_train, y_train)
    prediction = model.predict(X_test)
    print(type(model).__name__, "Accuracy:", accuracy_score(y_test, prediction))
