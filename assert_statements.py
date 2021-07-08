
# divisors = lambda num: [i for i in range(1, int(num) +1 ) if int(num) % i == 0]

# def main():
#     num = input('Ingresa un número entero positivo: ')
#     assert num.isalpha() == False, 'Debes ingresar un número'
#     assert int(num) >= 0 and num.isalpha() == False, 'No debe ingresar numeros negativos'
#     print('Divisores de', str(num) + ':')
#     print(divisors(num))
                               

# if __name__ == '__main__':
#     main()

def divisors(num):
    
        
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors
    

def run():
    
    num = input('Ingresa un número: ')
    assert num.isalpha()==False, "debes ingresar un número"
    assert (int(num )>0) and num.isalpha() == False , "Debes ingresar un numero positivo"
    print(divisors(int(num)))
    print("Terminó mi programa")
   
      


if __name__ == '__main__':
    run()