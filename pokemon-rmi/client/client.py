import sys
from pokemon import Pokemon
from trainer import Trainer
import Pyro4
import Pyro4.util

sys.excepthook = Pyro4.util.excepthook

def main():
    # test setup
    storage = Pyro4.Proxy("PYRONAME:pokestop.storage")
    cod = 2
    ash = Trainer(1, "Ash")
    charmander = Pokemon("Charmander", "Fire")
    pikachu = Pokemon("Pikachu", "Eletric")
    ash.catch(charmander, storage)
    ash.catch(pikachu, storage)
    treinadores = []
    treinadores.append(ash)
    treinadores_nome = []
    treinadores_nome.append("Ash")
    menu = "[1]usuario exitente\n[2]novo usuario\n[0]sair"

    run = True
    while run:
        print(menu)
        op = input(": ")
        if op == "1":
            nome = input("Digite seu nome:")
            if nome in treinadores_nome:
                treinador = None
                for t in treinadores:
                    if nome == t.name:
                        treinador = t
                        break
                run2 = True
                while run2:
                    menu2 = "[1]guardar pokemon\n[2]retirar pokemon\n[3]listar pokemons guardados\n[4]meus pokemons\n[0]sair"
                    print(menu2)
                    op2 = input(": ")
                    if op2 == "1":
                        pokemon = input("Nome do pokemon: ")
                        find = False
                        for p in treinador.pokemons:
                            if p.getName() == pokemon:
                                find = True
                                storage.store(treinador.getCod(), pokemon)
                                treinador.pokemons.remove(p)
                                print("Pokemon guardado")
                                break
                        if not find:
                            print("Pokemon não encontrado")

                    elif op2 == "2":
                        pokemon = input("Nome do pokemon: ")
                        find = False
                        stored_pokemons = storage.listStoredPokemons(treinador.getCod())
                        for p in stored_pokemons:
                            if p == pokemon:
                                find = True
                                storage.retrieve(treinador.getCod(), pokemon)
                                treinador.pokemons.append(pokemon)
                                print("Pokemon retirado")
                                break
                        if not find:
                            print("Pokemon não encontrado")
                    elif op2 == "3":
                        for p in storage.listStoredPokemons(treinador.getCod()):
                            print(p)
                    elif op2 == "4":
                        for p in treinador.pokemons:
                            if type(p) == str:
                                print(p)
                            else:
                                print(p.getName())
                    elif op2 == "0":
                        run2 = False
                    else:
                        print("Opção inválida")
            else:
                print("Usuario nao encontrado")

        elif op == "2":
            nome = input("Digite seu nome:")
            treinador = Trainer(cod, nome)
            treinadores.append(treinador)
            treinadores_nome.append(treinador.name)
            cod += 1
            print("Usuario criado!")
        elif op == "0":
            run = False
        else:
            print("Opção inválida")

if __name__ == "__main__":
    main()
