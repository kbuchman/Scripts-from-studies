# script with some most used constants and math operations in my acoustic calculations
from aenum import Constant
from math import  log10, pow, sqrt


def ans(num, value):
    return print(f'{num}. {value}')

    
def conv_ans(ans):
    return str(ans).replace('.', ',')


class Constants(Constant):
    P0 = 2 * pow(10, -5)
    W0 = pow(10, -12)
    I0 = pow(10, -12)


class Math:

    def w_to_lw(w):
        return 10 * log10((w / Constants.W0))

    def lw_to_w(lw):
        return pow(10, (lw / 10) + log10(Constants.W0))

    def li_to_i(li):
        return pow(10, (li / 10) + log10(Constants.I0))

    def i_to_li(i):
        return 10 * log10((i / Constants.I0))

    def lp_to_p(lp):
        return pow(10, (lp / 20) + log10(Constants.P0))

    def p_to_lp(p):
        return 10 * log10((pow(p, 2) / pow(Constants.P0, 2)))

    def p_to_pm(p):
        return p * sqrt(2)
    
    def pm_to_p(pm):
        return pm / sqrt(2)

