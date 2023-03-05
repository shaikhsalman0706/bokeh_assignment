from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
import random

# create a new plot with a line glyph
p = figure(title="Real-time Plot")
r = p.line(x=[], y=[], color="red")

# create a data source for the plot
source = ColumnDataSource(data=dict(x=[], y=[]))

# define a callback function that updates the plot data source
def update_data():
    new_data = dict(x=source.data['x'] + [random.random()*10],
                    y=source.data['y'] + [random.random()*10])
    source.data = new_data

# add the plot to the current document
curdoc().add_root(p)

# add a periodic callback that updates the plot data source every second
curdoc().add_periodic_callback(update_data, 1000)

# set the plot data source to the data source created earlier
r.data_source = source