import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor, QFont
import mysql.connector
import mysql
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class LogAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connectDB()
        self.loadData()

    def initUI(self):
        self.setWindowTitle('Log Analyzer')
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
            }
            QTableWidget {
                background-color: #ffffff;
                alternate-background-color: #f9f9f9;
                gridline-color: #e0e0e0;
                border: 1px solid #ddd;
            }
            QHeaderView::section {
                background-color: #2c3e50;
                color: white;
                padding: 5px;
                border: none;
                font-weight: bold;
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(15)
        
        # Diagramm
        self.chart = FigureCanvas(plt.Figure(figsize=(12, 4)))
        layout.addWidget(self.chart)
        
        # Tabelle
        self.table = QTableWidget()
        self.table.setAlternatingRowColors(True)
        self.table.setFont(QFont('Arial', 10))
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QTableWidget.SelectionMode.SingleSelection)
        layout.addWidget(self.table)
        
        self.setLayout(layout)

    def connectDB(self):
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',  # Ändere dies
                password='password',  # Ändere dies
                database='logs_db'  # Ändere dies
            )
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.conn = None

    def loadData(self):
        if not self.conn:
            return
        cursor = self.conn.cursor()
        # Für Diagramm
        cursor.execute("SELECT level, COUNT(*) FROM logs GROUP BY level")
        levels = cursor.fetchall()
        fig = self.chart.figure
        fig.clear()
        ax = fig.add_subplot(111)
        if levels:
            labels = [l[0] for l in levels]
            sizes = [l[1] for l in levels]
            # Farben für verschiedene Log-Level
            colors = {
                'DEBUG': '#95a5a6',
                'INFO': '#3498db',
                'WARNING': '#f39c12',
                'ERROR': '#e74c3c',
                'CRITICAL': '#c0392b'
            }
            pie_colors = [colors.get(label, '#95a5a6') for label in labels]
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=pie_colors, startangle=90)
        else:
            ax.text(0.5, 0.5, 'Keine Daten verfügbar', ha='center', va='center', fontsize=14)
        self.chart.draw()
        
        # Für Tabelle
        cursor.execute("SELECT id, level, message, timestamp FROM logs ORDER BY timestamp DESC")
        logs = cursor.fetchall()
        self.table.setRowCount(len(logs))
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['ID', 'Level', 'Nachricht', 'Zeitstempel'])
        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 100)
        self.table.setColumnWidth(2, 600)
        self.table.setColumnWidth(3, 250)
        
        level_colors = {
            'DEBUG': QColor('#ecf0f1'),
            'INFO': QColor('#d6eaf8'),
            'WARNING': QColor('#fef5e7'),
            'ERROR': QColor('#fadbd8'),
            'CRITICAL': QColor('#f5b7b1')
        }
        
        for i, log in enumerate(logs):
            level = log[1]
            bg_color = level_colors.get(level, QColor('#ffffff'))
            for j, val in enumerate(log):
                item = QTableWidgetItem(str(val))
                item.setBackground(bg_color)
                if j == 1:  # Level-Spalte fett
                    font = QFont('Arial', 10, QFont.Weight.Bold)
                    item.setFont(font)
                self.table.setItem(i, j, item)
        
        cursor.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LogAnalyzer()
    window.show()
    sys.exit(app.exec())