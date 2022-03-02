print("bienvenidos a la calculadora")
operadores = input("coloca +,-,* o / para hacer las operaciones = " )
factor1=input("ingresa el primer valor = ")
factor2=input("ingresa el segundo valor = ")

if operadores == "+" :
    resultado=print( int(factor1) + int(factor2) ) 
if operadores == "-" :
    resultado=print( int(factor1) - int(factor2) ) 
if operadores == "*" :
    resultado=print( int(factor1) * int(factor2) ) 
if operadores == "/" :
    resultado=print( int(factor1) / int(factor2) )       
