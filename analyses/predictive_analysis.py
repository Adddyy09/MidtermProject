import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import os

class PredictiveAnalysis:
    def __init__(self, dataset_path):
        self.data = pd.read_csv(dataset_path)
        os.makedirs("outputs/plots", exist_ok=True)

    def analyze(self, show=True, block=True):
        df = self.data.copy()

        # Map categorical to numeric
        df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})
        df['BusinessTravel'] = df['BusinessTravel'].astype('category').cat.codes
        df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

        # Select predictive variables only
        features = ['Age', 'BusinessTravel', 'JobLevel', 'MonthlyIncome', 'OverTime']
        X = df[features]
        y = df['Attrition']

        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        # Train decision tree
        model = DecisionTreeClassifier(max_depth=4, random_state=42)
        model.fit(X_train, y_train)

        # Predict and evaluate
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test, y_pred)
        print(f"\nDecision Tree Accuracy: {acc:.2f}")
        print(classification_report(y_test, y_pred))

        # Visualize tree
        plt.figure(figsize=(18, 10))
        plot_tree(model, filled=True, feature_names=features, class_names=['Stay', 'Leave'])
        plt.title("Decision Tree - Employee Attrition Prediction", fontsize=14)
        plt.savefig('outputs/plots/decision_tree.png', bbox_inches='tight')

        if show:
            plt.show(block=block)
        plt.close()
