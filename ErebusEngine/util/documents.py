import os

import ErebusEngine.config as config

class File:
	def __init__(self, filePath):
		self.filePath = filePath
		self.fileBackupPath = config.storageBackupPath

	def get_file_name(self, fileExtension):
		nameSplit = self.filePath.split('/')
		for split in nameSplit:
			if split.__contains__(fileExtension):
				return split.split('.')[0]
		return nameSplit[len(nameSplit) - 1].split('.')[0]

	def get_lines(self):
		lineCollection = []
		with open(self.filePath, "r") as file:
			getLines = file.readlines()

			for line in getLines:
				lineCollection.append(line)
		return lineCollection
	
	def write(self, text):
		with open(self.filePath, "a") as file:
			file.write(text + "\n")
		return

	def remove_value(self, text):
		fileLines = self.get_lines()
		if not os.path.exists(self.fileBackupPath):
			with open(self.fileBackupPath, "w"): pass

		with open(self.fileBackupPath, "w") as file:
			for line in fileLines:
				if line.find(text) == -1:
					file.write(line)
		os.replace(self.fileBackupPath, self.filePath)
		return

	def contains_value(self, text):
		with open(self.filePath, "r") as file:
			return text in file.read()

	def update_key(self, key, updated):
		if self.contains_value(key):
			self.remove_value(key)
		self.write(updated)
		return

	def get_value(self, key, backupValue):
		if not self.contains_value(key):
			self.write(key + backupValue)
			return backupValue

		fileLines = self.get_lines()
		for line in fileLines:
			if line.__contains__(key):
				return line.split(':')[1].replace("\n", "")
		return backupValue

class Folder:
	def __init__(self, filePath):
		self.filePath = filePath

	def get_file_list(self, fileExtension, returnExtension):
		collectedFiles = []
		for file in os.listdir(self.filePath):
			if not file.__contains__(fileExtension):
				continue
				
			if returnExtension:
				collectedFiles.append(file)
			else:
				collectedFiles.append(file.replace(fileExtension, ""))
		return collectedFiles

	def add_file(self):
		pass

	def remove_file(self):
		pass

	def contains_file(self, fileName):
		return os.listdir(self.filePath).__contains__(fileName)
	