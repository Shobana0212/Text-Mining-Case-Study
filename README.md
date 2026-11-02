# CSI4004 Smart News Categorization System

## Files
- `CSI4004_Smart_News_Categorization.ipynb`: end-to-end dataset loading, training, evaluation, visualizations, error analysis, and model export.
- `app.py`: Streamlit interface for interactive topic prediction.
- `requirements.txt`: Python dependencies.
- `CSI4004_Case_Study_Report.docx`: report draft following the supplied CSI4004 template.

## Run the notebook
1. Open the notebook in Google Colab or Jupyter.
2. Install dependencies with `pip install -r requirements.txt`.
3. Run cells from top to bottom. The first run requires internet access to download the 20 Newsgroups corpus.
4. Review the generated metrics and plots in the notebook and in the `outputs/` directory.
5. Copy `outputs/news_classifier.joblib` into the app folder (or keep the `outputs/` folder beside `app.py`).

## Run the application
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Dataset scope
The 20 Newsgroups dataset contains 18,846 discussion posts across 20 original newsgroup topics. It does not use the exact four labels Sports, Technology, Business, and Politics. This implementation keeps the 20 original categories to avoid unsupported label remapping. If the assignment specifically requires those four labels, change to a labeled news dataset such as AG News and document the dataset choice in the report.

## Reporting integrity
Model scores are not pre-filled because they must come from an actual run in your environment. Use the notebook's printed metrics, saved CSV files, and figures as the empirical results. Do not report expected or illustrative numbers as measured findings.
