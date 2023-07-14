import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. 

# Define a filename parameter
f_name = "movies.txt"


class Movie:
    """ This class a representation of a movie
        As read from the file
    """
    def __init__(self, title, description):
        self.title = title
        self.description = description

def get_movies(fname):
    """ readfile method, read the file movies.txt.
        :param string fname: the file name
        :returns: list of movies

        :rtype: list
    """
    # create a list to stores all movies
    movies = []
    with open(fname) as f:
         # read all the movies from the file
         lines = f.readlines()
         for line in lines:
             movie_details = line.split(":")
             movie = Movie(movie_details[0].strip(), movie_details[1].strip())
             movies.append(movie)

    return movies


def recommend_movies(movie_description):
    """ recommend_movies, get the movie description and return a list of recommended movies.
        :param string movie_description: movie description
        :returns: list of movies

        :rtype: list
    """

    # define a similarity index for which any values greater or equal to it will be recommended.
    similarity_index = 0.80

    # list of movies to recommend
    movies_to_recommend = []

    # tokenise the movie to compare
    model_movie = nlp(movie_description)
    movies = get_movies(f_name)
    for movie in movies:
        similarity = nlp(movie.description).similarity(model_movie)
        print(movie.title + " _ ", similarity)
        if similarity > similarity_index:
            movies_to_recommend.append(movie.title)
    
    return movies_to_recommend

        

description = """Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

recommended = recommend_movies(description)
# Print the recommended movies
print("___________These are the recommended movies_____________")
for title in recommended:
    print(title)