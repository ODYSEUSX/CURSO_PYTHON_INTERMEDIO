def run():
    my_list= [1,"hello", 4.5]
    my_dict={"firstname":"facundo", "lastname":"garcia"}


    super_list = [
        {"firstname":"facundo", "lastname":"garcia"},
        {"firstname":"Miguel", "lastname":"Torres"},
        {"firstname":"Pepe", "lastname":"Rodelo"},
        {"firstname":"Susana", "lastname":"Martinez"},
        {"firstname":"José", "lastname":"Maldonado"}

    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.43]
    }

    # for key,value in super_dict.items(): //para recorrer y mostrar los elementos de un diccionario
    #     print(key,"-",value) 
    for i in super_list:
        print(i["firstname"], "-", i["lastname"]) #para recorrer una lista(con diccionarios como elementos) y mostrar los elementos

if __name__=='__main__':
    run()    