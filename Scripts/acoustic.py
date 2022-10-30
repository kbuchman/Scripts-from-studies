# script with some most used constants and math operations in my acoustic calculations
from aenum import Constant
from math import  log10, pow, sqrt

class Constants(Constant):
    P0 = 2 * pow(10, -5)


class Math:

    def lp_to_p(value):
        return pow(10, (value / 20) + log10(Constants.P0))

    def p_to_pm(p):
        return p * sqrt(2)
    
    def pm_to_p(pm):
        return pm / sqrt(2)


print(Math.lp(5))