import streamlit as st
import queries 
from PIL import Image

img = Image.open('filmm.png')
st.image(img)

def main():
    st.title("Movie Search Application")
    menu = ["Keyword search", "Search by year", "Search by genre", "Search by imdb.rating", "Most popular queries"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Keyword search":
        st.subheader("Keyword search")
        keyword = st.text_input("Enter a keyword:")
        if st.button("Search"):
            queries.update_search_queries(keyword)
            movies = queries.search_movies_by_keyword(keyword)
            if not movies:
                st.error("Invalid choice. No movies found. Please, try again.",icon =":material/cruelty_free:")
            else:
                for movie in movies:
                        st.markdown(f"Title : {movie[1]}")
                        st.markdown(f"Rating : {movie[6]}")
                        st.markdown(f"Year : {movie[5]}")
                        st.markdown(f"Plot : {movie[2]}")
                        st.markdown(f"Awards : {movie[8]}")
                        st.markdown("***")
                       

    elif choice == "Search by year":
        st.subheader("Search by year")
        year = st.text_input("Enter a year from 2007-2015:")
        if st.button("Search"):
            queries.update_search_queries(year)
            movies = queries.search_movies_by_year(int(year))
            if not movies:
                st.error("Invalid year. Please enter a year between 2007 and 2015.",icon =":material/cruelty_free:")
            else:
                for movie in movies:
                        st.markdown(f"Title : {movie[1]}")
                        st.markdown(f"Rating : {movie[6]}")
                        st.markdown(f"Year : {movie[5]}")
                        st.markdown(f"Plot : {movie[2]}")
                        st.markdown(f"Awards : {movie[8]}")
                        st.markdown("***")

                
    elif choice == "Search by genre":
        st.subheader("Search by genre")
        genre = st.text_input("Enter a genre: action * adventure * animation * biography * comedy * crime * documentary * drama * family * fantasy * history * horror * music * musical * mystery * romance * sci-fi * short * sport * thriller * war * western ")
        if st.button("Search"):
            queries.update_search_queries(genre)
            movies = queries.search_movies_by_genre(genre)
            if not movies:
                st.error("Please enter the selected genre from the keyboard,make sure you use Latin letters & try again.",icon =":material/heart_broken:")
            else:
                for movie in movies:
                        st.markdown(f"Title : {movie[1]}")
                        st.markdown(f"Rating : {movie[6]}")
                        st.markdown(f"Year : {movie[5]}")
                        st.markdown(f"Plot : {movie[2]}")
                        st.markdown(f"Awards : {movie[8]}")
                        st.markdown("***")
  

    elif choice == "Search by imdb.rating":
        st.subheader("Search by imdb.rating")
        rating = st.text_input("Enter a minimum imdb.rating:")
        if st.button("Search"):
            queries.update_search_queries(rating)
            movies = queries.search_movies_by_rating(float(rating))
            if not movies:
                st.error("Invalid imdb.rating. Please enter a rating between 0 and 10.",icon =":material/cruelty_free:")
            else:
                for movie in movies:
                        st.markdown(f"Title : {movie[1]}")
                        st.markdown(f"Rating : {movie[6]}")
                        st.markdown(f"Year : {movie[5]}")
                        st.markdown(f"Plot : {movie[2]}")
                        st.markdown(f"Awards : {movie[8]}")
                        st.markdown("***")

               
    elif choice == "Most popular queries":
        st.subheader("Most popular queries")
        popular_queries = queries.get_popular_queries()
        for query, count in popular_queries:
            st.write(f"{query} - {count} searches")

if __name__ == '__main__':
    main()
