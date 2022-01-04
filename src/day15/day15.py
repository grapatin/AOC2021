"""
Template code
"""#import cmath for complex number operations
#from abc import abstractproperty
#import cmath
#import Path for file operations
from pathlib import Path
import time
import sys
import heapq
from collections import defaultdict
from math import inf as INFINITY

PROGBLEM_INPUT_TXT = Path("/Users/pergrapatin/Source/AOC2021/src/"\
    +"day15/input.txt").read_text()

EXAMPLE_INPUT1 = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""
EXAMPLE_RESULT1 = 40

def recursive_walker(current_pos, storage_dict, current_sum, visited_dict, target_pos):
    global best_result
    current_sum += storage_dict[current_pos]

    if current_pos not in visited_dict or current_sum < visited_dict[current_pos]:
        if (current_sum < best_result):
            visited_dict[current_pos] = current_sum
            if current_pos != target_pos: #still not there
                y = current_pos[0]
                x = current_pos[1]
                new_pos = (y+1,x)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos)
                new_pos = (y,x+1)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos)
                new_pos = (y,x-1)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos)
                new_pos = (y-1,x)
                start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos)
            else:
                best_result = current_sum
                #print('New best result found', best_result)
                pass

def start_next_walk(storage_dict, current_sum, new_pos, visited_dict, target_pos):
    if new_pos in storage_dict:
        recursive_walker(new_pos, storage_dict, current_sum, visited_dict, target_pos)

def problem_a(input_string, expected_result):
    """Problem A solved function
    """
    pos_x = pos_y = 0

    storage_dict = {}
    visited_dict = {}
    rows = input_string.split('\n')
    for row in rows:
        for char in row:
            storage_dict[(pos_y,pos_x)] = int(char)
            pos_x += 1
        pos_y += 1
        pos_x = 0
    
    #current_pos = (0,0)
    #target_pos = max(storage_dict)
    #recursive_walker(current_pos, storage_dict, 0, visited_dict, target_pos)
    #print_state(visited_dict, rows)

    solution = dijkstra(storage_dict)
    if solution == expected_result:
        print("Correct solution found:", solution)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def print_state(visited_dict, rows):
    for y in range(len(rows)):
        for x in range(len(rows)):
            if (y, x) in visited_dict:
                print(visited_dict[(y,x)], end=' ')
            else:
                print('-', end='')
        print()




def problem_b(input_string, expected_result):
    """Problem A solved function
    """
    time_start = time.time()
    pos_x = pos_y = 0

    storage_dict = {}
    visited_dict = {}
    rows = input_string.split('\n')
    for row in rows:
        for char in row:
            storage_dict[(pos_y,pos_x)] = int(char)
            pos_x += 1
        pos_y += 1
        pos_x = 0
    
    org_dict = storage_dict.copy()

    for l in range(1, 5):
        for pos in org_dict:
            y, x = pos[0], pos[1]
            y += pos_y*l
            number = storage_dict[pos] + l
            if number == 10:
                number = 1
            elif number == 11:
                number = 2
            elif number == 12:
                number = 3
            elif number == 13:
                number = 4
            elif number == 14:
                number = 5
            storage_dict[(y,x)] = number

    org_dict = storage_dict.copy()
    for l in range(1, 5):
        for pos in org_dict:
            y, x = pos[0], pos[1]
            x += pos_y*l
            number = storage_dict[pos] + l
            if number == 10:
                number = 1
            elif number == 11:
                number = 2
            elif number == 12:
                number = 3
            elif number == 13:
                number = 4
            elif number == 14:
                number = 5
            storage_dict[(y,x)] = number


    #print_state(storage_dict, rows*5)
    current_pos = (0,0)
    target_pos = max(storage_dict)
    recursive_walker(current_pos, storage_dict, 0, visited_dict, target_pos)
    #print_state(visited_dict, rows*5)


    solution = visited_dict[target_pos] - visited_dict[(0,0)]
    if solution == expected_result:
        time_stop = time.time()

        print("Correct solution found:", solution, 'in time:', time_stop - time_start)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

def neighbors4(r, c, grid):
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        rr, cc = (r + dr, c + dc)
        if (rr, cc) in grid:
            yield rr, cc

def dijkstra(grid_dict):
    source = (0, 0)
    destination = max(grid_dict)

    # Start with only the source in our queue of nodes to visit and in the
    # mindist dictionary, with distance 0.
    queue = [(0, source)]
    mindist = defaultdict(lambda: INFINITY, {source: 0})
    visited = set()

    while queue:
        # Get the node with lowest distance from the queue (and its distance)
        dist, node = heapq.heappop(queue)

        # If we got to the destination, we have our answer.
        if node == destination:
            return dist

        # If we already visited this node, skip it, proceed to the next one.
        if node in visited:
            continue

        # Mark the node as visited.
        visited.add(node)
        r, c = node

        # For each unvisited neighbor of this node...
        for neighbor in neighbors4(r, c, grid_dict):
            if neighbor in visited:
                continue

            # Calculate the total distance from the source to this neighbor
            # passing through this node.
            newdist = dist + grid_dict[neighbor]

            # If the new distance is lower than the minimum distance we have to
            # reach this neighbor, then update its minimum distance and add it
            # to the queue, as we found a "better" path to it.
            if newdist < mindist[neighbor]:
                mindist[neighbor] = newdist
                heapq.heappush(queue, (newdist, neighbor))

    # If we ever empty the queue without entering the node == destination check
    # in the above loop, there is no path from source to destination!
    return INFINITY

def mebeim_solution(fin, expected_result):
    time_start = time.time()
    pos_x = pos_y = 0

    storage_dict = {}
    rows = fin.split('\n')
    for row in rows:
        for char in row:
            storage_dict[(pos_y,pos_x)] = int(char)
            pos_x += 1
        pos_y += 1
        pos_x = 0
    
    org_dict = storage_dict.copy()

    for l in range(1, 5):
        for pos in org_dict:
            y, x = pos[0], pos[1]
            y += pos_y*l
            number = storage_dict[pos] + l
            if number == 10:
                number = 1
            elif number == 11:
                number = 2
            elif number == 12:
                number = 3
            elif number == 13:
                number = 4
            elif number == 14:
                number = 5
            storage_dict[(y,x)] = number

    org_dict = storage_dict.copy()
    for l in range(1, 5):
        for pos in org_dict:
            y, x = pos[0], pos[1]
            x += pos_y*l
            number = storage_dict[pos] + l
            if number == 10:
                number = 1
            elif number == 11:
                number = 2
            elif number == 12:
                number = 3
            elif number == 13:
                number = 4
            elif number == 14:
                number = 5
            storage_dict[(y,x)] = number

    solution = dijkstra(storage_dict)
    
    if solution == expected_result:
        time_stop = time.time()
        print("Correct solution found:", solution, 'in time:', time_stop - time_start)
    else:
        print("Incorrect solution, we got:", solution, "expected:", expected_result)

best_result = 9999999999999
sys.setrecursionlimit(50000)
problem_a(EXAMPLE_INPUT1, EXAMPLE_RESULT1)
best_result = 9999999999
problem_a(PROGBLEM_INPUT_TXT, 769)
print("\n")

best_result = 99999999999
sys.setrecursionlimit(50000)
problem_b(EXAMPLE_INPUT1, 315)
mebeim_solution(EXAMPLE_INPUT1, 315)
best_result = 4001
#problem_b(PROGBLEM_INPUT_TXT, 2963) #this one worked but was extremly slow....
mebeim_solution(PROGBLEM_INPUT_TXT, 2963)
print("\n")
