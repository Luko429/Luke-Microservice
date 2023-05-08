from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/calculate_growth_rate', methods=['POST'])
def calculate_growth_rate():
    data = request.get_json()

    if 'data' in data:
        newest_value, oldest_value, total_years = data['data']

        if total_years > 1:
            growth_rate = ((newest_value / oldest_value) ** (1 / (total_years - 1)) - 1) * 100
            result = round(growth_rate)
        else:
            result = "Total years must be greater than 1."

        return jsonify(answer=result)
    else:
        return jsonify(error="Invalid input format")

if __name__ == '__main__':
    app.run(debug=True)
