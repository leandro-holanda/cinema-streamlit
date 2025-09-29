from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.actors_repository = ActorRepository()

    def get_actors(self):
        return self.actors_repository.get_actors()

    def create_actor(self, name, birthday, nacionality):
        actor = dict(
            name=name,
            birthday=birthday,
            nacionality=nacionality,
        )
        return self.actors_repository.create_actor(actor)