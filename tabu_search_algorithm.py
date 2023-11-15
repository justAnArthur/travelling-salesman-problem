def getNeighbors(state):
    swapped_arrs = []
    n = len(state)
    for i in range(n - 1):
        for j in range(i + 1, n):
            swapped_arr = list(state)  # Copy the given array.
            swapped_arr[i], swapped_arr[j] = swapped_arr[j], swapped_arr[i]  # Swap the two elements.
            swapped_arrs.append(swapped_arr)  # Add the altered array to the list.
    return swapped_arrs


def run(NUM, getRandomGen, calcHeuristicValue, onBest):
    tabu_list = []
    gen = [None, getRandomGen(NUM)]

    statistics = {'depth': 0, 'gen_num': 1}

    while True:
        gens = [(calcHeuristicValue(_gen), _gen) for _gen in getNeighbors(gen[1])]

        statistics['gen_num'] += len(gens)

        filter_by_tabu = [item for item in gens if item[1] not in tabu_list]

        sorted_by_heuristic = list(sorted(filter_by_tabu, key=lambda row: row[0]))

        if gen[0] is None or sorted_by_heuristic[0][0] < gen[0]:
            gen = sorted_by_heuristic[0]

            onBest(gen, statistics['depth'], statistics['gen_num'])

            for _gen in sorted_by_heuristic[1:]:
                tabu_list.append(_gen)
        else:
            break

        statistics['depth'] += 1

    return gen
