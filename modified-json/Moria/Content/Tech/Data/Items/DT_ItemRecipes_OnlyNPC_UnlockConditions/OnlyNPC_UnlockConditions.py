import json
import copy
import os



def loadJson(path):
    #Loads and returns a JSON File
    try:
        with open(path,"r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error al cargar {path}: {e}")
        return{}

def saveJson(path,data):
    try:
        with open(path,"w",encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"Guardado en {path}")
    except Exception as e:
        print(f"Error al guardar {path}: {e}")

UnlockRequiredConstructions = {
    "$type": "UAssetAPI.PropertyTypes.Objects.ArrayPropertyData, UAssetAPI",
    "ArrayType": "StructProperty",
    "Name": "UnlockRequiredConstructions",
    "ArrayIndex": 0,
    "IsZero": False,
    "PropertyTagFlags": "None",
    "PropertyTagExtensions": "NoExtension",
    "Value": [
        {
            "$type": "UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI",
            "StructType": "MorConstructionRowHandle",
            "SerializeNone": True,
            "StructGUID": "{00000000-0000-0000-0000-000000000000}",
            "SerializationControl": "NoExtension",
            "Operation": "None",
            "Name": "UnlockRequiredConstructions",
            "ArrayIndex": 0,
            "IsZero": False,
            "PropertyTagFlags": "None",
            "PropertyTagExtensions": "NoExtension",
            "Value": [
                {
                    "$type": "UAssetAPI.PropertyTypes.Objects.NamePropertyData, UAssetAPI",
                    "Name": "RowName",
                    "ArrayIndex": 0,
                    "IsZero": False,
                    "PropertyTagFlags": "None",
                    "PropertyTagExtensions": "NoExtension",
                    "Value": "Settlement_Stone"
                }
            ]
        }
    ]
}

def changeUnlockConditions(props):
    if props[-1].get("Value") == "ERowEnabledState::Live":
        if props[-2]["Value"][0]["Value"] == "EMorRecipeUnlockType::Manual":
            props[-2]["Value"][0]["Value"] = "EMorRecipeUnlockType::DiscoverDependencies"
            props[-2]["Value"][-1] = UnlockRequiredConstructions

FILE_PATH = "F:/RtoM/modsRepository/modified-json/Moria/Content/Tech/Data/Items/DT_ItemRecipes_OnlyNPC_UnlockConditions/DT_ItemRecipes.json"
FILE_PATH_2 = "F:/RtoM/modsRepository/modified-json/Moria/Content/Tech/Data/Items/DT_ItemRecipes.json"


def main():
    data = loadJson(FILE_PATH_2)

    recipes = data["Exports"][0]["Table"]["Data"]

    for recipe in recipes:
        if recipe["Name"].startswith("TG_"):
            props = recipe["Value"]
            changeUnlockConditions(props)
    
    saveJson(FILE_PATH_2, data)

if __name__ == "__main__":
    main()