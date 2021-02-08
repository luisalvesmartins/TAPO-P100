from flask import Flask, jsonify, request
from flask_cors import CORS
from p100 import P100
import logging

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    response = {'running': True}
    return jsonify(response), 200

@app.route('/api/P100', methods=['POST', 'GET'])
def ezw():
    args_new_state=0

    state = request.args.get('state')
    args_address = request.args.get('address')
    args_tplink_email = request.args.get('email')
    args_tplink_password = request.args.get('password')
    if state:
        if state == '1':
            args_new_state=1
    

    logger = logging.getLogger('root')
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
    logging.basicConfig(format=FORMAT)
    logger.setLevel(logging.DEBUG)

    logger.info(f"Will change state of plug at '{args_address}' to '{args_new_state}'")

    my_bulb = P100(args_address)
    my_bulb.handshake()
    my_bulb.login_request(args_tplink_email, args_tplink_password)
    my_bulb.change_state(args_new_state, "88-00-DE-AD-52-E1")

    # Now check if the plug is on
    is_plug_on = my_bulb.is_on()
    logger.info(f"Returned result: {is_plug_on}")



    response = {'success': True, 'status': f"Will change state of plug at '{args_address}' to '{args_new_state}'"}

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')   
