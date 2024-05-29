from PyQt5.QtWidgets import QWidget

from gui.designer.Ui_homePage import Ui_homePage
from gui.pages.showFoodsPage import ShowFoodsPage
from gui.pages.showSymptomsPage import ShowSymptomsPage

class HomePage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_homePage()
        self.ui.setupUi(self.widget)

        self.pageSetup()
        self.buttonSetup()

    def pageSetup(self):
        self.show_foods_page = ShowFoodsPage()
        self.show_symptoms_page = ShowSymptomsPage()
        self.ui.stackedWidget.addWidget(self.show_foods_page.widget)
        self.ui.stackedWidget.addWidget(self.show_symptoms_page.widget)
        self.ui.stackedWidget.setCurrentWidget(self.show_foods_page.widget)

    def buttonSetup(self):
        self.ui.foodsPageBtn.clicked.connect(lambda: self.pageConnect(self.show_foods_page.widget))
        self.ui.symptomsPageBtn.clicked.connect(lambda: self.pageConnect(self.show_symptoms_page.widget))

    def pageConnect(self, page):
        self.ui.stackedWidget.setCurrentWidget(page)
