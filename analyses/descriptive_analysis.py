import pandas as pd
import matplotlib.pyplot as plt
import os

class DescriptiveAnalysis:
    def __init__(self, dataset_path):
        self.data = pd.read_csv(dataset_path)
        os.makedirs("outputs/plots", exist_ok=True)

    def analyze(self, show=True, block=True):
        # Attrition Count
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        self.data['Attrition'].value_counts().plot(kind='bar', color='teal', ax=ax1)
        ax1.set_title("Attrition Count")
        ax1.set_xlabel("Attrition")
        ax1.set_ylabel("Number of Employees")
        fig1.savefig('outputs/plots/descriptive_attrition.png', bbox_inches='tight')
        if show:
            plt.show(block=block)
        plt.close(fig1)

        # Department Distribution
        fig2, ax2 = plt.subplots(figsize=(7, 4))
        self.data['Department'].value_counts().plot(kind='bar', color='skyblue', ax=ax2)
        ax2.set_title("Department Distribution")
        ax2.set_xlabel("Department")
        ax2.set_ylabel("Count")
        fig2.savefig('outputs/plots/descriptive_department.png', bbox_inches='tight')
        if show:
            plt.show(block=block)
        plt.close(fig2)
