def palindrome(string):
    try:
        palindrome = string == string [::-1]
    except TypeError:
        print(f"No puedes utilizar números, {string} es un número. ")        
    else:
        if palindrome == True:
            print(f"'{string}' es un palíndromo!")
        elif palindrome == False:
            print(f"'{string}' no es un palíndromo.")

if__name__=='__main__':
    palindrome(palindrome)

