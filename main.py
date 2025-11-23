# ============================================================
#        PRÁCTICA 1 - PABLO CARRILLO
# Todas las funciones cumplen las normas: SIN input(), SIN print().
# 
# ============================================================


# ----------------------
#   FUNCIONES
# ----------------------

def acceso_sistema(usuario, clave):
    """
    Comprueba si el usuario y la clave son correctos.

    Args:
        usuario (str): El nombre de usuario.
        clave (str): La contraseña.

    Returns:
        bool: True si el usuario es "alumno" y la clave es "reyfer", False en caso contrario.
    """
    return usuario == "alumno" and clave == "reyfer"


def es_vocal(letra):
    """
    Comprueba si una letra es una vocal.

    Args:
        letra (str): La letra a comprobar.

    Returns:
        bool: True si la letra es una vocal, False en caso contrario.
    """
    return letra.lower() in "aeiou"


def es_divisible(a, b):
    """
    Comprueba si un número es divisible por otro.

    Args:
        a (int): El dividendo.
        b (int): El divisor.

    Returns:
        bool: True si a es divisible por b, False en caso contrario. Si b es 0, devuelve False.
    """
    if b == 0:
        return False
    return a % b == 0


def mayor_de_tres(a, b, c):
    """
    Devuelve el mayor de tres números.

    Args:
        a (float): El primer número.
        b (float): El segundo número.
        c (float): El tercer número.

    Returns:
        float: El mayor de los tres números.
    """
    mayor = a
    if b > mayor:
        mayor = b
    if c > mayor:
        mayor = c
    return mayor


def es_positivo(numero):
    """
    Comprueba si un número es positivo, negativo o cero.

    Args:
        numero (float): El número a comprobar.

    Returns:
        str: "Positivo", "Negativo" o "Cero".
    """
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"


def calcular_descuento(precio, cliente_vip):
    """
    Calcula el precio final con un descuento si el cliente es VIP.

    Args:
        precio (float): El precio original.
        cliente_vip (bool): True si el cliente es VIP, False en caso contrario.

    Returns:
        float: El precio con un 20% de descuento si el cliente es VIP, o el precio original.
    """
    return precio * 0.8 if cliente_vip else precio


def calcular_nota(examen, practica):
    """
    Calcula la nota final ponderando el examen y la práctica.

    Args:
        examen (float): La nota del examen.
        practica (float): La nota de la práctica.

    Returns:
        float: La nota final (70% examen, 30% práctica).
    """
    return examen * 0.7 + practica * 0.3


def nota_en_letra(nota):
    """
    Convierte una nota numérica a su equivalente en texto.

    Args:
        nota (float): La nota numérica (de 0 a 10).

    Returns:
        str: La calificación en formato texto.
    """
    if 9 <= nota <= 10:
        return "🎓 Sobresaliente"
    elif 7 <= nota < 9:
        return "📘 Notable"
    elif 5 <= nota < 7:
        return "📗 Suficiente"
    elif 0 <= nota < 5:
        return "📕 Insuficiente"
    return " Nota fuera de rango"


def convertir_k_f(kelvin):
    """
    Convierte grados Kelvin a Farenheit.

    Args:
        kelvin (float): La temperatura en Kelvin.

    Returns:
        float: La temperatura en Farenheit.
    """
    return (kelvin - 273.15) * 9/5 + 32


def convertir_f_k(farenheit):
    """
    Convierte grados Farenheit a Kelvin.

    Args:
        farenheit (float): La temperatura en Farenheit.

    Returns:
        float: La temperatura en Kelvin.
    """
    return (farenheit - 32) * 5/9 + 273.15


def suma_hasta(numero):
    """
    Calcula la suma de todos los números enteros desde 1 hasta el número dado.

    Args:
        numero (int): El número límite.

    Returns:
        int: La suma de los números.
    """
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    return suma


# Juego ESTRICTO: sin input dentro
def adivinar_numero(intentos_usuario, numero_secreto=7):
    """
    Comprueba si el intento del usuario coincide con el número secreto.

    Args:
        intentos_usuario (int): El número que intenta adivinar el usuario.
        numero_secreto (int, optional): El número a adivinar. Defaults to 7.

    Returns:
        str: "acertado", "menor" o "mayor" según el intento.
    """
    if intentos_usuario == numero_secreto:
        return "acertado"
    elif intentos_usuario < numero_secreto:
        return "menor"
    else:
        return "mayor"


