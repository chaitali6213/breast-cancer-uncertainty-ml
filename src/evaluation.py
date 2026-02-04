from sklearn.metrics import roc_auc_score


def evaluate_auc(model, X, y) -> float:
    """
    Computes ROC-AUC using predicted probabilities.
    """
    y_pred = model.predict_proba(X)[:, 1]
    return roc_auc_score(y, y_pred)



from sklearn.metrics import roc_auc_score
import numpy as np
from scipy import stats


def delong_test(y_true, y_pred1, y_pred2):
    """
    Approximate DeLong test for correlated ROC AUCs.
    Returns auc1, auc2, p-value.
    """
    auc1 = roc_auc_score(y_true, y_pred1)
    auc2 = roc_auc_score(y_true, y_pred2)

    diff = auc1 - auc2
    var = np.var(y_pred1 - y_pred2)

    z = diff / np.sqrt(var + 1e-8)
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))

    return auc1, auc2, p_value
