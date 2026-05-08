# Log Analyzer

Eine Desktop-Anwendung zur Auswertung von Logs aus einer MySQL-Datenbank.

## Voraussetzungen

- Python 3.7+
- MySQL oder MariaDB Server
- Eine Datenbank namens 'logs_db' mit einer Tabelle 'logs' mit Spalten: id (INT), level (VARCHAR), message (TEXT), timestamp (DATETIME)

## Installation

1. Klone oder lade das Projekt herunter.
2. Installiere die Abhängigkeiten:
   ```
   pip install -r requirements.txt
   ```
3. Passe die Datenbank-Verbindung in main.py an (host, user, password, database).

## Verwendung

Starte die Anwendung mit:
```
python main.py
```

Die App zeigt ein Kreisdiagramm mit der Verteilung der Log-Levels (z.B. WARNING, CRITICAL) und eine Tabelle mit allen Logs.

## Anpassungen

- Ändere die DB-Verbindungsparameter in der connectDB Methode.
- Passe die SQL-Abfragen an, wenn die Tabellenstruktur anders ist.