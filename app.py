from pathlib import Path
import joblib
import streamlit as st

st.set_page_config(page_title="Smart News Categorizer", page_icon="📰", layout="centered")
st.title("📰 Smart News Categorization System")
st.write("Paste a news-style article or discussion post to predict its topic.")

MODEL_PATH = Path("outputs/news_classifier.joblib")
if not MODEL_PATH.exists():
    MODEL_PATH = Path("news_classifier.joblib")

@st.cache_resource
def load_bundle(path):
    return joblib.load(path)

if not MODEL_PATH.exists():
    st.warning(
        "Model file not found. Run the notebook through the training and save-model cells, "
        "then place outputs/news_classifier.joblib in the app folder."
    )
    st.stop()

bundle = load_bundle(str(MODEL_PATH))
pipeline = bundle["pipeline"]
class_names = list(bundle["class_names"])
model_name = bundle.get("model_name", "Trained classifier")

st.caption(f"Loaded model: {model_name}")
article = st.text_area(
    "News text",
    height=220,
    placeholder="Paste the headline and article text here..."
)

if st.button("Classify article", type="primary", use_container_width=True):
    if len(article.strip().split()) < 5:
        st.error("Please enter at least five words for a more meaningful prediction.")
    else:
        prediction = int(pipeline.predict([article])[0])
        st.success(f"Predicted topic: **{class_names[prediction]}**")
        if hasattr(pipeline, "predict_proba"):
            probabilities = pipeline.predict_proba([article])[0]
            st.subheader("Class confidence scores")
            ranked = sorted(zip(class_names, probabilities), key=lambda x: x[1], reverse=True)[:5]
            st.bar_chart({label: float(score) for label, score in ranked})
            st.caption("Scores are model probabilities, not a guarantee that the label is correct.")
        elif hasattr(pipeline, "decision_function"):
            st.info("This model does not provide calibrated probabilities. Its decision score is not a probability.")

st.divider()
st.caption(
    "Educational prototype. The model uses the original 20 Newsgroups topic labels; "
    "it is not trained specifically on current journalism or the four categories "
    "Sports, Technology, Business and Politics."
)
