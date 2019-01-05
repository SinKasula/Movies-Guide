import movies
import fresh_tomatoes

print(movies.Movie.__module__)
print(movies.Movie.__name__)
print(movies.Movie.__doc__)

divergent = movies.Movie("divergent",
                         "As each person enters adulthood-must choose a faction and commit to it for life",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Divergent.jpg/220px-Divergent.jpg",
                         "https://www.youtube.com/watch?v=zFBZM-eA1K0")

insurgent = movies.Movie("Insurgent",
                         "Divergent -Sequal",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/a/af/Insurgent_poster.jpg/220px-Insurgent_poster.jpg",
                         "https://www.youtube.com/watch?v=IR-l_TSjlEo")

allegiant = movies.Movie("Allegiant",
                         "Insurgent-Sequal",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/f/f8/Allegiantfilmposter.jpg/220px-Allegiantfilmposter.jpg",
                         "https://www.youtube.com/watch?v=0G0C-vMHcQY")

midnight_in_paris = movies.Movie("Midnight In Paris",
                          "One of my all time Favorites",
                          "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                          "https://www.youtube.com/watch?v=BYRWfS2s2v4")

fantastic_beasts = movies.Movie("Fantastic Beasts: The Crimes of Grindelwald",
                                "To all poter-heads",
                                "https://upload.wikimedia.org/wikipedia/en/3/3c/Fantastic_Beasts_-_The_Crimes_of_Grindelwald_Poster.png",
                                "https://www.youtube.com/watch?v=vvFybpmyB9E")

aquaman = movies.Movie("Aquaman",
                        "What DC's Aquaman movie lacks in refinement, it makes up for with action spectacle and a whole lot of fun personality from Momoa's Arthur ",
                        "https://upload.wikimedia.org/wikipedia/en/3/3a/Aquaman_poster.jpg",
                        "https://www.youtube.com/watch?v=WDkg3h8PCVU")

list_movies = [ divergent, insurgent, allegiant, midnight_in_paris, aquaman , fantastic_beasts,]

fresh_tomatoes.open_movies_page(list_movies)
