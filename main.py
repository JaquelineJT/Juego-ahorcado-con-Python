#importa librerias que vamos a usar
import random
import string
from palabras import palabras
from diagramas import vidas_diccionario_visual

 
def obtener_palabra():
    palabra = random.choice(
        palabras)  #selecciona una palabra al azar dentro de la lista palabras
    return palabra.upper()


def run():
    print('BIENVENIDO AL JUEGO DE "EL AHORCADO"'
          )  #Bienvenida y asignacion de variables
    palabra = obtener_palabra() # usa la funcion obtener palabra
    abc = set(string.ascii_uppercase)
    letras_original = set(palabra)
    letras_buenas = set()
    vidas = 7
    print('_ ' * len(palabra))

    while len(letras_buenas) != len(letras_original) and vidas > 0:
        print(
            f'\nTe quedan {vidas} vidas y has usado estas letras: {" ".join(letras_buenas)}\n'
        )
        print(vidas_diccionario_visual[vidas])  #imprime figurilla
        letras_usuario = input('Ingresa una letrilla: \n').upper()

        #compara la letra que ingresa el usuario con las de la palabra original
        if letras_usuario in letras_original:
            print('Tu letra es correcta\n')
            letras_buenas.add(
                letras_usuario)  #se añade en el historial de letras usadas

            #ingresa cada letra a una lista para ver la posición de la letra correcta
            lista = []
            for i in palabra:
                if i in letras_buenas:
                    lista.append(i)
                else:
                    lista.append('_')
            print(lista)
        elif letras_usuario not in abc:  #caracteres que no son letras del abecesario
            print('error, error, no es una letra\n')
        else:
            print('sigue intentando\n')  #letra que no está en la palabra
            vidas -= 1
        if letras_buenas == letras_original:
            print('\nGanaste\n\n')  #Gana
            print(palabra)
        elif vidas == 0:
            print('Perdiste')  #Pierde
            print(vidas_diccionario_visual[0])


if __name__ == '__main__':
    run()
