#!/usr/bin/env python3

import grpc
from NPAF_pb2_grpc import RouteDataStub
from NPAF_pb2 import RouteRequest, DeviceRoutes

server_data = {
 
    'address':'127.0.0.1',
    'port':'51111'
}


def build_message():
    msg = RouteRequest()
    msg.hostname = 'router1'
    msg.afi = 0
    msg.safi = 0

    return msg


if __name__ == '__main__':
    with grpc.insecure_channel(f'{server_data["address"]}:{server_data["port"]}') as channel:
        stub = RouteDataStub(channel)
        request_message = build_message()

        print(f'Sending the CollectRequest to {server_data["address"]}:{server_data["port"]} ...')
        response_message = stub.CollectRoutes(request_message)

        print(f'Received the response to CollectRequest from {server_data["address"]}:{server_data["port"]}:\n')
        print(response_message)


