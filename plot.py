import matplotlib.pyplot as plt
from sklearn.metrics import (
    roc_curve, precision_recall_curve, average_precision_score,
    confusion_matrix
)
import seaborn as sns


def plot_roc(y_true, y_prob, out_path, model_name):
    fpr, tpr, _ = roc_curve(y_true, y_prob[:, 1])
    plt.figure()
    plt.plot(fpr, tpr, label=f"ROC curve (AUC)")

    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title(f"ROC Curve - {model_name}")
    
    plt.savefig(out_path)
    plt.close()


def plot_pr(y_true, y_prob, out_path, model_name):
    precision, recall, _ = precision_recall_curve(y_true, y_prob[:, 1])
    ap = average_precision_score(y_true, y_prob[:, 1])
    plt.figure()
    plt.plot(recall, precision, label=f"AP={ap:.2f}")
    plt.xlabel("Recall")
    plt.ylabel("Precision")
    plt.title(f"Precision-Recall Curve - {model_name}")
    plt.legend()
    plt.savefig(out_path)
    plt.close()


def plot_confusion(y_true, y_pred, out_path, model_name):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure()
    sns.heatmap(cm, annot=True, fmt="d", cmap="pink")
    plt.title(f"Confusion Matrix - {model_name}")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.savefig(out_path)
    plt.close()
