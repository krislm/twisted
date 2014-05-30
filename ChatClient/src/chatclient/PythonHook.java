package chatclient;

import java.util.List;

/**
 *
 * @author krismaini
 */
public interface PythonHook {
    
    void svr_con(String name);
    
    void disconnect();
    
    boolean send_message(String msg, String reciever);
    
    boolean is_connected();
    
    void handle_message();
    
    List<String> get_users();
    
    String get_message();
}
