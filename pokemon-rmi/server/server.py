import Pyro4
from storage import Storage

def main():
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    uri = daemon.register(Storage)
    ns.register("pokestop.storage", uri)
    print("Storage running")
    daemon.requestLoop()

if __name__ == "__main__":
    main()