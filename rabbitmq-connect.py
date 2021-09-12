#!/usr/bin/env python

"""Tests MilkyWay Galaxy rabbitmq with hardcoded test credentials """

import argparse
import sys
import pika

def rabbitmq_connect(ip=None):
    """Connects to ip using standard port and credentials."""
    credentials = pika.credentials.PlainCredentials('mangeshbb', 'Galactic2MilkyWay')
    parameters = pika.ConnectionParameters(
        host=ip, virtual_host='/', credentials=credentials)
    try:
        connection = pika.BlockingConnection(parameters)
        connection.channel()
    except Exception:
        sys.exit("Can't connect to %s" % ip)
    else:
        print("Connected.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ip", help="The IP to connect to")
    args = parser.parse_args()
    rabbitmq_connect(args.ip)
