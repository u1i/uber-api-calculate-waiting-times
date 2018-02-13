import plotly.plotly as py
from plotly.graph_objs import *
py.sign_in('username', 'api_key')
trace1 = {
  "x": ["142", "427", "201", "669", "717", "791", "784", "779", "1005", "426", "489", "588", "563", "308", "169", "578", "418", "442", "341", "224", "350", "572", "698", "635", "1470", "598", "1315", "436", "247", "648", "548", "552", "663", "419", "738", "582", "747", "521", "383", "684", "258", "396", "418", "1359", "1314", "406", "430", "301", "696", "364"], 
  "autobinx": True, 
  "autobiny": True, 
  "hoverinfo": "none", 
  "marker": {"line": {"width": 2.5}}, 
  "name": "Wait Time (Seconds)", 
  "opacity": 0.9, 
  "orientation": "v", 
  "type": "histogram", 
  "uid": "5ea3c5", 
  "xbins": {
    "end": 1599.5, 
    "size": 200, 
    "start": -0.5
  }, 
  "xsrc": "u1i:0:14d8f6", 
  "ybins": {
    "end": 1499.5, 
    "size": 500, 
    "start": -0.5
  }
}
data = Data([trace1])
layout = {
  "annotations": [
    {
      "x": 0.0266666666667, 
      "y": 1.0570719603, 
      "showarrow": False, 
      "text": "Data Source: https://api.uber.com/v1.2/history?limit=50", 
      "xref": "paper", 
      "yref": "paper"
    }
  ], 
  "autosize": True, 
  "bargroupgap": 0.12, 
  "boxmode": "group", 
  "dragmode": "zoom", 
  "hovermode": "closest", 
  "margin": {"t": 70}, 
  "plot_bgcolor": "rgb(255, 255, 255)", 
  "scene": {
    "aspectmode": "auto", 
    "aspectratio": {
      "x": 1.0, 
      "y": 1.0, 
      "z": 1.0
    }
  }, 
  "showlegend": False, 
  "title": "My last 50 Uber trips - How long did I have to wait for my ride?", 
  "titlefont": {"size": 27}, 
  "xaxis": {
    "autorange": True, 
    "range": [-0.5, 1599.5], 
    "side": "bottom", 
    "title": "Time elapsed between booking and start of the ride (in seconds)", 
    "type": "linear"
  }, 
  "yaxis": {
    "autorange": True, 
    "range": [0, 20], 
    "side": "left", 
    "title": "Number of Trips"
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)
