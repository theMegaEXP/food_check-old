# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HomePage.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homePage(object):
    def setupUi(self, homePage):
        homePage.setObjectName("homePage")
        homePage.resize(360, 640)
        homePage.setMaximumSize(QtCore.QSize(360, 640))
        self.verticalLayout = QtWidgets.QVBoxLayout(homePage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(homePage)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 340, 620))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.buttonDisplay = QtWidgets.QVBoxLayout()
        self.buttonDisplay.setObjectName("buttonDisplay")
        self.enterBarcodePage = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enterBarcodePage.setFont(font)
        self.enterBarcodePage.setObjectName("enterBarcodePage")
        self.buttonDisplay.addWidget(self.enterBarcodePage)
        self.enterSymptomPage = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enterSymptomPage.setFont(font)
        self.enterSymptomPage.setObjectName("enterSymptomPage")
        self.buttonDisplay.addWidget(self.enterSymptomPage)
        self.enterFoodPage = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enterFoodPage.setFont(font)
        self.enterFoodPage.setObjectName("enterFoodPage")
        self.buttonDisplay.addWidget(self.enterFoodPage)
        self.verticalLayout_2.addLayout(self.buttonDisplay)
        self.dataDisplay = QtWidgets.QVBoxLayout()
        self.dataDisplay.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.dataDisplay.setObjectName("dataDisplay")
        self.datalabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(22)
        self.datalabel.setFont(font)
        self.datalabel.setAlignment(QtCore.Qt.AlignCenter)
        self.datalabel.setObjectName("datalabel")
        self.dataDisplay.addWidget(self.datalabel)
        self.description = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.description.setAlignment(QtCore.Qt.AlignCenter)
        self.description.setObjectName("description")
        self.dataDisplay.addWidget(self.description)
        self.dateEdit = QtWidgets.QDateEdit(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateEdit.sizePolicy().hasHeightForWidth())
        self.dateEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit.setFont(font)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setMaximumDate(QtCore.QDate(2040, 1, 1))
        self.dateEdit.setMinimumDate(QtCore.QDate(2024, 1, 1))
        self.dateEdit.setDate(QtCore.QDate(2024, 1, 26))
        self.dateEdit.setObjectName("dateEdit")
        self.dataDisplay.addWidget(self.dateEdit)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.foodsPageBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.foodsPageBtn.setObjectName("foodsPageBtn")
        self.horizontalLayout.addWidget(self.foodsPageBtn)
        self.symptomsPageBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.symptomsPageBtn.setObjectName("symptomsPageBtn")
        self.horizontalLayout.addWidget(self.symptomsPageBtn)
        self.dataDisplay.addLayout(self.horizontalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMaximumSize(QtCore.QSize(320, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.dataDisplay.addWidget(self.stackedWidget)
        self.verticalLayout_2.addLayout(self.dataDisplay)
        self.verticalLayout_2.setStretch(1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(homePage)
        QtCore.QMetaObject.connectSlotsByName(homePage)

    def retranslateUi(self, homePage):
        _translate = QtCore.QCoreApplication.translate
        homePage.setWindowTitle(_translate("homePage", "HomePage"))
        self.enterBarcodePage.setText(_translate("homePage", "Enter Food (barcode)"))
        self.enterSymptomPage.setText(_translate("homePage", "Enter Food (manual entry)"))
        self.enterFoodPage.setText(_translate("homePage", "Enter Symptom"))
        self.datalabel.setText(_translate("homePage", "Data"))
        self.description.setText(_translate("homePage", "Here is what you have entered so far."))
        self.dateEdit.setDisplayFormat(_translate("homePage", "MM/dd/yyyy"))
        self.foodsPageBtn.setText(_translate("homePage", "Foods"))
        self.symptomsPageBtn.setText(_translate("homePage", "Symptoms"))
