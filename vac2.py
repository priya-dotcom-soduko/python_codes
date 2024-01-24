# Simulate a smart vaccuum cleaner that cleans a room size of nxn. The agent can move up, down, left and right.
# Calculate the overall performance.

import random
import time

# size of room is n
n = 3
room = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        room[i][j] = random.randint(0, 1)

 # reset data


def resett(i, j):
    room[i][j] = 0


def displayroom():
    for i in range(n):
        for j in range(n):
            print(str(room[i][j]), end=" ")
        print()


def clean_room():
    rows = 0
    cols = 0
    counter = 0
    while rows < n:
        print("Currently in location:", rows, cols)
        if room[rows][cols] == 1:
            resett(rows, cols)
            counter += 1
            print("|||| CLEANED ROOOM :::", rows,cols)
        cols += 1
        if cols % n == 0:
            cols = 0
            rows += 1
    return counter


print("The rooms in the beginning::")
displayroom()

start = time.time()
counter = clean_room()
end = time.time()
print("\nThe rooms after cleaning::")
displayroom()

performance = (counter/(n*n))*100
print("\nPerformance of the vaccum cleaner::", performance)
print("\nTotal number of rooms in the stimulation::", n*n)
print("\nTime Taken for all the rooms to be cleaned::",abs(end-start))
