from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_showSymptomsPage import Ui_showSymptomsPage

class ShowFoodsPage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_showSymptomsPage()
        self.ui.setupUi(self.widget)