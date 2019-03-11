# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import math
from BaseClassification import *
from level3_MultipleClassification import *

def ShowData(X,Y):
    for i in range(X.shape[1]):
        if Y[0,i] == 1:
            plt.plot(X[0,i], X[1,i], '.', c='r')
        elif Y[0,i] == 2:
            plt.plot(X[0,i], X[1,i], 'x', c='g')
        elif Y[0,i] == 3:
            plt.plot(X[0,i], X[1,i], '^', c='b')
        # end if
    # end for
    plt.show()

def ShowResult(X,Y,W,B,xt):
    for i in range(X.shape[1]):
        if Y[0,i] == 1:
            plt.plot(X[0,i], X[1,i], '.', c='r')
        elif Y[0,i] == 2:
            plt.plot(X[0,i], X[1,i], 'x', c='g')
        elif Y[0,i] == 3:
            plt.plot(X[0,i], X[1,i], '^', c='b')
        # end if
    # end for

    b12 = (B[1,0] - B[0,0])/(W[0,1] - W[1,1])
    w12 = (W[1,0] - W[0,0])/(W[0,1] - W[1,1])

    b23 = (B[2,0] - B[1,0])/(W[1,1] - W[2,1])
    w23 = (W[2,0] - W[1,0])/(W[1,1] - W[2,1])

    b13 = (B[2,0] - B[0,0])/(W[0,1] - W[2,1])
    w13 = (W[2,0] - W[0,0])/(W[0,1] - W[2,1])

    x = np.linspace(0,1,2)
    y = w13 * x + b13
    p13, = plt.plot(x,y)

    x = np.linspace(0,1,2)
    y = w23 * x + b23
    p23, = plt.plot(x,y)

    x = np.linspace(0,1,2)
    y = w12 * x + b12
    p12, = plt.plot(x,y)

    plt.legend([p13,p23,p12], ["13","23","12"])
    
    for i in range(xt.shape[1]):
        plt.plot(xt[0,i], xt[1,i], 'o')

    plt.axis([-0.1,1.1,-0.1,1.1])
    plt.show()


# 主程序
if __name__ == '__main__':
    # SGD, MiniBatch, FullBatch
    method = "FullBatch"
    # read data
    XData,YData = ReadData(x_data_name, y_data_name)
    X, X_norm = NormalizeData(XData)
    ShowData(XData, YData)
    num_category = 3
    Y = ToOneHot(YData, num_category)
    W, B = train(method, X, Y, ForwardCalculationBatch, CheckLoss)

    print("W=",W)
    print("B=",B)
    xt = np.array([5,1,7,6,5,6,2,7]).reshape(2,4,order='F')
    a, xt_norm, r = Inference(W,B,X_norm,xt)
    print("Probility=", a)
    print("Result=",r)
    ShowResult(X,YData,W,B,xt_norm)


