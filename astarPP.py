import pygame
import heapq
import math
import random
import numpy as np
pygame.init()

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 600
blockSize = 40 #Set the size of the grid block
RADIUS = 75
obst_x = 300
obst_y = 300
GRID_SIZE = 40
DIAGONAL_COST = math.sqrt(GRID_SIZE**2 + GRID_SIZE**2)

screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])

# Define node class
class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = float('inf')
        self.f = float('inf')
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f

# Define heuristic function (Euclidean distance)
def heuristic(node1, node2):
    #z = math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)
    #print("heuristic", z)
    return math.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2)


def astar(start, goal, grid):
    # Initialize open and closed lists
    open_list = []
    closed_list = []
    # Initialize start node
    start.g = 0
    start.f = heuristic(start, goal)
    heapq.heappush(open_list, start)
    count = 0
    # Loop until goal is reached or open list is empty
    while len(open_list) > 0 :
        # Get node with minimum f value from open list
        print(len(open_list))
        current = heapq.heappop(open_list)
        print(len(open_list))
        # Check if goal is reached
        if (current.x == goal.x) and (current.y == goal.y):
            path = []
            while current is not None:
                path.append((current.x, current.y))
                current = current.parent
            return path[::-1]
        # Add current node to closed list
        closed_list.append(current)
        # Loop through neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                # Skip current node
                if i == 0 and j == 0:
                    continue
                # Calculate neighbor node position
                neighbor_x = current.x + i * GRID_SIZE
                neighbor_y = current.y + j * GRID_SIZE
                # Check if neighbor node is inside the grid
                if neighbor_x < 0 or neighbor_x > WINDOW_WIDTH or neighbor_y < 0 or neighbor_y > WINDOW_HEIGHT:
                    continue
                # Create neighbor node
                neighbor = Node(neighbor_x, neighbor_y)
                # Skip neighbor node if it's already in the closed list or is an obstacle
                if any((node.x == neighbor.x and node.y == neighbor.y) for node in closed_list) or grid[int(neighbor_x / GRID_SIZE)][int(neighbor_y / GRID_SIZE)] == 1:
                    continue
                # Calculate neighbor node g and f values
                if i == 0 or j == 0:
                    neighbor_g = current.g + GRID_SIZE
                    #print("neighbor_g1", neighbor_g)
                else:
                    neighbor_g = current.g + DIAGONAL_COST
                    #print("neighbor_g2", neighbor_g)
                neighbor_f = neighbor_g + heuristic(neighbor, goal)
                # Add neighbor node to open list
                if any((node.x == neighbor.x and node.y == neighbor.y) for node in open_list):
                    #print("hello1")
                    for node in open_list:
                        if node.x == neighbor.x and node.y == neighbor.y:
                            # print("hello2")
                            # print(node.f, neighbor_f)
                            # print("hello2")
                            if node.f > neighbor_f:
                                #print("hello3")
                                node.g = neighbor_g
                                node.f = neighbor_f
                                node.parent = current
                                #print("hi")
                            break
                else:
                    neighbor.g = neighbor_g
                    neighbor.f = neighbor_f
                    neighbor.parent = current
                    heapq.heappush(open_list, neighbor)
                print(len(open_list))
        print("end")
        count = count + 1

def drawGrid():

    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)

def set_obstacle(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            x = j*GRID_SIZE
            y = i*GRID_SIZE
            distance = math.sqrt((x - obst_x) ** 2 + (y - obst_y) ** 2)
            if(distance < RADIUS):
                grid[i][j] = 1

grid = np.zeros((int(WINDOW_WIDTH/GRID_SIZE)+1, int(WINDOW_HEIGHT/GRID_SIZE)+1), dtype=int)
set_obstacle(grid)

start = Node(0, 0)
goal_x = 10*GRID_SIZE
goal_y = 13*GRID_SIZE

goal = Node(goal_x, goal_y)

path = astar(start, goal, grid)

print(path)


running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    drawGrid()

    # Draw a solid blue circle in the center
    pygame.draw.circle(screen, (255, 0, 0), (obst_x, obst_y), RADIUS)

    pygame.draw.lines(screen, (0, 0, 255), False, path, 5)
    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
