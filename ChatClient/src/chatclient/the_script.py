from kivy.support import install_twisted_reactor
install_twisted_reactor()
from twisted.internet import reactor, protocol
from chatclient import PythonHook


class EchoClient(protocol.Protocol):
    def connectionMade(self):
        self.factory.app.on_connection(self.transport)

    def dataReceived(self, data):
        self.factory.app.print_message(data)


class EchoFactory(protocol.ClientFactory):
    protocol = EchoClient
    def __init__(self, app):
        self.app = app

    def clientConnectionLost(self, conn, reason):
        self.app.print_message("connection lost")

    def clientConnectionFailed(self, conn, reason):
        self.app.print_message("connection failed")


class TwistedClient(PythonHook):

    def __init__(self):
        self.username = "EMPTY"
    
    def svr_con(self, name):
        print self.username
        reactor.connectTCP('localhost', 8000, EchoFactory(self))
        self.username = name
        print self.username


if __name__ == '__main__':
    TwistedClient().run()