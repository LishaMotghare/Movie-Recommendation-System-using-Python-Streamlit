
import streamlit as st
import pickle

movies = pickle.load(open("movie_list.pkl","rb"))
similarity = pickle.load(open("similarity.pkl","rb"))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommend_movies = []

    for i in movie_list:
        recommend_movies.append(movies.iloc[i[0]].title)

    return recommend_movies

st.set_page_config(page_title="Movie Recommendation System")

st.title("🎬 Movie Recommendation System")

selected_movie = st.selectbox(
    "Select Movie",
    movies['title'].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    for movie in recommendations:
        st.write("⭐", movie)
