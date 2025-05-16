from typing import Tuple
import math

import numpy as np
import matplotlib.pyplot as plt


def line(xy1: Tuple, xy2: Tuple, color: str="#000000") -> None:

    x = [xy1[0], xy2[0]]
    y = [xy1[1], xy2[1]]

    plt.plot(x,
             y,
             linewidth=0.5,
             color=color)


def triangle(xy1: Tuple, xy2: Tuple, xy3: Tuple, color: str="#000000") -> None:

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

    end_deg = start_deg + sweep_deg

    start_rad = math.radians(start_deg)
    endrad = math.radians(end_deg)

    x = []
    y = []

    for a in np.arange(start_rad, endrad + 0.1, 0.1):

        x.append( (math.cos(a) * radius) + centre[0])
        y.append( (math.sin(a) * radius) + centre[1])

    plt.plot(x,
             y,
             linewidth=0.5,
             color=color)


def circle(centre:Tuple, radius:float, color: str="#000000") -> None:

    arc(centre, radius, 0, 360, color)


def draw(xlim:Tuple, ylim:Tuple, xticks:Tuple, yticks:Tuple, title:str) -> None:

    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xticks(range(xticks[0], xticks[1]))
    plt.yticks(range(yticks[0], yticks[1]))
    ax = plt.gca()
    ax.set_aspect("equal")

    plt.title(title)
    plt.grid(color='#C0C0FF')

    plt.show()