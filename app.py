import pickle  # Load saved movie data
import streamlit as st  # Streamlit for UI
import requests  # Fetch movie posters
import os  # For environment variables
# Set page title and icon
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
# Apply custom CSS for styling (Font, Colors, Buttons, Layout)
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
    body {
        background-color: #121212; /* Dark mode background */
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    h1 {
        font-size: 45px;
        font-weight: 600;
        color: #FFD700; /* Gold color */
        text-align: center;
        text-shadow: 2px 2px 10px rgba(255, 215, 0, 0.7);
    }
    h4 {
        font-size: 22px;
        color: #EAEAEA; /* Light grey */
        text-align: center;
    }
    h5 {
        font-size: 18px;
        font-weight: 400;
        color: #FFA500; /* Orange */
        text-align: center;
    }
    .stButton > button {
        background: linear-gradient(90deg, #FF8C00, #FF4500);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 12px;
        transition: 0.3s;
        border: none;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #FF4500, #FF0000);
        transform: scale(1.05);
    }
    .stSelectbox {
        font-size: 18px !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Constants
NUM_RECOMMENDATIONS = 10
# Function to fetch the poster of a movie using The Movie Database (TMDb) API
def fetch_poster(movie_id):
    api_key = os.getenv('TMDB_API_KEY')  # Fetch API key from environment variable
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()
        poster_path = data.get('poster_path')
        return f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else "https://via.placeholder.com/500x750?text=No+Image"
    except requests.exceptions.RequestException:
        return "https://via.placeholder.com/500x750?text=Error"
# Function to recommend movies
def recommend(movie):
    if movie not in movie_titles_set:
        return [], []
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)
    movie_names = []
    movie_posters = []
    for i in distances[1:NUM_RECOMMENDATIONS + 1]:  # Avoid index errors
        movie_names.append(movies.iloc[i[0]].title)
        movie_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))
    return movie_names, movie_posters
# Streamlit App Header
st.markdown("<h1>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<h4>Find movies similar to your favorite ones! 🍿</h4>", unsafe_allow_html=True)
# Load model data
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
# Create a set for faster movie title lookups
movie_titles_set = set(movies['title'].values)
# Dropdown to select movie
selected_movie = st.selectbox("🎥 Choose a Movie", movies['title'].values, index=0)
# Show recommendations
if st.button("🔍 Show Recommendations"):
    names, posters = recommend(selected_movie)
    if names:
        st.markdown("<h3 style='text-align: center; color: #FFD700;'>Recommended Movies:</h3>", unsafe_allow_html=True)
        cols = st.columns(10)  # Create 10 columns for movie posters
        for col, name, poster in zip(cols, names, posters):
            with col:
                st.image(poster, use_container_width=True)  # ✅ Fixed parameter
                st.markdown(f"<h5>{name}</h5>", unsafe_allow_html=True)  # Display movie name
    else:
        st.error("🚨 No recommendations found. Please try another movie.")