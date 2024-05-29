from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_homePage import Ui_homePage
from gui.pages.showFoodsPage import ShowFoodsPage
from gui.pages.showSymptomsPage import ShowFoodsPage

class HomePage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_homePage()
        self.ui.setupUi(self.widget)

        self.pageSetup()
        self.buttonSetup()

    def pageSetup(self):
        show_foods_page = ShowFoodsPage()
        show_symptoms_page = ShowFoodsPage()
        self.ui.stackedWidget.addWidget(show_foods_page.widget)
        self.ui.stackedWidget.addWidget(show_symptoms_page.widget)
        self.ui.stackedWidget.setCurrentWidget(show_foods_page.widget)

    def buttonSetup(self):
        pass
