class Trainer(object):
    def __init__(self, cod, name):
        self.cod = cod
        self.name = name
        self.pokemons = []

    def getCod(self):
        return self.cod
    
    def catch(self, pokemon, storage):
        if len(self.pokemons) < 6:
            self.pokemons.append(pokemon)
        else:
            storage.store(self, pokemon)