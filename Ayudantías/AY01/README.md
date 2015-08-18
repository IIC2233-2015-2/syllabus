# Ayudantía 01

## Solución AC01 y repaso para la AC02

Al final de la clase.

## Git

Git tiene muchas funciones, pero en este curso no usaremos tantas.

La primera vez deberás:

0. Tener el setup recomendado o un setup propio **bajo tu propia responsabilidad**.
1. Con la consola del sistema, clonar tu repositorio con el comando

```sh
# La convención para los repositorios es: <usuario gihub>-repo
# Reemplaza 'miusuario' por tu usuario en Github.
git clone https://github.com/IIC2233-2015-2/miusuario-repo.git
```

La URL de un repositorio siempre la puedes sacar de aquí:

![clone_url](https://cloud.githubusercontent.com/assets/7570744/9314102/25c70f8a-44fd-11e5-8631-367297cd0b50.jpg)

Ahora, cada vez que tengas que trabajar deberás hacer lo siguiente:

0. Hacer `git pull` para bajar la última versión del repositorio.
0. Hacer cambios. Crear, modificar o eliminar archivos y carpetas.
1. Iniciar o navegar con la consola al directorio de tu repositorio.
2. Colocar ``git add --all``
3. Colocar ``git commit -m "Lo que hice fue..."``
  0. Usa mensajes descriptivos para que cuando necesites volver a un commit anterior puedas encontrarlo fácilmente.
4. Colocar ``git push`` para guardar los cambios en la nube. **Sin este comando ¡nada ha sido enviado!**.
  0. Una de las razones típicas por la cual este comando puede fallar es cuando en la nube hay cambios que no tienes localmente.
  0. Para estos casos tienes que hacer `git pull --rebase`
  1. Con esto, git guarda temporalmente los cambios locales, baja los cambios en la nube y aplica encima los cambios que teníamos antes. Ahora podemos hacer `git push`.
5. **Se recomienda revisar en Github.com si efectivamente se subieron los cambios.**

Recomendamos guardar tu trabajo con frecuencia en la nube, pues sirve como respaldo en caso de una emergencia. Al momento de las correciones, se bajará hasta el último commit antes de la hora de entrega.

Git es super completo, por ejemplo: puedes borrar los últimos cambios o volver a un *commit* anterior. **Ante cualquier problema siempre encontrarás la solución buscando en Google.**

#### Interfaces visuales

También existen clientes para el uso de git. **Solo recomendamos su uso una vez entendido cómo funciona por medio de la linea de comandos**, porque ante cualquier problema o uso más avanzado a futuro, es poco probable que estos clientes te entregen todas las funcionalidades.

Recomendamos (bajo tu propia responsabilidad):
* [Github Desktop](https://desktop.github.com/)
* [SourceTree](https://www.sourcetreeapp.com/)

#### Github Explore

Para terminar el tema de Git, **ojalá se motiven con todo el tema de la programación. En Github encontrarán todo tipo de proyectos código abierto, ejemplos, lenguajes de programación, herramientas, guías, etc.** Aquí encontrarán lo último que pasa: [Github Explore](https://github.com/explore) 😄

#### Otros servicios de Git.

Github es la alternativa más popular, pero los repositorios privados fuera de fines académicos son costosos.

Otras alternativas son:
* [BitBucket](https://bitbucket.org/): ilimitados repositorios privados, pero solo hasta 5 colaboradores.
* [Gitlab](https://gitlab.com/): ilimitados repositorios privados con ilimitados colaboradores.

Puede que estos te sirvan para proyectos personales privados o para otros ramos 👌. **Para cualquier proyecto código abierto, usar Github (muchas empresas de desarrollo de software consideran a Github como parte del curriculum).**

## PEP8

Es una guía de estilo. Es para mantener un estandar estre los programadores dentro de un lenguaje, así tenemos un código homogeneo, bien sólido y más fácil de leer. **"un código es leído más veces de lo que es escrito"**.

Para este curso exigiremos que apliques al menos:

- No ocupar la letra 'ñ' ni tildes en nombres de métodos, variables o clases. En general, ocupar sólo para imprimir mensajes al usuario. No exigiremos que programes en inglés, pero sería lo ideal.
- Los nombres de clase empiezan con una mayúscula y son en singular.
  - Siendo más técnicos, se usa el estilo [UpperCamelCase](https://en.wikipedia.org/wiki/CamelCase)
   - `estrella_fugaz = ... ` ó `PERSONAS = ... ` :negative_squared_cross_mark:
   - `EstrellaFugaz = ... ` ó `Persona = ... `:  :ballot_box_with_check:
- Los nombres de métodos y variables son completamente en minúsucula. Por cada palabra nueva se coloca un guión bajo.
  - Siendo más técnicos, se usa el estilo [snake_case](https://en.wikipedia.org/wiki/Snake_case)
  - `nameGenerator = ... ` :negative_squared_cross_mark:
  - `name_generator = ... ` :ballot_box_with_check:
- Mantener una buena identación de **4 espacios** y **preferir los espacios** en vez de **tabs**.

#### Sobre la calidad del código en general.

Uno a veces puede pensar que agregar clases o métodos solo complica más las cosas, porque todo podría hacerse con listas, tuplas, if's y for's.

Efectivamente **todo podría hacerse con listas, tupas, if's y for's.** Sin embargo, terminaríamos con código imposibles de entender para personas ajenas a este y cualquier error sería muy dificil de encontrar. O ante cualquier necesidad de cambiar algo tendríamos que revisar cientos y cientos de lineas rebundantes.

![clone_url](https://qph.is.quoracdn.net/main-qimg-5f29964e3a61ba96b6ddb27d2283cec5?convert_to_webp=true)

**Puede que paresca lento programar bien desde el principio, pero te agradecerás a ti mismo al largo plazo.**

Por esta razón, ten en consideración:

* Hacer clases por sobre tuplas con valores heterogeneos.
* Hacer métodos reutilizables. No escribas un código dos veces. [Don't repeat yourself (DRY)](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).
* Mantener un orden y respetar convenciones.

La mejor manera de escribir buen código es:

### "Piensa que la persona que leerá tu código es un psicópata asesino que sabe donde vives."

