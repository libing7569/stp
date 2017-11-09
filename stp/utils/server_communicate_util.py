#!/usr/bin/env python
#coding: utf-8

import socket
import sys
import os
#+
sys.path.append(os.path.dirname(os.path.realpath(__file__))+'/../thrift/gen-py')
#print(sys.path)

from server_communicate import ServerCommunicate
from server_communicate.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift import Thrift

class ServerCommunicateUtil:
    def __init__(self):
        pass

    def serve(self, ip, port, handler):
        processor = ServerCommunicate.Processor(handler)
        transport = TSocket.TServerSocket(ip, port)
        tfactory = TTransport.TBufferedTransportFactory()
        pfactory = TBinaryProtocol.TBinaryProtocolFactory()
        server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
        print "Starting thrift server in python..."
        server.serve()
        print "done!"

    def call(self, op, rip, rport, *args):
        try:
            transport = TSocket.TSocket(rip, rport)
            transport = TTransport.TBufferedTransport(transport)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            client = ServerCommunicate.Client(protocol)
            transport.open()
            print "client - ping"
            print "server - " + client.ping()
            print "client - say"
            if op == 'notify':
                client.notify(args[0], args[1])
            elif op == 'ping':
                client.ping()
            else:
                pass
            #msg = client.sync_tasks({'h1':'hello', 'h2':'hello2'})
            print "server - ok"
            transport.close()
        except Thrift.TException, ex:
            print "%s" % (ex.message)
            pass

class ServerCommunicateHandler:
    def ping(self):
        return "pong"

    def sync_tasks(self, tasks_map):
        print(tasks_map)
        return 'ok'

    def notify(self, ip, port):
        print((ip,port))
        return 'ok'


if __name__ == '__main__':
    sch = ServerCommunicateHandler()
    scu = ServerCommunicateUtil()
    scu.serve('localhost', 9000, sch)

