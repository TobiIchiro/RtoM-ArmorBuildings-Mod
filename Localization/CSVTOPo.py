import csv
import re

poFile = "F:/RtoM/modsRepository/Localization/de/Game.po"
csvFile = "F:/RtoM/modsRepository/Localization/de/Game_fr.csv"
poOutput = "F:/RtoM/modsRepository/Localization/fr/Game_fr.po"

# -----------------------------
# 1. Leer CSV y crear diccionario
# clave: (msgctxt, msgid)
# valor: msgstr traducido
# -----------------------------
translations = {}

with open(csvFile, newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        context = row["Context"].strip()
        source = row["Source"].strip()
        translation = row["Translation"].strip()

        if translation:  # solo si hay traducción
            translations[(context, source)] = translation

# -----------------------------
# 2. Procesar el PO
# -----------------------------
outputLines = []

currentCtxt = ""
currentId = ""
insideEntry = False

with open(poFile, "r", encoding="utf-8") as f:
    for line in f:
        stripped = line.strip()

        if stripped.startswith("msgctxt"):
            currentCtxt = re.findall(r'"(.*)"', stripped)[0]
            insideEntry = True
            outputLines.append(line)

        elif stripped.startswith("msgid"):
            currentId = re.findall(r'"(.*)"', stripped)[0]
            insideEntry = True
            outputLines.append(line)

        elif stripped.startswith("msgstr") and insideEntry:
            key = (currentCtxt, currentId)

            if key in translations:
                translated = translations[key].replace('"', '\\"')
                outputLines.append(f'msgstr "{translated}"\n')
            else:
                # No está en el CSV → se deja tal cual
                outputLines.append(line)

            insideEntry = False
            currentCtxt = ""
            currentId = ""

        else:
            outputLines.append(line)

# -----------------------------
# 3. Guardar PO resultante
# -----------------------------
with open(poOutput, "w", encoding="utf-8") as f:
    f.writelines(outputLines)

print("PO actualizado correctamente.")
print(f"Traducciones aplicadas: {len(translations)}")
