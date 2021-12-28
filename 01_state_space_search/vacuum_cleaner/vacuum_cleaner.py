# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 18:21:42 2021

@author: Dominik Chodounský
"""

import numpy as np
import time
from collections import deque

'''

Grid key:
0 - empty
1 - wall
2 - waste
3 - robot
4 - robot + waste

'''


def print_grid(grid): 
    """ Prints the grid in which the robot moves """
    print()
    for line in np.array(grid):
        print(line)

def generate_solutions(grid):
    """ Generates all possible finishing states """
    grid = np.array(grid)
    arr = grid.flatten()
    waste_cnt = np.count_nonzero(arr.flatten() == 2)
    solutions = []
    
    for i in range(waste_cnt): 
        w = 0
        solution = arr.copy()
        for j in range(len(solution)):
            if solution[j] == 3:
                solution[j] = 0
            if solution[j] == 2:
                if w == i:
                    solution[j] = 3
                else:
                    solution[j] = 0
                w += 1
        
        solutions.append(np.reshape(solution, (grid.shape[0], grid.shape[1])))
        
    return solutions
    

def generate_neighbours(grid):
    """ Generates neighbouring states based on all available actions for current state """
    neighbours = []
    arr = np.array(grid)
    height = arr.shape[0]
    width = arr.shape[1]
    
    robot_cnt = np.count_nonzero(arr.flatten() == 3)
    robot_waste_cnt = np.count_nonzero(arr.flatten() == 4)
    if robot_cnt + robot_waste_cnt > 1:
        print('Error: Multiple robots on the grid!')
        return None
    elif robot_cnt + robot_waste_cnt == 0:
        print('Error: No robot on the grid!')
        return None
    
    # if robot is standing on waste, next action is to vacuum it
    if robot_waste_cnt:
        robot_coord = np.argwhere(arr == 4)
        x_robot = robot_coord[0][0]
        y_robot = robot_coord[0][1]
        
        # vacuum current waste if robot is standing on it
        vacuum = arr.copy()
        vacuum[x_robot][y_robot] = 3
        neighbours.append(vacuum)
        #print_grid(vacuum)
        return neighbours
        
    # if robot is free-standing, it can move in 4 directions if it stays on the grid
    # and there are no obstacles in the way
    robot_coord = np.argwhere(arr == 3)
    x_robot = robot_coord[0][0]
    y_robot = robot_coord[0][1]    
        
    
    # movement to the right
    if y_robot < width - 1:
        right = arr[x_robot][y_robot + 1]
        
        # if there is no obstacle (either waste or empty space)
        if right != 1:
            n_right = arr.copy()
            n_right[x_robot][y_robot] = 0
            
            if right == 2:
                n_right[x_robot][y_robot + 1] = 4
            elif right == 0:
                n_right[x_robot][y_robot + 1] = 3
            else:
                print('Error: Unknown value on the grid')
                return None
                
            neighbours.append(n_right)
            #print_grid(n_right)
            
    # movement to the left
    if y_robot > 0:
        left = arr[x_robot][y_robot - 1]
        
        # if there is no obstacle (either waste or empty space)
        if left != 1:
            n_left = arr.copy()
            n_left[x_robot][y_robot] = 0
            
            if left == 2:
                n_left[x_robot][y_robot - 1] = 4
            elif left == 0:
                n_left[x_robot][y_robot - 1] = 3
            else:
                print('Error: Unknown value on the grid')
                return None
                
            neighbours.append(n_left)
            #print_grid(n_left)
    
    # movement up
    if x_robot > 0:
        up = arr[x_robot - 1][y_robot]
        
        # if there is no obstacle (either waste or empty space)
        if up != 1:
            n_up = arr.copy()
            n_up[x_robot][y_robot] = 0
            
            if up == 2:
                n_up[x_robot - 1][y_robot] = 4
            elif up == 0:
                n_up[x_robot - 1][y_robot] = 3
            else:
                print('Error: Unknown value on the grid')
                return None
                
            neighbours.append(n_up)
            #print_grid(n_up)

            
    # movement down
    if x_robot < height - 1:
        down = arr[x_robot + 1][y_robot]
        
        # if there is no obstacle (either waste or empty space)
        if down != 1:
            n_down = arr.copy()
            n_down[x_robot][y_robot] = 0
            
            if down == 2:
                n_down[x_robot + 1][y_robot] = 4
            elif down == 0:
                n_down[x_robot + 1][y_robot] = 3
            else:
                print('Error: Unknown value on the grid')
                return None
                
            neighbours.append(n_down)
            #print_grid(n_down)
    
    return neighbours


def BFS_fast(start, waste_cnt):
    """ 
    Uses BFS from start point to first piece of waste and then from that piece to the next
    and so on in an attempt to find the shortest path that covers all of them
    """
    # overall action plan
    complete_path = []
    
    for i in range(waste_cnt):
        q = deque()
        visited = {tuple()}
        path_to_next = []
        
        path_to_next.append(start)
        q.append(path_to_next)
        visited.add(tuple(start.flatten()))
        
        while q:
            curr = q.popleft()
            node = curr[-1]
            
            if np.count_nonzero(node.flatten() == 4):
                start = node.copy()
                start[start == 4] = 3
                
                # append actions to find certain piece of waste to the overall action plan
                for n in curr:
                    complete_path.append(n)
                break
            
            for n in generate_neighbours(node):
                
                if tuple(n.flatten()) not in visited:
                    visited.add(tuple(n.flatten()))
                    new_path = list(curr)
                    new_path.append(n)
                    q.append(new_path)
           
    complete_path.append(start)
    return complete_path
    


def BFS(start, end):
    """ Uses BFS to find shortest path between two states """
    q = deque()
    visited = {tuple()}
    path = []
    
    path.append(start)
    q.append(path)
    
    while q:
        curr = q.popleft()
        node = curr[-1]
        
        if np.array_equal(node, end):
            return curr
        
        for n in generate_neighbours(node):            
            if tuple(n.flatten()) not in visited:
                visited.add(tuple(n.flatten()))
                new_path = list(curr)
                new_path.append(n)
                q.append(new_path)
                
                
def naive_cleaner(grid):
    """ 
    Control function for the slower cleaner that uses BFS to determine which of
    the generted solutions is the closest to the starting state 
    """
    solutions = generate_solutions(grid)
    
    # search from all solutions towards start
    best_path = []
    best_length = np.inf
    for s in solutions:            
        path = BFS(grid, s)
        if len(path) - 1 < best_length:
            best_length = len(path) - 1
            best_path = path
    
        
    for i in range(len(best_path)):
        if i == 0:
            print('Start:')
        elif i == 1:
            print('\nAction plan:')
        print_grid(best_path[i])
        
    print('\nAction plan with cost: ' + str(len(best_path) - 1))
    
    
def fast_cleaner(grid, waste_cnt):  
    """ 
    Control function for the faster cleaner that uses BFS_fast to attempt to find
    the shortest path between all pieces of waste gradually
    """
    plan = BFS_fast(grid, waste_cnt)
    
    for i in range(len(plan)):
        if i == 0:
            print('Start:')
        elif i == 1:
            print('\nAction plan:')
        print_grid(plan[i])
        
    print('\nAction plan with cost: ' + str(len(plan) - 1))
    
def read_input(filename='./input3.txt'):
    waste_cnt = -1
    arr = []
    with open(filename) as file:
        i = 0
        for line in file:
            if i == 0:
                waste_cnt = int(line.strip())
            else:
                splits = line.split(',')
                arr.append( [int(x) for x in splits] )
            i += 1
    return np.array(arr), waste_cnt

if __name__ == "__main__":
    grid, waste_cnt = read_input('./input3.txt')
    
    start = time.time()
    #naive_cleaner(grid)
    fast_cleaner(grid, waste_cnt)
    print('Time: ' + str(time.time() - start))