from functools import lru_cache

import numpy as np
from bokeh.io import curdoc
from bokeh.layouts import column, row, widgetbox
from bokeh.models import (Button, ColorBar, ColumnDataSource, ContinuousTicker,
                          HoverTool, Label, LinearColorMapper, Panel, Slider,
                          Tabs)
from bokeh.palettes import Greys, Viridis
from bokeh.plotting import figure

from spherical_harmonics import spherical_harmonics

# Quantum numbers
l_max = max([k[0] for k in spherical_harmonics.keys()])
l, m = 3, 2
z = 1.5

# Color Maps
greys = Greys[256]
viridis = Viridis[11]

# Plotting Data
@lru_cache(maxsize=None)
def update_plot(l, m, z):
    Y = spherical_harmonics[(l, m)](xx, yy, z)
    return [Y]

num = 400

x = np.linspace(-2 * np.pi, 2 * np.pi, num=num)
y = np.linspace(-2 * np.pi, 2 * np.pi, num=num)
xx, yy = np.meshgrid(x, y)

source = ColumnDataSource({'image': [0], 'x': [0], 'y': [0], 'dw': [num], 'dh': [num]})
source.data['image'] = update_plot(l, m, z)

# Set up figure
hover = HoverTool(tooltips=[(f'Y_lm: ', '@image{0.2f}')])
p1 = figure(x_range=(0, num), y_range=(0, num), toolbar_location=None, match_aspect=True, aspect_scale=1, tools="", css_classes=["figure"])
p1.add_tools(hover)
p1.axis.visible = False
color_mapper = LinearColorMapper(palette=greys, low=-0.6, high=0.6)
p1.image(image='image', source=source, x='x', y='y', dw='dw', dh='dh', color_mapper=color_mapper)
button = Button(label="Color Palette: Greys", css_classes=['btn-grey'])

def button_on_click():
    if color_mapper.palette == greys:
        color_mapper.palette = viridis
        button.label = "Color Palette: Viridis"
        button.css_classes = ['btn-viridis']

    else:
        color_mapper.palette = greys
        button.label = "Color Palette: Greys"
        button.css_classes = ['btn-grey']

button.on_click(button_on_click)


# Set up widgets
nlm_label = Label(x=0, y=0, text="Quantum Numbers", render_mode="canvas")
l_slider = Slider(title="l", value=l, start=0, end=l_max, step=1) # , height=250)
m_slider = Slider(title="m", value=m, start=-l, end=l, step=1) # , height=250)
z_slider = Slider(title='z', value=z, start=-10, end=10, step=0.1) # , height=250)


def update_on_l_change(attrname, old, new):
    global l, m, z, source
    needs_updating = True

    l = l_slider.value

    if not -l <= m <= l:
        m = 0
        needs_updating = False
        
    m_slider.value = m
    m_slider.start = -l
    m_slider.end = l

    if needs_updating:
        source.data['image'] = update_plot(l, m, z)


l_slider.on_change('value', update_on_l_change)


def update_on_m_change(attrname, old, new):
    global l, m, z, source

    m = m_slider.value

    source.data['image'] = update_plot(l, m, z)

m_slider.on_change('value', update_on_m_change)


def update_on_z_change(attrname, old, new):
    global l, m, z, source

    z = z_slider.value

    source.data['image'] = update_plot(l, m, z)

z_slider.on_change('value', update_on_z_change)


inputs = column(z_slider, l_slider, m_slider, button, sizing_mode="scale_width")

p1.sizing_mode = "scale_both"

output = row(inputs, p1, sizing_mode="scale_both")

output.margin = 0
output.spacing = 0

curdoc().add_root(output)

curdoc().title = "Spherical Harmonics"
