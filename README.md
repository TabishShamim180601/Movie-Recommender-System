1. Content based recommender system that recommends 5 movies based on the input movie name provided by the user.
2. Utilised the "TMDB_5000 movies" (tmdb_5000_movies and tmdb_5000_credits) dataset.
3. The user chooses a movie present in the dataset. Then, the user is recommended 5 most similar movies from the dataset.
4. Used cosine similarity to find the similarity between movie vectors.
5. Used count vectorizer to convert the movies (along with tags) to vectors.
6. Tags comprise movie overview, genres, keywords, top 3 actors and director.  
