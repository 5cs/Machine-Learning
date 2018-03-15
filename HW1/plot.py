# -*- coding: utf-8 -*-
import random
import math
import matplotlib.pyplot as plt
import numpy as np


def load_data(filename):
    data = []
    with open(filename) as inp:
        for line in inp.readlines():
            line = line.strip()
            if 'A' not in line:
                data.append([int(x) for x in line.split()])

    return data


def loss_function(a, b, data):

    def square(x): return x*x
    def h(a, b, x): return a*x + b

    s = .0
    for d in data:
        s += square(a*d[0]+b - d[1])

    return s/(2*len(data))


def main():
    filename = './5-trainingdata.txt'
    data = load_data(filename)
    x = [d[0] for d in data]
    y = [d[1] for d in data]
    
    a, b = -2.06992700152, 545.236509046
    a1, b1 = -2.45927631313, 558.451008291

    filename = './5-testdata.txt'
    data = load_data(filename)
    print 'square error function: a = ' + str(a) + ', ' + 'b = ' + str(b)
    print loss_function(a, b, data)
    print 'huber error function: a = ' + str(a1) + ', ' + 'b = ' + str(b1)
    print loss_function(a1, b1, data)

    plt.plot(x, y, 'ro')
    plt.plot([15, 90], [a*15+b, a*90+b], 'r--', label='square loss')
    plt.plot([15, 90], [a1*15+b1, a1*90+b1], 'b--', label='huber loss')
    plt.axis([0, 100, 0, 800])
    leg = plt.legend(loc='best', ncol=1, mode="expand")
    leg.get_frame().set_alpha(0.5)
    plt.show()


if __name__ == '__main__':
    main()

