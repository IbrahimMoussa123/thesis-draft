import random
import matplotlib.pyplot as plt
import numpy as np

# Define the size of the area to be explored
width = 100
height = 100

# Define the starting position of the robot
x = random.randint(0, width)
y = random.randint(0, height)


# Define the number of steps the robot will take
num_steps = 70

# Define the positions of the obstacles
num_obstacles = 10
obstacle_positions = [(random.randint(0, width), random.randint(0, height)) for i in range(num_obstacles)]


# Define a function to check if a position is within the boundary of the area
def is_within_boundary(x, y):
    return x >= 0 and x <= width and y >= 0 and y <= height

# Define a function to calculate the potential field at a position
# def calculate_potential_field(x, y):
#     # Calculate the distance to each obstacle
#     distances = [np.sqrt((x-ox)**2 + (y-oy)**2) for ox, oy in obstacle_positions]
#     # Calculate the obstacle potential field
#     obstacle_field = sum([k_obstacle/d**2 for d in distances])
#     return obstacle_field

def obstacle_free(x, y):
    flag = True
    for i in range (len(obstacle_positions)):
        if (x == obstacle_positions[i][0] and y == obstacle_positions[i][1]):
            flag = False
            break
    return flag


# Define a function to move the robot in a straight line until it hits an obstacle or border, then turn in a random direction
def move_robot(x, y, dx, dy):

    while (is_within_boundary(x+dx, y+dy) and obstacle_free(x+dx, y+dy)):
        x += dx
        y += dy
    # If the robot hit an obstacle or border, turn in a random direction
    dx, dy = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1), (1, 2), (-1, -2), (1, -2), (-1, 2), (1, 3), (-1, -3), (1, -3), (-1, 3), (1, 4), (-1, -4), (1, -4), (-1, 4)])
    x_new = x + dx
    y_new = y + dy
    if (is_within_boundary(x_new, y_new) and obstacle_free(x_new, y_new)):
        return x_new, y_new, dx, dy

    return x, y, dx, dy

# Move the robot and record its path
print(obstacle_positions)
dx, dy = 1, 0 # Move in a straight line to start with
path = [(x, y)]
for i in range(num_steps):
    x, y, dx, dy = move_robot(x, y, dx, dy)
    path.append((x, y))
    print(path)

    print(x, y)

# Visualize the path of the robot and the obstacles
fig, ax = plt.subplots()
ax.scatter([p[0] for p in obstacle_positions], [p[1] for p in obstacle_positions], color='red', marker='s')
ax.plot([p[0] for p in path], [p[1] for p in path], color='blue')
ax.set_xlim([0, width])
ax.set_ylim([0, height])
plt.show()
