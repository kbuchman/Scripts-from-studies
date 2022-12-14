# PA UPEL Quiz 4 solutions
# using old version of get_value_from_text, needs a patch

from cmath import log10
import sys
sys.path.append(r'D:/Programming/Useful scripts for studies/')

from Scripts import acoustic as ac
from Scripts.get_values import get_value_from_text
from pyautogui import write, press
from keyboard import wait
import math as m


def task1():
    p = 10.6#get_value_from_text('równe', 'Pa,')
    f = 3409.9#get_value_from_text('częstotliwości', 'Hz,')
    t = 0.18#get_value_from_text('o', 's.')

    return ac.conv_ans(ac.Math.p_to_lp(p) + 3 + (10 * m.log10(1 + m.cos(2 * m.pi * f * t))) - 3) # -3 because teacher made a mistake


def task2():
    w1 = 12#get_value_from_text('akustycznej', 'W')
    w2 = 4#get_value_from_text('i', 'W.')
    r = 213.2#get_value_from_text('odległości', 'm')

    #print(w1, w2, r)

    lw12 = 10 * log10(pow(10, (ac.Math.w_to_lw(w1) / 10)).real + pow(10, (ac.Math.w_to_lw(w2) / 10)).real)
    return ac.conv_ans(lw12.real - (10 * log10(4 * m.pi * pow(r, 2))).real)

def test():
    p = 14.3
    f = 1353.9
    t = 0.328

    return ac.conv_ans(ac.Math.p_to_lp(p) + 3 + (10 * m.log10(1 + m.cos(2 * m.pi * f * t))) - 3) # -3 because teacher made a mistake


def task3():
    #l1 = get_value_from_text('długości', 'm')  no need to use it
    s = 0.4#get_value_from_text('poprzecznym', 'm*?2', True)
    w = 3.4#get_value_from_text('mocy', 'W.')
    l2 = 61.7#get_value_from_text('odległości', 'm')

    lir = ac.Math.i_to_li(w / s) + (10 * log10((4 * m.pi * pow(l2, 2))))
    return ac.conv_ans(ac.Math.lw_to_w(lir.real))

def main():
    print(task1())
    print(task3())
    '''wait('ctrl')
    x = task1()
    write(x, interval=0)
    press('tab', presses=3, interval=0)

    wait('ctrl')
    y = task2()
    write(y, interval=0)
    press('tab', presses=3, interval=0)

    wait('ctrl')
    z = task3()
    write(z, interval=0)
    press('tab', presses=10, interval=0)

    ac.ans(1, x)
    ac.ans(2, y)
    ac.ans(3, z)'''
    

if __name__ == '__main__':
    main()

