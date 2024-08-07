import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
import bz2file as bz2

def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = pickle.load(data)
    return data

def fetch_poster(movie_title):
    response = requests.get("http://www.omdbapi.com/?t={}&apikey=18744db8".format(movie_title))
    data = response.json()
    return data['Poster']


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_m_poster = []
    for j in movie_list:
        movie_title = movies_df.iloc[j[0]]['title']
        recommended_movies.append(movies_df.iloc[j[0]].title)
        recommended_m_poster.append(fetch_poster(movie_title))
    return recommended_movies, recommended_m_poster


movies_df = pd.read_pickle('movie.pkl')
similarity = decompress_pickle("similarity.pkl.bz2")
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