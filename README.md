# Titanic Survival Prediction

## Project Overview

This project predicts whether a passenger survived the Titanic disaster using Machine Learning.

The project covers the complete machine learning workflow:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Model Training
- Model Comparison
- Hyperparameter Tuning
- Cross Validation
- Feature Importance
- Model Saving
- Streamlit Deployment

## Dataset

Dataset: Titanic - Machine Learning from Disaster

Files:

- `train.csv`
- `test.csv`
- `gender_submission.csv`

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- SciPy
- SHAP
- Joblib
- Streamlit

## Models Used

- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors
- Support Vector Machine

## Best Model

Random Forest Classifier tuned using `GridSearchCV` with 5-fold cross-validation.

- Best CV score: **83.70%**
- Held-out test accuracy: **82.68%**
- Best parameters:
  - `n_estimators`: 200
  - `max_depth`: 5
  - `min_samples_split`: 5
  - `min_samples_leaf`: 1

## Project Structure

```text
Titanic-Survival-Prediction/
├── Data/
│   ├── train.csv
│   ├── test.csv
│   └── gender_submission.csv
├── Model/
│   └── titanic_model.pkl
├── Notebook/
│   └── Titanic1.ipynb
├── Screenshot/
├── app.py
├── requirements.txt
├── requirements-notebook.txt
├── run_project.bat
├── packages.txt
└── README.md
```

## How to Run in VS Code on Windows

### Option 1 — Easiest

Double-click:

```text
run_project.bat
```

It creates the virtual environment, installs the dependencies, and starts Streamlit.

### Option 2 — VS Code CMD

Open the project folder in VS Code, then open **Terminal → New Terminal**.

Make sure the terminal is inside the folder containing `app.py` and `requirements.txt`.

Run:

```cmd
python -m venv venv
venv\Scripts\activate
python -m pip install -r requirements.txt
python -m streamlit run app.py
```

Open the local URL shown by Streamlit, normally:

```text
http://localhost:8501
```

### If `streamlit is not recognized`

Use:

```cmd
python -m streamlit run app.py
```

instead of:

```cmd
streamlit run app.py
```

## Important

The saved model was serialized with **scikit-learn 1.9.0**. Keep the version in `requirements.txt` unchanged so the model can be loaded with the matching scikit-learn version.

## Notebook

For all notebook/EDA/SHAP dependencies, install:

```cmd
python -m pip install -r requirements-notebook.txt
```

## Author

Bhaskar Choudhary
