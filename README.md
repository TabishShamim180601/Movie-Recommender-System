1. Content based recommender system that recommends 5 movies based on the input movie name provided by the user.
2. Web App: https://movie-recommender-system-kx8jzktyer8rraerqunube.streamlit.app/
3. Utilised the "TMDB_5000 movies" (tmdb_5000_movies.csv and tmdb_5000_credits.csv) dataset.
4. The user chooses a movie present in the dataset. Then, the user is recommended 5 most similar movies from the dataset.
5. Used cosine similarity to find the similarity between movie vectors.
6. Used count vectorizer to convert the movies (along with tags) to vectors.
7. Tags comprise movie overview, genres, keywords, top 3 actors and director.  
