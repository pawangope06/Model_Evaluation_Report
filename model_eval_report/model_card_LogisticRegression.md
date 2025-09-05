# Model Card: LogisticRegression

## Overview
- **Task**: Binary Classification
- **Dataset**: Breast Cancer (sklearn)
- **Train/Test Split**: 80/20
- **Evaluation Date**: 2025-09-05 11:49:37

## Metrics
- **Accuracy**: 0.9561
- **F1**: 0.9655
- **AUC**: 0.9977
- **RMSE**: 0.1591
- **MAE**: 0.0475

## Plots
Hover over link to view plots
- ROC Curve  
  ![ROC Curve](roc_LogisticRegression.png)

- Precision-Recall Curve  
  ![PR Curve](pr_LogisticRegression.png)

- Confusion Matrix  
  ![Confusion Matrix](cm_LogisticRegression.png)

## Strengths
- Handles binary classification effectively.
- Useful for medical datasets.

## Limitations
- May not generalize to non-binary tasks.
- Performance may vary on imbalanced datasets.

## Intended Use
- Educational / demonstration purposes.
- Should **not** be used for medical decisions.

## Notes
- RMSE/MAE computed on predicted probabilities.
- Educational purpose only.
