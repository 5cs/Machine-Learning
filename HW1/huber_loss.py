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
            if line == '':
                break
            if 'A' not in line:
                data.append([int(x) for x in line.split()])

    return data


def huber_loss_function(a, b, data, sigma):

    def square(x): return x*x
    def abs(x): return x if x>=0 else -x
    def h(a, b, x): return a*x + b

    s = .0
    for d in data:
        if abs(d[1]-h(a, b, d[0])) <= sigma:
            s += (1.0/2) * square(d[1] - h(a, b, d[0]))
        else:
            s += sigma * (abs(d[1]- h(a,b,d[0])) - (1.0/2)*sigma)

    return s/(2*len(data))


def gradient_of_huber_loss_function(a, b, data, sigma):
    
    def h(a, b, x): return a*x + b
    def abs(x): return x if x>=0 else -x
    
    J_a, J_b = .0, .0
    for d in data:
        if abs(d[1]-h(a, b, d[0])) <= sigma:
            J_a += (a*d[0] + b - d[1]) * d[0]
            J_b += a*d[0] + b - d[1]
        elif d[1] >= h(a, b, d[0]):
            J_a += -1 * sigma * d[0]
            J_b += -1 * sigma
        else:
            J_a += sigma * d[0]
            J_b += sigma

    return J_a/len(data), J_b/len(data)


def linear_regression(data):

    def abs(x): return x if x>=0 else -x

    a, b = random.uniform(-10.0, 0.0), random.uniform(10.0, 50.0)
    alpha = 0.0013
    sigma = 13

    gradient = gradient_of_huber_loss_function(a, b, data, sigma)
    while abs(gradient[0]) > 0.00013 or abs(gradient[1] > 0.00013):
        a -= alpha*gradient[0]
        b -= alpha*gradient[1]
        gradient = gradient_of_huber_loss_function(a, b, data, sigma)
        # print a, b, huber_loss_function(a, b, data, sigma)

    return a, b


def test(a, b, data):

    def h(a, b, x): return a*x + b

    for d in data:
        print d[0], d[1], h(a, b, d[0])

def main():
    filename = './5-trainingdata.txt'
    data = load_data(filename)
    
    a, b = linear_regression(data)
    # test(a, b, data)
    print 'a = ' + str(a) + ' b = ' + str(b)


if __name__ == '__main__':
    main()

