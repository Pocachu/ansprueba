import sympy as sp

def muller(f, f_prime, x0, x1, tol=1e-5, max_iter=100):
    """
    Encuentra una raíz de la función f utilizando el método de Müller.

    Parámetros:
    f (function): La función para la que se busca la raíz.
    f_prime (function): La derivada de la función f.
    x0 (float): El primer punto de partida.
    x1 (float): El segundo punto de partida.
    tol (float, optional): La tolerancia para la precisión. Defaults to 1e-5.
    max_iter (int, optional): El máximo número de iteraciones. Defaults to 100.

    Returns:
    float: La raíz encontrada.
    """
    for _ in range(max_iter):
        # Calcular los valores de la función en los puntos de partida
        f0 = f(x0)
        f1 = f(x1)

        # Calcular la derivada en los puntos de partida
        f0_prime = f_prime(x0)
        f1_prime = f_prime(x1)

        # Calcular el valor de la función en el punto medio
        x2 = (x0 * f1 * f1_prime - x1 * f0 * f0_prime) / (f1 * f1_prime - f0 * f0_prime)

        # Calcular el valor de la función en el punto medio
        f2 = f(x2)

        # Verificar si se ha alcanzado la tolerancia
        if abs(f2) < tol:
            return x2

        # Actualizar los puntos de partida
        if f2 * f1 < 0:
            x0, x1 = x1, x2
        else:
            x0, x1 = x2, x2 + (x1 - x0)

    # Si no se ha alcanzado la tolerancia, se devuelve el último punto de partida
    return x1

# Solicitar el grado de la función al usuario
grado = int(input("Introduzca el grado de la función: "))

# Solicitar los coeficientes del polinomio al usuario
coeficientes = []
for i in range(grado, -1, -1):
    coef = float(input(f"Introduzca el coeficiente de x^{i}: "))
    coeficientes.append(coef)

# Crear la función polinómica usando sympy
x = sp.symbols('x')
polinomio = sum(coef * x**i for i, coef in enumerate(reversed(coeficientes)))

# Calcular la derivada del polinomio
polinomio_derivada = sp.diff(polinomio, x)

# Convertir la función y su derivada en funciones lambda
f = sp.lambdify(x, polinomio, 'math')
f_prime = sp.lambdify(x, polinomio_derivada, 'math')

# Solicitar los datos adicionales al usuario
x0 = float(input("Introduzca el primer punto de partida (x0): "))
x1 = float(input("Introduzca el segundo punto de partida (x1): "))
tol = float(input("Introduzca la tolerancia para la precisión (por defecto 1e-5): ") or 1e-5)
max_iter = int(input("Introduzca el máximo número de iteraciones (por defecto 100): ") or 100)

# Encontrar la raíz utilizando el método de Müller
root = muller(f, f_prime, x0, x1, tol, max_iter)
print("Raíz encontrada:", root)
