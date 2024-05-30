from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_addIngredients import Ui_addIngredients

class AddIngredients:
    def __init__(self, parent):
        self.p = parent
        self.widget = QWidget()
        self.ui = Ui_addIngredients()
        self.ui.setupUi(self.widget)