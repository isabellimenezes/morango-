def main ():

    idade= int (input (" qual a sua idade? ")) 
    if idade >= 18:
        print("entrada autorizada")  
    elif idade >= 16:
        acompanhante =  input ("algum responsavel presente ")
        if acompanhante == "sim": 
            print("entrada autorizada ")
        else: 
            print(" não autorizado ")
    else: 
        print("entrada proibida") 


main()
        
