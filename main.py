import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):

    # def __in__(self):
    def __init__(self, *args, **kwargs):
        # super(MainWindow, self).__in__()
        super(MainWindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com/'))
        self.setCentralWidget(self.browser)
        # pybutton.clicked.connect(self.clickMethod)
        self.show()


app = QApplication(sys.argv)
QApplication.setApplicationName('Simple Browser')
window = MainWindow()

# window.show()

app.exec_()
