movies = {
    "Inception": ["Sci-Fi", "Action", "Thriller"],
    "Interstellar": ["Sci-Fi", "Drama"],
    "The Dark Knight": ["Action", "Crime", "Drama"],
    "Titanic": ["Romance", "Drama"],
    "Avengers": ["Action", "Adventure", "Sci-Fi"],
    "Toy Story": ["Animation", "Comedy", "Family"]
}

print("Movie Recommendation System")
print("---------------------------")

movie = input("Enter a movie name: ")

if movie in movies:
    genres = movies[movie]

    print("\nMovies you may like:")

    found = False

    for name, movie_genres in movies.items():
        if name != movie and any(genre in movie_genres for genre in genres):
            print("-", name)
            found = True

    if not found:
        print("No similar movies found.")

else:
    print("Movie not found in the database.")