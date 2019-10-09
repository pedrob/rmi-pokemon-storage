import Pyro4

@Pyro4.expose
class Storage(object):
    def __init__(self):
        self.stored_pokemons = {}

    def store(self, trainer, pokemon):
        if not trainer in self.stored_pokemons: 
            self.stored_pokemons[trainer] = []
        pokemons = self.stored_pokemons[trainer]
        pokemons.append(pokemon)
        self.stored_pokemons[trainer] = pokemons

    def retrieve(self, trainer, pokemon):
        pokemons = self.stored_pokemons[trainer]
        pokemons.remove(pokemon)

    def listStoredPokemons(self, trainer):
        pokemons = []
        if trainer in self.stored_pokemons.keys():
            pokemons = self.stored_pokemons[trainer]
        return pokemons