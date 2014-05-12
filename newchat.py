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


    #def handle_REGISTER(self, name):
    #    if name in self.factory.users:
    #        self.sendLine("Name taken, please choose another.")
    #        return
    #    self.sendLine("Welcome, %s!" % (name,))
    #    self.broadcastMessage("%s has joined the channel." % (name,))
    #    self.name = name
    #    self.factory.users[name] = self
    #    self.state = "CHAT"

    def dataReceived(self, data):
        print self.factory.numConnections
        print data
        username = str(data).split("#")[0]
        message = str(data).split("#")[1]
        if message == "Connect$":
            self.users.append(username)
            print "user added"
            print self.users
        self.transport.write(data)
        self.transport.write("\nusers$#"+str(self.users))

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