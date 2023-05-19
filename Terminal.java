import java.io.*;
import java.lang.Runtime;

public class Terminal {
    Terminal() {
        Runtime.getRuntime();
        try {
            // Tạo tiến trình
            ProcessBuilder builder = new ProcessBuilder("cmd.exe", "/c",
                    "cd D:\\Coding\\OOP\\Final && py client.py");
            builder.redirectErrorStream(true);
            Process process = builder.start();

            // Lấy đầu ra từ tiến trình
            InputStream inputStream = process.getInputStream();
            BufferedReader reader = new BufferedReader(new InputStreamReader(inputStream));
            String line;
            while ((line = reader.readLine()) != null) {
                System.out.println(line);
            }

            // Chờ tiến trình kết thúc
            int exitCode = process.waitFor();
            System.out.println("Exit code: " + exitCode);
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
}
