#Write a function, in the programming language of your choice, which finds 
#contiguous regions (or "islands") in a matrix where all values in the 
#island are greater than a threshold (but not necessarily the same). The 
#function should take a threshold, a minimum island size, and an arbitrarily 
#sized matrix as inputs. The function should output a matrix (same size as 
#the input matrix) of booleans. Do not wrap around matrix edges. Corner 
#neighbors are not sufficient for island continuity. For example, if 
#the inputs are: threshold = 5, min island size = 3, and matrix = 
#[4, 4, 4, 2, 2; 4, 2, 2, 2, 2; 2, 2, 8, 7, 2; 2, 8, 8, 8, 2; 8, 2, 2, 2, 8]. 
#Then the output would be 
#[0, 0, 0, 0, 0; 0, 0, 0, 0, 0; 0, 0, 1, 1, 0; 0, 1, 1, 1, 0; 0, 0, 0, 0, 0].

import copy
import time

def find_islands(threshold, island_min, rows):

    rows_result = copy.deepcopy(rows)
    y = 0
    while (y < len(rows_result)):
        x = 0
        while (x < len(rows_result[y])):
            rows_result[y][x] = 0
            x += 1
        y += 1
    rows_result_final = copy.deepcopy(rows_result)

    #old stuff
    #rows = [[4,4,8,8,8], [4,2,2,2,7], [2,2,8,7,2], [2,8,8,8,2], [8,2,2,2,8]]
    #rows_result = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    #rows_result_final = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
    #threshold = 5
    #island_min = 3

    big_groups = []

    # print the give matrix
    def print_rows(matrix):
        y = 0
        while (y < len(matrix)):
            print("")
            x = 0
            while (x < len(matrix[y])):
                print(matrix[y][x], end= ", ")
                x += 1
            y += 1

    def find_neighbors(x,y):
        neighbors = []
        # y == len(rows) because len(rows) starts at 1 not 0
        if y+1 <= len(rows) -1:
            if rows[y+1][x] >= threshold:
                if rows_result[y+1][x] == 0:
                    neighbors.append([x,y+1])
                    rows_result[y+1][x] = group
        if y-1 >= 0:
            if rows[y-1][x] >= threshold:
                if rows_result[y-1][x] == 0:
                    neighbors.append([x,y-1])
                    rows_result[y-1][x] = group
        if x+1 <= len(rows[y]) -1:
            if rows[y][x+1] >= threshold:
                if rows_result[y][x+1] == 0:
                    neighbors.append([x+1,y])
                    rows_result[y][x+1] = group
        if x-1 >= 0:
            if rows[y][x-1] >= threshold:
                if rows_result[y][x-1] == 0:
                    neighbors.append([x-1,y])
                    rows_result[y][x-1] = group
        return neighbors

    def build_group(x, y, group):
        points = [[x,y]]
        # assign the initial point to its group
        rows_result[points[0][0]][points[0][1]] = group

        # repeat until the list is empty
        group_size = 0
        while len(points) > 0:
            #making point x and y readable
            x1 = points[0][0]
            y1 = points[0][1]
            
            # find neighbors of point and add them to the list
            for i in find_neighbors(x1,y1):
                points.append(i)
            # removes first item in list that was just processed
            points.pop(0)
            group_size += 1
        if group_size >= island_min:
            big_groups.append(group)


    # First iteration to find initial groups
    group = 1
    y = 0
    while (y < len(rows)):
        x = 0
        while (x < len(rows[y])):
            if rows[y][x] >= threshold:
                if rows_result[y][x] == 0:
                    build_group(x,y, group)
                    #print_rows(rows_result)
                    group += 1
            x += 1
        y += 1

    #print("")
    #print_rows(rows_result)
    #print("")

    # Print result
    y=0
    while (y < len(rows_result)):
        x = 0
        while (x < len(rows_result[y])):
            if rows_result[y][x] in big_groups:
                rows_result_final[y][x] = 1
            x += 1
        y += 1
    #print_rows(rows_result_final)

    return rows_result_final
        
# print the give matrix
def print_rows(matrix):
    y = 0
    while (y < len(matrix)):
        print("")
        x = 0
        while (x < len(matrix[y])):
            print(matrix[y][x], end= ", ")
            x += 1
        y += 1

start_time = time.time()

print_rows(find_islands(3, 3, [[6, 1, 5, 0, 9], [5, 8, 5, 4, 10],[1, 1, 10, 9, 6],[10, 7, 5, 7, 4],[3, 0, 5, 9, 2]]))

print("--- %s seconds ---" % (time.time() - start_time))


# main loop finds points where it reaches threshold and has not yet been assigned a group
# point gets sent to build_group function

# build_group:
# takes an origin point that meets threshold
# adds that point to the list of points to_process 
#   a) assing a group
#   b) find its neighbors that meet the threashold (result of find neighbors function)
#   c) adds those neighbors to the list to process (duplicates would be okay because it's just setting them to the group number again)
#   d) remove first item in list. repeat until list of to_process is empty


#find_neighbors:
# returns list of points