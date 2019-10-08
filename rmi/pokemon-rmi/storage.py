class Storage(object):
    def __init__(self):
        self.stored_pokemons = {}

    def store(self, trainer, pokemon):
        if not trainer.getCod() in self.stored_pokemons: 
            self.stored_pokemons[trainer.getCod()] = []
        pokemons = self.stored_pokemons[trainer.getCod()]
        pokemons.append(pokemon)
        self.stored_pokemons[trainer.getCod()] = pokemons

    def retrieve(self, trainer, pokemon):
        pokemons = self.stored_pokemons[trainer.getCod()]
        pokemons.remove(pokemon)

    def listStoredPokemons(self, trainer):
        pokemons = self.stored_pokemons[trainer.getCod()]
        for pokemon in pokemons:
            print(pokemon.getName())