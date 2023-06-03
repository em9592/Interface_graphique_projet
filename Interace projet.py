import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QStatusBar, QAction, QVBoxLayout, QLabel, QProgressBar
from PyQt5.QtGui import QColor, QPalette, QFont, QPainter, QPainterPath,QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QRectF
from math import pi

class CircularProgressBar(QProgressBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMinimum(0)
        self.setMaximum(100)
        self._pen_width = 10
        self._progress = 0

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
        
    def setProgress(self, value):
        self.progress = value
        self.update()

class Fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 600)
      
        
        self.setWindowTitle("Projet allergènes")
        
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabPosition(QTabWidget.North)
        self.tabs.setMovable(True)
        self.setCentralWidget(self.tabs)
        
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        self.menuBar().setNativeMenuBar(False)  # Pour les systèmes non-Mac
        
        self.menuFichier = self.menuBar().addMenu("Accueil")
        self.menuPollen = self.menuBar().addMenu("Pollen")
        self.menuParticules = self.menuBar().addMenu("Particules fines")
        
        self.pages = {}
        
        self.createPage("Accueil")
        self.createPage("Pollen")
        self.createPage("Particules fines")
        
        self.menuFichier.triggered.connect(lambda action: self.changePage(action.text()))
        self.menuPollen.triggered.connect(lambda action: self.changePage(action.text()))
        self.menuParticules.triggered.connect(lambda action: self.changePage(action.text()))
        
    def createPage(self, title):
        page = QWidget()
        layout = QVBoxLayout()
        
        if title == "Accueil":
            title_label = QLabel("Les conditions extérieures sont favorables/défavorables à la propagation de pollen/particules fines.")
            title_label.setAlignment(Qt.AlignCenter)
            title_label.setFont(QFont("Arial", 12, QFont.Bold))
            layout.addWidget(title_label)
            
            circular_progress_bar = CircularProgressBar()
            circular_progress_bar.setFixedSize(200, 200)  # Ajustez la taille selon vos besoins
            circular_progress_bar.setProgress(50)  # Exemple de pourcentage
            #circular_progress_bar.setStyleSheet("QProgressBar { border: none; }")  # Supprime la bordure
            layout.addWidget(circular_progress_bar)
            humidite_label = QLabel("Taux d'humidité: données à compléter")
            layout.addWidget(humidite_label)
            temperature_label = QLabel("Température: données à compléter")
            layout.addWidget(temperature_label)
            
            vent_label = QLabel("Vitesse du vent: données à compléter")
            layout.addWidget(vent_label)
           
        
        elif title == "Pollen":
            title_label = QLabel("Les taux de pollen sont relativement faibles/normaux/élevés.")
            title_label.setAlignment(Qt.AlignCenter)
            title_label.setFont(QFont("Arial", 12, QFont.Bold))
            layout.addWidget(title_label)
            
            pollen_label = QLabel("Quantité de pollen dans l'air: données à compléter")
            layout.addWidget(pollen_label)
            
          
        elif title == "Particules fines":
            title_label = QLabel("Les taux de particules fines sont relativement faibles/normaux/élevés.")
            title_label.setAlignment(Qt.AlignCenter)
            title_label.setFont(QFont("Arial", 12, QFont.Bold))
            layout.addWidget(title_label)
            
            pm25_label = QLabel("Quantité de PM2.5: données à compléter")
            layout.addWidget(pm25_label)
            
            pm10_label = QLabel("Quantité de PM10: données à compléter")
            layout.addWidget(pm10_label)
            
        else:
            label = QLabel("erreur")
            layout.addWidget(label)
        
        page.setLayout(layout)
        self.pages[title] = page
        
        action = QAction(title, self)
        action.triggered.connect(lambda: self.changePage(title))
        if title == "Accueil":
            self.menuFichier.addAction(action)
        elif title == "Pollen":
            self.menuPollen.addAction(action)
        elif title == "Particules fines":
            self.menuParticules.addAction(action)
        
    def changePage(self, title):
        if title in self.pages:
            self.tabs.clear()
            self.tabs.addTab(self.pages[title], title)
            self.setWindowTitle("Projet allergènes - " + title)
            self.tabs.setCurrentWidget(self.pages[title])
        
app = QApplication(sys.argv)
window = Fenetre()
window.show()
sys.exit(app.exec_())

