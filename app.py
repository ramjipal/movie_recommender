import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image



def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=0a448fc5d37bcbd887f8d411ee5ffe65&language=en-US&external_source=imdb_id".format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500"+data['poster_path']


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_m_poster = []
    for j in movie_list:
        movie_id = movies_df.iloc[j[0]]['movie_id']
        print(movie_id)
        recommended_movies.append(movies_df.iloc[j[0]].title)
        recommended_m_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_m_poster


movies_df = pickle.load(open('movie.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_lst = movies_df['title'].values
st.title("Best Movie Recommender")

selected_movie = st.selectbox(
    'Select Movie',
    movies_lst)

if st.button('Recommend'):
    recommendations, recom_posters = recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
       st.text(recommendations[0])
       st.image(recom_posters[0])
    with col2:
       st.text(recommendations[1])
       st.image(recom_posters[1])
    with col3:
       st.text(recommendations[2])
       st.image(recom_posters[2])
    with col4:
       st.text(recommendations[3])
       st.image(recom_posters[3])
    with col5:
       st.text(recommendations[4])
       st.image(recom_posters[4])