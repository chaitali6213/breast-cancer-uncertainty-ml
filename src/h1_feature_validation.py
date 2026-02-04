import pandas as pd
from sklearn.model_selection import train_test_split

from src.models import get_logistic_model
from src.evaluation import evaluate_auc


def run_h1_experiment(df: pd.DataFrame, feature_cols: list) -> float:
    """
    Trains a logistic regression model on selected features
    and returns ROC-AUC.
    """
    X = df[feature_cols]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, stratify=y, random_state=42
    )

    model = get_logistic_model()
    model.fit(X_train, y_train)

    auc = evaluate_auc(model, X_test, y_test)
    return auc
