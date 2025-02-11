# **Movie Recommendation System**  
**Content-Based Movie Recommendation Engine**  

![GitHub](https://img.shields.io/badge/License-MIT-blue)  
![Python](https://img.shields.io/badge/Python-3.8%2B-green)  
![Machine Learning](https://img.shields.io/badge/ML-scikit--learn-yellow)  
![Web App](https://img.shields.io/badge/Web%20App-Streamlit-orange)  

---

## **Overview**  
The **Movie Recommendation System** is a content-based recommendation engine that suggests movies to users based on metadata such as **genres**, **cast**, **crew**, and **keywords**. Built using **cosine similarity** and powered by the **TMDB API**, this system provides personalized movie recommendations through an interactive web application.

---

## **Features**  
- **Content-Based Filtering**: Recommends movies based on similarity in metadata (genres, cast, crew, keywords).  
- **Interactive Web App**: Displays movie posters, titles, and recommendations in a user-friendly interface.  
- **Scalable**: Can be extended to include collaborative filtering or hybrid recommendation techniques.  
- **Real-Time Data**: Fetches movie data dynamically using the TMDB API.  

---

## **Technology Stack**  
- **Programming Language**: Python  
- **Machine Learning**: scikit-learn, cosine similarity  
- **Web Framework**: Streamlit  
- **APIs**: TMDB API  
- **Data Processing**: Pandas, NLTK  
- **Serialization**: Pickle  

---

## **Installation**  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/Jash-Pastagia/Movie_Recommendation_System.git  
   cd Movie_Recommendation_System
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt
3. Set up TMDB API:
   -Obtain a TMDB API key from TMDB.
   -Add the API key to config.py or set it as an environment variable.  
4. Run the application:  
   ```bash  
   streamlit run app.py

## **Usage**  
1. **Launch the Web App**:  
   - Run the app using the command above.  
   - Open the provided local URL in your browser.  

2. **Search for Movies**:  
   - Enter a movie title in the search bar.  
   - The system will display similar movies based on metadata.  

3. **Explore Recommendations**:  
   - Click on a movie poster to view details like title, overview, and release date.  

---

## **Dataset**  
The system uses the **TMDB 5000 Movie Dataset**, which includes:  
- **Movies Metadata**: Title, genres, cast, crew, keywords, overview, release date, etc.  
- **Credits Data**: Cast and crew information for each movie.  
