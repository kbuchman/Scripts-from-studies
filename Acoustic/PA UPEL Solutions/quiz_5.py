# PA UPEL Quiz 5 solutions

from Scripts import acoustic as ac
from Scripts.get_values import get_value_from_text
from pyautogui import write, press
from keyboard import wait
import math as m


def task1():
    val_search = ((),)

    n = get_value_from_text(val_search)
    
    d = abs(m.log10(m.pow(10, (n / 10)) - 1))
    return ac.conv_ans(d)

def task2():
    val_search = (('akustycznej', 'W'),
                  ('o', 'm'),
                  ('i', 'm'))

    w, r1, r2 = get_value_from_text(val_search)

    lp1 = ac.Math.w_to_lw(w) - ac.Math.lr(r1)
    lp2 = ac.Math.w_to_lw(w) - ac.Math.lr(r2)
    return ac.conv_ans(ac.Math.lp_sum(lp1, lp2))

def task3():
    pass


def task4():
    pass


def main():
    wait('ctrl')
    x = task1()
    write(x, interval=0)
    press('tab', presses=3, interval=0)

    wait('ctrl')
    y = task2()
    write(y, interval=0)
    press('tab', presses=3, interval=0)

    wait('ctrl')
    v = task3()
    write(v, interval=0)
    press('tab', presses=3, interval=0)

    wait('ctrl')
    z = task4()
    write(z, interval=0)
    press('tab', presses=10, interval=0)

    ac.ans(1, x)
    ac.ans(2, y)
    ac.ans(3, v)
    ac.ans(4, z)
    

if __name__ == '__main__':
    main()