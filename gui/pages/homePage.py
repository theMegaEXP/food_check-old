from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_homePage import Ui_homePage

class HomePage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_homePage()
        self.ui.setupUi(self.widget)