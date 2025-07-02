from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit,
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout,
    QListWidget, QListWidgetItem, QSpinBox, QFormLayout, QMessageBox,
    QGroupBox, QRadioButton, QButtonGroup, QCompleter
)
from PySide6.QtCore import Qt
import sys

from modUtils import (
    architectureHandle, DTConstructionsHandle
)

class ConstructionAdderUI(QWidget):
    def __init__(self, scriptDir, Items, categoryTagsData):
        super().__init__()
        self.setWindowTitle("New Construction Adder")
        self.setMinimumWidth(400)
        self.setMaximumWidth(400)

        self.scriptDir = scriptDir
        
        self.Items = Items
        self.materialsWidgets = []

        self.categoryTags = categoryTagsData.get("Categories",[])

        self.setupUi()

    def setupUi(self):
        layout = QVBoxLayout()

        # Text Fields
        self.userNameInput = QLineEdit()
        self.nameInput = QLineEdit(maxLength=30)
        self.constructionTag = QLabel()
        self.descriptionInput = QLineEdit(maxLength=60)
        self.assetPathInput = QLineEdit()

        # Category tags
        self.categoryTagInput = QComboBox()
        self.categoryTagInput.setEditable(True)
        self.categoryTagInput.addItems(self.categoryTags)

        # Construction Category
        self.blueprintTypeInput = QComboBox()
        self.blueprintTypeInput.addItems(["Floor","Wall","Column","Deco"])

        # Required Materials
        self.materialsLayout = QVBoxLayout()
        self.addMaterialButton = QPushButton("Add Material")
        self.addMaterialButton.clicked.connect(self.addMaterial)

        # Unlocked conditions
        self.unlockTConditionsGroupBox = QGroupBox("Unlock Conditions")
        self.unlockConditionsLayout = QHBoxLayout()

        self.unlockConditionsButtonGroup = QButtonGroup()

        self.constructionRadioButton = QRadioButton("Discover Construction")
        self.materialRadioButton = QRadioButton("Discover Item")
        
        self.materialRadioButton.setChecked(True)

        self.unlockConditionsButtonGroup.addButton(self.materialRadioButton)
        self.unlockConditionsButtonGroup.addButton(self.constructionRadioButton)

        self.unlockRequiredItem = QComboBox()
        self.unlockRequiredConstruction = QComboBox()

        # Buttons
        self.saveButton = QPushButton("Save")
        self.saveButton.clicked.connect(self.saveConstruction)

        # Form Layout
        formLayout = QFormLayout()
        formLayout.addRow("User Name",self.userNameInput)
        formLayout.addRow("Name", self.nameInput)
        formLayout.addRow("Name Tag", self.constructionTag)
        formLayout.addRow("Description", self.descriptionInput)
        formLayout.addRow("Asset Path", self.assetPathInput)
        formLayout.addRow("Category", self.categoryTagInput)
        formLayout.addRow("Blueprint type", self.blueprintTypeInput)

        layout.addLayout(formLayout)
        layout.addWidget(QLabel("Materials (max 6):"))
        layout.addLayout(self.materialsLayout)
        layout.addWidget(self.addMaterialButton)

        self.unlockConditionsLayout.addWidget(self.materialRadioButton)
        self.unlockConditionsLayout.addWidget(self.constructionRadioButton)
        self.unlockTConditionsGroupBox.setLayout(self.unlockConditionsLayout)

        layout.addWidget(self.unlockTConditionsGroupBox)
        layout.addWidget(self.saveButton)

        self.setLayout(layout)
        self.addMaterial()
    
    def addMaterial(self):
        if len(self.materialsWidgets) >= 6:
            QMessageBox.warning(self, "Reached Limit", "You can only add up to 6 materials")
            return
        
        materialLayout = QHBoxLayout()

        materialCategoryInput = QComboBox()
        print(list(self.Items.keys()))
        materialCategoryInput.addItems(list(self.Items.keys()))

        materialNameInput = QComboBox()
        materialNameInput.setEditable(True)

        def updateItemList(category):
            materials = self.Items.get(category, [])
            materialNameInput.clear()
            materialNameInput.addItems(materials)
            completer = QCompleter(materials)
            completer.setFilterMode(Qt.MatchContains)
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            materialNameInput.setCompleter(completer)

        materialCategoryInput.currentTextChanged.connect(updateItemList)
        updateItemList(materialCategoryInput.currentText())
        

        countInput = QSpinBox()
        countInput.setMinimum(1)
        countInput.setMaximum(999)

        materialLayout.addWidget(materialCategoryInput)
        materialLayout.addWidget(materialNameInput)
        materialLayout.addWidget(QLabel("x"))
        materialLayout.addWidget(countInput)

        self.materialsLayout.addLayout(materialLayout)
        self.materialsWidgets.append((materialNameInput,countInput))
    
    def saveConstruction(self):
        materials = []
        for nameWidget, countWidget in self.materialsWidgets:
            if isinstance(nameWidget,QComboBox):
                materialName = nameWidget.currentText().strip()
                count = countWidget.value()

                '''
                if materialName not in itemlist
                    QMessageBox.warning(self,"Invalid Material", "f"'{materialName}' is not a valid material)
                '''
                materials.append((materialName,count))

        if self.materialRadioButton.isChecked():
            unlockType = 0
        elif self.constructionRadioButton.isChecked():
            unlockType = 1
        
        userName = self.userNameInput.text().strip()
        name = self.nameInput.text().strip()
        description = self.descriptionInput.text().strip()
        assetPath = self.assetPathInput.text().strip()
        category = self.categoryTagInput.currentText().strip()
        blueprint = self.blueprintTypeInput.currentText().strip()

        if not name or not description or not assetPath:
            QMessageBox.warning(self,"Empty Fields","Please fill the empty fields")
            return

        tag = userName + "Pack_" + name.title().replace(" ","")

        #Generate Unique tag and save Architecture.json for generating Mod and mantain for future updates
        uniqueTag = architectureHandle(tag, name, description, self.scriptDir)
        
        DTConstructionsHandle(uniqueTag, assetPath, category, self.scriptDir)

        #DT_ConstructionRecipes.json
        #NameMap append tag, check if materials are not in NameMaps if not, append them
        #Name: tag
        #Value[0].Value[0].Value : tag
        #Flags 2,3,4,5,8,9,10,11
        #Value[16].Value append each material
            #Value[0].Value[0].Value : material[0]
            #Value[2].Value : material[1]
        #checkedItem ? Value[20].Value[3] = selectedItemTemplate, Value[20].Value[4] = ConstructionDumyStruct : 
        #              Value[20].Value[3] = MateriaDumyStruct,    Value[20].Value[4] = selectedConstructionTemplate
        
    



