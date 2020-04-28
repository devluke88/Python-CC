#Cubes:

import matplotlib.pyplot as plt

# Data declaration
x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

# Making plot
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=10)

# Title of the graph and labels
ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Size of tick labels and axis range
ax.tick_params(axis='both', labelsize=14)
ax.axis([0, 5100, 0, 5100**3])

# Show plot
plt.show()