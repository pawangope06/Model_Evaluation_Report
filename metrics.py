from sklearn.metrics import (
    accuracy_score, f1_score, roc_auc_score,
    mean_squared_error, mean_absolute_error
)
import numpy as np


def compute_classification_metrics(y_true, y_pred, y_prob):
    
    metrics = {}
    metrics["Accuracy"] = accuracy_score(y_true, y_pred)
    metrics["F1"] = f1_score(y_true, y_pred)
    metrics["ROC_AUC"] = roc_auc_score(y_true, y_prob[:, 1])
    metrics["RMSE_on_prob"] = np.sqrt(mean_squared_error(y_true, y_prob[:, 1]))
    metrics["MAE_on_prob"] = mean_absolute_error(y_true, y_prob[:, 1])
    return metrics
