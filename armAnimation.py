# I created this file from the following github https://github.com/byu-controlbook/controlbook_public
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import armParam as P



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
        # line object will only be updated.
        # The following 13 lines of code are used the create the shape of the image that is shown when running my simulation
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
        R = np.array([[np.cos(theta), np.sin(theta)], # This and the following 3 lines are used to  
                                                        # spin the object when simulated
                      [-np.sin(theta), np.cos(theta)]])
        pts = R @ pts
        xy = np.array(pts.T)
        if self.flagInit == True:

            # to the handle list
            self.handle.append(mpatches.Polygon(xy,
                                                facecolor='blue', # This line creates the blue color of my shape
                                                edgecolor='black')) # This line creates the black edge of my shape
            # Add the patch to the axes
            self.ax.add_patch(self.handle[0]) # this line makes the dashed black line to 
                                                # represent the motor

            self.flagInit = False
        else:

            self.handle[0].set_xy(xy) 
        plt.draw()
