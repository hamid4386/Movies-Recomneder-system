import streamlit as st
import pandas as pd
import pickle
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]
    recommended_movies = []
    recommended_movie_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        movie_title = movies.iloc[i[0]].title
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movies.append(movie_title)
    return recommended_movies, recommended_movie_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')


selected_movi = st.selectbox(
    'Select a movie',
     movies['title'].values)

if st.button('Recommend'):
    st.subheader('Movies similar to ' + selected_movi)
    recommended_movies, recommended_movie_posters = recommend_movies(selected_movi)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(recommended_movie_posters[0])
        st.text(recommended_movies[0])
    with col2:
        st.image(recommended_movie_posters[1])
        st.text(recommended_movies[1])
    with col3:
        st.image(recommended_movie_posters[2])
        st.text(recommended_movies[2])
    with col4:
        st.image(recommended_movie_posters[3])
        st.text(recommended_movies[3])
    with col5:
        st.image(recommended_movie_posters[4])
        st.text(recommended_movies[4])
    col6, col7, col8, col9, col10 = st.columns(5)
    with col6:
        st.image(recommended_movie_posters[5])
        st.text(recommended_movies[5])
    with col7:
        st.image(recommended_movie_posters[6])
        st.text(recommended_movies[6])
    with col8:
        st.image(recommended_movie_posters[7])
        st.text(recommended_movies[7])
    with col9:
        st.image(recommended_movie_posters[8])
        st.text(recommended_movies[8])
    with col10:
        st.image(recommended_movie_posters[9])
        st.text(recommended_movies[9])
