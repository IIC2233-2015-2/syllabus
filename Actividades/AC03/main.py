# coding=utf-8

# Defina la clase 'Rational' en este espacio


if __name__ == "__main__":
    r1 = Rational(26, 4)
    r2 = Rational(-2, 6)
    r3 = Rational(34, 7)

    # 13/2 -1/3 34/7
    print(r1, r2, r3, sep=", ")

    # [Rational(1), Rational(-11/2)]
    print([Rational(1, 1), Rational(22, -4)])

    # 41/6
    print(r1 - r2)

    # 221/7
    print(r1 * r3)

    # 7/5
    print(r2 / Rational(5, -7))

    # True
    print(Rational(-4, 6) < Rational(1, -7))

    # True
    print(Rational(12, 8) == Rational(-24, -16))
