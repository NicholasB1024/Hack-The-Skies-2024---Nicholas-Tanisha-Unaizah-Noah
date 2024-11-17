import osmnx as ox # import osmnx
from geopy.geocoders import Nominatim # enable HTTP requests to Nominatim API
from flask import Flask, render_template # flask
import Mapping

locator = Nominatim(user_agent='Hack the Skies') # establish locator object
graph = ox.load_graphml(filepath='Hack-The-Skies\\backend\\toronto_geodata.graphml') # load city graph (below generates city graph instead)
# graph = ox.graph_from_place(f'{locConstant.city, locConstant.province, locConstant.country}', network_type='drive')

city = Mapping.City('Toronto', 'Ontario', 'Canada') # constant information for locations

locStart = Mapping.address_validation('pickup address', city, locator)
locStop = Mapping.address_validation('dropoff address', city, locator)
Mapping.shortest_path(locStart, locStop, graph, ox)

app = Flask(__name__)

@app.route('/')
def __main__():
    return render_template('')

app.run()