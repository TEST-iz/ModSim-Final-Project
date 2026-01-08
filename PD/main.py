
# main.py
# Author sahwho
# This file serves as a reference for creating scatter plots with sizes
# for mod/sim project1, fall 2024 (MBHS)
import matplotlib.pyplot as plt

# assume that P1 has a the following preferences for Strategy 1 (note the string of 1.0s at the end)
# p1Strats = [0.5, 0.49, 0.47, 0.48, 0.5, 0.55, 0.61, 0.63, 0.68, 0.71, 0.74, 0.76, 0.79, 0.81, 0.95, 0.99, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]

# we need the unique values for our graph (we don't want to plot the same value over and over).
# Repeated values will have that fact reflected in their **size**, or a count of that value
# convert to a Set to have the unique values
# https://stackoverflow.com/questions/12897374/get-unique-values-from-a-list-in-python
# p1StratsUnique = set(p1Strats)
# convert back into a list
# p1XVals = list(p1StratsUnique)

# https://stackoverflow.com/questions/10741346/frequency-counts-for-unique-values-in-a-numpy-array
# unique, counts = np.unique(p1XVals, return_counts=True)

# the same procedure could be done for P2

# P1 Preferences (Dummy Data)
P1y = [1.0, 0.91, 0.75, 0.63, 0.52, 0.44]
P1x = []
for P1yVal in P1y:
    P1x.append(1-P1yVal) # generate the x value as 1-y

# P1 Sizes (Dummy Data)
P1sizes = [1, 700, 225, 40, 20, 10]

# P2 Preferences (Dummy Data)
P2y = [1.0, 0.98, 0.85, 0.75, 0.61, 0.54]
P2x = []
for P2yVal in P2y:
    P2x.append(1-P2yVal) # generate the x value as 1-y

# P2 Sizes (Dummy Data)
P2sizes = [1, 450, 175, 50, 30, 15]

# plot
fig, ax = plt.subplots()

# adjusting transparency of scatter points by using 'alpha' parameter
# https://dfrieds.com/data-visualizations/customize-scatter-plot-styles-python-matplotlib.html#adjust-the-size-of-scatter-points
ax.scatter(P1x, P1y, s=P1sizes, c='blue', label='P1', alpha=0.3)
ax.scatter(P2x, P2y, s=P2sizes, c='orange', label='P2', alpha=0.4)

# labels and title
ax.set_xlabel('quiet', fontsize=10)
ax.set_ylabel('confess', fontsize=10)
ax.set_title('Prisoner\'s Dilemma')

# show grid
ax.grid(True)

# create some mock scatterpoints for the legend, otherwise
# the circles in the legend are too big
# this seems like not the best way to do it but i'm tired
p1LegendX = [0.5]
p1LegendY = [0.5]
p1LegendSize = [50]
p1CollectionLegend = ax.scatter(p1LegendX, p1LegendY, s=p1LegendSize, c='blue', alpha=0.3)

p2LegendX = [0.5]
p2LegendY = [0.5]
p2LegendSize = [50]
p2CollectionLegend = ax.scatter(p2LegendX, p2LegendY, s=p2LegendSize, c='orange', alpha=0.4)

plt.legend([p1CollectionLegend, p2CollectionLegend], ['P1', 'P2'])
# end legend code

# show plot
plt.show()