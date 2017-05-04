class Movie():
    """This class provides a way to store movie related information
    
    Attributes:
        title: A string that contains the name of the movie
        poster_image_url: A string that contains the url for the poster image of the movie
        trailer_youtube_url: A string that contains the url for the youtube trailer of the movie
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Initiatlizes Movie class with a title, poster_image_url, and trailer_youtube_url"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url