import csv
import re

poFile = "F:/RtoM/modsRepository/Localization/de/Game.po"
csvFile = "F:/RtoM/modsRepository/Localization/de/Game_de.csv"

entries = []
current = {"msgctxt": "", "msgid": "", "msgstr": ""}

def flush_entry():
    if current["msgid"]:
        entries.append(current.copy())

with open(poFile, "r", encoding="utf-8-sig") as f:
    for line in f:
        line = line.strip()

        if line.startswith("msgctxt"):
            current["msgctxt"] = re.findall(r'"(.*)"', line)[0]

        elif line.startswith("msgid"):
            current["msgid"] = re.findall(r'"(.*)"', line)[0]

        elif line.startswith("msgstr"):
            current["msgstr"] = re.findall(r'"(.*)"', line)[0]

        elif line == "":
            flush_entry()
            current = {"msgctxt": "", "msgid": "", "msgstr": ""}

    flush_entry()  # última entrada

with open(csvFile, "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["Context", "Source", "Translation"])
    for e in entries:
        writer.writerow([e["msgctxt"], e["msgid"], e["msgstr"]])

print(f"Convertido: {len(entries)} entradas → {csvFile}")
