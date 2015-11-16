# Expresiones regulares

### Motivación

¿Cómo escribirían una función que reciba un string y verifique si corresponde a un email de la PUC? Suponiendo que en la parte local solo puede haber letras, dígitos, y el caracter "_"

```python
def is_mail_uc(string):
	if not string.count("@") == 1:
	    return False
    local, domain = string.split("@")
    if domain is not "uc.cl" and domain is not "puc.cl":
        return False
    if not local:
        return False
    valids = [i for i in range(ord('a'), ord('z')+1)]
    valids += [i for i in range(ord('A'), ord('Z')+1)]
    valids.append(ord('_'))
    for c in local:
        if ord(c) not in valids:
            return False
    return True
```

¿Cómo la modificarían si hubiera que permitir además, correos con dominio `ing.pug.cl`, `mat.puc.cl`, `ing.uc.cl` o `mat.uc.cl`? **ARGH!** Así es como **NO** se hace esta función.

### El módulo `re`

La misma función (incluyendo mails de ingeniería y matemática) puede escribirse como:
```python
import re


def is_mail_uc(string):
    pattern = "[a-zA-Z0-9_]+@((ing|mat)\.)?p?uc.cl"
    return bool(re.fullmatch(pattern, string))
```

¡Y funciona!

### ¿Qué es esto? ¿Magia negra?

Algo así... las expresiones regulares son patrones de strings especialmente útiles para:
* Ver si otro string cumple el patrón (`fullmatch`)
* Ver si algún sub-string lo cumple (`search`)
* Reemplazar el patrón por otra secuencia de caracteres (`sub`)
* Separar el string de acuerdo al patrón (`split`)
* En general, jugar con patrones de strings!

### ¿Cómo funciona?

La sintaxis de los patrones se basa en caracteres especiales.
Por ejemplo,
* `"["` y `"]"`. Sirven para indicar distintos caracteres posibles en esa posición. Por ejemplo, `"a[bcde]f"` es un patrón que representa a los strings: `"abf"`, `"acf"`, `"adf"`, `"aef"`.
* `"-"` sirve para indicar *rangos* de caracteres. El patrón del ejemplo anterior también podía escribirse como `"a[b-e]f"`.
* `"+"` indica que la expresión anterior (ojo, esta puede contener varios caracteres posibles internamente) estará presente una o más veces. Así, `"a[b-e]+f"` hace referencia a los mismos strings del primer ejemplo, pero también a `"abbf"`, `"abcf"`, `"abdedeeebdef"`, etc.
* `"*"` es similar a `"+"`, pero permite que la expresión previa no esté ninguna vez. `"a[b-e]*f"` permite, además de los strings anteriores, al string `"af"`.
* `"|"` es para separar dos secuencias, y buscará que en dicho lugar, haya una o la otra. Por ejemplo, `"abc|def"` representa a los strings `"abc"` o `"def"`, y `"(abc|def)+"`, también permite `"abcabcabc"` o `"abcabcdefabcabcdefdef"`.
* `"?"` indica que la expresión anterior puede estar una vez, o no estar.
* `"."` representa cualquier caracter, excepto un salto de línea.
* `"("` y `")"` funcionan como delimitadores.
* `"\"`. Como es usual en python, se usa para evitar que los caracteres de arriba se traten como especiales. Por ejemplo, si se desea escribir un patrón para los strings `""`, `"*"`, `"**"`, `"***"`, ..., se puede hacer con `"\**"`.

### Entendiendo la magia...
Entonces, `"[a-zA-Z0-9_]+@((ing|mat)\.)?p?uc.cl"` está diciendo que:
* `"[a-zA-Z0-9_]"` representa a una letra (tanto mayúsculas como minúsculas, sin considerar la ñ), un dígito del 0 al 9, o el caracter "_"
* Estos caracteres pueden aparecer una o más veces, pues están seguidos de `"+"`
* Luego, debe estar el caracter "@"
* Después, `"(ing|mat)\."` representa a las secuencias `"ing"` o `"mat"`, seguidas de un punto. Esto puede estar o no, ya que está seguida de `"?"`
* Puede o no estar el caracter `"p"`
* Debe terminar con `"uc.cl"`

### Conclusión (?)
* ¡No más funciones "a la antigua" para verificar cumplimiento de patrones en strings!
* Las expresiones regulares proporcionan una forma **optimizada**, **simple** y **comprensible** de hacer el mismo trabajo.
* ¡Hay varios otros caracteres especiales y funciones que pueden usar! Busquen en internet dependiendo de lo que quieran hacer.
