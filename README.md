# 🎥 Movie Recommender System

This project is a Movie Recommender System built using Python and Streamlit. It provides personalized movie recommendations based on a content-based filtering approach.

## 🚀 Features
- **Content-Based Recommendations**: Suggests movies similar to the one selected by the user.
- **Interactive User Interface**: Built with Streamlit for a seamless and intuitive experience.
- **Top 5 Recommendations**: Displays the top 5 most similar movies in a numbered list.

## 🛠️ How It Works
1. **Data Loading**: Preprocessed movie data and similarity matrix are loaded using pickle.
   - Link to files: [Google Drive](https://drive.google.com/drive/folders/16sP3OJV5JXhQ0B_Nh-Knt6rk0ziW7ABl?usp=sharing)
2. **Recommendation Logic**:
   - The `recommend()` function calculates the similarity of the selected movie with all other movies using a cosine similarity matrix.
   - Returns the top 5 most similar movies.
3. **Streamlit UI**:
   - Users select a movie from a dropdown menu.
   - Upon clicking the "Recommend" button, the app displays the top 5 recommended movies in a numbered format.

## 📦 Dependencies
- Streamlit: For building the interactive web app.
- Pandas: For handling movie data.
- Pickle: For loading preprocessed data and similarity matrix.

## 📈 Future Enhancements
- Add collaborative filtering for better recommendations.
- Deploy the app on a cloud platform for public access.
- Improve the UI for a more engaging user experience.

## 🌟 Star the Repository!
 - If you like this project, don't forget to give it a ⭐ on GitHub!

## 🖥️ How to Run
```sh
# Clone the repository
git clone https://github.com/piyush814325/Movie-recommendation-system.git
cd movie-recommender-system

# Install dependencies
pip install streamlit pandas

# Run the Streamlit app
streamlit run app.py

