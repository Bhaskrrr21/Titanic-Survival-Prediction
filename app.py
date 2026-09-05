import streamlit as st
import pandas as pd
import joblib

# ---------------- Page Configuration ----------------

st.set_page_config(
    page_title="Titanic Survival Predictor",
    page_icon="🚢",
    layout="wide"
)

# ---------------- Load Model ----------------

from pathlib import Path

MODEL_PATH = Path(__file__).parent / "Model" / "titanic_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
except Exception as exc:
    st.error(
        "The model could not be loaded. Please install the exact packages "
        "from requirements.txt and restart the app."
    )
    st.exception(exc)
    st.stop()

# ---------------- Sidebar ----------------

st.sidebar.title("🚢 Titanic Survival Predictor")

st.sidebar.info(
    """
This application predicts whether a passenger would survive the Titanic disaster using a Machine Learning model.
"""
)

st.sidebar.markdown("---")

st.sidebar.markdown("""
### 📊 Model Information

- **Algorithm:** Random Forest Classifier
- **Dataset:** Kaggle Titanic
- **Framework:** Streamlit
- **Language:** Python
""")

# ---------------- Main Title ----------------

st.title("🚢 Titanic Survival Predictor")

st.write("Fill in the passenger details below and click **Predict Survival**.")

# ---------------- Project Information ----------------

with st.expander("📖 Project Information"):

    st.write("""
This project predicts whether a passenger would survive the Titanic disaster.

### Workflow

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Data Preprocessing
- Random Forest Model
- Hyperparameter Tuning
- Model Evaluation
- Streamlit Deployment
""")

# ---------------- Input Section ----------------

col1, col2 = st.columns(2)

with col1:

    pclass = st.selectbox(
        "🎟 Passenger Class",
        [1, 2, 3]
    )

    sex = st.selectbox(
        "👤 Gender",
        ["male", "female"]
    )

    age = st.slider(
        "🎂 Age",
        0,
        80,
        25
    )

    embarked = st.selectbox(
        "🚢 Embarked",
        ["S", "C", "Q"]
    )

with col2:

    fare = st.number_input(
        "💰 Fare",
        min_value=0.0,
        value=32.0
    )

    family_size = st.slider(
        "👨‍👩‍👧 Family Size",
        1,
        10,
        1
    )

    title = st.selectbox(
        "🪪 Title",
        ["Mr", "Mrs", "Miss", "Master", "Rare"]
    )

# ---------------- Create DataFrame ----------------

# The trained model expects IsAlone as a feature.
is_alone = 1 if family_size == 1 else 0

input_df = pd.DataFrame({
    "Pclass": [pclass],
    "Sex": [sex],
    "Age": [age],
    "Fare": [fare],
    "Embarked": [embarked],
    "FamilySize": [family_size],
    "IsAlone": [is_alone],
    "Title": [title]
})

# ---------------- Prediction ----------------

if st.button("🔍 Predict Survival", width="stretch"):

    st.subheader("📋 Passenger Details")

    st.dataframe(input_df, width="stretch")

    prediction = model.predict(input_df)

    probability = model.predict_proba(input_df)

    st.subheader("🎯 Prediction Result")

    if prediction[0] == 1:
        st.success("🎉 Passenger is likely to survive!")
        st.balloons()
    else:
        st.error("❌ Passenger is unlikely to survive.")

    survival_probability = probability[0][1] * 100
    death_probability = probability[0][0] * 100

    col3, col4 = st.columns(2)

    with col3:
        st.metric(
            "✅ Survival Probability",
            f"{survival_probability:.2f}%"
        )

    with col4:
        st.metric(
            "❌ Death Probability",
            f"{death_probability:.2f}%"
        )

    confidence = max(probability[0]) * 100

    st.metric(
        "📈 Model Confidence",
        f"{confidence:.2f}%"
    )

    st.progress(float(probability[0][1]))

    chart_df = pd.DataFrame({
        "Outcome": ["Survive", "Not Survive"],
        "Probability": [
            probability[0][1],
            probability[0][0]
        ]
    })

    st.subheader("📊 Prediction Chart")

    st.bar_chart(chart_df.set_index("Outcome"))

# ---------------- Footer ----------------

st.markdown("---")

st.caption(
    "🚀 Developed by Bhaskar Choudhary | Titanic Survival Prediction using Machine Learning"
)