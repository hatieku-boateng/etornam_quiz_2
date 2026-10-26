# Quiz 2 — Linear Regression and Logistic Regression

**Name:** Godfred Bonsu
**Index Number:** PUIT/22210080
**Branch:** `godfred-bonsu`

## Files

| File | Description |
|---|---|
| `Godfred_Bonsu_PUIT_22210080.ipynb` | Jupyter notebook with the full analysis, code, outputs and plots |
| `Godfred_Bonsu_PUIT_22210080.md` | This README |

## What the notebook does

### Part A — Linear Regression
- Dataset: scikit-learn **Diabetes** dataset (442 patients, 10 features)
- Target: a continuous disease-progression score
- Steps: data exploration, correlation analysis, 80/20 train-test split, model training, evaluation
- Results: MAE ≈ 42.8, RMSE ≈ 53.9, R² ≈ 0.45
- Plots: feature-vs-target scatter plots, correlation bar chart, actual-vs-predicted, residual plot

### Part B — Logistic Regression
- Dataset: scikit-learn **Breast Cancer Wisconsin** dataset (569 samples, 30 features)
- Target: malignant (0) or benign (1)
- Steps: class-balance check, stratified 80/20 split, feature standardisation, model training, evaluation
- Results: Accuracy ≈ 98.2 %, Precision ≈ 0.99, Recall ≈ 0.99, F1 ≈ 0.99, ROC-AUC ≈ 0.995
- Plots: class distribution, confusion matrix, ROC curve

### Part C — Comparison
A side-by-side table contrasting the two models (problem type, output, link function, loss, metrics) and a short conclusion.

## How to run

```bash
pip install numpy pandas matplotlib scikit-learn jupyter
jupyter notebook Godfred_Bonsu_PUIT_22210080.ipynb
```

Both datasets are bundled with scikit-learn, so no downloads are needed. Run all cells from top to bottom (Kernel → Restart & Run All).
