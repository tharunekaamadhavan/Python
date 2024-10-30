import java.io.*;
import java.net.*;
import java.util.*;

public class ChatServer {

    private static final int PORT = 12345;
    private static Set<Socket> clientSockets = new HashSet<>();
    private static final Object lock = new Object();

    public static void main(String[] args) {
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            System.out.println("ChatServer is listening on port " + PORT);

            while (true) {
                Socket clientSocket = serverSocket.accept();
                System.out.println("Client connected: " + clientSocket.getInetAddress().getHostAddress());

                synchronized (lock) { 
                    clientSockets.add(clientSocket);
                }

                Thread clientThread = new Thread(() -> handleClient(clientSocket));
                clientThread.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void handleClient(Socket clientSocket) {
        try (BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
             PrintWriter writer = new PrintWriter(clientSocket.getOutputStream(), true)) {

            String clientMessage;
            while ((clientMessage = reader.readLine()) != null) {
                System.out.println("Received from client: " + clientMessage);

                // Broadcast the message to all connected clients
                synchronized (lock) {
                    for (Socket socket : clientSockets) {
                        if (socket != clientSocket) { // avoid sending the message back to the sender
                            PrintWriter clientWriter = new PrintWriter(socket.getOutputStream(), true);
                            clientWriter.println(clientMessage);
                        }
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            synchronized (lock) {
                clientSockets.remove(clientSocket);
            }
            System.out.println("Client disconnected: " + clientSocket.getInetAddress().getHostAddress());
        }
    }
}
