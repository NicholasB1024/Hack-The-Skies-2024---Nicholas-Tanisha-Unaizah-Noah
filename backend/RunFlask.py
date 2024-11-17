import osmnx as ox # import osmnx
from geopy.geocoders import Nominatim # enable HTTP requests to Nominatim API
from flask import Flask, render_template, request, jsonify # flask
import Mapping
import datetime

locator = Nominatim(user_agent='PathFindr') # establish locator object
graph = ox.load_graphml(filepath='Hack-The-Skies\\backend\\toronto_geodata.graphml') # load city graph (below generates city graph instead)
# graph = ox.graph_from_place(f'{locConstant.city, locConstant.province, locConstant.country}', network_type='drive')
city = Mapping.City('Toronto', 'Ontario', 'Canada') # constant information for locations

# Initialize flask application
app = Flask(__name__)

@app.route('/api/find_route', methods=['POST'])
def find_route():
    try:
        data = request.json
        if not data or "currentLocation" not in data or "destination" not in data:
            return jsonify({"error": "Invalid input."}), 400
        
        print(data)
        locStart = locator.geocode(f'{data['currentLocation']}, {city.city}, {city.province}, {city.country}')
        locStop = locator.geocode(f'{data['destination']}, {city.city}, {city.province}, {city.country}')

        if not locStart or not locStop:
            return jsonify({"error": "Unable to locate one or both addresses."}), 400

        path = Mapping.give_directions(locStart, locStop, graph, ox)
        directions = Mapping.interpret_directions(path, graph, ox)

        return jsonify({
        "shortestPathLength": None,
        "directions": directions
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# return render_template('frontend\\')