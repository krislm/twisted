package chatclient;

import java.net.*;
import java.io.*;

/**
 *
 * @author krismaini
 */
public class Client {
    
    private ObjectInputStream sInput;       // to read from the socket
    private ObjectOutputStream sOutput;     // to write on the socket
    private Socket socket;

    private String server, username;
    private int port;
    
    private boolean connected;
//    private boolean clientVisible;
    
    private ClientJGUI gui = new ClientJGUI();

    public Client(String server, int port, String username) {
        this.server = server;
        this.port = port;
        this.username = username;
        this.connected = false;
//        if(!clientVisible){
//            gui.setVisible(true);
//        }        
    }
    
//    public boolean guiVisible(){
//        gui.setVisible(true);
//        clientVisible = true;
//        return true;
//    }
    
    private void display(String msg){
        System.out.println(msg);      // println in console 
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public boolean isConnected() {
        return connected;
    }
    
//    public boolean start(){
//       if (connect()){
//           connected = true;          
//       }
//       //return true if connection established - else false
//       return connected;
//    }
    
    public boolean connect(){
        
        try {
            socket = new Socket(server, port);
        }
        catch(Exception ec) {
            display("Error connectiong to server:" + ec);
            return false;
        }

        String msg = "Connection accepted " + socket.getInetAddress() + ":" + socket.getPort();
        display(msg);

        try
        {
            sInput  = new ObjectInputStream(socket.getInputStream());
            sOutput = new ObjectOutputStream(socket.getOutputStream());
        }
        catch (IOException eIO) {
            display("Exception creating new Input/output Streams: " + eIO);
            return false;
        }

        return true;
    }
    
    public boolean sendMessage(String msg){
        if (connected){
            try {
                sOutput.writeObject(username+"#"+msg);
                System.out.println(username+" sending "+msg);
            } catch (IOException eIO) {
                display("Exception creating new Input/output Streams: " + eIO);
                return false;
            }
        }
        return true;
    }
    
    public boolean handleMessage(){
        String response;
        if(connected){
            try {
                response = (String)sInput.readObject();
                System.out.println(username+" handling "+ response);
            } catch (IOException eIO) {
                display("Exception creating new Input/output Streams: " + eIO);
                return false;
            } catch (ClassNotFoundException eIO) {
                display("Exception creating new Input/output Streams: " + eIO);
                return false;
            }
        }
        return true;
    }
    
}
