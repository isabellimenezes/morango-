def main ():
    num = int (input("digite um número : " ) ) 

    i = 2

    while num  != i and num > 1:
       if num % i == 0:
           break
       i += 1

    if num == i:
        print("o número ", num, "é primo")
    elif num == 1:
        print("o número 1 nao e primo")
    else:
        print("o número", num, " nao e primo pois e divisivel por", i) 


    return 0
main()