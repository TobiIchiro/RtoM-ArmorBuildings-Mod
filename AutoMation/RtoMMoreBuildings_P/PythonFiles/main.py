import sys
from PySide6.QtWidgets import QApplication
from jsonHandler import loadJson
from constructionUI import ConstructionAdderUI
import os

if __name__ == "__main__":
    app = QApplication(sys.argv)

    scriptDir = os.path.dirname(__file__)
    dataDir = os.path.abspath(os.path.join(scriptDir,"..","Data"))
    
    #DT_Items, Category
    itemsData = loadJson(os.path.abspath(os.path.join(dataDir, "Items.json")))
    categoryTagsData = loadJson(os.path.abspath(os.path.join(dataDir,"CategoryTags.json")))

    construcionAdder = ConstructionAdderUI(scriptDir, itemsData, categoryTagsData)
    construcionAdder.show()

    sys.exit(app.exec())