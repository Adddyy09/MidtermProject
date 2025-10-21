from utils.data_curation import DataCuration
from analyses.correlation_analysis import CorrelationAnalysis
from analyses.descriptive_analysis import DescriptiveAnalysis
from analyses.predictive_analysis import PredictiveAnalysis

# MAIN EXECUTION
if __name__ == "__main__":
    print("=== HR ANALYTICS PROJECT START ===")

    dataset_path = "data/HR_Analytics.csv"

    # --- Data Curation ---
    curator = DataCuration(dataset_path)
    corr = curator.create_correlation_dataset()
    desc = curator.create_descriptive_dataset()
    pred = curator.create_predictive_dataset()
    print("✅ Sub datasets created.")

    # --- Analyses ---
    corr_analysis = CorrelationAnalysis("outputs/Correlation.csv")
    corr_analysis.analyze()
    print("✅ Correlation analysis complete.")

    desc_analysis = DescriptiveAnalysis("outputs/Descriptive.csv")
    desc_analysis.analyze()
    print("✅ Descriptive analysis complete.")

    pred_analysis = PredictiveAnalysis("outputs/Predictive.csv")
    pred_analysis.analyze()
    print("✅ Predictive analysis complete.")

    print("=== ALL ANALYSES DONE ===")
