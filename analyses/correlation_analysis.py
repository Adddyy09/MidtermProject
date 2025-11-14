import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class CorrelationAnalysis:
    def __init__(self, dataset_path):
        self.data = pd.read_csv(dataset_path)
        self.output_dir = "outputs/plots"
        os.makedirs(self.output_dir, exist_ok=True)

    def analyze(self, show=True, block=True):
        df = self.data.copy()

        corr = df.corr()

        print("\n[Correlation Matrix]\n", corr)

        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', linewidths=.5)
        plt.title("Correlation Heatmap of Employee Data", pad=20)
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)

        plt.tight_layout()
        plt.savefig(os.path.join(self.output_dir, 'correlation_heatmap.png'), bbox_inches='tight')

        if show:
            plt.show(block=block)
        plt.close()
