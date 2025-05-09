import joblib
import pandas as pd

# Step 1: Load the trained model and feature columns
model = joblib.load('movie_success_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

# Step 2: Create a sample movie input (you can get this from user input or a form)
# NOTE: Ensure this dict has only the features used in training
input_data = {
    'budget': 150000000,
    'duration': 130,
    'title_year': 2025,
    'cast_size': 3,
    'director_fame': 7.5,
    # genre columns — make sure to match all one-hot encoded genres used
    'genre_Action': 1,
    'genre_Comedy': 0,
    'genre_Drama': 0,
    'genre_Horror': 0,
    'genre_Adventure': 0,
    'genre_Romance': 0,
    'genre_Thriller': 0,
    'genre_Biography': 0,
    'genre_Crime': 0,
    'genre_Animation': 0,
    'genre_Fantasy': 0,
    'genre_Mystery': 0,
    'genre_Sci-Fi': 0,
    'genre_Musical': 0,
    'genre_War': 0,
    'genre_Western': 0,
    'genre_History': 0,
    'genre_Sport': 0,
    'genre_Music': 0,
    'genre_Film-Noir': 0,
    'genre_Family': 0,
    'genre_Documentary': 0,
    'genre_News': 0
}

# Step 3: Ensure all expected features are present
for col in feature_columns:
    if col not in input_data:
        input_data[col] = 0

# Step 4: Prepare the DataFrame in correct column order
X_input = pd.DataFrame([input_data])[feature_columns]

# Step 5: Predict
prediction = model.predict(X_input)[0]
label = "Hit" if prediction == 1 else "Flop"
print(f"Prediction: {label}")
