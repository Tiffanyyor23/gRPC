#!/usr/bin/env python3


import grpc
from NPAF_pb2 import RouteRequest, DeviceRoutes
import NPAF_pb2_grpc
from concurrent import futures


server_data = {

    'address':'127.0.0.1',
    'port':'51111'
}


class RouteDataServicer(NPAF_pb2_grpc.RouteDataServicer):
    def CollectRoutes(self, request, context):
        print(request)
        return self.__constructResponse(request.hostname, request.afi, request.safi)

    
    def __constructResponse(self, hostname, afi, safi):
        msg = DeviceRoutes()
        msg.hostname = hostname
        msg.id = 1
        msg.routes_number = 10
        
        msg.routes.afi = afi
        msg.routes.safi = safi


        msg.routes.route.add(route='192.168.1.0/24', next_hop='10.0.0.1')
        msg.routes.route.add(route='192.168.2.0/24', next_hop='10.0.0.2')
        msg.routes.route.add(route='192.168.3.0/24', next_hop='10.0.0.3')


        return msg


if __name__ == '__main__':
    server = grpc.server(thread_pool=futures.ThreadPoolExecutor(max_workers=10))
    NPAF_pb2_grpc.add_RouteDataServicer_to_server(RouteDataServicer(), server)


    print(f'Starting gRPC service at {server_data["port"]} ...')
    server.add_insecure_port(f'{server_data["address"]}:{server_data["port"]}')
    server.start()
    server.wait_for_termination()
