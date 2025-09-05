import os
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from metrics import compute_classification_metrics
from plot import plot_roc, plot_pr, plot_confusion
from report_generator import save_model_card, generate_html_report


def main():
    outdir = "model_eval_report" # Output directory for report and plots
    os.makedirs(outdir, exist_ok=True)

    # Load dataset
    data = load_breast_cancer()
    X_train, X_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.2, random_state=42
    )

    models = {
        "LogisticRegression": LogisticRegression(max_iter=10000),
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
    }

    # this results dictionary will store the evaluation metrics, plot paths, and model card paths for each model and will be used to generate the final HTML report
    results = {}
    
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)

        # Compute metrics
        metrics = compute_classification_metrics(y_test, y_pred, y_prob)


        # Save plots
        roc_filename = f"roc_{name}.png"
        pr_filename = f"pr_{name}.png"
        cm_filename = f"cm_{name}.png"

        roc_path = os.path.join(outdir, roc_filename)
        pr_path = os.path.join(outdir, pr_filename)
        cm_path = os.path.join(outdir, cm_filename)

        plot_roc(y_test, y_prob, roc_path, name)
        plot_pr(y_test, y_prob, pr_path, name)
        plot_confusion(y_test, y_pred, cm_path, name)

        md_filename = save_model_card(name,
        {
            "metrics": metrics,
            "plots": {
                "roc": roc_filename,
                "pr": pr_filename,
                "cm": cm_filename
            }
        },
        outdir
    )

        results[name] = {
            "metrics": metrics,
            "plots": {"roc": roc_filename, "pr": pr_filename, "cm": cm_filename},
            "model_card": {"md": md_filename},
        }

    # Generate report
    report_path = generate_html_report(results, outdir)
    print(f"Report generated: {report_path}")
    
if __name__ == "__main__":
    main()
