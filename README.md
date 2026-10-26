# etornam_quiz_2

This project compares simple and multiple linear regression on a synthetic dataset.

## Progress of work

1. Set up the project workspace and prepared it for Python work.
2. Created a Python virtual environment in `.venv` and added a `.gitignore`
   covering virtual environments, Python cache files, local environment
   variables, and editor/OS files.
3. Added `regression_comparison.ipynb`, a reproducible simple-versus-multiple
   linear regression exercise, plus `requirements.txt` for its Python
   dependencies. The notebook creates and saves `regression_data.csv` when run.
4. Generated and validated `regression_data.csv` with 5,000 observations for
   the regression comparison.

## Run the regression notebook

From the project folder in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
code regression_comparison.ipynb
```

In VS Code, select the project's `.venv` Python kernel and run all notebook
cells. The notebook generates `regression_data.csv` in the project folder and
compares SLR and MLR with MSE, MAE, RMSE, R², and residual plots. The
`ipykernel` dependency enables the virtual environment as a notebook kernel.

## Regression models

- **Simple linear regression:** predict `exam_score` using `experience_years`.
- **Multiple linear regression:** predict `exam_score` using study hours,
  experience, attendance, prior score, sleep, and tutoring.

The observations are synthetic and intended for practice, not as real student
data.

## Submission workflow recorded in the tutorial

The supplied step-by-step tutorial records this workflow for the quiz
submission:

1. Installed and opened Visual Studio Code, then cloned the quiz repository and
   opened it as a workspace.
2. Created a personal working branch and Python environment. When the
   environment initially produced thousands of Git changes, added a correctly
   named `.gitignore` so the virtual-environment and Python-generated files
   would not be treated as source files.
3. Created and ran `regression_comparison.ipynb` with a fixed random seed. The
   notebook generated a 5,000-row regression dataset, trained simple and
   multiple linear regression models, evaluated them on a test set, and
   displayed prediction/residual plots. Installed `ipykernel` in the
   environment to run notebook cells.
4. Removed an ignore rule that prevented the tutorial's generated
   `regression_data.csv` from being staged, then staged and committed the
   submission files.
5. Pushed the working branch to the fork and opened Pull Request #6 against the
   upstream quiz repository, as recorded in the supplied screenshots.

The tutorial also describes the Git push and pull-request workflow. The files
for its regression exercise are now included: `regression_comparison.ipynb`
and `requirements.txt`; running the notebook creates `regression_data.csv`.
