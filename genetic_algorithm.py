import math
import random


def getPMXCrossover(state1, state2):
    offset = random.randint(1, len(state1) - 2)

    _state1 = list(state1)

    for index in range(offset):
        index_of_N_number_in = _state1.index(state2[index])
        _state1[index_of_N_number_in] = _state1[index]
        _state1[index] = state2[index]

    _state2 = list(state2)

    for index in range(offset):
        index_of_N_number_in = _state2.index(state1[index])
        _state2[index_of_N_number_in] = _state2[index]
        _state2[index] = state1[index]

    return _state1, _state2


def run(NUM, getRandomGen, calcHeuristicValue, onBest):
    num_of_gens = NUM * 5
    mutation_num = math.ceil(NUM * 0.2)

    gens = [getRandomGen(NUM) for _ in range(num_of_gens)]
    num_of_pairs = math.ceil((1 + math.sqrt(1 + 8 * num_of_gens / 2)) / 2)

    gen = None  # less is preferred
    check_on_satisfactory = None

    statistics = {'depth': 0, 'gen_num': len(gens)}

    while True:
        for index, _gen in enumerate(gens):
            gens[index] = [calcHeuristicValue(_gen), _gen]

        sorted_by_heuristic = sorted(gens, key=lambda row: row[0])[:num_of_pairs]

        if gen is None or gen[0] > sorted_by_heuristic[0][0]:
            gen = sorted_by_heuristic[0]
            check_on_satisfactory = math.ceil(num_of_gens / 2)
            onBest(gen, statistics['depth'], statistics['gen_num'])
        else:
            if check_on_satisfactory == 0:
                break
            else:
                check_on_satisfactory -= 1

        gens = [item for sublist in [
            getPMXCrossover(sorted_by_heuristic[i][1], sorted_by_heuristic[j][1]) for i in
            range(len(sorted_by_heuristic)) for j in range(i + 1, len(sorted_by_heuristic))
        ] for item in sublist]

        for item in gens[int(len(gens) / 2):]:
            indices = random.sample(range(NUM), mutation_num)
            temp = [item[i] for i in indices]

            # rotate elements in a temporary list
            temp = temp[1:] + temp[:1]

            # Replace original indices in item with rotated elements
            for i, idx in enumerate(indices):
                item[idx] = temp[i]

        statistics['gen_num'] += len(gens)
        statistics['depth'] += 1

    return gen
