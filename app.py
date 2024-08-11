import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=87afe65fb39fe7260a359ef325ae2c9b'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    recommended_movies_poster = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    
    return recommended_movies, recommended_movies_poster  # Return both names and posters

# Load the data
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

option = st.selectbox(
    'Select a movie:',
    movies['title'].values)

if st.button('Recommend'):
    st.write(f"Selected Movie: {option}")
    
    names, posters = recommend(option)
    
    # Display recommendations
    if names:
        col1, col2, col3, col4, col5 = st.columns(5)
        with col1:
            st.header(names[0])
            st.image(posters[0])
        with col2:
            st.header(names[1])
            st.image(posters[1])
        with col3:
            st.header(names[2])
            st.image(posters[2])
        with col4:
            st.header(names[3])
            st.image(posters[3])
        with col5:
            st.header(names[4])
            st.image(posters[4])
    else:
        st.write("No recommendations found.")
