import plotly.graph_objects as go
import numpy as np
from plotly.figure_factory import create_quiver
from utilities import F, Var, MathNotation, LambdaNotation

colormap = {'math': 'blues', 'science': 'viridis', 'engineering': 'thermal', 'geoland': 'speed', 'geowater': 'tempo'}


def PlotFunc(fs, x0, x1, prec=10001):
    fig = go.Figure()
    xs = np.linspace(x0, x1, prec)
    fig.add_traces([go.Scatter(x=xs, y=[F(f, [x]) for x in xs], name=MathNotation(LambdaNotation(f))) for f in fs])
    fig.show()


def PlotScatter(data):
    fig = go.Figure()
    fig.add_traces([go.Scatter(x=d[0], y=d[1], name=d[2], mode='markers') for d in data])
    fig.show()


def PlotQuiver(f, x0, x1, y0, y1, n=21):
    xs, ys = np.linspace(x0, x1, n), np.linspace(y0, y1, n)
    us, vs, centers = [], [], [[], []]
    for y in ys:
        u, v = [], []
        for x in xs:
            vector = f(x, y)
            u.append(vector[0])
            v.append(vector[1])
            if vector[0] == 0 and vector[1] == 0:
                centers[0].append(x)
                centers[1].append(y)
        us.append(u)
        vs.append(v)
    xs, ys = np.meshgrid(xs, ys)
    fig = create_quiver(xs, ys, us, vs, scaleratio=1, name='vector')
    fig.add_trace(go.Scatter(x=centers[0], y=centers[0], mode='markers', name='null point'))
    fig.show()


def PlotPie(data):
    labels = [d[0] for d in data]
    values = [d[1] for d in data]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent', textposition='auto')])
    fig.show()


def PlotBar(data):
    fig = go.Figure(data=[go.Bar(x=d[0], y=d[1], name=d[2]) for d in data])
    fig.show()


def PlotNum(n):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=n, y=[0] * len(n), mode='markers', marker_size=12))
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, zeroline=True, zerolinecolor='black', zerolinewidth=3, showticklabels=False)
    fig.update_layout(height=200, plot_bgcolor='white')
    fig.show()


def PlotTable(f, x0, x1, step=1, r=4):
    f_name = MathNotation(LambdaNotation(f))
    var = MathNotation(Var(f))
    xs = [round(x, r) for x in np.arange(x0, x1 + step, step)]
    fs = [F(f, [x], n='undefined', r=r, is_round=True) for x in xs]
    fig = go.Figure(data=[go.Table(header=dict(values=[var, f_name]), cells=dict(values=[xs, fs]))])
    fig.show()


def PlotFunc3D(f, x0, x1, y0, y1, mode='', prec=101):
    x, y = np.linspace(x0, x1, prec), np.linspace(y0, y1, prec)
    xs, ys = np.meshgrid(x, y)
    z = np.array([F(f, (x, y)) for x, y in zip(np.ravel(xs), np.ravel(ys))])
    zs = z.reshape(xs.shape)
    fig = go.Figure(data=[go.Surface(x=xs, y=ys, z=zs, colorscale=colormap.get(mode, 'plasma'))])
    fig.update_layout(title=MathNotation(LambdaNotation(f)))
    fig.show()


def PlotScatter3D(data):
    fig = go.Figure(data=[go.Scatter3d(x=d[0], y=d[1], z=d[2], mode='markers') for d in data])
    fig.show()


def PlotQuiver3D(f, x0, x1, y0, y1, z0, z1, n=11, mode=''):
    fig = go.Figure()
    xs, ys, zs = np.linspace(x0, x1, n), np.linspace(y0, y1, n), np.linspace(z0, z1, n)
    xv, yv, zv, uv, vv, wv, centres = [], [], [], [], [], [], [[], [], []]
    for x in xs:
        for y in ys:
            for z in zs:
                v = f(x, y, z)
                xv.append(x)
                yv.append(y)
                zv.append(z)
                uv.append(v[0])
                vv.append(v[1])
                wv.append(v[2])
                if v[0] == 0 and v[1] == 0 and v[2] == 0:
                    centres[0].append(x)
                    centres[1].append(y)
                    centres[2].append(z)
    fig.add_trace(go.Cone(x=xv, y=yv, z=zv, u=uv, v=vv, w=wv, name='vector', colorscale=colormap.get(mode, 'plasma')))
    fig.add_trace(go.Scatter3d(x=centres[0], y=centres[1], z=centres[2], mode='markers', name='null point'))
    fig.show()
    
