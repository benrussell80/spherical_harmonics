# spherical_harmonics
A Bokeh app for visualizing the first few real, Cartesian spherical harmonics

## Installation
Requires Python 3.6+
```
# clone the repository and cd into it
# optionally create a virtual environment
pip install -r requirements.txt

# run the bokeh server and navigate to localhost:5006
bokeh serve --show app

# or run the script to create an html file
python no_server/main.py
```

The server app is quicker than the html file because the server app employs numpy. The html file is slower because the math functions are written in pure python then converted to JavaScript using pscript.
The html file is, however, easier to embed into something like a flask app. For example, (as taken from the Bokeh documentation)

```python
import json
from bokeh.embed import json_item
from no_server.main import plot
from flask import Flask


app = Flask(__name__)

@app.route('/figure')
def figure():
    return json.dumps(json_item(plot()))


if __name__ == "__main__":
    app.run()

```

Then wherever you would like to display the plot do

```js
<script>
fetch('/figure')
    .then(function(response) { return response.json(); })
    .then(function(item) { Bokeh.embed.embed_item(item); })
</script>
```
