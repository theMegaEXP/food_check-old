from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QDate, QTime

from gui.designer.Ui_addSymptomPage import Ui_addSymptomPage
from data.init import symptomsAvailable as symptoms

class AddSymptomPage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_addSymptomPage()
        self.ui.setupUi(self.widget)

        self.form_setup()

    def form_setup(self):
        items = [symptom['symptom'] for symptom in symptoms.data]
        self.ui.symptomInput.addItems(items)

        self.ui.dateInput.setDate(QDate.currentDate())
        self.ui.timeInput.setTime(QTime.currentTime())