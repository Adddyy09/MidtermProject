import matplotlib.pyplot as plt
import pandas as pd
import os

class CorrelationAnalysis:
    def __init__(self, dataset_path):
        self.data = pd.read_csv(dataset_path)
        os.makedirs("outputs/plots", exist_ok=True)

    def analyze(self, show=True, block=True):
        corr = self.data.corr()
        print("\n[Correlation Matrix]\n", corr)

        fig, ax = plt.subplots(figsize=(8, 6))
        cax = ax.matshow(corr, cmap='coolwarm')
        ax.set_title("Correlation Heatmap", pad=20)
        fig.colorbar(cax)
        fig.savefig('outputs/plots/correlation_heatmap.png', bbox_inches='tight')

        if show:
            plt.show(block=block)
        plt.close(fig)
    
    
