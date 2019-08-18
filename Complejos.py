'LIBRERÍA COMPUTACIÓN CUÁNTICA'
'Calculadora números complejos'
import math

#Suma.
def sumar(num1,num2):
    a=num1[0]+num2[0]
    b=num1[1]+num2[1]
    return(a,b)

#Resta.
def restar(num1,num2):
    a=num1[0]-num2[0]
    b=num1[1]-num2[1]
    return(a,b)

#Multiplicación.
def producto(num1,num2):
    a=(num1[0]*num2[0])-(num1[1]*num2[1])
    b=(num1[0]*num2[1])+(num1[1]*num2[0])
    return(a,b)

#Conjugado.
def conjugado(num):
    return(num[0],-1*num[1])


#Modulo.
def modulo(num):
    m=math.sqrt(num[0]**2+num[1]**2)
    return(round(m,2))

#División.
def division(num1,num2):
    deno=num2[0]**2+num2[1]**2
    a=(num1[0]*num2[0])+(num1[1]*num2[1])
    b=(num1[1]*num2[0])-(num1[0]*num2[1])
    return(round(a/deno,2),round(b/deno,2))

#Conversión de representación polar a cartesiana.
#El ángulo ingresado es en radianes
def pol_a_car(cord):
    a= cord[0]*math.cos(cord[1])
    b= cord[0]*math.sin(cord[1])
    return(round(a,2),round(b,2))

#Conversión de representación cartesiana a polar.
#El ángulo retornado es en grados
def car_a_pol(num):
    p=math.sqrt(num[0]**2+num[1]**2)
    θ=math.atan(num[1]/num[0])
    return (round(p,2),round(math.degrees(θ),2))

#Fase
#El ángulo retornado es en grados
def fase(num):
    f1=math.atan(num[1]/num[0])
    if num[0]<0 and num[1]<0:
        return(round(180+math.degrees(f1),0))
    elif num[0]<0:
        return (round(180+math.degrees(f1),0))
    elif num[1]<0:
        return(round(360+ math.degrees(f1),0))
    else:
        return(round(math.degrees(f1),0))





