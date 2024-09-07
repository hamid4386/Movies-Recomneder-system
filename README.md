# 🎥 Movie Recommender System

This is a web-based Movie Recommender System that helps users find movies similar to their favorite ones. It leverages machine learning and The Movie Database (TMDb) API to recommend top 10 similar movies and display their posters. The system uses cosine similarity to compare movies based on their features.

## 🛠 Features
- Select a movie from the dropdown list.
- Get the top 10 movie recommendations similar to your selected movie.
- View the poster of each recommended movie.
- Intuitive and easy-to-use interface powered by Streamlit.

## 🚀 How to Use

### Prerequisites
Make sure you have the following installed on your system:
- Python 3.11 or latests
- Streamlit
- Pandas
- Requests
- Pickle (for loading pre-saved data)

### Installation Steps
1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/movie-recommender-system.git
    cd movie-recommender-system
    ```

2. **Install the required libraries:**
    Run the following command to install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. **Obtain an API Key:**
    This project uses The Movie Database (TMDb) API to fetch movie posters. To use it, you need an API key. You can get one by signing up at [The Movie Database](https://www.themoviedb.org/).

4. **Set up your environment:**
    In the Python script, replace the `api_key` in the `fetch_poster` function with your own API key:
    ```python
    api_key = 'your_api_key_here'
    ```

5. **Run the application:**
    Run the following command to start the Streamlit app:
    ```bash
    streamlit run app.py
    ```

6. **Using the app:**
    - Select a movie from the dropdown list.
    - Click the "Recommend" button to see similar movies and their posters.

### Usage Example
After running the app, you will be greeted with a title and a dropdown list of movies. Once you select a movie and hit the "Recommend" button, the app will display the top 10 similar movies along with their posters, neatly arranged in a grid.

## 📦 Dataset
The dataset used for this recommender system includes movie titles and their similarity scores. The data is pre-processed and stored as a pickle file (`movie_dict.pkl`) to load faster within the app. The similarity matrix (`similarity.pkl`) contains pre-calculated similarity scores between movies.

## 🤖 How It Works
1. **Cosine Similarity:** The system uses a cosine similarity matrix to find how similar two movies are based on their features (e.g., genres, keywords, etc.).
2. **Poster Fetching:** Once similar movies are identified, the app fetches posters from TMDb using the movie's unique ID and displays them alongside the titles.

## 📈 Future Improvements
- **Enhanced Similarity:** Improve recommendations by incorporating more features such as ratings, user preferences, and genre-specific filtering.
- **UI Enhancements:** Add more interactive components like search, filters, and sorting options.
- **Custom Recommendations:** Allow users to select multiple favorite movies for personalized recommendations.

## 🛠 Built With
- **Streamlit:** For building the interactive web application.
- **Pandas:** For data manipulation.
- **Requests:** For fetching data from TMDb API.
- **Pickle:** For storing and loading pre-processed data.

## 🌟 Why It’s Helpful
This movie recommender system is useful for:
- Movie enthusiasts looking for recommendations similar to their favorite films.
- People who want to discover new movies based on their preferences.
- Learning about how recommender systems and content-based filtering work in practice.

## 🤝 Contributing
Contributions are welcome! If you find any bugs or want to add new features, feel free to submit a pull request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## 📧 Contact
If you have any questions, feel free to reach out at muhammadhamid4386@gmail.com.
