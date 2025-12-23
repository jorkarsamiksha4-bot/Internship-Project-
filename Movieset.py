# Step 1: Movie dataset
movies = {
    "Avengers": "Action",
    "Titanic": "Romance",
    "Inception": "Sci-Fi",
    "Gladiator": "Action",
    "Notebook": "Romance"
}

# Step 2: Take user preference
user_preference = input("Enter your preferred genre (Action / Romance / Sci-Fi): ")

# Step 3: Recommendation
print("\nRecommended Movies:")
found = False

for movie, genre in movies.items():
    if genre.lower() == user_preference.lower():
        print(movie)
        found = True

if not found:
    print("No movies found for this genre.")