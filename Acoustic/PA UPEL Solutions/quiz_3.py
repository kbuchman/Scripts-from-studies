# PA UPEL Quiz 3 solutions

import math as m

def ans(num, value):
    return print(f'{num}. {value}')

def main():
    print('Solutions for tasks:\n')

    # task 1
    r = 14
    lp = 111.2
    lw = 10 * m.log10(4 * m.pi * m.pow(r, 2)) + lp
    w = m.pow(10, 0.1 * lw) * m.pow(10, -12)
    ans(1, w)

    # task 2
    x = 1.4
    lp = abs(10 * m.log10(m.pow((1 / x) / (2 * m.pow(10, -5)), 2)) - 10 * m.log10(m.pow(1 / (2 * m.pow(10, -5)), 2)))
    ans(2, lp)

    # task 3
    w = 2.6
    lp = 47.4
    lw = 10 * m.log10((w / m.pow(10, -12)))
    p = m.pow(10, ((lw - lp) / 10))
    r = m.sqrt(p / (4 * m.pi))
    ans(3, r)

    # task 4
    w = 5.9
    lp = 115
    r = 13
    lw = 10 * m.log10(w / m.pow(10, -12))
    temp = 10 * m.log10(4 * m.pi * m.pow(r, 2))
    n = m.pow(10, (lp - lw + temp) / 10)
    ans(4, n)


if __name__ == '__main__':
    main()