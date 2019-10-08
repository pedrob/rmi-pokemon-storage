from pokemon import Pokemon
from trainer import Trainer
from storage import Storage

charmander = Pokemon("Charmander", "Fire")
pikachu = Pokemon("Pikachu", "Eletric")
ash = Trainer(1, "Ash")
storage = Storage()

ash.catch(charmander, storage)

storage.store(ash, charmander)
storage.store(ash, pikachu)
storage.retrieve(ash, charmander)
# print(storage.listStoredPokemons(ash))
storage.listStoredPokemons(ash)