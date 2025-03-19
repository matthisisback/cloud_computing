from flask import Flask, jsonify
import json
import yaml

app = Flask(__name__)

def load_data(file_path):
    with open(file_path, 'r') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file)

@app.route('/api/events', methods=['GET'])
def get_events():
    data = load_data('data/events.json')
    return jsonify(data)

@app.route('/api/news', methods=['GET'])
def get_news():
    data = load_data('data/news.yaml')
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
