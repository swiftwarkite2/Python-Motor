from matplotlib import get_backend
import matplotlib.pyplot as plt 
from matplotlib.lines import Line2D
import numpy as np

plt.ion()  # enable interactive drawing


class dataPlotter:
    def __init__(self):
        # Number of subplots = num_of_rows*num_of_cols
        self.num_rows = 3    # Number of subplot rows
        self.num_cols = 1    # Number of subplot columns
        # Crete figure and axes handles
        self.fig, self.ax = plt.subplots(self.num_rows, self.num_cols, sharex=True)
        # move_figure(self.fig, 500, 500)
        # Instantiate lists to hold the time and data histories
        self.time_history = []  # time
        self.theta_ref_history = []  # reference angle
        self.theta_history = []  # angle theta
        self.torque_history = []  # control torque
        self.thetadot_ref_history = []
        self.thetadot_history = []
        # create a handle for every subplot.
        self.handle = []
        self.handle.append(myPlot(self.ax[0], ylabel='theta(rotations)', title='Motor Wheel Data'))
        self.handle.append(myPlot(self.ax[1], xlabel='t(s)', ylabel='Voltage(V)'))
        self.handle.append(myPlot(self.ax[2], xlabel='t(s)', ylabel='thetadot(RPM)'))
        #self.handle.append(myPlot(self.ax[3], xlabel='t(s)', ylabel='torqe(N-m)'))


    def update(self, t, reference, states, ctrl):
        # update the time history of all plot variables
        self.time_history.append(t)  # time
        self.theta_ref_history.append(0.5/np.pi*reference)  # reference base position
        self.theta_history.append(0.5/np.pi*states[0,0])  # rod angle (converted to degrees)
        self.torque_history.append(ctrl)  # force on the base
        self.thetadot_ref_history.append(30/np.pi*reference)
        self.thetadot_history.append(30/np.pi*states[1,0])
        # update the plots with associated histories
        self.handle[0].update(self.time_history, [self.theta_history])#, self.theta_ref_history])
        self.handle[1].update(self.time_history, [self.torque_history])
        self.handle[2].update(self.time_history, [self.thetadot_history,self.thetadot_ref_history])
        #self.handle[3].update(self.time_history, [self.torque_history])

    def write_data_file(self):
        with open('io_data.npy', 'wb') as f:
            np.save(f, self.time_history)
            np.save(f, self.theta_history)
            np.save(f, self.torque_history)


class myPlot:
    ''' 
        Create each individual subplot.
    '''
    def __init__(self, ax,
                 xlabel='',
                 ylabel='',
                 title='',
                 legend=None):
        ''' 
            ax - This is a handle to the  axes of the figure
            xlable - Label of the x-axis
            ylable - Label of the y-axis
            title - Plot title
            legend - A tuple of strings that identify the data. 
                     EX: ("data1","data2", ... , "dataN")
        '''
        self.legend = legend
        self.ax = ax                  # Axes handle
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'b']
        # A list of colors. The first color in the list corresponds
        # to the first line object, etc.
        # 'b' - blue, 'g' - green, 'r' - red, 'c' - cyan, 'm' - magenta
        # 'y' - yellow, 'k' - black
        self.line_styles = ['-', '-', '--', '-.', ':']
        # A list of line styles.  The first line style in the list
        # corresponds to the first line object.
        # '-' solid, '--' dashed, '-.' dash_dot, ':' dotted

        self.line = []

        # Configure the axes
        self.ax.set_ylabel(ylabel)
        self.ax.set_xlabel(xlabel)
        self.ax.set_title(title)
        self.ax.grid(True)

        # Keeps track of initialization
        self.init = True   

    def update(self, time, data):
        ''' 
            Adds data to the plot.  
            time is a list, 
            data is a list of lists, each list corresponding to a line on the plot
        '''
        if self.init == True:  # Initialize the plot the first time routine is called
            for i in range(len(data)):
                # Instantiate line object and add it to the axes
                self.line.append(Line2D(time,
                                        data[i],
                                        color=self.colors[np.mod(i, len(self.colors) - 1)],
                                        ls=self.line_styles[np.mod(i, len(self.line_styles) - 1)],
                                        label=self.legend if self.legend != None else None))
                self.ax.add_line(self.line[i])
            self.init = False
            # add legend if one is specified
            if self.legend != None:
                plt.legend(handles=self.line)
        else: # Add new data to the plot
            # Updates the x and y data of each line.
            for i in range(len(self.line)):
                self.line[i].set_xdata(time)
                self.line[i].set_ydata(data[i])

        # Adjusts the axis to fit all of the data
        self.ax.relim()
        self.ax.autoscale()
        plt.draw()
           
def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    figmgr = plt.get_current_fig_manager()
    figmgr.canvas.manager.window.raise_()
    geom = figmgr.window.geometry()
    x,y,dx,dy = geom.getRect()
    figmgr.window.setGeometry(10, 10, dx, dy)
    # backend = get_backend()
    # if backend == 'TkAgg':
    #     f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    # elif backend == 'WXAgg':
    #     f.canvas.manager.window.SetPosition((x, y))
    # else:
    #     # This works for QT and GTK
    #     # You can also use window.setGeometry
    #     #f.canvas.manager.window.move(x, y)
    #     f.canvas.manager.setGeometry(x, y)

# f, ax = plt.subplots()
# move_figure(f, 500, 500)
# plt.show()
