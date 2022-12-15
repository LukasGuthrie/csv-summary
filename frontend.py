import sys, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtCore import Qt, QUrl, QObject, pyqtSignal

class ConnectionSignal(QObject):
    
    list_signal = pyqtSignal(list)


class ListboxWidget(QListWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.resize(600, 300)
        self.links = []

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            event.accept()

            links = []

            for url in event.mimeData().urls():
                if url.isLocalFile():
                    links.append(str(url.toLocalFile()))
                    self.links.append(str(url.toLocalFile()))
                else:
                    links.append(str(url.toString()))
                    self.links.append(str(url.toString()))

            self.addItems(links)
        else:
            event.ignore()



class FrontendApp(QMainWindow):
    def __init__(self, connection_signal):
        super().__init__()
        self.connection_signal = connection_signal
        self.resize(1100, 302)

        self.lstbox_view = ListboxWidget(self)

        self.button = QPushButton('Importar', self)
        self.button.setGeometry(750, 160, 300, 50)

        self.button.clicked.connect(self.connection_signal.emit(self.lstbox_view.links))

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    signal = ConnectionSignal()
    gui = FrontendApp(signal.list_signal)
    sys.exit(app.exec_())
