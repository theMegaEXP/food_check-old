# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FoodListing.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_foodListing(object):
    def setupUi(self, foodListing):
        foodListing.setObjectName("foodListing")
        foodListing.resize(318, 109)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(foodListing.sizePolicy().hasHeightForWidth())
        foodListing.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(foodListing)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.brandLabel = QtWidgets.QLabel(foodListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brandLabel.sizePolicy().hasHeightForWidth())
        self.brandLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.brandLabel.setFont(font)
        self.brandLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.brandLabel.setObjectName("brandLabel")
        self.verticalLayout_4.addWidget(self.brandLabel)
        self.productLabel = QtWidgets.QLabel(foodListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.productLabel.sizePolicy().hasHeightForWidth())
        self.productLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.productLabel.setFont(font)
        self.productLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.productLabel.setObjectName("productLabel")
        self.verticalLayout_4.addWidget(self.productLabel)
        self.barcodeLabel = QtWidgets.QLabel(foodListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.barcodeLabel.sizePolicy().hasHeightForWidth())
        self.barcodeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.barcodeLabel.setFont(font)
        self.barcodeLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.barcodeLabel.setObjectName("barcodeLabel")
        self.verticalLayout_4.addWidget(self.barcodeLabel)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.dateLabel = QtWidgets.QLabel(foodListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateLabel.sizePolicy().hasHeightForWidth())
        self.dateLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateLabel.setFont(font)
        self.dateLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.dateLabel.setObjectName("dateLabel")
        self.verticalLayout_5.addWidget(self.dateLabel)
        self.timeLabel = QtWidgets.QLabel(foodListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timeLabel.sizePolicy().hasHeightForWidth())
        self.timeLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.timeLabel.setFont(font)
        self.timeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.timeLabel.setObjectName("timeLabel")
        self.verticalLayout_5.addWidget(self.timeLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ingredientsLabel = QtWidgets.QLabel(foodListing)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ingredientsLabel.sizePolicy().hasHeightForWidth())
        self.ingredientsLabel.setSizePolicy(sizePolicy)
        self.ingredientsLabel.setObjectName("ingredientsLabel")
        self.verticalLayout.addWidget(self.ingredientsLabel)

        self.retranslateUi(foodListing)
        QtCore.QMetaObject.connectSlotsByName(foodListing)

    def retranslateUi(self, foodListing):
        _translate = QtCore.QCoreApplication.translate
        foodListing.setWindowTitle(_translate("foodListing", "FoodListing"))
        self.brandLabel.setText(_translate("foodListing", "TextLabel"))
        self.productLabel.setText(_translate("foodListing", "TextLabel"))
        self.barcodeLabel.setText(_translate("foodListing", "123123123123"))
        self.dateLabel.setText(_translate("foodListing", "MM/DD/YYYY"))
        self.timeLabel.setText(_translate("foodListing", "12:00AM"))
        self.ingredientsLabel.setText(_translate("foodListing", "Ingredients"))
