import queries

def greetings():
    print('Welcome to Movie Search')

def show_menu():
    print('Choose a number from the options provided:')
    print('1. Keyword search.')
    print('2. Search by year.')
    print('3. Search by genre.')
    print('4. Search by imdb.rating.')
    print('5. Most popular queries.')
    print('EXIT')
    return input('Your choice: ')

def main():
    greetings()
    while True:
        choice = show_menu()
        if choice == '1':
            query = input('Enter a keyword: ')
            queries.update_search_queries(query)
            movies = queries.search_movies_by_keyword(query)
            if not movies:
                print('No movies found. Please, try again.')
            else:
                for movie in movies:
                    print(f"\nTitle: {movie[1]}\nRating: {movie[6]}\nYear: {movie[5]}\nPlot: {movie[2]}\nAwards: {movie[8]}")
        elif choice == '2':
            query = input('Enter a year from 2007-2015: ')
            queries.update_search_queries(query)
            movies = queries.search_movies_by_year(int(query))
            if not movies:
                print('No movies found.Please enter a year between 2007 and 2015 & try again.')
            else:
                for movie in movies:
                    print(f"\nTitle: {movie[1]}\nRating: {movie[6]}\nYear: {movie[5]}\nPlot: {movie[2]}\nAwards: {movie[8]}")
        elif choice == '3':
            query = input('Enter a genre: action * adventure * animation * biography * comedy * crime * documentary * drama * family * fantasy * history * horror * music * musical * mystery * romance * sci-fi * short * sport * thriller * war * western\nMy choice: ')
            queries.update_search_queries(query)
            movies = queries.search_movies_by_genre(query)
            if not movies:
                print('No movies found for this genre. Please, try again.')
            else:
                for movie in movies:
                    print(f"\nTitle: {movie[1]}\nRating: {movie[6]}\nYear: {movie[5]}\nPlot: {movie[2]}\nAwards: {movie[8]}")
        elif choice == '4':
            query = input('Enter a minimum imdb.rating: ')
            queries.update_search_queries(query)
            movies = queries.search_movies_by_rating(float(query))
            if not movies:
                print('Invalid imdb.rating. Please enter a rating between 0 and 10 & try again.')
            else:
                for movie in movies:
                    print(f"\nTitle: {movie[1]}\nRating: {movie[6]}\nYear: {movie[5]}\nPlot: {movie[2]}\nAwards: {movie[8]}")
        elif choice == '5':
            popular_queries = queries.get_popular_queries()
            if not popular_queries:
                print('No popular queries found.')
            else:
                for query, count in popular_queries:
                    print(f"{query} - {count} searches")
        elif choice.upper() == 'EXIT':
            break
        else:
            print('Invalid choice. Please, try again.')

if __name__ == '__main__':
    main()
