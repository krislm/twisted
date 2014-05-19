from chatclient import PythonHook
import socket


class TwistedClient(PythonHook):

    def __init__(self):
        self.username = "EMPTY"
    
    def svr_con(self, name):
        print self.username
        s = socket.socket()
        s.connect(("localhost", 8000))
        self.username = name
        print self.username
        s.send("Connect$#test")
        

if __name__ == '__main__':
    TwistedClient().run()