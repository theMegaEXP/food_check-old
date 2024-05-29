from PyQt5.QtWidgets import QMainWindow

from gui.designer.Ui_MainWindow import Ui_MainWindow
from gui.pages.homePage import HomePage
from gui.pages.addSymptomPage import AddSymptomPage

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.page_setup()

    def show(self):
        self.main_win.show()

    def page_setup(self):
        self.home_page = HomePage(self)
        self.add_symptom_page = AddSymptomPage()
        self.ui.stackedWidget.addWidget(self.home_page.widget)
        self.ui.stackedWidget.addWidget(self.add_symptom_page.widget)
        self.ui.stackedWidget.setCurrentWidget(self.home_page.widget)

    def page_connect_add_symptoms(self):
        print("method called")
        self.ui.stackedWidget.setCurrentWidget(self.add_symptom_page.widget)

