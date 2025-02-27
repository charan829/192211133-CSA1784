import math
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 0 or node_index >= len(values):
        return values[node_index]
    
    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):  # Assuming binary tree
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Beta cut-off
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):  # Assuming binary tree
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Alpha cut-off
        return min_eval

def decision_tree_example():
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Decision Tree Accuracy:", metrics.accuracy_score(y_test, y_pred))

def feed_forward_neural_network():
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    
    model = Sequential([
        Dense(10, activation='relu', input_shape=(X_train.shape[1],)),
        Dense(10, activation='relu'),
        Dense(3, activation='softmax')
    ])
    
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=50, verbose=0)
    loss, accuracy = model.evaluate(X_test, y_test)
    print("Neural Network Accuracy:", accuracy)

# Example usage
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1]  # Terminal node values
    tree_depth = math.log2(len(values))
    optimal_value = alpha_beta_pruning(int(tree_depth), 0, True, values, -math.inf, math.inf)
    print("The optimal value is:", optimal_value)
    decision_tree_example()
    feed_forward_neural_network()
