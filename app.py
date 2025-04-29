import streamlit as st
import pickle
import pandas as pd
import gzip  # Import gzip for reading compressed files

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# Load compressed files
with gzip.open('movies_dict_compressed.pkl.gz', 'rb') as f:
    movies_dict = pickle.load(f)

movies = pd.DataFrame(movies_dict)

with gzip.open('similarity_compressed.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

st.title("Movie Recommender System")
selected_movie = st.selectbox("Select an option", movies['title'].values)

if st.button('Recommend'):
    names = recommend(selected_movie)
    count = 0
    for i in names:
        count += 1
        st.write(f"{count} {i}")



