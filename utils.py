import math

import matplotlib.pyplot as plt

plt.figure()


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def calcPointsNum(lines):
    # Solve the quadratic equation n(n-1)/2 = lines for n
    return math.ceil((1 + math.sqrt(1 + 8 * lines)) / 2)


def drawState(state, points, SIZE):
    _points = [points[i] for i in state]

    x, y = zip(*[(point[0], point[1]) for point in _points])

    plt.clf()
    plt.xlim(0, SIZE)
    plt.ylim(0, SIZE)

    plt.scatter(x, y, color='b')  # Plot points
    plt.plot(x + x[:1], y + y[:1], color='r')  # Plot lines

    plt.draw()
    plt.grid(True)
    plt.pause(0.5)  # Adjust to needed delay
