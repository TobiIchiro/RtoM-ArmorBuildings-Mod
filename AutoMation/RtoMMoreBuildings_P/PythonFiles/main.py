import sys
from PySide6.QtWidgets import QApplication
from jsonHandler import loadJson
from constructionUI import ConstructionAdderUI
import os

if __name__ == "__main__":
    app = QApplication(sys.argv)

    scriptDir = os.path.dirname(__file__)
    dataDir = os.path.abspath(os.path.join(scriptDir,"..","Data"))
    
    #DT_Items, Architecture, CategoryTags, DT_CategoryTags, DT_Constructions, DT_ConstructionRecipes
    itemsData = loadJson(os.path.abspath(os.path.join(dataDir, "Items.json")))
    #architectureData = loadJson("../data/Architecture.json")

    #categoryTagsData = loadJson("../data/CategoryTags.json")

    #constructionsData = loadJson("../data/DT_Constructions.json")

    #constructionRecipesData = loadJson("../daata/DT_ConstructionRecipes.json")


    construcionAdder = ConstructionAdderUI(itemsData)
    construcionAdder.show()

    sys.exit(app.exec())