import logging

from flask import request, jsonify
from flask_restful import Api
from flask_swagger import swagger

from app import create_app
from config import DevConfig
import json

cdp_app = create_app(DevConfig)
req_logger = logging.getLogger('RequestLogger')
api = Api(cdp_app)


@cdp_app.before_request
def cdp_app_before_request():
    log_params = {
        'ip': request.headers.get('X-Forwarded-For', request.remote_addr),
        'device_type': request.headers.get('User-Agent'),
        'method': request.method,
        'path': request.path,
    }
    if request.args:
        log_params['args'] = request.args
    if request.json:
        log_params['json'] = request.json

    req_logger.info(json.dumps(log_params))


"""@cdp_app.route("/swag", methods=['GET'])
def spec():
    swag = swagger(cdp_app)
    swag['info']['version'] = '1.0'
    swag['info']['title'] = 'Your API'
    return jsonify(swag)"""


@cdp_app.route("/square/<int:num>", methods=['GET'])
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


if __name__ == "__main__":
    cdp_app.run(debug=True)
