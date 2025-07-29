import random
def main ():
    numeroAleatorio = random.randint (0, 10 )

    numero = -1

    i = 0

    while numeroAleatorio  != numero:

        numero=int(input("digite um nemero: ")) 

        if numero > numeroAleatorio:
            print("O seu numero e maior ")
        elif numero < numeroAleatorio:
            print("O seu numero e menor")

        i+= 1

    print("Você acertou com ", i, " tentativa")



    return 0
main()