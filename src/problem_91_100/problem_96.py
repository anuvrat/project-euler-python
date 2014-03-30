'''
Created on Mar 31, 2014

@author: anuvrat

Use python 2.7 for this one
'''

from ortools.constraint_solver import pywrapcp

def read_puzzle(lines):
    puzzle_name = lines[0]
    puzzle = []
    
    for line in lines[1:]:
        puzzle.extend(map(int, list(line.strip())))
    
    return puzzle_name.strip(), puzzle

def solve_puzzle(lines):
    puzzle_name, puzzle = read_puzzle(lines)
    print(puzzle_name)
    
    solver = pywrapcp.Solver(puzzle_name)
    tiles = [solver.IntVar(1, 9, 'Tile-%i' % i) for i in range(81)]
    
    # rows all different condition
    for row in range(9):
        solver.Add(solver.AllDifferent(tiles[row * 9 : (row + 1) * 9]))
    
    # columns all different condition
    for column in range(9):
        solver.Add(solver.AllDifferent([tiles[column + 9 * i] for i in range(9)]))
    
    # blocks all different condition
    block_start = 0
    for block in range(9):
        block_tiles = []
        for a, b in ((i, j) for i in range(3) for j in range(3)):
            block_tiles.append(tiles[block_start + 9 * a + b])
        solver.Add(solver.AllDifferent(block_tiles))    
        block_start = block_start + 21 if block % 3 == 2 else block_start + 3
    
    # add known tile values
    for idx in range(81):
        tile_value = puzzle[idx]
        if tile_value != 0: 
            solver.Add(tiles[idx] == tile_value)
    
    solution = solver.Assignment()
    solution.Add(tiles)

    collector = solver.FirstSolutionCollector(solution)
    solver.Solve(solver.Phase(tiles, solver.CHOOSE_LOWEST_MIN, solver.ASSIGN_MIN_VALUE), [collector])
    
    solved_puzzle = map(str, [collector.Value(0, val) for val in tiles])
    
    # print solved puzzle
    for row in range(9):
        print(' '.join(solved_puzzle[row * 9 : (row + 1) * 9]))
    
    return int(solved_puzzle[0]) * 100 + int(solved_puzzle[1]) * 10 + int(solved_puzzle[2])

if __name__ == '__main__':
    input_data_file = open('/Users/anuvrat/git/project-euler-python/resource/problem_96_input.txt', 'r')
    lines = input_data_file.readlines()
    input_data_file.close()
    
    total = 0
    for idx in range(len(lines) / 10):
        total += solve_puzzle(lines[idx * 10 : (idx + 1) * 10])
        
    print(total)