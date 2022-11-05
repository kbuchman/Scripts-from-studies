# PA UPEL Quiz 5 solutions
# current time record - 10 s 

import sys
sys.path.append(r'D:/Programming/Useful scripts for studies/')
from Scripts import acoustic as ac
from Scripts.get_values import get_value_from_text
from pyautogui import write, press
from keyboard import wait
import math as m


def task1():
    val_search = (('niż', 'dB)'),)

    n = get_value_from_text(val_search)[0]
    
    d = abs(10 * m.log10(m.pow(10, (n / 10)) - 1))
    return ac.conv_ans(d)

def task2():
    val_search = (('akustycznej', 'W'),
                  ('o', 'm'),
                  ('i', 'm'))
    val = get_value_from_text(val_search)

    w, r1, r2 = val[0], val[1], val[2]

    lp1 = ac.Math.w_to_lw(w) - ac.Math.lr(r1)
    lp2 = ac.Math.w_to_lw(w) - ac.Math.lr(r2)
    return ac.conv_ans(ac.Math.lp_sum(lp1, lp2))

def task3():
    val_search = (('akustycznej', 'W'),
                  ('odpowiednio', 'i'),
                  ('i', 'm'),
                  ('częstotliwości', 'Hz.'))
    val = get_value_from_text(val_search)

    w, r1, r2, f, = val[0], val[1], val[2], val[3]

    k = ac.Math.k(f)
    lpd = 10 * m.log10(1 + (2 * r1 * r2) / (m.pow(r1, 2) + m.pow(r2, 2)) * m.cos(k * (r1 - r2)))
    lp1 = ac.Math.w_to_lw(w) - ac.Math.lr(r1)
    lp2 = ac.Math.w_to_lw(w) - ac.Math.lr(r2)
    lp = ac.Math.lp_sum(lp1, lp2) + lpd
    return ac.conv_ans(lp)


def task4():
    val_search1 = (('Sygnał', 'Hz'),
                  ('mocy', 'W'),
                  ('odległości', 'm'))
    val = get_value_from_text(val_search1)

    f, w1, r1 = val[0], val[1], val[2]
    # fi is actually a constans in this task XD
    #val_search2 = (('o', 'Jeśli'),) 

    #str_fi = get_value_from_text(val_search2, str)[0]
    fi = m.pi / 4 #float(str_fi[3 : -1])

    k = ac.Math.k(f)
    r2 = ((m.pi - fi) / k) + r1
    w2 = (w1 * m.pow(r2, 2)) / m.pow(r1, 2)
    return ac.conv_ans(w2)


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
    press('enter', interval=0)

    ac.ans(1, x)
    ac.ans(2, y)
    ac.ans(3, v)
    ac.ans(4, z)
    

if __name__ == '__main__':
    main()