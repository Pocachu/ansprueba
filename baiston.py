import sympy as Sympy
import sympy as sp
import numpy as np
import math
import cmath
import re
from sympy import cos, sin, tan, cot, sec, csc, sinh, cosh, tanh, csch, sech, coth
from numpy.polynomial import Polynomial as P
from sympy.simplify.radsimp import numer

x, e, y, z = Sympy.symbols('x e y z')

#♪-------------------------------------------- FUNCIONES NECESARIAS -----------------------------------------------------------------

def Sustituir_y_Evaluar_Funcion(funcion, valor, seDeriva, ordenDerivada):#Evualua las funciones que se envien en los parametros, las deriva si es necesario, si la funcion es incorrecta devuleve un False sino, devuleve el valor
    try:
        funcioon = 0
        if seDeriva == 1:
            if ordenDerivada == 1:
                funcioon = sp.sympify(funcion)
                gxValor = sp.diff(funcioon, x).subs([(x, valor), (e, cmath.e)])
                return gxValor
            else:
                funcioon = sp.sympify(funcion)
                gxValor = sp.Derivative(funcion, x, 2).subs([(x, valor), (e, cmath.e)])
                return gxValor
        else:
            resultado = sp.sympify(funcion).subs([(x, valor), (e, cmath.e)])
            return resultado
    except:
        return "Error"

def Calculo_Ea(xr, xrAnterior):#Calcula el Error absoluto
    resultado = (abs(xr-xrAnterior)/xr)*100
    if resultado < 0:
        resultado = resultado*-1
    return resultado

def ordenPolinomio(x,lista):
    listaResultados = []
    if x == 3:
        raicesFaltantes = factorizar(0, 0, lista[0], lista[1], lista[2])
        listaResultados.extend(raicesFaltantes)
    elif x == 4:
        raicesFaltantes = factorizar(0,lista[0], lista[1], lista[2], lista[3])
        listaResultados.extend(raicesFaltantes)
    elif x == 5:
        raicesFaltantes = factorizar(lista[0], lista[1], lista[2], lista[3], lista[4])
        listaResultados.extend(raicesFaltantes)

    return listaResultados

    return listaResultados

def factorizarCuadratica(a, b, c):
    dd = b**2-4*a*c


def factorizarBicuadradas(a, b, c):
    aa = float(a)
    bb = float(b)
    cc = float(c)

def factorizar(a, b, c, d, e):
    aa = float(a)
    bb = float(b)
    cc = float(c)
    dd = float(d)
    ee = float(e)

    listaResultados = []

    if aa == 0.0 and bb == 0.0 and cc == 0.0:
        return factorizacionSimple(dd, ee)
    elif aa == 0.0 and bb == 0.0:
        return factorizarCuadratica(cc, dd, ee)
    elif bb == 0.0 and dd == 0.0:
        if a != 1:
            nuevoB = cc/aa
            nuevoC = ee/aa
            return factorizarBicuadradas(1, nuevoB, nuevoC)
        else:
            return factorizarBicuadradas(aa, cc, ee)
    else:
        return []

