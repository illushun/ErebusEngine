import json, os

import ErebusEngine.util.documents as doc

defaultConfigFolder = "ErebusEngine/config/"

defaultConfigPath = defaultConfigFolder + "college_adventure.json"
inputMessagesPath = defaultConfigFolder + "settings/messages.json"

storagePath = defaultConfigFolder + "storage/temp_storage.txt"
storageBackupPath = defaultConfigFolder + "storage/temp_storage_copy.txt"


# for ease of use when rendering dialog in games
def get_message_list(key, secondKey):
	startMessages = Config(inputMessagesPath).get_json_list_double(
		Config(inputMessagesPath).get_json_object(),
		key,
		secondKey
	)
	return startMessages


class Config:
	def __init__(self, configPath):
		doc.File(storagePath).update_key("loadedConfig:", "loadedConfig:" + configPath)
		self.configPath = configPath

	def load_config(self):
		configName = doc.File(self.configPath).get_file_name(".json")
		if not os.listdir(defaultConfigFolder).__contains__(configName + ".json"):
			defaultStage = {}

			with open(self.configPath, "w") as jsonFile:
				defaultStage["start"] = {
					"messages": ["sample dialog"], 
					"decisions": ["sample decision"]
				}
				json.dump(defaultStage, jsonFile, indent=4)
		return

	def get_loaded_config(self):
		return doc.File(storagePath).get_value("loadedConfig:", self.configPath)

	def get_json_object(self):
		with open(self.configPath, "r") as jsonFile:
			jsonData = json.load(jsonFile)
		return jsonData

	def get_json_list(self, jsonObject, key):
		return jsonObject[key]

	def get_json_list_double(self, jsonObject, key, secondKey):
		return jsonObject[key][secondKey]

	def add_json_section(self, jsonObject, key):
		with open(self.configPath, "w") as jsonFile:
			jsonObject[key] = {
				"messages": ["sample dialog"],
				"decisions": ["sample decision"]
			}
			json.dump(jsonObject, jsonFile, indent=4)
		return

	def remove_json_section(self, jsonObject, key):
		with open(self.configPath, "w") as jsonFile:
			del jsonObject[key]["messages"]
			del jsonObject[key]["decisions"]
			del jsonObject[key]
			json.dump(jsonObject, jsonFile, indent=4)
		return

	def add_json_value(self, jsonObject, key, value):
		with open(self.configPath, "w") as jsonFile:
			jsonObject[key].append(value)
			json.dump(jsonObject, jsonFile, indent=4)
		return

	def edit_json_value(self, jsonObject, key, index, value):
		with open(self.configPath, "w") as jsonFile:
			jsonObject[key][index] = value
			json.dump(jsonObject, jsonFile, indent=4)
		return

	def remove_json_value(self, jsonObject, key, index):
		with open(self.configPath, "w") as jsonFile:
			jsonObject[key].pop(index)
			json.dump(jsonObject, jsonFile, indent=4)
		return
	
	def add_json_value_double(self, jsonObject, key, secondKey, value):
		with open(self.configPath, "w") as jsonFile:
			jsonObject[key][secondKey].append(value)
			json.dump(jsonObject, jsonFile, indent=4)
		return

	def edit_json_value_double(self, jsonObject, key, secondKey, index, value):
		with open(self.configPath, "w") as jsonFile:
			jsonObject[key][secondKey][index] = value
			json.dump(jsonObject, jsonFile, indent=4)
		return

	def remove_json_value_double(self, jsonObject, key, secondKey, index):
		with open(self.configPath, "w") as jsonFile:
			jsonObject[key][secondKey].pop(index)
			json.dump(jsonObject, jsonFile, indent=4)
		return