import sympy as sp
import math

x, e, y, z = sp.symbols('x e y z')

def Sustituir_y_Evaluar_Funcion(funcion, valor, seDeriva, ordenDerivada):
    try:
        if seDeriva == 1:
            funcioon = sp.sympify(funcion)
            gxValor = sp.diff(funcioon, x, ordenDerivada).subs([(x, valor), (e, math.e)])
            return gxValor
        else:
            resultado = sp.sympify(funcion).subs([(x, valor), (e, math.e)])
            return resultado
    except:
        return "Error"

def Calculo_Ea(xr, xrAnterior):
    resultado = abs((xr - xrAnterior) / xr) * 100
    return abs(resultado) if resultado.is_real else abs(resultado.evalf())

def metodoMuller(funcion, valor0, valor1, valor2, cifrasSignificativas):
    Solucion_Listado = []
    header = ["Iteracion", "X0", "X1", "X2", "Xr", "EA"]
    Solucion_Listado.append(header)

    iteracion = 0
    x0 = float(valor0)
    x1 = float(valor1)
    x2 = float(valor2)

    cifr = int(cifrasSignificativas)
    xr = 0.0
    ea = 0
    es = 0.5 * (10 ** (2 - cifr))
    salida = 0

    while salida == 0:
        iteracion += 1

        fx0 = Sustituir_y_Evaluar_Funcion(funcion, x0, 0, 0)
        fx1 = Sustituir_y_Evaluar_Funcion(funcion, x1, 0, 0)
        fx2 = Sustituir_y_Evaluar_Funcion(funcion, x2, 0, 0)

        h0 = x1 - x0
        h1 = x2 - x1

        ampersand0 = (fx1 - fx0) / h0
        ampersand1 = (fx2 - fx1) / h1

        a = (ampersand1 - ampersand0) / (h1 + h0)
        b = a * h1 + ampersand1
        c = fx2

        d = ((b ** 2) - (4 * a * c)) ** 0.5

        if abs(b + d) > abs(b - d):
            xr = x2 + (-2 * c) / (b + d)
        else:
            xr = x2 + (-2 * c) / (b - d)

        ea = Calculo_Ea(xr, x2)

        Solucion_Listado.append([iteracion, x0, x1, x2, xr, ea])

        if ea <= es:
            salida = 1
        else:
            x0 = x1
            x1 = x2
            x2 = xr

    return Solucion_Listado

print(metodoMuller(x**3 - 13*x - 12, 4.5, 5.5, 5, 0.05))