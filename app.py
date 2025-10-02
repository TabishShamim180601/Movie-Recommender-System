import streamlit as st 
import pickle
import pandas as pd
import requests

api_key = st.secrets["TMDB_API_KEY"]

#for getting poster
def get_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/"+str(movie_id)+"?api_key="+str(api_key))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(movie):
    #getting index of movie 
    movie_index = movies[movies['title'].str.lower() == movie.lower()].index[0]
    #getting similarity score with each movie
    similarities = similarity[movie_index]
    #getting 5 most similar movies 
    movies_list = sorted(list(enumerate(similarities)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_posters=[]

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(get_poster(movie_id))
    
    return recommended_movies,recommended_movies_posters


st.title('Movie Recommender System')

movies_dict = pickle.load(open('movies.p','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.p','rb'))

selected_movie_name = st.selectbox('Select a movie',movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

