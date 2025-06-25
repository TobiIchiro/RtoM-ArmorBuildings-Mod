import json
import re
import copy
import os

# Función para quitar _white_, _black_, _gold_
def clean_name(name):
    return re.sub(r'_(White|Black|Gold)_', '_', name)

# Cargar archivo JSON
with open("F:/RtoM/modsRepository/modified-json/Moria/Content/Tech/Data/Items/DT_ItemRecipes.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("F:/RtoM/modsRepository/modified-json/UnlockRequiredItems.json","r",encoding="utf-8") as f:
    template_obj = json.load(f)

# Acceder al primer Export
exports = data.get("Exports", [])
if not exports:
    raise ValueError("No hay elementos en 'Exports'.")

table_data = exports[0].get("Table", {}).get("Data", [])

for item in table_data:
    try:
        raw_name = item["Value"][0]["Value"][0]["Value"]
    except (IndexError, KeyError, TypeError):
        print("[Advertencia] No se encontró Value[0].Value[0].Value en un item")
        continue
    if any(color in raw_name for color in ["_White_", "_Black_", "_Gold_"]):
        # Paso 1: limpiar nombre
        base_name = clean_name(raw_name)

        # Paso 2: Cambiar UnlockType si es necesario
        try:
            unlock_type = item["Value"][12]["Value"][0]["Value"]
            if unlock_type == "EMorRecipeUnlockType::Manual":
                item["Value"][12]["Value"][0]["Value"] = "EMorRecipeUnlockType::DiscoverDependencies"
        except (IndexError, KeyError):
            print(f"[Advertencia] No se pudo modificar UnlockType en {raw_name}")

        # Paso 3: Reemplazar posición 3 con JSON de plantilla
        try:
            new_obj = copy.deepcopy(template_obj)
            new_obj["Value"][0]["Value"][0]["Value"] = base_name
            item["Value"][12]["Value"][3] = new_obj
        except (IndexError, KeyError, TypeError):
            print(f"[Advertencia] No se pudo reemplazar RequiredRecipe en {raw_name}")
# Guardar el archivo modificado
with open("F:/RtoM/modsRepository/modified-json/Moria/Content/Tech/Data/Items/DT_ItemRecipes.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)