from jsonHandler import (
        loadJson, saveJson
)
import os

def genUniqueTag(baseTag, exports):
        from string import ascii_uppercase

        existingEntries = {entry[0] for entry in exports if isinstance(entry, list) and len(entry) == 2}

        for letter in ascii_uppercase:
                newTag = f"{baseTag}_{letter}.Name"
                if newTag not in existingEntries:
                        return letter
        raise ValueError("Could'nt generate a unique name for the base tag '{basTag}' (A-Z deoleated)")

def architectureHandle(tag, name, description, path):

        #File paths
        modPath = os.path.abspath(os.path.join(path,"..","Saves","mod","Architecture.json"))
        newPath = os.path.abspath(os.path.join(path,"..","Saves","newConstructions","Architecture.json"))

        #Loading Files
        architectureModData = loadJson(modPath)
        architectureNewData = loadJson(newPath)

        #Export Lists
        exportsMod = architectureModData["Exports"][0]["Table"]["Value"]
        exportsNew = architectureNewData["Exports"][0]["Table"]["Value"]

        #Get unique tag
        uniqueLetter = genUniqueTag(tag, exportsMod)
        uniqueTag = f"{tag}_{uniqueLetter}"

        #Preapering string arrays
        nameArray = [f"{uniqueTag}.Name", name]
        descriptionArray = [f"{uniqueTag}.Description", description]

        #Adding values
        exportsMod.append(nameArray)
        exportsMod.append(descriptionArray)

        exportsNew.append(nameArray)
        exportsNew.append(descriptionArray)

        #mod
        saveJson(modPath, architectureModData)

        #newConstructions
        saveJson(newPath, architectureNewData)

        return uniqueTag

def DTConstructionsHandle(uniqueTag, assetPath, categoryTag, path):
        #File paths
        modPath = os.path.abspath(os.path.join(path,"..","Saves","mod","DT_Constructions.json"))
        newPath = os.path.abspath(os.path.join(path,"..","Saves","newConstructions","DT_Constructions.json"))

        templatePath = os.path.abspath(os.path.join(path,"..","Data","ConstructionTemplate.json"))

        DT_ConstructionsModData = loadJson(modPath)
        DT_ConstructionsNewData = loadJson(newPath)

        template = loadJson(templatePath)

        #Get blueprint name
        blueprintName = assetPath.split("/")[-1]

        #Edit template
        #Edite name
        template["Name"] = uniqueTag
        #Edit Arqchitecture.json references
        template["Value"][0]["Value"] = f"{uniqueTag}.Name"
        template["Value"][1]["Value"] = f"{uniqueTag}.Description"
        #Edit Actor path
        template["Value"][3]["Value"]["AssetPath"]["AssetName"] = assetPath
        #Edit Backwards Compatibility Actor path
        template["Value"][4]["Value"][0]["Value"][0]["Value"]["AssetPath"]["AssetName"] = f"{assetPath}.{blueprintName}_C"
        template["Value"][5]["Value"][0]["Value"].append(categoryTag)

        DT_ConstructionsModData["NameMap"].extend([
                uniqueTag,
                assetPath,
                f"{assetPath}.{blueprintName}_C"
        ])
        DT_ConstructionsNewData["NameMap"].extend([
                uniqueTag,
                assetPath,
                f"{assetPath}.{blueprintName}_C"
        ])

        DT_ConstructionsModData["Exports"][0]["Table"]["Data"].append(template)
        DT_ConstructionsNewData["Exports"][0]["Table"]["Data"].append(template)

        saveJson(modPath, DT_ConstructionsModData)
        saveJson(newPath, DT_ConstructionsNewData)
        






