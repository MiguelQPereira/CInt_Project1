import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier, MLPRegressor
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, classification_report, mean_squared_error, mean_absolute_error
from sklearn.model_selection import GridSearchCV
import joblib

df = pd.read_csv('../FIS/generated_data_set_10000.csv')

x = df.drop(columns=['Expected_CLP'])
y = df['Expected_CLP']

#separate data into train, validation and test
x_train_val, x_test, y_train_val, y_test = train_test_split(x, y, test_size=0.2, random_state=69420)
x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=0.3, random_state=69420)

#make a MLP regressor and use gride search with 5 cv to find best hyperparameters
best_mlp = MLPRegressor(random_state=69420, max_iter = 15000, hidden_layer_sizes=(10,10), activation='tanh', solver='lbfgs', alpha=1e-5)
#grid_search = GridSearchCV(mlp, { 'hidden_layer_sizes': [10], 'activation': ['logistic'], 'solver': ['sgd'], 'alpha': [0.00001, 0.001, 0.01]}, cv=5)

#train the model
best_mlp.fit(x_train, y_train)
#grid_search.fit(x_train, y_train)

#get the best model from grid search
#best_mlp = grid_search.best_estimator_

#predict on validation set
y_val_pred = best_mlp.predict(x_val)
#predict on test set
y_test_pred = best_mlp.predict(x_test)

#evaluate the model on the validation set
print(f"Mean Squared Error on validation Set: {mean_squared_error(y_val, y_val_pred)}")
print(f"Mean Absolute Error on validation Set: {mean_absolute_error(y_val, y_val_pred)}")

#evaluate the model on the test set
print(f"Mean Squared Error on test Set: {mean_squared_error(y_test, y_test_pred)}")
print(f"Mean Absolute Error on test Set: {mean_absolute_error(y_test, y_test_pred)}")

# Total number of layers (input + hidden + output)
print(f"Total number of layers (input + hidden + output): {best_mlp.n_layers_}")

# Input layer perceptrons (input features)
print(f"Input layer has {best_mlp.coefs_[0].shape[0]} perceptrons (input features)")

# Hidden layers and output layer perceptrons
for i, coef in enumerate(best_mlp.coefs_):
    print(f"Layer {i + 1} has {coef.shape[1]} perceptrons")

# Output layer perceptrons
print(f"Output layer has {best_mlp.coefs_[-1].shape[1]} perceptrons (output neurons)")

print(f"Alpha (L2 regularization strength): {best_mlp.alpha}")

#save the NN
joblib.dump(best_mlp, 'mlp_model.pkl')
