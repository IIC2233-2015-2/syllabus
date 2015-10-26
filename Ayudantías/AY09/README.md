# Ayudantía 9: Para la vida

## Python args

Seamos realistas, a nadie le gusta usar `input()` para pedir argumentos al usuario.

¿No sería más elegante usar algo de este estilo?:
```sh
python pizza-system.py order --user=User --ingredients tomate jamon queso
```

Ver [args](args)


## Git Avanzado

Hasta el momento, y a modo de repaso, solo sabemos hacer:
* `git clone`: Para clonar un repositorio
* `git pull`: Para bajar el estado final del repositorio en la nube
* `git add`: Para preparar los archivos a commitear (`stagging`)
* `git commit`: Guarda el estado de los archivos del paso anterior
* `git push`: Manda el estado del repositorio a la nube.

Esto es solo la punta del iceberg. Si bien satisface el uso diario, podemos encontrar muchos conflictos al trabajar en equipo, en proyectos grandes, al colaborar en el proyecto de alguien, etc.

### Conceptos y uso

#### Stash

A veces hay cambios que no queremos. Para esto podemos usar:
```sh
# Nos guardamos los cambios no-commiteados al 'bolsillo'
# Ahora el repositorio está limpio :)
# Por ejemplo: Podemos hacer un 'pull' limpio.
git stash
```

Para recuperar lo guardado:
```sh
git stash pop
```

#### Branch

![branches](https://www.atlassian.com/git/images/tutorials/collaborating/using-branches/01.svg)

Una rama, estas se desprenden de algún commit en específico de alguna rama. Todos los repositorios parten con la rama `master`.

Es muy probable al trabajar en equipo que hayan problemas de `merge` si todos trabajan en `master`

Si queremos desarrollar una *feature* o queremos hacer una prueba sin arriesgar lo que llevamos, nos conviene hacer todo eso en una branch. Una vez lista, hacemos el `merge` a la rama original. O simplemente descartamos la branch.

* `merge` es cuando se unen dos ramas. Git automáticamente se encarga de **solo mezclar los cambios que hayan ocurrido en esa branch**.

Uso de branches:
```sh
# Mostrar las branches
git branch
# > * master

# Crear branch llamada 'my-branch' (sin espacios)
git branch my-branch

# Mostrar las branches
git branch
# > * master
#     my-branch

# Para movernos a una branch:
git checkout my-branch
# > Switched to branch 'my-branch'

# Si hacemos git status nos muestra la branch actual
git status
# > On branch my-branch
# > nothing to commit, working directory clean

# Creemos un archivo y hagamos el commit a 'my-branch'
echo "Hello world" > file.txt
git add file.txt
git commit -m "add file with hello world"

# Podemos volver a 'master'
git checkout master

# Aquí el archivo 'file.txt' no existe
cat file.txt
# > cat: file.txt: No such file or directory

# Hacemos el merge de my-branch a master
# Ojo que debemos (y estamos) parados en 'master'
git merge my-branch
# > Updating 78a5e34..8fa6b18
# > Fast-forward
# >  file.txt | 1 +
# >  1 file changed, 1 insertion(+)
# >  create mode 100644 file.txt

# Ahora si existe
cat file.txt
# > Hello world

# Borramos la branch puesto que no la usaremos más
git branch -D my-branch
```

> En vez de crear archivos, también puedes modificar existentes y el procedimiento es el mismo.

Podemos subir branches al repositorio:
```sh
git branch development
git checkout development
git push --set-upstream origin development
```

#### Logs

Podemos ver el historial de commits con `log`:
```sh
git log
# > commit 2ca4120d2a02c1e37093835027e2911b6e1ec702
# > Author: Patricio López <lopezjuripatricio@gmail.com>
# > Date:   Mon Oct 19 11:10:41 2015 -0300
# >
# >     moved footer inside section
# >
# > commit 5fdb246bac71471fa6226a3780cfe6d3338e3cfd
# > Author: Patricio López <lopezjuripatricio@gmail.com>
# > Date:   Mon Oct 19 08:49:10 2015 -0300
# >
# >     css from http to https
# > ...
```

#### Viajar en el tiempo

Vemos el [`SHA`](https://en.wikipedia.org/wiki/SHA-1) del paso anterior:
```sh
# > ...
# > commit 5fdb246bac71471fa6226a3780cfe6d3338e3cfd <- ESTE!
# > Author: Patricio López <lopezjuripatricio@gmail.com>
# > ...
```

```sh
# Viajar al pasado
git checkout 5fdb246bac71471fa6226a3780cfe6d3338e3cfd
# No hagas cambios o la pasarás mal

# Volver al presente
git checkout master
```

Si queremos revertir hasta llegar a cierto commit:
```sh
# Esto crea un commit nuevo que revierte los cambios
# No los borra, así que es seguro
git revert 5fdb246bac71471fa6226a3780cfe6d3338e3cfd
```

Podemos hacer algo más destructivo y viajar al pasado y definirlo como presente:
```sh
git reset 5fdb246bac71471fa6226a3780cfe6d3338e3cfd --HARD
# Si habías hecho push de los cambios, vas a tener que usar al momento de subirlos:
# git push --force
# Esto es peligroso, hacerlo con mucho cuidado.
```

#### Remote

Es quien hospeda un repositorio. Por defecto partimos con `origin` que en nuestro caso es nuestro amigo *Github*.

```sh
git remote -v
# > origin	https://github.com/mrpatiwi/repositorio.git (fetch)
# > origin	https://github.com/mrpatiwi/repositorio.git (push)
```

Por ejemplo, podriamos tener una cuenta y un repositorio llamado `backup` en [Bitbucket.org](https://bitbucket.org/). Queremos subir nuestro repositorio de Github a este y llamar al remote *'respaldo'*:
```sh
git remote add respaldo https://bitbucket.org/mrpatiwi/backup.git
```

Ahora podemos hacer `push` a ese remote a la branch `master`:
```sh
git push respaldo master
```
