import random
from matplotlib import pyplot as plt

def f(x, t1, t2):
    return ((t2-t1)*x)+t1

def main(n):
    t1=0
    t2=10

    lst=[f(random.random(), t1, t2) for _ in list(range(n))]

    return lst
