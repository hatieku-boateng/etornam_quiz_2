# etornam_quiz_2

This project compares Simple Linear Regression (SLR) and Multiple Linear
Regression (MLR) in `regression_analysis.ipynb`.

## Set up the virtual environment

From this folder, create and activate a virtual environment, then install the
packages listed in `requirements.txt`:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

If PowerShell prevents activation, run the environment's Python directly:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Open `regression_analysis.ipynb` using the `.venv` Python kernel. Run the
notebook from top to bottom. It generates the reproducible 5,000-row
`regression_data.csv` in the working folder before loading and analyzing it.
