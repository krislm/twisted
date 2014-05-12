from twisted.internet.protocol import Factory
from twisted.internet import protocol, reactor
from twisted.protocols.basic import LineReceiver

class Echo(protocol.Protocol):#, LineReceiver):
    users = []
    def __init__(self, factory):
        self.factory = factory
        #self.name = None
        #self.state = "REGISTER"

    def connectionMade(self):
        self.factory.numConnections += 1


    def dataReceived(self, data):
        print self.factory.numConnections
        print data
        username = str(data).split("#")[0]
        message = str(data).split("#")[1]
        if message == "Connect$":
            self.users.append(username)
            print "user added"
            print self.users
            self.transport.write("\nusers$#"+str(self.users))

        self.transport.write(data)


    def connectionLost(self, reason):
        self.factory.numConnections -= 1

class EchoFactory(protocol.Factory):
    numConnections = 0

#    def __init__(self):
#        self.users = {}

    def buildProtocol(self, addr):
        return Echo(self)

reactor.listenTCP(8000, EchoFactory())
reactor.run()