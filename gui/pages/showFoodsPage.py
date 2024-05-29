from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_showFoodsPage import Ui_showFoodsPage

class ShowFoodsPage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_showFoodsPage()
        self.ui.setupUi(self.widget)