def metodoBairstow(coeficientes,r,s,cifrasSig):

    largo = len(coeficientes)

    if largo <= 5:
        listaSalida = ordenPolinomio(largo,coeficientes)
        return listaSalida

    elif largo >5:

        try:

            #Variable salida controlara el bucle while hasta que se cumpla la condición
            salida = 0

            iteracion = 0

            #Esta lista sera la que contendra las respuestas 
            Solucion_Listado = []

            #Primero convertimos a número los valores de r y s  
            r = float(r)
            s = float(s)

            #Declaramos Ear y Eas y Es 
            E_ar = 0
            E_as = 0 
            Es = (10 ** (2 - cifrasSig)) / 2

            listaA = coeficientes #La lista a es igual a los coeficientes que acompañan a las X en la funcion
            listaB = []
            listaC = []
            #Primero creamos una variable para saber cuantas variables b y c tendremos
            while salida == 0:
                numeroVariables = len(listaA)

                #Debemos limpiar las listas siempre al inicio si no van a acumular los datos de todas las iteraciones
                listaB = []
                listaC = []

                iteracion += 1 
                #Ahora procedemos a llenar los valores de listaB 
                for i in range(0,numeroVariables):
                    if i == 0:
                        listaB.append(listaA[i])
                    elif i == 1:
                        listaB.append(listaA[i] + r*listaB[0])
                    else:
                        listaB.append(listaA[i] + (r*listaB[i-1])+(s*listaB[i-2]))

                #Ahora procedemos a llenar los valores de listaC
                for i in range(0,numeroVariables):
                    if i == 0:
                        listaC.append(listaB[i])
                    elif i == 1:
                        listaC.append(listaB[i] + r*listaC[0])
                    else:
                        listaC.append(listaB[i]+(r*listaC[i-1])+(s*listaC[i-2]))

                listaB.reverse()
                listaC.reverse()

                deltas = despejarEcuaciones(listaC[2], listaC[3], -1*listaB[1], listaC[1], listaC[2],-1*listaB[0])

                # Determinamos los valores actuales de R y S
                r = r + deltas[0]
                s = s + deltas[1]

                # Determinamos los errores
                E_ar = abs(deltas[0]/r)*100
                E_as = abs(deltas[1]/s)*100

                # Hacemos la validacion de si E_ar y E_as < Es salga del bucle
                if E_ar < Es and E_as < Es:

                    #Verificamos si obtendremos raices imaginarias
                    if (r**(2)+4*s) < 0:
                
                        listaA.reverse()
                        p = P(listaA)
                        raicesExtras = p.roots()
                        for x in range(len(raicesExtras)):
                            Solucion_Listado.append(raicesExtras[x])
                
                        salida = 1
                                              
                    #Si (r**2+4*s) > 0 no hay raices imaginarias 
                    else:
                        
                        x1 = "%.5f" % float((r+(r**2+4*s)**0.5)/2)
                        x2 = "%.5f" % float((r-(r**2+4*s)**0.5)/2)

                        #Las convertimos de nuevo a número
                        x1 = float(x1)
                        x2 = float(x2)

                        #Agregamos las primeras 2 raices a la lista de respuestas 
                        Solucion_Listado.append(x1)
                        Solucion_Listado.append(x2)

                        polinomioResultante = divisionSinteticaBairstown(listaA, x1, x2)                    
                        ordenPolinomioResultante = len(polinomioResultante)

                        #Si es una funcion mayor o igual a x^5
                        if ordenPolinomioResultante >= 6:

                            p = P(polinomioResultante)
                            raicesExtras = p.roots()

                            #Borramos los parentesis que nos agrega numpy y eliminamos la J cuando no es necesaria
                            tamanio = len(raicesExtras)-1
                            control = 0
                            salida2 = 1
                            

                            while salida2 == 1:
                                if control <= tamanio and control>=0 :
                                    salidaBuena = ""
                                    raizTexto = str(raicesExtras[control])

                                    for x in raizTexto:
                                        if x == "(" :
                                             salidaBuena += ""
                                        elif x == ")":
                                            salidaBuena += ""
                                        else:
                                            salidaBuena += x
                                            
                                    Solucion_Listado.append(salidaBuena)
                                    control = control + 1
                                else:
                                    salida2 = 0

                            salida = 1

                        #Si es una funcion menor o igual a x^4
                        else:
                            raiPo = ordenPolinomio(ordenPolinomioResultante, polinomioResultante)
                            for x in range(len(raiPo)):
                                Solucion_Listado.append(raiPo[x])
                            salida = 1
        except:
            print("Surgio un problema")
        
        return Solucion_Listado

# Definición de la función exponencial
funcion_expresion = x**4 + x**3 + 7*x**2 - x + 6

# Obtener los coeficientes de la expresión
coeficientes = sp.Poly(funcion_expresion, x).all_coeffs()

# Llamar a la función metodoBairstow con los coeficientes obtenidos
resultado = metodoBairstow(coeficientes, 1, 1.2, 0.05)

print(resultado)