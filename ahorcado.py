import random
import os

categorias = {
    "Equipos de futbol Europeo": ["barcelona", "real madrid", "chelsea", "liverpool", "arsenal", "ajax"],
    "Marca de autos": ["volkswagen", "chevrolet", "toyota", "suzuki", "kia", "ferrari", "mercedes", "porsche"],
    "Animales": ["tortuga", "leon", "tigre", "elefante", "tiburon", "delfin", "araña", "mono", "jimmyz"]
}

os.system("clear")
print("Categorías disponibles:")
for categoria in categorias.keys():
    print("-", categoria)

categoria_elegida = input("Elige una categoría para empezar el juego: ")

if categoria_elegida in categorias:
    palabra = categorias[categoria_elegida]
    palabra_secreta = random.choice(palabra)
    letra_adivinada = ["_"] * len(palabra_secreta)

cont = 0
intentos = 6
estado_muñeco = 0

imagenes_muñeco = [
    """
      +---+
          |
          |
          |
          |
         ===
    """,
    """
      +---+
      O   |
          |
          |
          |
         ===
    """,
    """
      +---+
      O   |
      |   |
          |
          |
         ===
    """,
    """
      +---+
      O   |
     /|   |
          |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
          |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     /    |
          |
         ===
    """,
    """
      +---+
      O   |
     /|\\  |
     / \\  |
          |
         ===
    """
]

while intentos > 0:
    letra = input("Ingrese una letra: ").lower()
    if letra in palabra_secreta:
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                letra_adivinada[i] = letra
        print(letra_adivinada)
    else:
        intentos -= 1
        estado_muñeco += 1
        print("Letra incorrecta. Te quedan", intentos, "intentos.")
        print(imagenes_muñeco[estado_muñeco])

    if "_" not in letra_adivinada:
        os.system("clear")
        print(f"¡Felicidades! ¡Has adivinado la palabra! \nLa palabra era {palabra_secreta}")
        break

    if intentos == 0:
        print("Perdiste el juego. La palabra secreta era:", palabra_secreta)
        print(imagenes_muñeco[estado_muñeco])
        break
