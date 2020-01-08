from math import pi

from bokeh.layouts import column, row, widgetbox
from bokeh.models import ColumnDataSource, Slider, HoverTool
from bokeh.models.callbacks import CustomJS
from bokeh.plotting import figure, show
from pscript import py2js

try:
    from no_server import sh_funcs
except:
    import sh_funcs

def plot(num=50, lo=-2*pi, hi=2*pi, z=1.5, l=3, m=2):
    source = ColumnDataSource({
        'image': [None],
        'x': [0],
        'y': [0],
        'dw': [num],
        'dh': [num],
        'num': [num],
        'lo': [lo],
        'hi': [hi],
        'z': [z],
        'l': [l],
        'm': [m],
    })

    sh_funcs.update(source)

    js_code = py2js(sh_funcs)

    p = figure(x_range=(0, num), y_range=(0, num), toolbar_location=None, match_aspect=True, aspect_scale=1, tools="",)
    p.axis.visible = False
    p.image(image='image', x='x', y='y', dw='dw', dh='dh', source=source)
    hover = HoverTool(tooltips=[(f'Y_lm: ', '@image{0.2f}')])
    p.add_tools(hover)


    z_slider = Slider(start=-10, end=10, value=0.4, step=.1, title="z",
                        callback=CustomJS(args={'source': source}, code=js_code + """\n
                        source.data['z'] = [cb_obj.value];
                        update(source);
                        source.change.emit();
                        """))

    m_slider = Slider(start=-l, end=l, value=m, step=1, title='m',
                        callback=CustomJS(args={'source': source}, code=js_code + """\n
                        source.data['m'] = [cb_obj.value];
                        update(source);
                        source.change.emit();
                        """))

    l_slider = Slider(start=0, end=4, value=l, step=1, title="l",
                        callback=CustomJS(args={'source': source, 'm_slider': m_slider}, code=js_code + """\n
                        source.data['l'] = [cb_obj.value];
                        let m = m_slider.value;
                        let l = cb_obj.value;
                        if (m > l || m < -l) {
                        m = 0;
                        }
                        m_slider.start = -l;
                        m_slider.end = l;
                        m_slider.value = m;
                        source.data['m'] = [m];
                        update(source);
                        source.change.emit();
                        """))

    sliders = column(z_slider, l_slider, m_slider, sizing_mode="scale_width")
    layout = row(sliders, p, sizing_mode="scale_both")
    
    return layout

if __name__ == "__main__":
    show(plot())