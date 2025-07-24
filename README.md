# NLP-Based Movie Recommendation System

## 🎬 Overview
This project implements a content-based movie recommendation system using Natural Language Processing (NLP) techniques. The system analyzes movie metadata (titles, descriptions, genres) to suggest similar movies based on textual similarity.

## 🔍 Features
- Content-based recommendation using movie descriptions
- Multiple NLP techniques implemented:
  - Bag-of-Words (BoW)
  - TF-IDF Vectorization
  - Cosine similarity for recommendations
- Clean and intuitive command-line interface
- Scalable architecture to handle large datasets

## 🛠️ Technologies Used
- Python 3.x
- Scikit-learn (for vectorization and similarity calculations)
- NLTK (for text preprocessing)
- Pandas (for data handling)
- Optional: Streamlit for web interface

## 📂 Dataset
The system uses the [TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata) which contains:
- 5000+ movie entries
- Metadata including titles, overviews, genres, keywords
- Additional information like cast, crew, ratings

## ⚙️ Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/movie-recommender-nlp.git
cd movie-recommender-nlp
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
```

## 🚀 Usage
1. Run the recommendation system:
```python
python recommend.py
```

2. Enter a movie title when prompted:
```
Enter a movie title: The Dark Knight
```

3. View recommendations:
```
Top 5 similar movies:
1. Batman Begins (2005)
2. The Dark Knight Rises (2012)
3. Batman (1989)
4. Batman Returns (1992)
5. Batman Forever (1995)
```

## 🧠 Methodology
1. **Text Preprocessing**:
   - Lowercasing
   - Tokenization
   - Stopword removal
   - Stemming/Lemmatization

2. **Feature Extraction**:
   - Bag-of-Words representation
   - TF-IDF vectorization
   - Genre one-hot encoding

3. **Similarity Calculation**:
   - Cosine similarity between movie vectors
   - Combined similarity score from multiple features

## 📊 Performance
The system was evaluated using:
- Precision@K metric
- User satisfaction surveys
- Comparison with baseline popularity-based recommender

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements.

📧 Contact
For questions or suggestions, please contact:  
Shivam Pandey - pandeyshivam7031@gmail.com
