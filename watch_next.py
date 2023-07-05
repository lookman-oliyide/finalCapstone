# pylint: disable=invalid-name
# pylint: disable=line-too-long
'''Recommendation Engine'''
import spacy
nlp = spacy.load('en_core_web_md')

film_description = """Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, the Illuminati 
trick Hulk into a shuttle and launch him into space to a planet where
the Hulk can live in peace. Unfortunately, Hulk lands on the planet
Sakaar where he is sold into slavery and trained as a gladiator."""

watched = nlp(film_description)

films_ = []

with open('movies.txt', 'r', encoding='utf8') as films:
    # Apply the str.strip function to every film item in films
    for film in map(str.strip, films):
        # populate empty films_ list with film items
        films_.append(film)

def watch_next(watched_films):
    '''
    Function takes film description as argument and returns the 
    similarity score and film recommendations
    '''
    print(f"Based on your recently watched: {watched_films}\n")
    similarities = []
    for film_ in films_:
        film_ = nlp(film_)
        # compare the decription for watched film with each film in list
        similarities.append((film_.text, film_.similarity(watched_films)))
    # using dict comprehension to create a dict with similarity scores as values and text as keys
    similarites_dict = dict([(key, value) for key, value in similarities])

    # variable that stores largest similarity score
    max_similarity = max(similarites_dict, key=similarites_dict.get)
    # bracket notation using label to get value
    print(f"RECOMMENDED FILM: {max_similarity}\n\nSIMILARITY SCORE: {similarites_dict[max_similarity]}")
    # separator
    print('-'*75, '\n')

    # sorts in order of highest to lowest similarity scores
    print('WATCH NEXT:\n') # more recommendations
    for key, value in sorted(similarites_dict.items(), key=lambda x: x[1], reverse=True):
        print(f"{key}\nSimilarity score: {value}\n")

# call watch next function
watch_next(watched)
