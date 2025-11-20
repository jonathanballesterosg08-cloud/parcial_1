
import random

class Criatura:
    def __init__(self, nombre, energia, amigable):
        self.nombre = nombre
        self.energia = energia
        self.amigable = amigable

    def interactuar(self, jugador):
        pass

class CriaturaAmigable(Criatura):
    def __init__(self, nombre, energia, regalo):
        super().__init__(nombre, energia, True)
        self.regalo = regalo

    def interactuar(self, jugador):
        print(f"\n La criatura amigable '{self.nombre}' te ofrece un regalo: {self.regalo}")
        jugador.inventario.append(self.regalo)
        jugador.vida += 10
        print("Tu vida aumenta en 10 puntos.")
        print(f"Vida actual: {jugador.vida}")

class CriaturaHostil(Criatura):
    def __init__(self, nombre, energia, daño):
        super().__init__(nombre, energia, False)
        self.daño = daño

    def interactuar(self, jugador):
        print(f"\n La criatura hostil '{self.nombre}' te ataca y te causa {self.daño} de daño.")
        jugador.vida -= self.daño
        print(f"Vida actual: {jugador.vida}")

class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vida = 100
        self.inventario = []

    def decidir(self):
        print("\n¿Qué quieres hacer?")
        print("1. Avanzar")
        print("2. Huir")
        print("3. Interactuar")

        opcion = input("Elige una opción (1/2/3): ")
        return opcion

    def interactuar(self, criatura):
        criatura.interactuar(self)

class Bosque:
    def __init__(self, criaturas):
        self.criaturas = criaturas

    def generar_evento(self):
        return random.choice(self.criaturas)

    def recorrer(self, jugador):
        print("\n Bienvenido al Bosque Encantado ")
        print(f"Jugador: {jugador.nombre} | Vida: {jugador.vida}")

        while jugador.vida > 0:
            print("\n--- Te adentras más en el bosque... ---")

            criatura = self.generar_evento()
            print(f"Te encontraste con: {criatura.nombre}")

            opcion = jugador.decidir()

            if opcion == "3":
                jugador.interactuar(criatura)
            elif opcion == "2":
                print(" Huyes rápidamente de la criatura.")
            elif opcion == "1":
                print(" Avanzas más en el bosque.")
            else:
                print ("Opción inválida. Pierdes tiempo en el bosque...")

        print("\n Has perdido... Fin del juego.")


def inicio():
    jugador = Jugador(nombre="JONATHAN")

    criatura1 = CriaturaAmigable("Hada", 30, "Poción Mágica")
    criatura2 = CriaturaHostil("Troll", 50, 20)

    criaturas = [criatura1, criatura2]

    bosque = Bosque(criaturas)
    bosque.recorrer(jugador)


inicio()
