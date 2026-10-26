# Quiz 2: Linear Regression and Logistic Regression

This is my work for Quiz 2 in Etornam's class.

**Name:** Grace Angmor (PUIT/22110039)
**School:** Pentecost University
**Course:** Artificial Intelligence

## What this project is about

I built one Jupyter notebook that uses two machine learning models on the same small student dataset:

1. **Linear regression** predicts a number. Here it predicts a student's exam score from the hours they studied.
2. **Logistic regression** predicts a category. Here it predicts whether a student passes or fails (pass means a score of 50 or more).

## Files

| File | What it is |
| --- | --- |
| `grace_quiz_2.ipynb` | The notebook with all the code, graphs and my explanations |
| `README.md` | This file |

## What is inside the notebook

1. Import the libraries
2. Create the dataset (100 students)
3. Look at the data and plot it
4. Linear regression: train, test, and check with MAE, RMSE and R2
5. Logistic regression: train, test, and check with accuracy and a confusion matrix
6. Use both models on a new student
7. Conclusion

## How to run it

1. Clone the repository:
   ```
   git clone https://github.com/Grace-45/etornam_quiz_2.git
   cd etornam_quiz_2
   ```
2. Switch to my branch:
   ```
   git checkout grace-45
   ```
3. Install the libraries:
   ```
   pip install numpy pandas matplotlib scikit-learn notebook
   ```
4. Open the notebook:
   ```
   jupyter notebook grace_quiz_2.ipynb
   ```
5. Click **Kernel > Restart & Run All**.

## What I learned

- Linear regression is for predicting a number, and logistic regression is for predicting yes or no.
- I should always split my data into a training set and a test set, so I can check the model on data it has not seen.
- Different models need different ways of checking how good they are (MAE and R2 for linear, accuracy and confusion matrix for logistic).

## Note

The dataset is made up using random numbers (with a fixed seed so the results are the same every time). It is only for practice.
