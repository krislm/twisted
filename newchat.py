from twisted.internet.protocol import Factory
from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver

class Echo(protocol.Protocol):#, LineReceiver):
    users = [] #List of users, which the server sends to the clients
    connections = {} #dictionary of the TCP connections, with key = username
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numConnections += 1
        print self.factory.numConnections
        print self.connections
        print self.users

    def dataReceived(self, data):

        print data
        username = str(data).split("#")[0]
        message = str(data).split("#")[1]

        if username == "Connect$":
            self.users.append(message)
            self.connections[message] = self.transport
            print self.connections
            print "user added"

            for userkey in self.connections.keys():
                self.transport = self.connections[userkey]
                self.transport.write("users$#s"+str(self.users))
        else:
            #check for who to send to
            for userkey in self.connections.keys():
                if userkey == username:
                    self.transport = self.connections[userkey]
                    self.transport.write(username + "#" + message)

            #self.transport.write(username + "#" + message)


    def connectionLost(self, reason):
        self.factory.numConnections -= 1
        print self.factory.numConnections
        for userkey in self.connections:
            tempuser = ""
            if self.connections[userkey] == self.transport:
                tempuser=userkey
        del self.connections[tempuser]
        self.users.remove(tempuser)
        for userkey in self.connections.keys():
                self.transport = self.connections[userkey]
                self.transport.write("users$#s"+str(self.users))


class EchoFactory(protocol.Factory):
    numConnections = 0

#    def __init__(self):
#        self.users = {}

    def buildProtocol(self, addr):
        return Echo(self)

reactor.listenTCP(8000, EchoFactory())
reactor.run()