import media
import revs_movie_week

"""This file includes all of the information for the movie tiles."""

title_int = "Interstellar"  # Movie's Title Name
tagline_int = "Go Further"  # Movie's tag line
poster_int = "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg"  # URL link to poster
trailer_int = "https://youtu.be/Lm8p5rlrSkY"  # URL to youtube.com trailer
duration_int = "2h 49m"  # Length of the movie
rating_int = "PG-13"  # Movie's MPAA Rating
interstellar = media.Movie(title_int,  # Creates a class object for the film
                           tagline_int,
                           poster_int,
                           trailer_int,
                           duration_int,
                           rating_int)

title_mad = "Mad Max Fury Road"
tagline_mad = "The Future Belongs to the Mad"
poster_mad = "https://upload.wikimedia.org/wikipedia/en/6/6e/Mad_Max_Fury_Road.jpg"
trailer_mad = "https://youtu.be/hEJnMQG9ev8"
duration_mad = "2h"
rating_mad = "PG-13"
mad_max = media.Movie(title_mad,
                      tagline_mad,
                      poster_mad,
                      trailer_mad,
                      duration_mad,
                      rating_mad)

title_t2 = "Terminator 2: Judgement Day"
tagline_t2 = "It's Nothing Personal."
poster_t2 = "https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg"
trailer_t2 = "https://youtu.be/7QXDPzx71jQ"
duration_t2 = "2h 36m"
rating_t2 = "R"
terminator2 = media.Movie(
                          title_t2,
                          tagline_t2,
                          poster_t2,
                          trailer_t2,
                          duration_t2,
                          rating_t2)

title_lego = "The Lego Movie"
tagline_lego = "The Story of a Nobody who Saved Everybody"
poster_lego = "https://upload.wikimedia.org/wikipedia/en/1/10/The_Lego_Movie_poster.jpg"
trailer_lego = "https://youtu.be/fZ_JOBCLF-I"
duration_lego = "1h 41m"
rating_lego = "PG"
lego_movie = media.Movie(
                         title_lego,
                         tagline_lego,
                         poster_lego,
                         trailer_lego,
                         duration_lego,
                         rating_lego)

title_tdk = "The Dark Knight"
tagline_tdk = "Welcome to a  World Without Rules"
poster_tdk = "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg"
trailer_tdk = "https://youtu.be/EXeTwQWrcwY"
duration_tdk = "2h 32m"
rating_tdk = "PG-13"
the_dark_knight = media.Movie(
                              title_tdk,
                              tagline_tdk,
                              poster_tdk,
                              trailer_tdk,
                              duration_tdk,
                              rating_tdk)

title_tm = "Transformers Movie"
tagline_tm = "Beyond Good, Beyond Evil, Beyond your Wildest Imagination."
poster_tm = "https://upload.wikimedia.org/wikipedia/en/9/91/Transformers-movieposter-west.jpg"
trailer_tm = "https://youtu.be/Sh3HW3mZAoQ"
duration_tm = "1h 30m"
rating_tm = "PG"
transformers_the_movie = media.Movie(
                                     title_tm,
                                     tagline_tm,
                                     poster_tm,
                                     trailer_tm,
                                     duration_tm,
                                     rating_tm)

movies = [interstellar,
          mad_max,
          terminator2,
          lego_movie,
          the_dark_knight,
          transformers_the_movie]

# Calls the function inside the .py file that creates the HTML and passes
# the movie instances.
revs_movie_week.open_movies_page(movies)
