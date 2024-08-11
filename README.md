# Recommendation-System
Overview
This project implements a movie recommender system using machine learning techniques. The system provides movie recommendations based on user input using a cosine similarity-based approach. It utilizes movie metadata and credits to generate accurate recommendations.
Features
Movie Selection: Users can select a movie from a dropdown menu.
Recommendations: Get a list of recommended movies with posters.
Movie Posters: Displayed alongside the movie titles for visual appeal.
Technologies Used
Python: Programming language used for development.
Streamlit: Framework for creating interactive web applications.
Pandas: Data manipulation and analysis.
Scikit-learn: For machine learning models and similarity computation.
Requests: For fetching movie posters from the TMDb API.
Data
The system uses the following datasets:

TMDb 5000 Movies Dataset: This dataset includes movie metadata such as genres, keywords, cast, and crew, which are used to build the recommendation model.

TMDb 5000 Credits Dataset: Contains additional movie credit information, which is merged with the movies dataset to enhance recommendation accuracy.

Dataset Source: Both datasets can be found on Kaggle:

TMDb 5000 Movies Dataset
TMDb 5000 Credits Dataset
Usage
Place the datasets (movies.pkl, similarity.pkl) in the project directory.

Run the Streamlit app:

bash
Copy code
streamlit run app.py
Open your web browser and navigate to http://localhost:8501 to interact with the recommender system.

