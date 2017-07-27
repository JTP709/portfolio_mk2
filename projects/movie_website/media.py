import webbrowser
"""This module is used to define the media Classes."""


class Movie():
    """This Class provides a way to store movie related information"""

    def __init__(self, movie_title,
                 movie_storyline,
                 poster_image,
                 trailer_youtube,
                 movie_duration,
                 movie_rating):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.duration = movie_duration
        self.rating = movie_rating

    def show_trailer(self):
        """This function opens web browser and loads the youtube trailer"""
        webbrowser.open(self.trailer_youtube_url)
