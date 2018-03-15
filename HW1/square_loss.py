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


def gradient_of_loss_function(a, b, data):
    J_a, J_b = .0, .0
    for d in data:
        J_a += (b + a*d[0] - d[1]) * d[0]
        J_b += b + a*d[0] - d[1]

    return J_a/len(data), J_b/len(data)



def linear_regression(data):

    def abs(x): return x if x>=0 else -x

    a, b = random.uniform(-10.0, 0.0), random.uniform(10.0, 50.0)
    alpha = 0.00013

    gradient = gradient_of_loss_function(a, b, data)
    while abs(gradient[0]) > 0.00013 or abs(gradient[1] > 0.00013):
        a -= alpha*gradient[0]
        b -= alpha*gradient[1]
        gradient = gradient_of_loss_function(a, b, data)
        # print a, b, loss_function(a, b, data)

    return a, b


def test(a, b, data):

    def h(a, b, x): return a*x + b

    for d in data:
        print d[0], d[1], h(a, b, d[0])


def main():
    filename = './4-data.txt'
    # filename = './5-trainingdata.txt'
    data = load_data(filename)
    
    a, b = linear_regression(data)
    # test(a, b, data)
    print 'a = ' + str(a) + ' b = ' + str(b)


if __name__ == '__main__':
    main()

