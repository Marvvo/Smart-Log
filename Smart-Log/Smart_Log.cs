namespace SmartLogNamespace
{
    public class Smart_Log
    {
        private readonly string _logDirectory;
        private readonly string _logFilePath;

        public Smart_Log(string logDirectory, string logFileName = null)
        {
            _logDirectory = logDirectory;

            if (!Directory.Exists(_logDirectory))
                Directory.CreateDirectory(_logDirectory);

            // Eine Logdatei pro Tag erzeugen:
            // Beispiel: 2025-02-14.log
            string fileName = $"{DateTime.Now:yyyy-MM-dd}.log";

            _logFilePath = Path.Combine(_logDirectory, fileName);
        }

        public void WriteInfo(string message)
        {
            WriteEntry("INFO", message);
        }

        public void WriteWarning(string message)
        {
            WriteEntry("WARNING", message);
        }

        public void WriteError(string message)
        {
            WriteEntry("ERROR", message);
        }

        public void WriteDebug(string message)
        {
            WriteEntry("DEBUG", message);
        }

        private void WriteEntry(string severity, string message)
        {
            string line = $"{DateTime.Now} [{severity}] {message}";
            File.AppendAllText(_logFilePath, line + Environment.NewLine);
        }
    }
}
