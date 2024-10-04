import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC, SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report
from sklearn.model_selection import GridSearchCV

columns_haberman = ['Age', 'Year of Operation', 'Positive Nodes', 'Survivability']
columns_iris = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class']

iris = pd.read_csv('iris/iris.data', names=columns_iris)
haberman = pd.read_csv('haberman/haberman.data', names=columns_haberman)

x = iris.drop(columns=['class'])
y = iris['class']

#separating data into train, validation and test
x_train_val, x_test, y_train_val, y_test = train_test_split(x, y, test_size=0.2, random_state=69420)
x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=0.3, random_state=69420)


mlp = MLPClassifier(random_state=69420)
mlp.fit(x_train, y_train)
# Print the total number of layers (input + hidden + output)
print(f"Total number of layers (input + hidden + output): {mlp.n_layers_}")

# Input layer perceptrons (features)
print(f"Input layer has {mlp.coefs_[0].shape[0]} perceptrons (input features)")

# Hidden and output layers perceptrons
for i, coef in enumerate(mlp.coefs_):
    print(f"Layer {i + 1} has {coef.shape[1]} perceptrons")

# Output layer perceptrons
print(f"Output layer has {mlp.coefs_[-1].shape[1]} perceptrons (output classes)")
y_pred = mlp.predict(x_val)
print("Classification Report:\n", classification_report(y_val, y_pred))

grid_search = GridSearchCV(mlp, { 'hidden_layer_sizes': [5, 10, 20], 'activation': ['logistic', 'relu'], 'solver': ['sgd', 'lbfgs'], 'alpha': [0.00001, 0.001, 0.01]}, cv=5)
grid_search.fit(x_train, y_train)
best_mlp = grid_search.best_estimator_
y_pred = best_mlp.predict(x_val)
# Print the total number of layers (input + hidden + output)
print(f"Total number of layers (input + hidden + output): {best_mlp.n_layers_}")

# Input layer perceptrons (features)
print(f"Input layer has {best_mlp.coefs_[0].shape[0]} perceptrons (input features)")

# Hidden and output layers perceptrons
for i, coef in enumerate(best_mlp.coefs_):
    print(f"Layer {i + 1} has {coef.shape[1]} perceptrons")

# Output layer perceptrons
print(f"Output layer has {best_mlp.coefs_[-1].shape[1]} perceptrons (output classes)")
print("Classification Report:\n", classification_report(y_val, y_pred))

y_test_pred1 = mlp.predict(x_test)
print("Classification Report on Test Set:")
print(classification_report(y_test, y_test_pred1))
y_test_pred2 = best_mlp.predict(x_test)
print("Classification Report on Test Set:")
print(classification_report(y_test, y_test_pred2))
