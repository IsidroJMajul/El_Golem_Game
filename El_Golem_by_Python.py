#  Si (como afirma el griego en el Cratilo)
# el nombre es arquetipo de la cosa
# en las letras de 'rosa' está la rosa
# y todo el Nilo en la palabra 'Nilo'

def get_world():
    x, y = "Ideas", "Real" # In Python you can assign multiple values to multiple variables on a single line
    world = None

    while not (world == x or world == y):
        if world is not None: print("Insert a valid answer.") # The first time world == None, from the second loop onwards it will contain a string value
        world = input("Where do you live?  ")

    if world == x: print("las letras de 'rosa' está la rosa y todo el Nilo en la palabra 'Nilo'")
    elif world == y: print("Game over") # In this situation, this could also be an else statement

    return world

chosen_world=get_world()

print('Continue')

# Y, hecho de consonantes y vocales,
# habrá un terrible Nombre, que la esencia
# cifre de Dios y que la Omnipotencia
# guarde en letras y sílabas cabales.

from turtle import *

def poligono(lado, n):
    for i in range(3):
        forward(lado)
        right(120)

def espiral():
    for i in range(10, 200, 5):
        poligono(i, 3)
        right(10)
        speed(10)

espiral()