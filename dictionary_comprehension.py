# def run():
#     my_dict= {}                #//como crear un diccionario con una función for

#     # for i in range(1,101):     //un elemento i va recorrer 100 veces(rango del al 100) abajo del for se hace referencia la función o parametro que va tomar como unidad de entrada el elemento "i".
#     #     my_dict[i]= i**3      //esto representa los elementos del diccionario(key y value) que van hacer guardadas en el my_dict(vació)
#     for i in range(1,101):
#         if i % 3 != 0:
#             my_dict[i]=i**3
#     print(my_dict)    



# if __name__=='__main__':
#     run()    

# metodo dictionary comprehension
def run():
    # my_dict={i:i**3  for i in range(1,101) if i % 3 !=0} // formula {key:value | for i in range | condition(opcional)}
     import math
     my_dict={ i:math.sqrt(i)   for i in range(1,1001)} // my_dict={ i:round(i**0.5)   for i in range(1,1001)}

     print(my_dict)

if __name__=='__main__':
    run()    
