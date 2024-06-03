import sympy as sp
import math
import cmath

x, e, y, z = sp.symbols('x e y z')

def Sustituir_y_Evaluar_Funcion(funcion, valor, seDeriva, ordenDerivada):
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

def Calculo_Ea(xr, xrAnterior):
    resultado = (abs(xr - xrAnterior) / xr) * 100
    if resultado < 0:
        resultado = resultado * -1
    return resultado

def metodoHorner(listaCoeficientes, valorInicial, cifrasSignificativas):
    Solucion_Listado = []  # Lista de valores a mostrar en la lista que mira el usuario
    header = ["Iteracion", "Xi", "Xi+1", "R", "S", "Ea"]
    Solucion_Listado.append(header)
    listaCoeficientes.reverse()
    numeroMultiplicaciones = len(listaCoeficientes)
    iteracion = 0
    salida = 0
    es = 0.5 * (10 ** (2 - cifrasSignificativas))
    ea = 0
    valorAnterior = 0
    valorProximo = float(valorInicial)
    listaConResultados = []  # Lista donde se guardara el resultado de la division sintetica
    listaConResultados2 = []
    R = 0
    S = 0

    while salida == 0:
        iteracion += 1
        listaConResultados.clear()
        listaConResultados2.clear()
        listaConResultados.append(listaCoeficientes[0])

        for i in range(1, numeroMultiplicaciones):  # Primera division sintetica
            listaConResultados.append(
                (listaConResultados[i - 1] * valorProximo) + listaCoeficientes[i])
        R = "%.5f" % float(listaConResultados[len(listaConResultados) - 1])

        listaConResultados2.append(listaCoeficientes[0])
        for i in range(1, numeroMultiplicaciones - 1):  # Segunda division sintetica
            listaConResultados2.append(
                (listaConResultados2[i - 1] * valorProximo) + listaConResultados[i])
        S = "%.5f" % float(listaConResultados2[len(listaConResultados2) - 1])

        valorAnterior = valorProximo

        valorProximo = valorAnterior - (float(R) / float(S))

        ea = Calculo_Ea(valorProximo, valorAnterior)

        Solucion_Listado.append(
            [iteracion, valorAnterior, valorProximo, R, S, ea])

        if ea <= es:
            salida = 1

    return Solucion_Listado

# Lista de coeficientes del polinomio 6*x**3 + 5*x**2 + 3*x + 1
coeficientes = [6, 5, 3, 1]

# Ejecutar el método de Horner
resultado = metodoHorner(coeficientes, -0.45, 0.05)

# Imprimir resultados
for fila in resultado:
    print(fila)
