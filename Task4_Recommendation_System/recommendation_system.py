# CodSoft Internship - Task 4
# Movie Recommendation System
# Content-Based Filtering

import difflib

# Movie dataset
movies = {
    "Inception": {
        "genre": "Sci-Fi Thriller",
        "description": "A thief enters people's dreams to steal secrets."
    },
    "Interstellar": {
        "genre": "Sci-Fi Adventure",
        "description": "Astronauts travel through space to find a new home."
    },
    "The Dark Knight": {
        "genre": "Action Crime",
        "description": "A superhero fights crime and protects a city."
    },
    "Avengers": {
        "genre": "Action Sci-Fi",
        "description": "Superheroes unite to save the world."
    },
    "Titanic": {
        "genre": "Romance Drama",
        "description": "A romantic story aboard a famous ship."
    },
    "The Notebook": {
        "genre": "Romance Drama",
        "description": "A beautiful love story between two people."
    },
    "Jurassic Park": {
        "genre": "Sci-Fi Adventure",
        "description": "Scientists create a dinosaur theme park."
    },
    "Avatar": {
        "genre": "Sci-Fi Adventure",
        "description": "A human explores an alien world."
    },
    "Joker": {
        "genre": "Crime Drama",
        "description": "A man's life changes after facing society."
    },
    "Frozen": {
        "genre": "Animation Fantasy",
        "description": "Two sisters experience a magical adventure."
    }
}


def recommend_movies(movie_name):

    movie_name = movie_name.strip().title()

    # Check whether movie exists
    if movie_name not in movies:

        matches = difflib.get_close_matches(
            movie_name,
            movies.keys(),
            n=3,
            cutoff=0.4
        )

        print("\nMovie not found!")

        if matches:
            print("Did you mean:", ", ".join(matches))

        return

    selected_movie = movies[movie_name]

    selected_genres = set(
        selected_movie["genre"].lower().split()
    )

    recommendations = []

    for title, details in movies.items():

        if title == movie_name:
            continue

        other_genres = set(
            details["genre"].lower().split()
        )

        common_genres = selected_genres.intersection(
            other_genres
        )

        if common_genres:

            score = len(common_genres)

            recommendations.append(
                (title, details["genre"], score)
            )

    # Sort by similarity score
    recommendations.sort(
        key=lambda item: item[2],
        reverse=True
    )

    print("\n===================================")
    print("       RECOMMENDED MOVIES")
    print("===================================")

    if recommendations:

        for index, (title, genre, score) in enumerate(
            recommendations[:5], start=1
        ):
            print(f"{index}. {title} - {genre}")

    else:
        print("No similar movies found.")

    print("===================================")


def main():

    print("===================================")
    print("       MOVIE RECOMMENDATION AI")
    print("===================================")

    print("\nAvailable Movies:")

    for movie in movies:
        print("-", movie)

    while True:

        movie_name = input(
            "\nEnter a movie you like: "
        )

        recommend_movies(movie_name)

        choice = input(
            "\nDo you want another recommendation? (yes/no): "
        ).lower().strip()

        if choice != "yes":
            print("\nThank you for using Movie Recommendation AI!")
            break


if __name__ == "__main__":
    main()
