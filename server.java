import java.io.*;

class TransferPy {

    public void option(int o) throws IOException {
        // set up the command and parameter
        String[] name = { "Client.py", "Soft_up.py", "Soft_down.py", "KNN.py" };
        String[] cmd = new String[0];

        cmd[0] = "py" + " " + name[o];

        Runtime rt = Runtime.getRuntime();
        Process pr = rt.exec(cmd);
    }
}
