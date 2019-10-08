class Pokemon(object):
    def __init__(self, name, type_p):
        self.name = name
        self.type_p = type_p

    def getName(self):
        return self.name

    def getType(self):
        return self.type_p
