from sklearn.linear_model import LogisticRegression


def get_logistic_model(class_weight=None):
    """
    Returns a logistic regression model.
    
    Parameters:
        class_weight: dict or 'balanced' or None
    """
    return LogisticRegression(
        max_iter=1000,
        solver="liblinear",
        class_weight=class_weight,
        random_state=42,
    )

