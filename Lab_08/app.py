from flask import Flask, jsonify  # Flask - локальний сервер
import geopandas as gpd
from shapely.geometry import Point, mapping

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/get_json/<string:filename>', methods=['GET'])
def get_json(filename):
    try:
        with open(filename + '.json', 'r') as file:
            json_data = file.read()
            return jsonify(json_data)
    except FileNotFoundError:
        return jsonify({'error': 'File not found'})


@app.route("/field/<string:filename>", methods=['GET'])
def get_field_json(filename):
    try:
        path = "../Lab_06/centroids/updated_field_centroids.geojson"
        gdf = gpd.read_file(path)
        for i, row in gdf.iterrows():
            if row["name"] == filename:
                print("Good")
                row_df = row.to_frame().T
                # return jsonify(row.__geo_interface__)
                return row_df.to_json()
        return jsonify({'sorry': 'We couldn\'t find this file'})
    except FileNotFoundError:
        return jsonify({'error': 'File not found :('})


@app.errorhandler(404)  # page doesn't exists
def page_not_found(error):
    msg_not_found = "<div style=\"display: flex; justify-content: center\">\n\t<div style=\"display: flex; flex-direction: column\">\n\t\t<h1>Page isn't found</h1>"
    msg_go_home = "\n\t\t<a href=\"/\">Home Page</a>\n\t</div>\n</div>"
    msg = msg_not_found + msg_go_home
    print(msg)
    return msg, 404


if __name__ == '__main__':
    # start server. 'debug=True' param lets to track errors in the app and show them on the web-page in the browser during developer work
    app.run(debug=True)
