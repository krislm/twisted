from twisted.internet.protocol import Factory
from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory
        self.users = []

    def connectionMade(self):
        self.factory.numConnections += 1
        self.users.append(self.factory.numConnections)

    def dataReceived(self, data):
        print self.factory.numConnections
        self.transport.write(data)

    def connectionLost(self, reason):
        self.factory.numConnections -= 1

class EchoFactory(protocol.Factory):
    numConnections = 0

    def buildProtocol(self, addr):
        return Echo(self)

reactor.listenTCP(8000, EchoFactory())
reactor.run()