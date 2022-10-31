# Script ADA

Para correr el script deben poner sus archivos `.h` en las carpetas "puzzle", "nqueens" o "horse", según corresponda. Las carpetas ya tienen archivos de ejemplo.

Además, deberán poner los argumentos de los programas "horse" y "nqueens" en los archivos de texto "inhorse.txt" y "inqueens.txt" respectivamente.

El formato serán tres enteros separados por comas en cada línea. Podrán usar cuantas líneas quieran, cada linea se usará una vez y se pasará a ejecutar la siguiente hasta el final del archivo, sacando un promedio del tiempo.

Despues, en la consola escriben `python script.py` y dan enter.

Allí les preguntarán "Use script to generate random puzzle.txt? [y/n]", si responden que no el script no modificará el archivo que deberá estar output/puzzle/puzzle.txt

Si responden que si hará 2 preguntas:
- "Puzzle size:". Acá responderán con el tamaño del lado del puzzle
- "Number of moves to shuffle the puzzle:" Acá responderan con cuantos movimientos se mezclará el puzzle. Si no saben que poner, 100 es una buena opción.

Cabe resaltar que también se puede usar el archivo "puzzle.py" para generar puzzles en la consola, su sintaxis es:

```
python puzzle.py <TAMAÑO_PUZZLE> <NUM_ITERACIONES>
```

Por defecto NUM\_ITERACIONES es 100. Un ejemplo sería

```
$ python puzzle.py 5
6       2       9       15      4
21      1       13      8       3
7       11      5       20      #
22      17      18      19      12
16      23      10      14      24
```

Volvamos al programa principal. La siguiente pregunta será "Number of puzzles:", que será el número de puzzles generados para resolver y sacar el promedio del tiempo.

Despues se ejecutará todos los programas y mostrará los errores, tiempos y una gráfica de barras (es necesario instalar matplotlib y numpy).

Si ocurre un error, el tiempo mostrado será infinito, excepto en un error de timeout, en ese caso el tiempo será el máximo permitido por ejecución (por defecto son 60 segundos).

Cada programa se ejecuta con un limitador de memoria, si se pasa de 6 millones de kilobytes (<= 6GB), el proceso se interrumpirá. Esa cantidad se puede modificar.
