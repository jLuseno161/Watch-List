class Movie:
    '''
    Movie class to define Movie Objects
    '''

    def __init__(self, id, title, overview, poster, vote_average, vote_count):
        self.id = id
        self.title = title #name of movie
        self.overview = overview #short descripton
        self.poster = 'https://image.tmdb.org/t/p/w500/' + poster   #poster image for the movie
        self.vote_average = vote_average    #average ratings
        self.vote_count = vote_count    #how many people have rated this movie
