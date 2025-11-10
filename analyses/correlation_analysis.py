import matplotlib.pyplot as plt
import pandas as pd
import os

class CorrelationAnalysis:
    def __init__(self, dataset_path):
        self.data = pd.read_csv(dataset_path)
        os.makedirs("outputs/plots", exist_ok=True)

    def analyze(self, show=True, block=True):
        selected_columns = [
            'Age', 'MonthlyIncome', 'YearsAtCompany',
            'WorkLifeBalance', 'JobSatisfaction',
            'OverTime', 'PerformanceRating', 'Attrition'
        ]

        df = self.data[selected_columns].copy()

        # Map categorical to numeric for correlation calculation
        if 'OverTime' in df.columns:
            df['OverTime'] = df['OverTime'].map({'Yes': 1, 'No': 0})
        
        if 'Attrition' in df.columns:
            df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

        corr = df.corr()

        print("\n[Correlation Matrix]\n", corr)

        fig, ax = plt.subplots(figsize=(8, 6))
        cax = ax.matshow(corr, cmap='coolwarm')
        plt.title("Correlation Heatmap", pad=20)
        plt.xticks(range(len(corr.columns)), corr.columns, rotation=45, ha='left')
        plt.yticks(range(len(corr.columns)), corr.columns)
        plt.colorbar(cax)

        plt.tight_layout()
        plt.savefig('outputs/plots/correlation_heatmap.png', bbox_inches='tight')

        if show:
            plt.show(block=block)
        plt.close(fig)
