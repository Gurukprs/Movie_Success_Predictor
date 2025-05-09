from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model and features
model = joblib.load('movie_success_model.pkl')
feature_columns = joblib.load('feature_columns.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        # Collect form inputs
        form_data = request.form.to_dict()
        input_data = {}

        # Basic numeric inputs
        input_data['budget'] = float(form_data.get('budget', 0))
        input_data['duration'] = int(form_data.get('duration', 0))
        input_data['title_year'] = int(form_data.get('title_year', 0))
        input_data['cast_size'] = int(form_data.get('cast_size', 0))
        input_data['director_fame'] = float(form_data.get('director_fame', 0))

        # Genre (one-hot)
        selected_genre = form_data.get('genre')
        for genre in [col for col in feature_columns if col.startswith('genre_')]:
            input_data[genre] = 1 if genre == f'genre_{selected_genre}' else 0

        # Fill in missing columns
        for col in feature_columns:
            if col not in input_data:
                input_data[col] = 0

        # Predict
        df_input = pd.DataFrame([input_data])[feature_columns]
        result = model.predict(df_input)[0]
        prediction = "Hit" if result == 1 else "Flop"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
