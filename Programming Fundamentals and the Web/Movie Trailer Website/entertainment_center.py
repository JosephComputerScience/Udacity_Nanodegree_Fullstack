import media
import fresh_tomatoes

def __main__():
    #Avenger instance of the Movie class
    avengers = media.Movie("Avengers",
                           "https://s-media-cache-ak0.pinimg.com/736x/0f/03/e6/0f03e6733b0cf567cc92e8e20290462f.jpg",
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8")

    #Guardian of the galaxy instance of the Movie class
    guardian_of_the_galaxy = media.Movie("Guardians Of The Galaxy",
                                         "https://images-na.ssl-images-amazon.com/images/I/51T5sJngQLL.jpg",
                                         "https://www.youtube.com/watch?v=d96cjJhvlMA")

    #Iron Man instance of the Movie class
    iron_man = media.Movie("Iron Man",
                           "http://www.impawards.com/2008/posters/iron_man_ver3.jpg",
                           "https://www.youtube.com/watch?v=8hYlB38asDY")

    #Avatar instance of the Movie Class
    avatar = media.Movie("Avatar",
                         "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                         "http://www.youtube.com/watch?v=-9ceBgWV8io")

    #Toy Story instance of the Movie lass
    toy_story = media.Movie("Toy Story",
                            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                            "https://www.youtube.com/watch?v=vwyZH85NQC4")

    #Kung Fu Panda instance of the Movie class
    kung_fu_panda = media.Movie("Kung Fu Panda",
                                "https://www.cinematerial.com/media/posters/md/v0/v0nqkcwo.jpg?v=1456844132",
                                "https://www.youtube.com/watch?v=PXi3Mv6KMzY")

    movies = [avengers, guardian_of_the_galaxy, iron_man, avatar, toy_story, kung_fu_panda]
    #Using the fresh_tomatoes module to use the open_movies_page(Movie) function to run the webpage
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    __main__()