def contar_pares_impares(limite):
    """
    Cuenta la cantidad de números pares e impares hasta un límite.

    Args:
        limite (int): El número hasta el cual contar.

    Returns:
        tuple: Una tupla con la cantidad de pares e impares.
    """
    pares = 0
    impares = 0
    for i in range(1, limite + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares


# ----------------------
#       MENÚ
# ----------------------

def mostrar_menu():
    """
    Imprime el menú principal de opciones en la consola.
    """
    print("\n==============================")
    print("    MENÚ PRINCIPAL - PRÁCTICA 1")
    print("==============================")
    print("1. 🔐 Acceso al Sistema")
    print("2. 🔤 Verificar Vocal")
    print("3. ➗ Verificar Divisibilidad")
    print("4. 🔢 Mayor de Tres")
    print("5. ➕ Positivo/Negativo/Cero")
    print("6. 💸 Calcular Descuento")
    print("7. 📝 Calcular Nota Media")
    print("8. 🎓 Nota en Letra")
    print("9. 🌡 Kelvin → Farenheit")
    print("10. 🌡 Farenheit → Kelvin")
    print("11. 🔢 Suma hasta N")
    print("12. 🎲 Adivinar Número")
    print("13. 2️⃣ Contar Pares e Impares")
    print("0. 🚪 Salir")
    print("==============================")



def main():
    """
    Función principal que ejecuta el menú y gestiona las opciones del usuario.
    """
    while True:
        mostrar_menu()
        opcion = input("👉 Selecciona una opción: ")

        if opcion == "0":
            print("\n👋 ¡Hasta pronto! Programa finalizado.")
            break

        try:
            # ----------------------------
            # Opciones normales
            # ----------------------------
            if opcion == "1":
                u = input("👤 Usuario: ")
                c = input("🔑 Clave: ")
                if acceso_sistema(u, c):
                    print("✅ Acceso concedido")
                else:
                    print("❌ Acceso denegado")

            elif opcion == "2":
                letra = input("Letra: ")
                print("✔ Vocal" if es_vocal(letra) else "✖ No es vocal")

            elif opcion == "3":
                a = int(input("A: "))
                b = int(input("B: "))
                print("✔ Divisible" if es_divisible(a, b) else "✖ No divisible")

            elif opcion == "4":
                a = float(input("A: "))
                b = float(input("B: "))
                c = float(input("C: "))
                print(f"👉 El mayor es: {mayor_de_tres(a, b, c)}")

            elif opcion == "5":
                n = float(input("Número: "))
                print(f"👉 Resultado: {es_positivo(n)}")

            elif opcion == "6":
                precio = float(input("Precio: "))
                vip = input("¿Es VIP? (s/n): ").lower() == "s"
                print(f"💰 Precio final: {calcular_descuento(precio, vip):.2f}€")

            elif opcion == "7":
                ex = float(input("Examen: "))
                pr = float(input("Práctica: "))
                print(f"📘 Nota final: {calcular_nota(ex, pr):.2f}")

            elif opcion == "8":
                nota = float(input("Nota (0-10): "))
                print(nota_en_letra(nota))

            elif opcion == "9":
                k = float(input("Kelvin: "))
                print(f"{k} K = {convertir_k_f(k):.2f} °F")

            elif opcion == "10":
                f = float(input("Farenheit: "))
                print(f"{f} °F = {convertir_f_k(f):.2f} K")

            elif opcion == "11":
                n = int(input("Número: "))
                print(f"🔢 Suma total: {suma_hasta(n)}")

            # ----------------------------
            #    JUEGO
            # ----------------------------
            elif opcion == "12":
                print("\n🎲 Adivina el número entre 1 y 10")
                while True:
                    intento = int(input("Tu intento: "))
                    res = adivinar_numero(intento)

                    if res == "acertado":
                        print("🎉 ¡Correcto! Adivinaste el número!")
                        break
                    elif res == "menor":
                        print("📉 El número secreto es MAYOR.")
                    else:
                        print("📈 El número secreto es MENOR.")

            elif opcion == "13":
                limite = int(input("Límite: "))
                pares, impares = contar_pares_impares(limite)
                print(f"2️⃣ Pares: {pares} | 1️⃣ Impares: {impares}")

            else:
                print(" Opción inválida. Intenta de nuevo.")

        except ValueError:
            print(" Error: introduce un número válido.")

# Ejecutar programa
if __name__ == "__main__":
    main()
