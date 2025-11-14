
using SmartLogNamespace;
using System;
using System.IO;
using System.Reflection.Metadata;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Smart-Log Testlauf");
        Console.WriteLine("-------------------");

        // Zielverzeichnis für Logs
        string logDir = Path.Combine(Environment.CurrentDirectory, "ConsoleLogs");

        // LogWriter initialisieren
        var logger = new Smart_Log(logDir);

        Console.WriteLine($"Logverzeichnis: {logDir}");
        Console.WriteLine("Es wird nun eine neue Logdatei angelegt...\n");

        // Testeinträge schreiben
        logger.WriteInfo("Die Anwendung wurde gestartet.");
        logger.WriteWarning("Dies ist eine Testwarnung.");
        logger.WriteError("Ein Beispiel-Fehler ist aufgetreten.");

        Console.WriteLine("Logeinträge wurden geschrieben.");
        Console.WriteLine();

        // geschriebene Datei finden
        string[] files = Directory.GetFiles(logDir);
        if (files.Length == 0)
        {
            Console.WriteLine("Keine Logdatei gefunden.");
            return;
        }

        string logFile = files[0];

        Console.WriteLine($"Gefundene Logdatei: {Path.GetFileName(logFile)}");
        Console.WriteLine("Inhalt der Logdatei:\n");

        // Inhalt anzeigen
        string content = File.ReadAllText(logFile);
        Console.WriteLine(content);

        Console.WriteLine("\nTestlauf abgeschlossen.");
        Console.ReadLine();
    }
}
