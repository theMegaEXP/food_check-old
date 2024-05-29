from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_addSymptomPage import Ui_addSymptomPage

class AddSymptomPage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_addSymptomPage()
        self.ui.setupUi(self.widget)