import random
import sys
import time

from utils import *

SIZE = 100
points = []


def getRandomGen(len):
    array = list(range(len))
    random.shuffle(array)
    return array


def calcHeuristicValue(state):
    heuristic = 0

    len_of_state = len(state)

    for index in range(len_of_state - 1):
        heuristic += distance(points[(state[index])], points[state[index + 1]])

    return heuristic


if __name__ == "__main__":
    def onBest(best, actual_depth, actual_gen_gen_num):
        drawState(best[1], points, SIZE)
        print(
            f"Best: {best[0]} | "
            f"Depth: {actual_depth} | "
            f"Gen Gen: {actual_gen_gen_num}",
            end="\r", flush=True)


    def g():
        from genetic_algorithm import run

        gen = run(NUM, getRandomGen, calcHeuristicValue, onBest)

        print('')
        print(f"Order: {gen[1]}")


    def t():
        from tabu_search_algorithm import run

        gen = run(NUM, getRandomGen, calcHeuristicValue, onBest)

        print('')
        print(f"Order: {gen[1]}")


    if len(sys.argv) > 2 and sys.argv[1] == '-a':
        NUM = 11
        if len(sys.argv) > 4 and sys.argv[3] == '-n':
            NUM = int(sys.argv[4])

        points = (lambda: [(random.randint(0, SIZE), random.randint(0, SIZE)) for _ in range(NUM)])()
        # points = [
        #     (50, 65),
        #     (36, 80),
        #     (70, 83),
        #     (13, 73),
        #     (10, 55),
        #     (94, 74),
        #     (35, 20),
        #     (90, 40),
        #     (50, 7)
        # ]

        timer = time.perf_counter()
        match sys.argv[2]:
            case 'g':
                g()
            case 't':
                t()
        print(f"Time: {round(abs(timer - time.perf_counter()), 4)} sec")
    else:
        print('use:\n   python main.py <algorithm> [options]')
        print('algorithm:\n  -a [g = genetic, t = tabu-search]')
        print('options:\n  -n [int(default=11)]')
