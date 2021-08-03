### LISTA Y DICCIONARIOS ANIDADOS


def run():
    my_list = [1,"Hello",True, 4.5]
    my_dict = {"firstname":"ilche", "lastname":"park"}


    super_list = [
        {"firstname":"ilche", "lastname":"park"},
        {"firstname":"marce", "lastname":"zega"},
    ]

    super_dict = {
         "natural_nums": [1,2,3,4,5],
         "integer_nums": [-1,-2,-3],
         "floating_nums":[1.1,4.5,6.43]
    }


    for key, value in super_dict.items():
        print(key,"-", value)

  

##Esto es el entry point, lo que hace es iniciar la función al ejecutar 
##la función

if __name__ == '__main__':
    run()