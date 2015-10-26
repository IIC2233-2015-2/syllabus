# Pizza System

## Usage:

See all available commands and options:
```
$ python3 pizza-system.py --help
```

Help menu:
```sh
usage: pizza-system.py [-h] -u USER [-r RADIUS] -i INGREDIENTS
                       [INGREDIENTS ...]
                       order

Pizzeria System

positional arguments:
  order                 Order a pizza

optional arguments:
  -h, --help            show this help message and exit
  -u USER, --user USER  Customer username
  -r RADIUS, --radius RADIUS
                        Pizza radius
  -i INGREDIENTS [INGREDIENTS ...], --ingredients INGREDIENTS [INGREDIENTS ...]
                        Ingredients to add to the pizza

Copyleft @mrpatiwi
```

### Example:
#### Using full-name flags:
```sh
python pizza-system.py order --user=User --ingredients tomate jamon queso
```

#### Short version:
```sh
python pizza-system.py order -u User -i tomate jamon queso
```

#### Using optional `radius`:
```sh
python pizza-system.py order --user User --ingredients piña -r 30
```

Output:
```sh
Ordered:
- Pizza with: piña
- Size: 30
Customer: User
```
