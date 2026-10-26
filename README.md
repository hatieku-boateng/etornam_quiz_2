# etornam_quiz_2
This is quiz two for Etornam's class

## Run the regression notebook

The notebook compares simple and multiple linear regression, and creates
`regression_data.csv` in the project folder when its data-generation cell runs.

From the project folder, create and activate a virtual environment, then install
the project requirements:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m ipykernel install --user --name etornam-quiz-2 --display-name "Python (etornam-quiz-2)"
```

Open `linear_regression_comparison.ipynb` in VS Code with its Python and Jupyter
extensions, select the `Python (etornam-quiz-2)` kernel, and run the notebook
from top to bottom.
