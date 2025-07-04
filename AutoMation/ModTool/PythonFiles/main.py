import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, 
    QWidget, QLabel, QVBoxLayout
    )
from jsonHandler import loadJson
from constructionUI import ConstructionAdderUI
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("TobiIchiro Moding Tool")
        self.resize(500,500)

        #Tabs container
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        #Loading Needed Files
        scriptDir = os.path.dirname(__file__)
        dataDir = os.path.abspath(os.path.join(scriptDir,"..","Data"))
        
        #DT_Items, Category
        itemsData = loadJson(os.path.abspath(os.path.join(dataDir, "Items.json")))
        categoryTagsData = loadJson(os.path.abspath(os.path.join(dataDir,"CategoryTags.json")))
        unlockRequirementsItemsConstructions = loadJson(os.path.abspath(os.path.join(dataDir,"UnlockRequirementsItemsConstructions.json")))

        #Tab 1: UI Adding New Construction Recipes
        constructRecipeAdderTab = ConstructionAdderUI(scriptDir, itemsData, categoryTagsData, unlockRequirementsItemsConstructions)
        self.tabs.addTab(constructRecipeAdderTab, "New Construction Adder")

        #Tab 2: UI More Buildings Mantain Mod
        moreBuildingMantainModTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("More Buildings Mantain Mod - Coming Soon"))
        moreBuildingMantainModTab.setLayout(layout)
        self.tabs.addTab(moreBuildingMantainModTab, "More Buildings Mantain Mod")

        #Tab 3: UI Adding New Armor Recipes
        moreBuildingMantainModTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("New Armor Adder - Coming Soon"))
        moreBuildingMantainModTab.setLayout(layout)
        self.tabs.addTab(moreBuildingMantainModTab, "New Armor Adder")

        #Tab 4: Custmo Armor Recipes Mantain Mod
        moreBuildingMantainModTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Custmo Armor Recipes Mantain Mod - Coming Soon"))
        moreBuildingMantainModTab.setLayout(layout)
        self.tabs.addTab(moreBuildingMantainModTab, "Custmo Armor Recipes Mantain Mod")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())