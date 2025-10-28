import pandas as pd
import matplotlib.pyplot as plt
import os

class DescriptiveAnalysis:
    def __init__(self, dataset_path):
        # Load dataset
        self.data = pd.read_csv(dataset_path)
        # Ensure output directory exists
        os.makedirs("outputs/plots", exist_ok=True)

    def analyze(self, show=True, block=True):
        """Performs descriptive visualizations based on HR Analytics variables."""

        # 1. Attrition Count
        fig1, ax1 = plt.subplots(figsize=(6, 4))
        self.data['Attrition'].value_counts().plot(kind='bar', color='teal', ax=ax1)
        ax1.set_title("Attrition Count")
        ax1.set_xlabel("Attrition (Yes/No)")
        ax1.set_ylabel("Number of Employees")
        fig1.savefig('outputs/plots/descriptive_attrition.png', bbox_inches='tight')
        if show: plt.show(block=block)
        plt.close(fig1)

        # 2. Department Distribution
        fig2, ax2 = plt.subplots(figsize=(7, 4))
        self.data['Department'].value_counts().plot(kind='bar', color='skyblue', ax=ax2)
        ax2.set_title("Department Distribution")
        ax2.set_xlabel("Department")
        ax2.set_ylabel("Count")
        fig2.savefig('outputs/plots/descriptive_department.png', bbox_inches='tight')
        if show: plt.show(block=block)
        plt.close(fig2)

        # 3. Job Role Distribution
        fig3, ax3 = plt.subplots(figsize=(8, 4))
        self.data['JobRole'].value_counts().plot(kind='bar', color='orange', ax=ax3)
        ax3.set_title("Job Role Distribution")
        ax3.set_xlabel("Job Role")
        ax3.set_ylabel("Count")
        plt.xticks(rotation=45, ha='right')
        fig3.savefig('outputs/plots/descriptive_jobrole.png', bbox_inches='tight')
        if show: plt.show(block=block)
        plt.close(fig3)

        # 4. Gender Distribution
        fig4, ax4 = plt.subplots(figsize=(5, 4))
        self.data['Gender'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightblue'], ax=ax4)
        ax4.set_ylabel('')
        ax4.set_title("Gender Distribution")
        fig4.savefig('outputs/plots/descriptive_gender.png', bbox_inches='tight')
        if show: plt.show(block=block)
        plt.close(fig4)

        # 5. Marital Status Distribution
        fig5, ax5 = plt.subplots(figsize=(6, 4))
        self.data['MaritalStatus'].value_counts().plot(kind='bar', color='lightgreen', ax=ax5)
        ax5.set_title("Marital Status Distribution")
        ax5.set_xlabel("Marital Status")
        ax5.set_ylabel("Count")
        fig5.savefig('outputs/plots/descriptive_maritalstatus.png', bbox_inches='tight')
        if show: plt.show(block=block)
        plt.close(fig5)

        # # 6. Overtime vs Attrition (Stacked)
        # fig6, ax6 = plt.subplots(figsize=(6, 4))
        # overtime_attrition = pd.crosstab(self.data['OverTime'], self.data['Attrition'])
        # overtime_attrition.plot(kind='bar', stacked=True, color=['#4CAF50', '#F44336'], ax=ax6)
        # ax6.set_title("OverTime vs Attrition")
        # ax6.set_xlabel("OverTime")
        # ax6.set_ylabel("Employee Count")
        # fig6.savefig('outputs/plots/descriptive_overtime_attrition.png', bbox_inches='tight')
        # if show: plt.show(block=block)
        # plt.close(fig6)

        # # 7. Work-Life Balance Distribution
        # fig7, ax7 = plt.subplots(figsize=(6, 4))
        # self.data['WorkLifeBalance'].value_counts().sort_index().plot(kind='bar', color='mediumpurple', ax=ax7)
        # ax7.set_title("Work-Life Balance Ratings")
        # ax7.set_xlabel("Work-Life Balance (1=Poor, 4=Excellent)")
        # ax7.set_ylabel("Count")
        # fig7.savefig('outputs/plots/descriptive_worklifebalance.png', bbox_inches='tight')
        # if show: plt.show(block=block)
        # plt.close(fig7)

        # print("✅ Descriptive analysis complete. Plots saved to 'outputs/plots/' folder.")
