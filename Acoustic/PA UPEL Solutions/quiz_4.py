# PA UPEL Quiz 4 solutions

from cmath import log10
import sys
sys.path.append(r'D:/Programming/Useful scripts for studies/')

from Scripts import acoustic as ac
from Scripts.get_values import get_value_from_text
from pyautogui import write, press
import keyboard
import math as m
import winsound


def task1():
    lp = get_value_from_text('równe', 'Pa')
    f = get_value_from_text('częstotliwości', 'Hz,')
    t = get_value_from_text('o', 's.')

    return ac.conv_ans(lp + 3 + (10 * m.log10(1 + m.cos(2 * m.pi * f * t))))


def task2():
    w1 = get_value_from_text('akustycznej', 'W')
    w2 = get_value_from_text('i', 'W.')
    r = get_value_from_text('odległości', 'm')

    # not sure about that
    lw12 = 10 * log10(abs(pow(10, (ac.Math.w_to_lw(w1))) - pow(10, (ac.Math.w_to_lw(w2)))))
    return ac.conv_ans(lw12 - 10 * log10(4 * m.pi * pow(r, 2)))

def test():
    l1 = 100
    s = 0.4
    w = 2
    l2 = 38.6

    # nah, not da way
    lir = ac.Math.i_to_li(w / s) - (10 * log10((4 * m.pi * pow(l1, 2)) / s))
    return ac.conv_ans((lir + (10 * log10((4 * m.pi * pow(l2, 2)) / s))) * s)


#def task3():
    l1 = get_value_from_text('długości', 'm')
    s = get_value_from_text('poprzecznym', 'm^2')
    w = get_value_from_text('mocy', 'W.')
    l2 = get_value_from_text('odległości', 'm')

    lir = ac.Math.i_to_li(w / s) - (10 * log10((4 * m.pi * pow(l1, 2)) / s))
    return ac.conv_ans((lir + (10 * log10((4 * m.pi * pow(l2, 2)) / s))) * s)

def main():
    print(test())

if __name__ == '__main__':
    main()


