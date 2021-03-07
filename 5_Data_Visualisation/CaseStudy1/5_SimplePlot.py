"""
Let the x axis data points and y axis data points be X = [1,2,3,4] y = [20, 21, 20.5, 20.8]
5.1: Draw a Simple plot
5.2: Configure the line and markers in simple plot
5.3: configure the axes
5.4: Give title of Graph & labels of x axis and y axis
5.5: Give error bar if y_error = [0.12, 0.13, 0.2, 0.1]
5.6: define width, height as figsize=(4,5) DPI and adjust plot dpi=100
5.7: Give a font size of 14
"""

import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [20, 21, 20.5, 20.8]

fig, ax = plt.subplots(1, 2, figsize=(10, 5), dpi=100)
fig.tight_layout(h_pad=2)

plt.subplot(1, 2, 1)
plt.plot(x, y, ls=':', marker='D')
plt.title('With Line & Markers')

plt.grid()
plt.axis([0, 5, 19.8, 21.2])
plt.xlabel('X-Axis Data points')
plt.ylabel('Y-Axis Data points')

plt.subplot(1, 2, 2)
y_error = [0.12, 0.13, 0.2, 0.1]
plt.errorbar(x, y, yerr=y_error)
plt.title('With Error Bar')

plt.grid()
plt.axis([0, 5, 19.8, 21.2])
plt.xlabel('X-Axis Data points')

plt.subplots_adjust(top=0.85, bottom=0.1, left=0.08)
plt.suptitle('Simple Plot Example', fontsize=14)

plt.show()
plt.close()
