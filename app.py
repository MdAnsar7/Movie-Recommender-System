import requests
import streamlit as st
import pickle



def fetch_poster(movie_ids):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_ids)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list_func = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommended_movies_posters = []

    for i in movies_list_func:
        movie_id = movies.iloc[i[0]].movie_id

        recommend_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommend_movies, recommended_movies_posters


movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Choose What Kind Of Recommendation You Want',
    movies_list)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.markdown(names[0])
        st.image(posters[0])

    with col2:
        st.markdown(names[1])
        st.image(posters[1])

    with col3:
        st.markdown(names[2])
        st.image(posters[2])

    with col4:
        st.markdown(names[3])
        st.image(posters[3])

    with col5:
        st.markdown(names[4])
        st.image(posters[4])