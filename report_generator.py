from jinja2 import Template
import os
from datetime import datetime


def build_model_card_md(name, info):
    md = f"""# Model Card: {name}

## Overview
- **Task**: Binary Classification
- **Dataset**: Breast Cancer (sklearn)
- **Train/Test Split**: 80/20
- **Evaluation Date**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Metrics
"""
    for k, v in info["metrics"].items():
        md += f"- **{k}**: {v:.4f}\n"

    md += f"""
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
"""
    return md



def md_to_html_simple(md_text):
    return f"<html><body><pre>{md_text}</pre></body></html>"


def save_model_card(name, info, outdir):
    md = build_model_card_md(name, info)

    md_path = os.path.join(outdir, f"model_card_{name}.md")
    # html_path = os.path.join(outdir, f"model_card_{name}.html")
    
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md)

    # try:
    #     import markdown
    #     html = markdown.markdown(md)
    # except:
    #     html = md_to_html_simple(md)

    # with open(html_path, "w", encoding="utf-8") as f:
    #     f.write(html)

    # return just the filenames for report linking
    return os.path.basename(md_path)
# , os.path.basename(html_path)


def generate_html_report(results, outdir):
    template = Template("""
<html>
<head>
    <title>Model Evaluation Report</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        h1 { text-align: center; color: #2c3e50; }

        /* Use grid for side-by-side models */
        .models-container {
            display: grid;
            grid-template-columns: 1fr 1fr; /* Two columns */
            gap: 20px;
        }

        .model-block {
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
            background: #fff;
        }

        a { text-decoration: none; color: #2980b9;}

        .plots img {
            margin: 5px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }

        .metrics-table {
            border-collapse: collapse;
            margin-bottom: 10px;
            width: 100%;
        }
        .metrics-table th, .metrics-table td {
            border: 1px solid #ccc;
            padding: 6px 10px;
            text-align: center;
        }
        .metrics-table th {
            background: #f4f4f4;
        }
    </style>
</head>
<body>
    <h1> Model Evaluation Report</h1>

    <div class="models-container">
        {% for model, info in results.items() %}
        <div class="model-block">
            <h2>{{ model }}</h2>

            <h3>Metrics</h3>
            <table class="metrics-table">
                <tr><th>Metric</th><th>Value</th></tr>
                {% for k,v in info.metrics.items() %}
                <tr><td>{{k}}</td><td>{{ "%.4f"|format(v) }}</td></tr>
                {% endfor %}
            </table>

            <h3>Plots</h3>
            <div class="plots">
                <img src="{{ info.plots.roc }}" width="300">
                <img src="{{ info.plots.pr }}" width="300">
                <img src="{{ info.plots.cm }}" width="300">
            </div>

            <h3>Model Card</h3>
            <a href="{{ info.model_card.md }}" target="_blank"> View Markdown Card</a>
        </div>
        {% endfor %}
    </div>
</body>
</html>
""")

    html = template.render(results=results)
    report_path = f"{outdir}/model_evaluation_report.html"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(html)
    return report_path
