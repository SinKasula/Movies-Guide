import webbrowser
class Movie():
    """Class to define Object - Movie"""
    def __init__(self, movie_title, movie_storyLine, movie_poster_ImageUrl, movie_youtube_Trailer_url):
        self.title = movie_title
        self.storyLine = movie_storyLine
        self.poster_image_url = movie_poster_ImageUrl
        self.trailer_youtube_url = movie_youtube_Trailer_url
    def show_trailer(self):
        url_link = webbrowser.open(self.trailer_youtube_url)




