# coding=utf-8

from argparse import ArgumentParser


if __name__ == '__main__':
    parser = ArgumentParser(
        description='Pizzeria System',
        epilog="Copyleft @mrpatiwi",
    )

    parser.add_argument('order', help='Order a pizza')

    parser.add_argument(
        '-u',
        '--user',
        type=str,
        required=True,
        help="Customer username",
    )

    parser.add_argument(
        '-r',
        '--radius',
        type=int,
        default=22,
        help="Pizza radius",
    )

    parser.add_argument(
        '-i',
        '--ingredients',
        required=True,
        nargs='+',  # 1 or more | use '*' to accept zero or more
        help='Ingredients to add to the pizza',
    )

    args = parser.parse_args()

    if args.order:
        print('''
        Ordered:
        - Pizza with: {ingredients}
        - Size: {size}
        Customer: {customer}
        '''.format(
            ingredients=', '.join(args.ingredients),
            size=args.radius,
            customer=args.user
        ))
