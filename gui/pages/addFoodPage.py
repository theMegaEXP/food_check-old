from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_addFoodPage import Ui_addFoodPage
from data.init import foods

class AddFoodPage:
    def __init__(self, main_window):
        self.main_window = main_window
        self.widget = QWidget()
        self.ui = Ui_addFoodPage()
        self.ui.setupUi(self.widget)