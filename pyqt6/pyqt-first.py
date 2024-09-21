import sys
from PyQt6.QtWidgets import QApplication, QWidget

class SampleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first Qt window")
        self.setGeometry(100, 100, 300, 150)
            # Window location (100, 100), window size (300, 150)
            # Use move() to change the window location. 
            # Use resize() to change the window size.
    
qAp = QApplication(sys.argv)
myWindow = SampleWindow()
myWindow.show()
qAp.exec()
