'''
Lie_theory.py, by MGD. Written in python 3.

Up to this point, this module will contain implementation of some
algorithms related to matrix Lie theory and matrix curve visualization
in 2 dimensions.

This module relies heavily on numpy, matplotlib and ffmpeg. Make
sure to have them installed.

TO-DO:
    -test this section.
'''
import numpy as np
import math
import matplotlib.pyplot as plt

def LeftMultiplication(A,X,Y):
    '''
    Given X and Y coming from an np.mgrid, LeftMultiplication returns
    the x coordinates U and the Y coordinates V of what results after
    multiplying the points (x;y) in the X,Y mgrid by A. That is, this
    function returns A*(x;y).
    
    A must be a 2x2 matrix, and X and Y must come from the same mgrid.

    Example: the snippet

        A = np.eye(2)
        X, Y = np.mgrid[-4:5,-4:5]
        U, V = LeftMultiplication(A,X,Y)

    returns U == X and Y == V, because A is precisely the identity.

    '''
    if np.shape(X) != np.shape(Y):
        raise ValueError('X and Y must come from the same np.mgrid')
    U, V = X.copy(), Y.copy()
    for i in range(0,len(X)):
        for j in range(0,len(X[0])):
            x = np.matrix([[X[i][j]],[Y[i][j]]])
            b = A*x
            # print(x,b)
            U[i][j] = float(b[0])
            V[i][j] = float(b[1])
    return U, V

def video_maker(video_name, X, Y, axis_limit, initial_time, final_time, step, curve):
    '''
    video_maker is a script which creates a video of a matrix curve.

    video_name: a string, the resulting video will be named [video_name].mp4
    X,Y: the result of an np.mgrid
    axis_limit: a positive float, the video will be a rectangle that
    measures -axis_limit times axis_limit in each axis.
    initial_time: the first value for t, where c(t) is the curve.
    final_time: the last value for t, where c(t) is the curve.
    step: the amount of time to be added in between each frame.
    curve: a matrix function c(t) which outputs two things: a matrix which
    depends on t, and a string that will go on the video's title.

    An example of a curve that could go in the parameters is:
    def c(t):
        return np.matrix([[t, t**2], [1, 2*t]]), 'A = [t, t**2;1,2t]'

    Thus, in the title would be the string 'A = [t, t**2;1,2t]'.
    '''
    figure_counter = 0
    time = initial_time
    empty, video_title = curve(float(time))
    while time <= final_time:
        plt.figure()
        A, empty2 = curve(float(time))
        U, V = LeftMultiplication(A, X, Y)
        plt.quiver(X,Y,U,V)
        plt.xlim(-axis_limit,axis_limit)
        plt.ylim(-axis_limit,axis_limit)
        plt.title(video_title + " t = %2.3f" % time)
        plt.savefig("fig%09i.png" % figure_counter, dpi=300)
        figure_counter += 1
        time += step
    os.system("ffmpeg -framerate 60 -i fig%09d.png -c:v libx264 -r 60 -pix_fmt yuv420p " + video_name)
    os.system("rm *.png")
