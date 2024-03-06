# Definimos la interfaz para el tipo de tropa
class Troop:
    def military(self):
        pass

# Implementación del comportamiento de infanteria
class Infantery(Troop):
    def military(self):
        print("¿Espada?")

# Implementación del comportamiento de caballería
class Chivalry(Troop):
    def military(self):
        print("* rechino *")

# Implementación del comportamiento de arquería
class Archery(Troop):
    def military(self):
        print("¿Arco y flecha?")

class Stats:
    def numbers(self):
        pass

# Definimos la interfaz para el ataque
class Attack(Stats):
    def stat(self):
        print('¡Hard attack!')

# Definimos la interfaz para el movimiento
class Movement(Stats):
    def stat(self):
        print('Moving fast...')

# Definimos la interfaz para el movimiento
class Distance(Stats):
    def stat(self):
        print('Long shoot')


# Clase base para los soldados
class Soldier:
    def __init__(self, Troop, Stats):
        self.Troop = Troop
        self.Stats = Stats

    def type_soldier(self):
        self.Troop.military()

    def type_attack(self):
        self.Stats.stat()

# Clase concreta para huscarle
class Huscarle(Soldier):
    def __init__(self):
        super().__init__(Infantery(), Attack())

# Clase concreta para un ballesterogit
class Ballestero(Soldier):
    def __init__(self):
        super().__init__(Archery(), Distance())

class Jinete(Soldier):
    def __init__(self):
        super().__init__(Chivalry(), Movement())

# Ejemplo de uso
if __name__ == "__main__":
    Huscarle_1 = Huscarle()
    Ballestero_1 = Ballestero()
    Jinete_1 = Jinete()

    print("Huscarle:")
    Huscarle_1.type_soldier()
    Huscarle_1.type_attack()

    print("Ballestero:")
    Ballestero_1.type_soldier()
    Ballestero_1.type_attack()
    
    print("Jinete:")
    Jinete_1.type_soldier()
    Jinete_1.type_attack()
