from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_sum', methods=['POST'])
def calculate_sum():
    data = request.get_json()
    
    # Extract integers from the data
    num1 = int(data['num1'])
    num2 = int(data['num2'])

    # Calculate the sum
    result = num1 + num2

    # Return the result as JSON
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)

