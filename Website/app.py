# import streamlit as st
# import pandas as pd
# import pickle
# import requests

# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=1c78377146ea8ea690b37f728fb4b6e5&language=en-US'.format(movie_id))
#     data = response.json()
#     return 'https://image.tmdb.org/t/p/w500/' + data['poster_path'] 


# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distance = similarity[movie_index]
#     movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
#     recommended_movies = []
#     recommended_movies_posters = []
#     for i in movie_list:
#         movie_id = movies.iloc[i[0]].movie_id
#         recommended_movies.append(movies.iloc[i[0]].title)
#         recommended_movies_posters.append(fetch_poster(movie_id))
#     return recommended_movies, recommended_movies_posters

# movies_dict = pickle.load(open('movies.pkl','rb'))
# movies = pd.DataFrame(movies_dict)

# similarity = pickle.load(open('similarity.pkl','rb'))

# st.title('Movie Recommendation System')

# selected_movie_name = st.selectbox(
#     'Which movie do you like best?',
#     (movies['title'].values))

# if st.button('Recommend'):
#     st.write('You should also watch:')
#     names, posters = recommend(selected_movie_name)
    
#     columns = st.columns(5)
#     for i, col in enumerate(columns):
#         col.markdown(
#             f"""
#             <div style="text-align: center; line-height: 1.2;">
#                 <div style="min-height: 60px; margin-bottom: 10px;"> <!-- Adjust min-height as needed -->
#                     <h6 style="margin: 0; overflow: hidden; text-overflow: ellipsis;">{names[i]}</h6>
#                 </div>
#                 <img src="{posters[i]}" style="width: 100%; height: 200px; display: block; margin: auto;">
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )
#     # col1, col2, col3, col4, col5 = st.columns(5)

#     # with col1:
#     #     st.header(names[0])
#     #     st.image(posters[0])
#     # with col2:
#     #     st.header(names[1])
#     #     st.image(posters[1])
#     # with col3:
#     #     st.header(names[2])
#     #     st.image(posters[2])
#     # with col4:
#     #     st.header(names[3])
#     #     st.image(posters[3])
#     # with col5:
#     #     st.header(names[4])
#     #     st.image(posters[4])
    
    

import streamlit as st
import pandas as pd
import pickle
import requests

# Fetch movie poster function
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=1c78377146ea8ea690b37f728fb4b6e5&language=en-US')
    data = response.json()
    return f'https://image.tmdb.org/t/p/w500/{data["poster_path"]}'

# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_posters

# Load data
movies_dict = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Page Configuration
st.set_page_config(page_title="Movie Recommendation System", layout="wide")

# Initialize variables
names = []
posters = []

# Sidebar for movie selection
st.sidebar.title("🎬 Movie Recommendation System")
selected_movie_name = st.sidebar.selectbox('Choose your favorite movie:', movies['title'].values)
st.sidebar.markdown("**Discover similar movies based on your selection!**")

if st.sidebar.button('Recommend'):
    st.markdown("<h2 style='text-align: center;'>🎥 Recommended Movies 🎥</h2>", unsafe_allow_html=True)
    names, posters = recommend(selected_movie_name)

# Display recommendations if available
if names and posters:
    for i in range(0, len(names), 3):  # Display in rows of 3
        cols = st.columns(3)
        for j, col in enumerate(cols):
            if i + j < len(names):
                col.markdown(
                    f"""
                    <div style="text-align: center; margin: 10px;">
                        <img src="{posters[i+j]}" 
                             style="width: 80%; height: auto; border-radius: 10px; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);">
                        <h4 style="margin-top: 10px; margin-bottom: 10px; font-size: 20px; font-weight: bold;">{names[i+j]}</h4>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

# Footer
st.markdown(
    "<hr style='border-top: 2px solid #ccc;'>",
    unsafe_allow_html=True
)