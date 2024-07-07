import mysql.connector
import re

config = {
    'host':'******',
    'user': '****',
    'password': '************',
    'database': 'imdb'
}

def search_movies_by_keyword(keyword):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies_normalized WHERE title LIKE %s OR plot LIKE %s LIMIT 10", (f"%{keyword}%", f"%{keyword}%"))
    movies = cursor.fetchall()

    cursor.close()
    conn.close()

    return movies

def search_movies_by_year(year):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies_normalized WHERE year = %s LIMIT 10", (year,))
    movies = cursor.fetchall()

    cursor.close()
    conn.close()

    return movies

def search_movies_by_genre(genre):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies_normalized JOIN movie_genres ON movies_normalized.id = movie_genres.movie_id JOIN genres ON genres.id = movie_genres.genre_id WHERE genres.name = %s LIMIT 10", (genre,))
    movies = cursor.fetchall()

    cursor.close()
    conn.close()

    return movies

def search_movies_by_rating(rating):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM movies_normalized WHERE imdb_rating >= %s LIMIT 10", (rating,))
    movies = cursor.fetchall()

    cursor.close()
    conn.close()

    return movies

def get_popular_queries():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute("SELECT query_text,search_count FROM search_queries  ORDER BY search_count DESC LIMIT 10")
    queries = cursor.fetchall()

    cursor.close()
    conn.close()

    return queries

def update_search_queries(query):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM search_queries WHERE query_text = %s", (query,))
    search_result = cursor.fetchone()

    if search_result:
        cursor.execute("UPDATE search_queries SET search_count = search_count + 1 WHERE query_text = %s", (query,))
    else:
        cursor.execute("INSERT INTO search_queries (query_text) VALUES (%s)", (query,))

    conn.commit()
    cursor.close()
    conn.close()
