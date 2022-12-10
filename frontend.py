import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtCore import Qt, QUrl

class ListboxWidget(QListWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 300)


class AppDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1100, 302)
        
        self.lstView = ListboxWidget(self)

        self.button = QPushButton('Importar', self)
        self.button.setGeometry(750, 160, 300, 50)
    

app = QApplication(sys.argv)
demo = AppDemo()
demo.show()

sys.exit(app.exec_())
