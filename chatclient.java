import java.io.*; import java.net.*;
import java.util.Scanner;

public class ChatClient

{

private static final String SERVER_ADDRESS = "localhost";

private static final int PORT = 12345;

public static void main(String[] args)

{

try (Socket socket = new Socket(SERVER_ADDRESS, PORT); BufferedReader reader = new BufferedReader(new
InputStreamReader(socket.getInputStream())); PrintWriter writer = new PrintWriter(socket.getOutputStream(), true);
Scanner scanner = new Scanner(System.in))

{

System.out.println("Connected to ChatServer at " + SERVER_ADDRESS + ":" + PORT); System.out.println("Type your messages and press Enter to send, or type 'exit' to quit.");
// Create a separate thread to receive messages from the server

Thread receiveThread = new Thread(() ->

{

String serverMessage; 
try

{

while ((serverMessage = reader.readLine()) != null)

{

System.out.println("Server says: " + serverMessage);

}

} catch (IOException e)

{

e.printStackTrace();

}

});

receiveThread.start();

// Read input from the user and send messages to the server
String input; Do

{

input = scanner.nextLine();

writer.println(input);

}

while (!input.equalsIgnoreCase("exit"));

}

catch (IOException e)

{

e.printStackTrace();

}

}

}


