# Práctica Paridad

Este repositorio contiene el script **paridad.py**, que:

- Pide al usuario un número entero.
- Comprueba si el número es par o impar.
- Muestra el resultado en pantalla.

## Uso

```bash
python paridad.py

```

## Verificación local

Ejercicio de aprendizaje con funciones importables, validación de entrada y pruebas sin dependencias externas.

```powershell
python -X utf8 paridad.py
python -X utf8 -m unittest discover -v
```

La entrada inválida devuelve código de salida 1 sin traceback. Las pruebas verifican límites y la consola.

## Validación automática

GitHub Actions ejecuta las pruebas de regresión offline y la compilación de fuentes en Python 3.13 y 3.14 para cada PR y cambio en main. El workflow usa permisos de lectura y acciones fijadas por SHA. No instala dependencias ni inicia servidores.
