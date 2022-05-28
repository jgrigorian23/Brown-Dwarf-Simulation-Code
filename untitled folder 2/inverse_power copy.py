import math
import random
from matplotlib import pyplot as plt



def f(x, m1, m2, alpha):
    if alpha == 1:
        return math.exp((x*(math.log(m2/m1)))+math.log(m1))
    else:
        return ((x*(((m2)**(1-alpha))-((m1)**(1-alpha))))+((m1)**(1-alpha)))**(1/(1-alpha))




def main(alpha, n):
    m1_a=0.01
    m1_b=0.005
    m1_c=0.001
    m2=0.1
    lst_1=[f(random.random(), m1_a, m2, alpha) for _ in list(range(n))]
    lst_2=[f(random.random(), m1_b, m2, alpha) for _ in list(range(n))]
    lst_3=[f(random.random(), m1_c, m2, alpha) for _ in list(range(n))]
    return [lst_1, lst_2, lst_3]