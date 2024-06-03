import math

def main():
    n = int(input("Introduzca el grado del polinomio: "))

    if n == 0:
        print("No existen raices en polinomios grado 0")
        return

    m = n
    n += 1
    contadorDivisionSintetica = contadorIteraciones = 0

    Coeficientes = [0.0] * n
    Mr = [0.0] * n
    Ms = [0.0] * n
    Mat1 = [0.0] * n
    Mat2 = [0.0] * n  # Cambiado a n
    raizReal = [0.0] * n
    raizImaginaria = [0.0] * n
    Mat = [0.0] * n

    print("Introduzca a continuacion los coeficientes del polinomio")
    for i in range(n):
        Coeficientes[i] = float(input(f"Introducir el coeficiente de x^{(n - 1) - i} : "))

    if n == 2:
        print("\nRaices Calculadas:")
        raiz = (-Coeficientes[1]) / Coeficientes[0]
        print(f"\nX0 = {raiz}")
        return

    r0 = float(input("Introduzca el valor inicial de r : "))
    s0 = float(input("Introduzca el valor inicial de s : "))
    TOLERANCIA = float(input("Introduzca el valor de Tolerancia para la convergencia: "))
    iteracionesMaximas = int(input("Introduzca numero maximo de iteraciones : "))

    for j in range(0, 2 * (n - 1), 2):
        b1 = b0 = 1.0
        gradoPolinomio_j = (n - 1) - 2 * contadorDivisionSintetica
        nx = n - 1 - 2 * contadorDivisionSintetica
        mx = nx - 1

        if gradoPolinomio_j <= 2:
            if gradoPolinomio_j == 2:
                raiz = Coeficientes[1] ** 2 - 4 * Coeficientes[2]
                if raiz < 0:
                    raiz = abs(raiz)
                    raizReal[j] = raizReal[j + 1] = -Coeficientes[1] / 2
                    raizImaginaria[j] = math.sqrt(raiz) / 2
                    raizImaginaria[j + 1] = -math.sqrt(raiz) / 2
                else:
                    raizReal[j] = (-Coeficientes[1] + math.sqrt(raiz)) / 2
                    raizReal[j + 1] = (-Coeficientes[1] - math.sqrt(raiz)) / 2
                    raizImaginaria[j] = raizImaginaria[j + 1] = 0
            else:
                raizReal[j] = -Coeficientes[1]
            break
        else:
            contadorIteraciones = 0
            r = r0
            s = s0
            for i in range(gradoPolinomio_j + 1):
                Mr[i] = Ms[i] = Mat1[i] = 0  # Eliminado Mat2[i] = 0

            while abs(b1) > TOLERANCIA or abs(b0) > TOLERANCIA:
                for i in range(gradoPolinomio_j + 1):
                    Mat1[i] = Coeficientes[i] + Mr[i] + Ms[i]
                    if i + 1 < len(Mr):
                        Mr[i + 1] = -r * Mat1[i]
                    if i + 2 < len(Ms):
                        Ms[i + 2] = -s * Mat1[i]

                for i in range(gradoPolinomio_j + 1):
                    Mr[i] = Ms[i] = 0

                for i in range(gradoPolinomio_j):
                    Mat2[i] = -Mat1[i] + Mr[i] + Ms[i]
                    if i + 1 < len(Mr):
                        Mr[i + 1] = -r * Mat2[i]
                    if i + 2 < len(Ms):
                        Ms[i + 2] = -s * Mat2[i]

                b1 = ((Mat2[mx - 1] * -Mat1[nx - 1]) - (-Mat1[nx] * Mat2[mx - 2])) / ((Mat2[mx - 1] ** 2) - ((Mat2[mx] + Mat1[nx - 1]) * Mat2[mx - 2]))
                b0 = ((-Mat1[nx] * Mat2[mx - 1]) - ((Mat2[mx] + Mat1[nx - 1]) * -Mat1[nx - 1])) / ((Mat2[mx - 1] ** 2) - ((Mat2[mx] + Mat1[nx - 1]) * Mat2[mx - 2]))

                r += b1
                s += b0
                contadorIteraciones += 1

                if contadorIteraciones > iteracionesMaximas:
                    print("Fallo en la convergencia")
                    break

            raiz = (r ** 2) - (4 * s)

            if raiz < 0:
                raiz = abs(raiz)
                raizReal[j] = raizReal[j + 1] = -r / 2
                raizImaginaria[j] = math.sqrt(raiz) / 2
                raizImaginaria[j + 1] = -math.sqrt(raiz) / 2
            else:
                raizReal[j] = (-r + math.sqrt(raiz)) / 2
                raizReal[j + 1] = (-r - math.sqrt(raiz)) / 2
                raizImaginaria[j] = raizImaginaria[j + 1] = 0

            contadorDivisionSintetica += 1
            newsize = (n - 1) - (2 * contadorDivisionSintetica)
            for i in range(int(newsize) + 1):
                Coeficientes[i] = Mat1[i]

    print("\nRaices Calculadas:")

    for i in range(n - 1):
        if raizImaginaria[i] == 0:
            print(f"X{i} = {raizReal[i]}")
        else:
            if raizImaginaria[i] < 0:
                if raizImaginaria[i] == -1:
                    print(f"X{i} = {raizReal[i]}-i")
                else:
                    print(f"X{i} = {raizReal[i]}{raizImaginaria[i]}i")
            else:
                if raizImaginaria[i] == 1:
                    print(f"X{i} = {raizReal[i]}+i")
                else:
                    print(f"X{i} = {raizReal[i]}+{raizImaginaria[i]}i")

if __name__ == "__main__":
    main()
