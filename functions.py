def square(x):         #def(define) square(function)(x)(argument)
    return x * x

#for i in range(10):
#    print("{} squared is {}".format(i, square(i)))

def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))
#def main() es una solucion para correr esta funcion unicamente dentro del archivo functions.py
#entonces cuando es llamada este archivo functions.py desde otro archivo por ejemplo modules.py
#no se ejecuta todo, sino que solamente a lo que se esta llamando.

if __name__ == "__main__":
    main()
#si estoy corriendo esta funcion particular, entonces corre Main function.
