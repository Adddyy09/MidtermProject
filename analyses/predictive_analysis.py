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
        df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})
        df['BusinessTravel'] = df['BusinessTravel'].astype('category').cat.codes
        df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

        X = df.drop('Attrition', axis=1)
        y = df['Attrition']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

        model = DecisionTreeClassifier(max_depth=4, random_state=42)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        print(f"\nDecision Tree Accuracy: {accuracy_score(y_test, y_pred):.2f}")
        print(classification_report(y_test, y_pred))

        plt.figure(figsize=(20, 10))
        plot_tree(model, filled=True, feature_names=X.columns, class_names=['No', 'Yes'])
        plt.title("Decision Tree - Attrition Prediction")
        plt.savefig('outputs/plots/decision_tree.png', bbox_inches='tight')

        if show:
            plt.show(block=block)
        plt.close()