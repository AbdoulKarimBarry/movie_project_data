# %%
from database import SessionLocal
import query_helpers as query_helpers

# Créer une session
db = SessionLocal()

# %%
# Tester la récupération de films
movies = query_helpers.get_movies(db, limit=5, genre="Comedy")
movie = query_helpers.get_movie(db, 1)

print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")
print("--------------------------------")

for movie in movies:
    print(f"ID: {movie.movieId}, Titre: {movie.title}, Genres: {movie.genres}")

# %%
# Fermer la session
db.close()