emotion_to_genre = {
    # Core emotions from research papers
    "joy": ["Comedy", "Musical", "Animation", "Family"],
    "sadness": ["Drama", "Romance", "War", "Historical"],
    "fear": ["Horror", "Thriller", "Psychological", "Crime"],
    "disgust": ["Psychological", "Horror", "True Crime"],
    "anger": ["Action", "Crime", "War", "Revenge"],
    "surprise": ["Mystery", "Suspense", "Twist Ending"],

    # Complex emotional states
    "excitement": ["Action", "Adventure", "Sci-Fi", "Sports"],
    "calm": ["Documentary", "Nature", "Art Film", "Slow Cinema"],
    "nostalgia": ["Classic Cinema", "Period Drama", "Biographical"],

    # Emotion combinations from Grenze research
    "high_intensity_fear": ["Found Footage Horror", "Extreme Horror"],
    "fear+surprise": ["Psychological Thriller", "Mind-Bender"],
    "anger+disgust": ["Crime Drama", "Film Noir"],

    # Positive social emotions
    "love": ["Rom-Com", "Period Romance", "Young Adult"],
    "hope": ["Inspirational Drama", "Faith-Based", "Coming-of-Age"],

    # Meta-emotions from Frontiers study
    "aesthetic_sadness": ["Art House Drama", "Poetic Realism"],
    "controlled_fear": ["Suspense", "Heist Films"]
}

# Add confidence-weighted fusion
def fuse_modalities(text_emotion, text_confidence, img_emotion, img_confidence):
    if img_confidence > 0.7 and img_confidence > text_confidence:
        return img_emotion
    else:
        return text_emotion



from sklearn.metrics.pairwise import cosine_similarity

def recommend_movies(emotion, user_id=None):
    # Content-based filtering
    genres = emotion_to_genre.get(emotion, ["Drama"])  # Default genre
    candidates = movies[movies["genres"].str.contains("|".join(genres))]

    # Collaborative filtering (if user data exists)
    if user_id:
        user_ratings = ratings[ratings["userId"] == user_id]
        # Add logic to find similar users

    return candidates.sample(5)  # Return 5 random movies
