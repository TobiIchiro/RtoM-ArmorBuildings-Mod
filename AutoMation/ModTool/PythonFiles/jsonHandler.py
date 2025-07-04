import json

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