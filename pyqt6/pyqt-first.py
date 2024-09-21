import sys, os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
os.environ["QTWEBENGINE_DICTIONARIES_PATH"] = os.path.join(
    CURRENT_DIR, "qtwebengine_dictionaries")        
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first Qt window")
        self.setGeometry(100, 100, 300, 150)
            # Window location (100, 100), window size (300, 150)
            # Use move() to change the window location. 
            # Use resize() to change the window size.
        
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)        
        webEngineView = QWebEngineView(centralWidget)
        webEngineView.setGeometry(10,10,270,110)
#         webEngineView.setUrl(QtCore.QUrl("about:blank"))
#         webEngineView.setUrl(QUrl("https://qt-project.org/"))


        



qAp = QApplication(sys.argv)
myWindow = MainWindow()
myWindow.show()
qAp.exec()
