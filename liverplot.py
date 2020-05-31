import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation as animation

# Remove toolbar. Will be useless with frequently plot
mpl.rcParams['toolbar'] = 'None'


def begin(file_name, x_axis, file_path='', filter_columns=None, fresh_rate=100, sample=-1, figsize=(15, 6)):
    fig = plt.figure(figsize=figsize)

    fig.canvas.set_window_title('Liverplot')

    def animate(i):
        df = pd.read_csv(file_path + file_name)

        # If user is going to plot specifc columns, he'll not pass the x_axis inside
        # filter_columns again. For this convenience, we shall add to the array
        columns = filter_columns + [x_axis] if filter_columns else df.columns

        # Tail do whats suppose to do. By default, Liverplot will plot the whole
        # dataframe, however, it's possible to plot only a sample
        df = df[columns].tail(sample)

        # Clear axis for next plot
        plt.cla()

        for column in df.columns:
            if column != x_axis:
                plt.plot(df[x_axis], df[column], label=column)

        plt.legend(loc='upper left')
        plt.tight_layout()

    ani = animation(fig, animate, interval=fresh_rate)

    plt.show()
