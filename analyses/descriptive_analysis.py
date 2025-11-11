import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os

class DescriptiveAnalysis:
    
    def __init__(self, dataset_path):
        self.data = pd.read_csv(dataset_path)
        os.makedirs("outputs/plots", exist_ok=True) 

    def summary(self):
        print("# Summary Statistics")
        return self.data.describe(include='all')

    def attrition_rates(self):
        rates = self.data['Attrition'].value_counts(normalize=True)
        print("# Attrition Rates\n", rates)
        return rates

    def visualize_distribution(self, show=True, block=True):
        plt.figure(figsize=(8, 5))
        sns.histplot(self.data['Age'], bins=20, kde=True)
        plt.title("Age Distribution")
        plt.xlabel("Age")
        plt.ylabel("Number of Employees")
        plt.tight_layout()
        plt.savefig('outputs/plots/age_distribution.png')
        if show:
            plt.show(block=block)
        plt.close()

        # Monthly Income by Job Role Boxplot
        plt.figure(figsize=(12, 6))
        sns.boxplot(x='JobRole', y='MonthlyIncome', data=self.data)
        plt.xticks(rotation=45, ha='right')
        plt.title("Monthly Income by Job Role")
        plt.xlabel("Job Role")
        plt.ylabel("Monthly Income")
        plt.tight_layout()
        plt.savefig('outputs/plots/monthly_income_by_jobrole.png')
        if show:
            plt.show(block=block)
        plt.close()

        # Prepare data for attrition plots
        dept_attrition = self.data.copy()
        dept_attrition['Attrition'] = dept_attrition['Attrition'].map({'No':0, 'Yes':1})

        # Bar Plot: Attrition Count by Department
        dept_count_agg = dept_attrition.groupby('Department')['Attrition'].sum().reset_index()
        plt.figure(figsize=(8, 5))
        sns.barplot(x='Department', y='Attrition', data=dept_count_agg)
        plt.title("Attrition Count by Department")
        plt.xlabel("Department")
        plt.ylabel("Number of Attritions")
        plt.tight_layout()
        plt.savefig('outputs/plots/attrition_count_by_department.png')
        if show:
            plt.show(block=block)
        plt.close()

        # Bar Plot: Attrition Rate by Department
        dept_rate_agg = dept_attrition.groupby('Department')['Attrition'].mean().reset_index()

        plt.figure(figsize=(8, 5))
        ax = sns.barplot(x='Department', y='Attrition', data=dept_rate_agg)
        plt.title("Attrition Rate by Department")
        plt.xlabel("Department")
        plt.ylabel("Attrition Rate")
        plt.tight_layout()
        plt.savefig('outputs/plots/attrition_rate_by_department.png')
        if show:
            plt.show(block=block)
        plt.close()
