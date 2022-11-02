# Script ADA Grupo 3

## Integrantes

- Bruno Fernandez
- Joaquin Pino
- Fredy Quispe

## Requisitos

- Compilador g++ en el PATH de su sistema operativo
- Python 3.6+ con matplotlib y numpy

## Instrucciones

Para correr el script deben poner sus archivos `.h` en las carpetas "puzzle", "nqueens" o "horse", según corresponda. Estas ya tienen archivos de ejemplo.

Deberán poner los argumentos de los programas "horse" y "nqueens" en los archivos de texto "inhorse.txt" y "inqueens.txt" respectivamente.

El formato serán tres enteros separados por comas en cada línea. Podrán usar cuantas líneas quieran, cada linea se usará una vez y se pasará a ejecutar la siguiente hasta el final del archivo, sacando un promedio del tiempo.

Las coordenadas se asumen de 0 a n-1. Por ejemplo, si el tablero es de tamaño 8, (0,7) es una coordena valida, pero (1,8) no. No se verifica si las coordenadas son validas.

Despues, en la consola ejecutan `python script.py`.

Allí les preguntarán *Use script to generate random puzzle.txt?*, si responden que no se usara el archivo en `output/puzzle/puzzle.txt`

Si responden que si habrán 2 preguntas:

- *Puzzle size*
- *Number of moves to shuffle the puzzle*

También se puede usar el archivo "puzzle.py" para generar puzzles en la consola, su sintaxis es:

```
python puzzle.py <TAMAÑO_PUZZLE> <NUM_ITERACIONES>
```

Por defecto NUM\_ITERACIONES es 100. Un ejemplo sería:

```
$ python puzzle.py 5
7       1       3       9       4
6       2       14      13      18
11      8       19      5       10
23      16      15      22      20
17      12      24      21      #
```

El espacio vacío siempre estará en la esquina inferior derecha.

La última pregunta será *Number of puzzles*, que será el número de puzzles generados (o el número de veces que se usará `puzzle/puzzle.txt`).

Si ocurre un error, el tiempo mostrado será infinito, excepto en un error de *Timeout*, en ese caso el tiempo será el máximo permitido por ejecución. Por defecto son 10 segundos, pero se puede modificar con la variable TIMEOUT.

Cada programa se ejecuta con un limitador de memoria, si se pasa de 1 millon de kilobytes (<= 1GB), el proceso se terminará. Esa cantidad se puede modificar en la variable MAXMEM.

## Créditos

- <https://github.com/pshved/timeout>
- <https://github.com/lowleveldesign/process-governor>
