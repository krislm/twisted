package chatclient;

import org.python.util.PythonInterpreter;

/**
 *
 * @author krismaini
 */
public class ChatClient {

    public static void main(String[] args) {
        PythonInterpreter interpreter = new PythonInterpreter();
//        interpreter.execfile("src/p_script.py");
//        interpreter.execfile("scr/newchat.py");
        interpreter.execfile("src/some_thing.py");
    }
    
}