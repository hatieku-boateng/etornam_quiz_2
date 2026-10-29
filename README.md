# Student Performance: Regression and Classification

This project compares Simple Linear Regression, Multiple Linear Regression, and Logistic Regression on a reproducible synthetic student-performance dataset with 5,000 rows.

## Dataset

The dataset contains four input features:

- `study_hours`
- `attendance_pct`
- `assignment_score`
- `sleep_hours`

`exam_score` is the continuous target for the regression models. `passed` is a binary target equal to 1 when `exam_score` is at least 60, and 0 otherwise. The logistic model uses only the four input features, not `exam_score`, to avoid target leakage.

## Run the project

From the project directory, install the dependencies:

```powershell
py -m pip install -r requirements.txt
```

Generate the CSV dataset:

```powershell
py generate_dataset.py
```

Open `regression_model_comparison.ipynb` in Jupyter or VS Code and run all cells.

The notebook evaluates the two regression models with MAE, RMSE, and R-squared. It evaluates Logistic Regression on a stratified holdout set with a confusion matrix, accuracy, precision, recall, and F1 score.
