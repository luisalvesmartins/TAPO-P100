import logging

import azure.functions as func

from p100 import P100
import logging
import argparse

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    parser = argparse.ArgumentParser(description="Change plug state.")
    parser.add_argument('tplink_email', metavar='TPLINK_EMAIL', type=str, help="Your TPLink account email")
    parser.add_argument('tplink_password', metavar='TPLINK_PASS', type=str, help="Your TPLink account password")
    parser.add_argument('address', metavar='ADDR', type=str, help="Address of your plug (ex. 192.168.2.22)")
    parser.add_argument('new_state', metavar='STATE', type=int, help="New state of the plug (on=1 off=0) ")

    args_address="192.168.2.18"
    args_tplink_email="luis.martins@microsoft.com"
    args_tplink_password="Password123"
    args_new_state=0

    state = req.params.get('state')
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


    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if args_address:
        return func.HttpResponse(
             f"status:{is_plug_on}",
             status_code=200
        )
    else:
        return func.HttpResponse(f"Parameters: address, email, password, new_state")
