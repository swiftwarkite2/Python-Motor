import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import armParam as P
# if you are having difficulty with the graphics, 
# try using one of the following backends 
# See https://matplotlib.org/stable/users/explain/backends.html
# import matplotlib
# matplotlib.use('qtagg')  # requires pyqt or pyside
# matplotlib.use('ipympl')  # requires ipympl
# matplotlib.use('gtk3agg')  # requires pyGObject and pycairo
# matplotlib.use('gtk4agg')  # requires pyGObject and pycairo
# matplotlib.use('gtk3cairo')  # requires pyGObject and pycairo
# matplotlib.use('gtk4cairo')  # requires pyGObject and pycairo
# matplotlib.use('tkagg')  # requires TkInter
# matplotlib.use('wxagg')  # requires wxPython


class armAnimation:
    def __init__(self):
        # Used to indicate initialization
        self.flagInit = True
        # Initializes a figure and axes object
        self.fig, self.ax = plt.subplots()
        # Initializes a list object that will be used to
        # contain handles to the patches and line objects.
        self.handle = []
        self.length=P.length
        self.width=P.width
        # Change the x,y axis limits
        plt.axis([-2.0*P.length, 2.0*P.length, -2.0*P.length, 2.0*P.length])
        # Draw a base line
        plt.plot([0, P.length], [0, 0],'k--')

    def update(self, x):
        # Process inputs to function
        theta = x[0][0]   # angle of arm, rads
        ##X = [0, self.length*np.cos(theta)]  # X data points
        ##Y = [0, self.length*np.sin(theta)]  # Y data points
        # When the class is initialized, a line object will be
        # created and added to the axes. After initialization, the
        # line object will only be updated.
        pts =np.matrix([
            [self.width/2.0, -self.width/2.0],
            [self.width/2.0, -self.width/6.0],
            [self.width/2.0 + self.width/6.0, -self.width/6.0],
            [self.width/2.0 + self.width/6.0, self.width/6.0],
            [self.width/2.0, self.width/6.0],
            [self.width/2.0, self.width/2.0],
            [-self.width/2.0, self.width/2.0],
            [-self.width/2.0, self.width/6.0],
            [-self.width/2.0 - self.width/6.0, self.width/6.0],
            [- self.width/2.0 - self.width/6.0, -self.width/6.0],
            [- self.width/2.0, -self.width/6.0],
            [-self.width/2.0, -self.width/2.0]]).T
        R = np.array([[np.cos(theta), np.sin(theta)],
                      [-np.sin(theta), np.cos(theta)]])
        pts = R @ pts
        xy = np.array(pts.T)
        if self.flagInit == True:
            # Create the line object and append its handle
            # to the handle list.
            ##line, = self.ax.plot(X, Y, lw=5, c='blue')
            ##self.handle.append(line)
            ##self.flagInit=False
                 # Create the Rectangle patch and append its handle
            # to the handle list
            self.handle.append(mpatches.Polygon(xy,
                                                facecolor='blue',
                                                edgecolor='black'))
            # Add the patch to the axes
            self.ax.add_patch(self.handle[0]) 
            self.flagInit = False
        else:
            ##self.handle[0].set_xdata(X)   # Update the line
            ##self.handle[0].set_ydata(Y)
            self.handle[0].set_xy(xy) 
        plt.draw()
