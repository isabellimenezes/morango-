import random
def main ():
    notas = [0.0] * 4

    i = 0
    
    while i < 4:
        notas[i] = float  (random.uniform(0.0, 10.0 ))
        i +=  1

        print(notas)
    return 0
main ()