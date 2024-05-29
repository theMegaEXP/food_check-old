from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.designer.Ui_MainWindow import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

    def show(self):
        self.main_win.show()
