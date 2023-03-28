import matplotlib.pyplot as plt
import numpy as np

# Define the size of the workspace and the obstacles
workspace_size = [100, 100]
obstacles = [[25, 25, 10], [60, 70, 15], [80, 40, 20]]

# Define the starting position of the robot
x = 50
y = 50

# Define the step size of the robot
step_size = 5

# Define the number of steps to take
num_steps = 5000

# Define the number of steps to walk in a straight line
num_straight_steps = 5

# Initialize the plot
fig, ax = plt.subplots()

# Set the limits of the plot
ax.set_xlim(0, workspace_size[0])
ax.set_ylim(0, workspace_size[1])

# Plot the obstacles
for obstacle in obstacles:
    circle = plt.Circle((obstacle[0], obstacle[1]), obstacle[2], color='r')
    ax.add_artist(circle)

# Define a function to check if the robot has collided with an obstacle
def check_collision(x, y):
    for obstacle in obstacles:
        distance = np.sqrt((x - obstacle[0])**2 + (y - obstacle[1])**2)
        if distance < obstacle[2]:
            return True
    return False

# Initialize the list to store the robot's path
path = [(x, y)]

# Initialize the direction to walk in
theta = np.random.uniform(0, 2*np.pi)

# Initialize the number of steps to walk in a straight line
num_steps_straight = num_straight_steps

# Perform the random walk algorithm
for i in range(num_steps):
    # Check if the robot has collided with an obstacle or the borders of the grid
    if check_collision(x + step_size*np.cos(theta), y + step_size*np.sin(theta)) or x + step_size*np.cos(theta) < 0 or x + step_size*np.cos(theta) > workspace_size[0] or y + step_size*np.sin(theta) < 0 or y + step_size*np.sin(theta) > workspace_size[1]:
        # Choose a random direction to move in
        theta = np.random.uniform(0, 2*np.pi)
        num_steps_straight = num_straight_steps
    else:
        # Update the position of the robot in the chosen direction
        x += step_size * np.cos(theta)
        y += step_size * np.sin(theta)

        # Decrease the number of steps to walk in a straight line
#        num_steps_straight -= 1

        # Check if the robot needs to change direction
 #       if num_steps_straight == 0:
  #          # Choose a random direction to move in
   #         theta = np.random.uniform(0, 2*np.pi)
    #        num_steps_straight = num_straight_steps

    # Add the new position to the path list
    path.append((x, y))

# Convert the path list to a numpy array
path = np.array(path)

# Plot the path of the robot
ax.plot(path[:,0], path[:,1], 'b-')

# Show the plot
plt.show()
