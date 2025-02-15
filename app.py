import streamlit as st
import pickle
import pandas as pd
import numpy as np

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True,key = lambda x:x[1])[1:8]
    recommended = []
    for i in movies_list:
        movie_id = i[0]
        recommended.append(movies.iloc[i[0]].title)
    return recommended

movies = pd.read_feather("data.feather")

similarity = np.load("similarity.npy")

st.title("Movie Recommender System")
selected_movie_name = st.selectbox("Enter Movie name: ",movies['title'].values)
if st.button("Recommend"):
    recommendation = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)
    