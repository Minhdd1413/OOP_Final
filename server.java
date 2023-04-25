import java.net.*;
import java.io.*;

class Server {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(8080);
        System.out.println("Server started, waiting for connection...");

        Socket clientSocket = serverSocket.accept();
        System.out.println("Connection established!");

        BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        String inputLine;
        while ((inputLine = in.readLine()) != null) {
            System.out.println("Received message: " + inputLine);
        }

        in.close();
        clientSocket.close();
        serverSocket.close();
    }
}
