# con for

def run():

    # my_list= [2,2,2,2,2]

    # all_multiplied =1
    # for i in my_list:
    #     all_multiplied = all_multiplied*i

    # print(all_multiplied)  

 # con reduce

#  from functools import reduce

#  my_list= [2,2,2,2,2]

#  all_multiplied = reduce(lambda a,b: a*b , my_list)

#  print(all_multiplied)


#   #ejemplo1 resuelto con la funcion "map"

#      my_list= [1,2,3,4,5]

#      cuadrados= list(map(lambda x: x**2 , my_list))

#      print(cuadrados)


#con filter

 #ejemplo1 resuelto con la funcion "map"

     my_list= [1,4,5,6,9,13,19,21]

     impares= list(filter(lambda x: x%2 != 0 , my_list))

     print(impares)


          



if __name__=='__main__':
    run()    