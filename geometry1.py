from typing import Tuple
import math

import numpy as np
import matplotlib.pyplot as plt


def line(xy1: Tuple, xy2: Tuple, color: str="#000000") -> None:

    '''
    Draws a line between the points with 
    coordinates in the xy1 and xy2 tuples.
    '''

    # for Matplotlib we need the x and y 
    # coordinates as separate tuples
    x = (xy1[0], xy2[0])
    y = (xy1[1], xy2[1])

    plt.plot(x,
             y,
             linewidth=0.5,
             color=color)


def triangle(xy1: Tuple, xy2: Tuple, xy3: Tuple, color: str="#000000") -> None:

    '''
    Draw a triangle with corners at the 
    coordinates in the 3 xy tuples.
    '''

    # This is a slicker way of drawing a circle
    # but calling the line function is more
    # in accord with the manual process of 
    # drawing a circle with pencil and paper.
    # x = [xy1[0], xy2[0], xy3[0], xy1[0]]
    # y = [xy1[1], xy2[1], xy3[1], xy1[1]]

    # plt.plot(x,
    #          y,
    #          linewidth=0.5,
    #          color=color)

    line(xy1, xy2, color)
    line(xy2, xy3, color)
    line(xy3, xy1, color)


def arc(centre:Tuple, radius:float, start_deg:float, sweep_deg:float, color: str="#000000") -> None:

    '''
    Draws a section of a circle with specified centre and radius.
    start_deg is from the 3 o'clock position and sweep 
    is measured anti-clockwise.
    This function can be used to draw a circle with a sweep_deg
    argument of 360.
    '''

    # the sweep is more convenient for 
    # calling code but to draw an arc
    # we need the ending angle
    end_deg = start_deg + sweep_deg

    # the trigonometric functions have radian
    # arguments so are converted here.
    start_rad = np.radians(start_deg)
    end_rad = np.radians(end_deg)

    # an array of radians between required angles
    # with a 0.1rad interval.
    # (Might need to descrease the interval for larger radii.)
    radians = np.arange(start_rad, end_rad + 0.1, 0.1)

    # These calculations use the radians Numpy array
    # and so return new Numpy arrays, with the loops
    # abstracted away.
    # The brackets round the first terms aren't 
    # necessary but make things a bit clearer.
    x = (np.cos(radians) * radius) + centre[0]
    y = (np.sin(radians) * radius) + centre[1]

    plt.plot(x,
             y,
             linewidth=0.5,
             color=color)


def circle(centre:Tuple, radius:float, color: str="#000000") -> None:

    '''
    Draws a circle with specified centre and radius
    '''

    arc(centre, radius, 0, 360, color)


def draw(xlim:Tuple, ylim:Tuple, xticks:Tuple, yticks:Tuple, title:str) -> None:

    '''
    To be called after all required elements have been 
    added to finish and show the drawing.
    '''

    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xticks(range(xticks[0], xticks[1]))
    plt.yticks(range(yticks[0], yticks[1]))
    ax = plt.gca()
    ax.set_aspect("equal")

    plt.title(title)
    plt.grid(color='#C0C0FF')

    plt.show()