# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:31:29 2023

@author: emmab
"""

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QRectF

class CircularProgressBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimumSize(200, 200)
        self.progress = 0

    def setProgress(self, value):
        self.progress = value
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Définir les couleurs pour la barre de progression et le fond
        progress_color = QColor("#6495ED")  # Blue
        background_color = QColor("#D3D3D3")  # Light Gray

        # Définir le rectangle de la barre de progression
        rect = QRectF(10, 10, self.width() - 20, self.height() - 20)

        # Dessiner le fond
        painter.setPen(QPen(background_color, 12, Qt.SolidLine))
        painter.drawArc(rect, 0, 360 * 16)

        # Dessiner la barre de progression
        angle = self.progress * 360 / 100
        painter.setPen(QPen(progress_color, 12, Qt.SolidLine))
        painter.drawArc(rect, 90 * 16, -angle * 16)

        # Ajouter le pourcentage de progression au centre de la barre
        painter.setPen(Qt.black)
        painter.setFont(QFont("Arial", 16, QFont.Bold))
        painter.drawText(rect, Qt.AlignCenter, f"{self.progress}%")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Barre de progression circulaire")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.progress_bar = CircularProgressBar()
        layout.addWidget(self.progress_bar)

        # Exemple de mise à jour de la progression
        self.progress_bar.setProgress(70)  # Remplacez cette valeur par la progression réelle du taux d'humidité

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
