# https://www.acmicpc.net/problem/1969
import sys

def solve_easy_version():
    N, M = map(int, sys.stdin.readline().split())

    dna_list = []
    for _ in range(N):
        dna_list.append(sys.stdin.readline().rstrip())

    bestcase = ""
    totalvalue = 0

    for col_index in range(M):
        dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

        for row_index in range(N):
            character = dna_list[row_index][col_index]
            dict[character] += 1

        maxvalue = -1
        onebest = ''

        for char_type in ['A', 'C', 'G', 'T']:
            case = dict[char_type]

            if case > maxvalue:
                maxvalue = case
                onebest = char_type

        bestcase += onebest

        totalvalue += (N - maxvalue)

    print(bestcase)
    print(totalvalue)

solve_easy_version()
