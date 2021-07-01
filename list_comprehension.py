def run():
    # squares=[]                   //metodo normal: imprimir los cuadrados del 1 al 100 que no sean multiplos de tres.
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         squares.append(i**2)

    # squares = [i**2 for i in range(1,101) if i % 3 !=0]  //metódo list comprehensions
    #                                                        se lee del medio ,despues a la izquierda ,terminando por la derecha.
    #                                                        [element | for element in iterable | if condition]   
    ##se lee: por cada elemento en el rango (1,101) guarde el elemento(i**2) solo si cumple con la condición(i%3 != 3) .
    
    # multiples=[  i for i in range(1,100000) if i % 36 ==0]   
                                                                         

    # print(multiples)  

    #ejemplo 1
    # cuadrados=[i**2 for i in range(1,6) ] 
    # print(cuadrados) 



    


if __name__=='__main__':
    run()