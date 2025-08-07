def main ():
    num = int (input("digite um número : " ) )
    divisores = " "
    i = 2
    j = 0
    while num  != i and num > 1:
       if num % i == 0:
           divisores  +=  "\n" + str (i)
           j += 1
       i += 1

    if j == 0 and num > 1: 
        print("o número ", num, "é primo")
    elif num == 1 or num == -1:
        print("o número 1 nao e primo")
    else:
        print("o número", num, " nao e primo pois e divisivel por", divisores) 
    return 0
main()