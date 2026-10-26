# Quiz 2: Linear and Logistic Regression

**Student:** Asomani Henry
**Student ID:** PUIT/22110011
**Repository:** https://github.com/hatieku-boateng/etornam_quiz_2
**Branch:** `asomani-henry-22110011`

## Overview

This repository contains my submission for Quiz 2 in Etornam's class. The notebook demonstrates two fundamental machine learning models:

- **Linear Regression**, used to predict a continuous value.
- **Logistic Regression**, used to classify data into categories.

## Files

| File | Description |
|---|---|
| `quiz2_asomani_henry_22110011.ipynb` | Jupyter notebook with both models, evaluation and conclusions |
| `README.md` | This file |

## Notebook Contents

1. **Imports**: NumPy, pandas, Matplotlib and scikit-learn.
2. **Linear Regression**
   - Dataset: scikit-learn Diabetes dataset (predicting disease progression)
   - 80/20 train-test split
   - Evaluation: MSE, RMSE and R², plus an actual-vs-predicted plot
3. **Logistic Regression**
   - Dataset: scikit-learn Breast Cancer dataset (malignant vs benign)
   - Stratified 80/20 split with feature scaling (`StandardScaler`)
   - Evaluation: accuracy, confusion matrix, classification report, and a predicted-probability plot
4. **Comparison** of the two models.
5. **Conclusion**

Both datasets ship with scikit-learn, so no external downloads are needed.

## Requirements

- Python 3.8+
- numpy
- pandas
- matplotlib
- scikit-learn
- jupyter

Install with:

```bash
pip install numpy pandas matplotlib scikit-learn notebook
```

## How to Run

```bash
# 1. Clone the repository
git clone https://github.com/hatieku-boateng/etornam_quiz_2.git
cd etornam_quiz_2

# 2. Switch to my branch
git checkout asomani-henry-22110011

# 3. Launch Jupyter and open the notebook
jupyter notebook quiz2_asomani_henry_22110011.ipynb
```

Then choose **Kernel → Restart & Run All** to reproduce every result.

## Git Workflow Used

```bash
git clone https://github.com/hatieku-boateng/etornam_quiz_2.git
cd etornam_quiz_2
git checkout -b asomani-henry-22110011
git add quiz2_asomani_henry_22110011.ipynb README.md
git commit -m "Quiz 2: linear and logistic regression - Asomani Henry PUIT/22110011"
git push -u origin asomani-henry-22110011
```
