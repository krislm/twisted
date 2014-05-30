from chatclient import PythonHook
#from kivy.support import install_twisted_reactor
#install_twisted_reactor()
#from twisted.internet import protocol, reactor
import socket


######## ATTEMPTING TO USING TWISTED IMPORT #######
#class TwistedTest(protocol.Protocol):
#    def connectionMade(self):
#        self.factory.app.on_connection(self.transport)
#
#    def dataReceived(self, data):
#        self.factory.app.print_message(data)
#        
#class FactoryTest(protocol.ClientFactory):
#    protocol = EchoClient
#    def __init__(self, app):
#        self.app = app
#
#    def clientConnectionLost(self, conn, reason):
#        self.app.print_message("connection lost")
#
#    def clientConnectionFailed(self, conn, reason):
#        self.app.print_message("connection failed")
    
#####################################################

class TwistedClient(PythonHook):

    def __init__(self):
        self.username = "EMPTY"
        self.connected = False
        self.users = []
        self.s = None
        self.recv_msg = ""
    
    def svr_con(self, name):
        print self.username
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect(("localhost", 8000))
            self.connected = True
            print "Connection"
            t = threading.Thread(target=handle_message)
            t.setDaemon(True)
            t.start()
            print "thread started"
        except Exception:
            print Exception
        self.username = name
        print self.username
        con = "Connect$#"+str(self.username)
        self.s.send(str(con))
        
    def disconnect(self):
        if self.connected == True:
            self.s.close()
            self.connected == False
        
    def send_message(self, msg, reciever):
        if msg and self.connected:
            try:
                          # hardcoded to 'bob', should be variable 'reciever' 
                self.s.send(str(reciever+"#"+msg))
                print "Outgoing: "+msg
                return True
            except Exception:
                print "Failed to send message"
                return False
        else:
            if msg == False:
                print "No message given"
            if reciever == False:
                print "No reciever given"
            return False
        
    def is_connected(self):
        return self.connected
    
    def handle_message(self):
        while True:
            data = self.s.recv(1024)
            print "Incoming: "+data
            if data:
                print data
                username = str(msg).split("#")[0]
                print(username)
                message = str(msg).split("#")[1]
                message = message[1:-1]
            
                if username == "users$":
                    msg_users = message.split(",")
                    for curr_user in msg_users:
                        self.users.append(curr_user[2:-1])
                        #return ""
                    else:
                        self.recv_msg = message
            #else: return False
    
    def get_message(self):
        return self.recv_msg
            
    def get_users(self):
        return self.users
    

#if __name__ == '__main__':
    #TwistedClient().run()
    