# Cifrador/Descifrador de Código Bacon (Este .md es un WIP)
## Introducción
El Código Bacon o clave Baconiana (en inglés Baconian cipher), es un método criptográfico desarrollado por Francis Bacon. El mensaje estaría oculto en la presentación del texto, más que en su contenido.

De acuerdo a Sir Francis Bacon, existen tres propiedades que debe de tener un cifrado

1) Debe de ser fácil de escribir y de leer

2) Que debe de ser confiable y que no pueda ser descifrado

3) Si es posible libre de sospecha.

Debido a que si un mensaje llegara a caer en manos incorrectas, este no pueda ser descifrado a pesar de que sea examinado por expertos.s
Esta última condición hace que el código Bacon suponga un híbrido entre los sistemas criptográficos y los esteganográficos compartiendo características de ambos.


Para codificar un mensaje, cada letra de texto plano es reemplazada por un grupo de cinco letras 'A' o 'B'. El reemplazo se hace de acuerdo con el alfabeto del código Bacon, mostrado abajo.




| Clave | Valor | Clave | Valor | Clave | Valor | Clave | Valor |
| ---   | ---   | ---   | ---   | ---   | ---   | ---   | ----  |
| a     | AAAAA | g     | AABBA | n     | ABBAA | t     |BAABA  |
| b     | AAAAB | h     | AABBB | o     | ABBAB | u-v   |BAABB  |
| c     | AAABA | i-j   | ABAAA | p     | ABBBA | w     |BABAA  |
| d     | AAABB | k     | ABAAB | q     | ABBBB | x     |BABAB  |
| e     | AABAA | l     | ABABA | r     | BAAAA | y     |BABBA  |
| f     | AABAB | m     | ABABB | s     | BAAAB | z     |BABBB  |




Nota: En esta implementación las letras I y J poseen su propio patrón.


El escritor debe emplear dos diferentes tipos de letra para su código. Tras preparar un falso mensaje con el mismo número de letras que de letras A y B del mensaje real, dos tipos de letra son elegidos, uno para representar las Aes y otro para las Bes. Entonces, cada letra del falso mensaje debe ser presentada con el tipo de letra apropiado, según corresponda a una A o una B.

Por ejemplo, supongase que se quiere encriptar el mensaje:

`te espero a las cinco`

Al codificarlo utilizando el código Bacón:


`BAABA AABAA AABAA BAAAB ABBBA AABAA BAAAA ABBAB AAAAA ABABA AAAAA BAAAB AAABA ABAAA ABBAA AAABA ABBAB`

Si se eliminan los espacios:


`BAABAAABAAAABAABAAABABBBAAABAABAAAAABBABAAAAAABABAAAAAABAAABAAABAABAAAABBAAAAABAABBAB`


Luego debemos construir un mensaje falso que tenga el mismo número de letras que el mensaje encriptado original o verdadero:

```
BAABAAABAAAABAABAAABABBBAAABAABAAAAABBABAAAAAABABAAAAAABAAABAAABAABAAAABBAAAAABAABBAB
NODESEOVERTEMASMEHASDECEPCIONADOPREFIEROESTARSOLOADIOSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
```

Los estilos de letras serán mayúsculas para las B y minúsculas para las A. El resultado seria :

```
BAABAAABAAAABAABAAABABBBAAABAABAAAAABBABAAAAAABABAAAAAABAAABAAABAABAAAABBAAAAABAABBAB
NodEseoVerteMasMehaSdECEpciOnaDoprefIErOestarsOlOadiossSsssSsssSssSssssSSsssssSssSSsS
```

Finalmente colocando los espacios:


`No dEseo Verte Mas Me haS dECEpciOnaDo prefIErO estar sOlO adiossSsssSsssSssSssssSSsssssSssSSsS`

## Dependencias
## Usar la clase BaconCoding
## Usar la GUI
## Archivo ejecutable para Windows
