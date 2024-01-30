from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)


@app.route('/hello/<string:name>', methods=['GET'])
def hello(name):
    """
    This endpoint returns a greeting message for the provided name.
    ---
    parameters:
      - name: name
        in: path
        type: string
        required: true
        description: The name to greet.
    responses:
      200:
        description: A greeting message.
    """
    return jsonify({'message': f'Hello, {name}!'}), 200


@app.route('/square/<int:num>', methods=['GET'])
def square(num):
    """
    This endpoint returns the square of the provided number.
    ---
    parameters:
      - name: num
        in: path
        type: integer
        required: true
        description: The number to square.
    responses:
      200:
        description: The square of the number.
    """
    return jsonify({'result': num * num}), 200


if __name__ == '__main__':
    app.run(debug=True)