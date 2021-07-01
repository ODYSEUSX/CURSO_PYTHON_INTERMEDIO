def run():
    palindrome= lambda string: string == string[::-1]   

    print(palindrome('ana'))

if __name__=='__main__':
    run()    
//Las funciones anónimas nos permiten tener funciones sin nombre (identificador). En Python son conocidas como funciones lambda.

lamba argumentos:expresión

Lambda solamente puede tener 1 expresión.

//su equivalente con la función "def"

def palindrome(string):
    return string == string[::-1]

print(palindrome('ana'))

