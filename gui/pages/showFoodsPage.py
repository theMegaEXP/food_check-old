from PyQt5.QtWidgets import QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt

from gui.designer.Ui_showFoodsPage import Ui_showFoodsPage
from gui.widgets.foodListing import FoodListing

class ShowFoodsPage:
    def __init__(self):
        self.widget = QWidget()
        self.ui = Ui_showFoodsPage()
        self.ui.setupUi(self.widget)

        self.generate_listings()
        self.add_items()
    
    def generate_listings(self):
        for _ in range(7):
            food_listing = FoodListing(ingredients=['wheat', 'milk', 'soy'], date="10/05/2024", time="5:50PM")
            self.ui.verticalLayout.addWidget(food_listing.widget, alignment=Qt.AlignTop)
        
    def add_items(self):    
        self.ui.verticalLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
