"""Paridad para enteros positivos, negativos y cero."""


def es_par(numero):
    return numero % 2 == 0


def main():
    try:
        numero = int(input("Ingresa un número entero: "))
        print(f"{numero} es {'par' if es_par(numero) else 'impar'}.")
    except (ValueError, EOFError):
        print("Entrada inválida: ingrese un número entero.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
