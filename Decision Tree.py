import math
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
def alpha_beta_pruning(depth, node_index, maximizing_player, values, alpha, beta):
    if depth == 0 or node_index >= len(values):
        return values[node_index]
    if maximizing_player:
        max_eval = -math.inf
        for i in range(2):  
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break 
        return max_eval
    else:
        min_eval = math.inf
        for i in range(2):  
            eval = alpha_beta_pruning(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval
def decision_tree_example():
    iris = datasets.load_iris()
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("Decision Tree Accuracy:", metrics.accuracy_score(y_test, y_pred))
if __name__ == "__main__":
    values = [3, 5, 6, 9, 1, 2, 0, -1] 
    tree_depth = math.log2(len(values))
    optimal_value = alpha_beta_pruning(int(tree_depth), 0, True, values, -math.inf, math.inf)
    print("The optimal value is:", optimal_value)
    decision_tree_example()

