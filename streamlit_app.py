import streamlit as st
import joblib
import pandas as pd

# Load model and feature list
model = joblib.load("movie_success_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

# UI layout
st.set_page_config(page_title="🎬 Movie Success Predictor", layout="centered")
st.title("🎬 Movie Success Predictor")

# User input
budget = st.number_input("💰 Budget (USD)", min_value=0)
duration = st.number_input("🎞️ Duration (minutes)", min_value=0)
year = st.number_input("📅 Release Year", min_value=2000)
cast_size = st.number_input("👥 Cast Size", min_value=1)
director_fame = st.slider("⭐ Director Fame (0–10)", 0.0, 10.0, 5.0)

genres = [
    "Action", "Comedy", "Drama", "Horror", "Adventure", "Romance", "Thriller",
    "Biography", "Crime", "Animation", "Fantasy", "Mystery", "Sci-Fi", "Musical",
    "War", "Western", "History", "Sport", "Music", "Film-Noir", "Family",
    "Documentary", "News"
]
genre = st.selectbox("🎭 Genre", genres)

# When user clicks Predict
if st.button("🔮 Predict"):
    # Construct input
    input_data = {
        "budget": budget,
        "duration": duration,
        "title_year": year,
        "cast_size": cast_size,
        "director_fame": director_fame,
    }
    for g in ["genre_" + g for g in genres]:
        input_data[g] = 1 if g == f"genre_{genre}" else 0

    # Ensure all features are present
    for col in feature_columns:
        if col not in input_data:
            input_data[col] = 0

    # Predict
    df = pd.DataFrame([input_data])[feature_columns]
    pred = model.predict(df)[0]
    label = "🎯 Hit" if pred == 1 else "❌ Flop"

    st.success(f"Prediction: {label}")
