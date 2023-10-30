import streamlit as st
import pickle
import requests

movies_list = pickle.load(open('movie.pkl', 'rb'))
Projection = pickle.load(open('Projection.pkl', 'rb'))
movie_title = movies_list['title']
st.header('Movie Recommendation System')


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(selected_movie_title):
    movie_index = movies_list[movies_list['title'] == selected_movie_title].index[0]
    similarity = Projection[movie_index]
    movies_recommended = sorted(list(enumerate(similarity)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movie_poster = []
    recommended_movie_title = []
    for i in movies_recommended:
        recommended_movie_poster.append(fetch_poster(movies_list.iloc[i[0]].movie_id))
        recommended_movie_title.append(movies_list.iloc[i[0]].title)
    return recommended_movie_title, recommended_movie_poster


selected_movie = st.selectbox('How do you like to be connected', movie_title)

if st.button("Amaze Me"):
    st.write("I hope u like following movies,", selected_movie, "Fan")
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
