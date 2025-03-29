import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import imageio

# Create a new figure
fig, ax = plt.subplots()

# Initialize the x-axis values
x = np.arange(0, 2*np.pi, 0.01)

# Initialize the line plot
line, = ax.plot(x, np.sin(x))

# Set the axis limits
ax.set_ylim(-1.1, 1.1)

# Define the animation function
def animate(i):
    line.set_ydata(np.sin(x + i / 50))  # update the data.
    return line,

# Create the animation
ani = animation.FuncAnimation(
    fig, animate, interval=20, blit=True, save_count=50)

# Save the animation as a GIF
ani.save('animation.gif', writer='imagemagick')

# Alternatively, you can use imageio to save the animation as a GIF
# images = []
# for i in range(50):
#     line.set_ydata(np.sin(x + i / 50))
#     plt.draw()
#     images.append(np.array(plt.get_cmap('viridis')(plt.imshow(np.random.rand(10, 10)))))
# imageio.mimsave('animation.gif', images, 'GIF', duration=0.1)
