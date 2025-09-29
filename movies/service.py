from movies.repository import MovieRepository


class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        return self.movie_repository.get_movies()

    def create_movie(self, title, genre, actors, 
                    duration_minutes, release_date, resume, poster):
        movie = dict(
            title=title,
            genre=genre,
            actors=actors,
            duration_minutes=duration_minutes,
            release_date=release_date,
            resume=resume,
            poster=poster,
        )
        return self.movie_repository.create_movie(movie)


