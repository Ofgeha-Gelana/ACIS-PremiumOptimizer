# ACIS Premium Optimizer

## Overview
ACIS Premium Optimizer is a comprehensive data analysis project focused on insurance data. The primary goal is to optimize premium structures and claims analysis using Exploratory Data Analysis (EDA) and insightful visualizations. This project leverages Python's data science stack to uncover trends, correlations, and anomalies in the dataset.

## Features
- **Data Summarization**: Gain insights into the data with descriptive statistics and data structure reviews.
- **Data Quality Assessment**: Identify missing values and assess the overall quality of the data.
- **Univariate Analysis**: Understand the distributions of numerical and categorical variables.
- **Bivariate and Multivariate Analysis**: Analyze correlations and associations between key metrics.
- **Outlier Detection**: Identify anomalies in numerical data.
- **Geographical Trends**: Compare changes in insurance features across different regions.
- **Creative Visualizations**: Create insightful and beautiful plots for data storytelling.

## Requirements

- Python 3.8+
- Required Libraries:
  - pandas
  - numpy
  - matplotlib
  - seaborn

Install dependencies using:
```bash
pip install -r requirements.txt
```

## Dataset
The dataset includes the following columns:
- **Date**: Date of the record
- **TotalPremium**: Total premium collected
- **TotalClaim**: Total claims processed
- **ZipCode**: Geographical identifier
- Additional features such as insurance cover type, auto make, etc.

Ensure the dataset is in CSV format and placed in the `data/` directory with the name `insurance_data.csv`.

## Steps to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/Ofgeha-Gelana/ACIS-PremiumOptimizer.git
   cd ACIS-PremiumOptimizer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your dataset in the `data/` directory.

4. Run the EDA script:
   ```bash
   python eda.py
   ```

## Exploratory Data Analysis Workflow

### Task 1: Data Summarization
1. Calculate descriptive statistics for numerical features (e.g., `TotalPremium`, `TotalClaim`).
2. Review column data types to ensure proper formatting.
3. Check for missing values and handle them appropriately.

### Task 2: Univariate Analysis
1. Plot histograms for numerical columns.
2. Create bar charts for categorical columns to visualize distributions.

### Task 3: Bivariate and Multivariate Analysis
1. Analyze correlations between `TotalPremium`, `TotalClaim`, and other numerical features using scatter plots and correlation matrices.
2. Explore geographical trends in premiums and claims by analyzing `ZipCode` and other geographical features.

### Task 4: Outlier Detection
1. Use box plots to identify outliers in key numerical columns.

### Task 5: Visualizations
1. Create three insightful visualizations to highlight key findings.
   - Example: Correlation heatmaps, time-series trends, and premium-claim comparisons by geography.

## Results
- Key insights from the analysis will be saved to the `results/` directory.
- Generated plots will be stored in the `plots/` directory for further review.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy analyzing! 🚀
