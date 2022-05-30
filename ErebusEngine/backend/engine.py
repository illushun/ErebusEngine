import json

import ErebusEngine.display.render as render
import ErebusEngine.util.documents as doc
import ErebusEngine.util.console as console
import ErebusEngine.config as config

availableOptions = ["1", "2", "3", "4", "5", "6", "7", "8", "exit"]

# Creating the game
class Game:
	def __init__(self, stage = "start", loadedConfig = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)):
		self.stage = stage
		self.loadedConfig = loadedConfig

	def create_stage(self):
		configPath = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)
		config.Config(configPath).add_json_section(
					config.Config(configPath).get_json_object(),
					self.stage
				)
		#print("Created new stage -> '" + self.stage + "'")
		return

	def remove_stage(self):
		configPath = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)
		config.Config(configPath).remove_json_section(
					config.Config(configPath).get_json_object(),
					self.stage
				)
		#print("Removed stage -> '" + self.stage + "'")
		return

	def create_dialog(self, message):
		configPath = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)
		config.Config(configPath).add_json_value_double(
					config.Config(configPath).get_json_object(),
					self.stage,
					"messages",
					message
				)
		#print("Added dialog to the stage -> '" + self.stage + "'")
		return

	def remove_dialog(self, index):
		configPath = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)
		config.Config(configPath).remove_json_value_double(
					config.Config(configPath).get_json_object(),
					self.stage,
					"messages",
					index
				)
		#print("Removed dialog from the stage -> '" + self.stage + "'")
		return

	def edit_dialog(self, index, message):
		configPath = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)
		oldJsonObject = config.Config(configPath).get_json_object()
		oldMessage = oldJsonObject[self.stage]["messages"][index]

		config.Config(configPath).edit_json_value_double(
					config.Config(configPath).get_json_object(),
					self.stage,
					"messages",
					index,
					message
				)
		#print("Edited '" + oldMessage + "' to '" + message + "' in stage -> " + self.stage)
		return

	def dialog_list(self):
		configPath = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)
		jsonObject = config.Config(configPath).get_json_object()
		return jsonObject[self.stage]["messages"]

	def create_decision(self, decision):
		configPath = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)
		config.Config(configPath).add_json_value_double(
					config.Config(configPath).get_json_object(),
					self.stage,
					"decisions",
					decision
				)
		#print("Added a decision to the stage -> '" + self.stage + "'")
		return

	def remove_decision(self, index):
		configPath = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)
		config.Config(configPath).remove_json_value_double(
					config.Config(configPath).get_json_object(),
					self.stage,
					"decisions",
					index
				)
		#print("Removed a decision from the stage -> '" + self.stage + "'")
		return

	def edit_decision(self, index, message):
		configPath = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)
		oldJsonObject = config.Config(configPath).get_json_object()
		oldMessage = oldJsonObject[self.stage]["decisions"][index]

		config.Config(configPath).edit_json_value_double(
					config.Config(configPath).get_json_object(),
					self.stage,
					"decisions",
					index,
					message
				)
		return

	def decision_list(self):
		configPath = doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)
		jsonObject = config.Config(configPath).get_json_object()
		return jsonObject[self.stage]["decisions"]

	def game_setup(self, configPath):
		render.clear_console()
		createMessages = config.get_message_list("create", "messages")
			
		console.Console().print_list(createMessages)

		config.Config(configPath).load_config()
			
		self.loadedConfig = config.Config(doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)).get_loaded_config()

		gameStages = console.Console("Number of stages for your game: ", "Please input a numerical value.\n").input_integer()
		stageCounter = 1
		render.clear_console()
			
		for stage in range(gameStages):
			dialogLines = []
			decisionLines = []
					
			stageName = console.Console("Stage {} / {} name: ".format(str(stageCounter), str(gameStages)), "Please input a valid stage name.\n").input_unique_string("start").lower()

			while not stageName.isalnum():
				print("Stage names must be alphanumeric strings only.\n")
				stageName = console.Console("Stage {} / {} name: ".format(str(stageCounter), str(gameStages)), "Please input a valid stage name.\n").input_unique_string("start").lower()
				
			stageDialogAmount = console.Console("Number of dialog lines for stage '{}': ".format(stageName), "Please input a numerical value.\n").input_integer()

			dialogCounter = 1
			render.clear_console()
					
			for dialog in range(stageDialogAmount):
				dialogInput = console.Console("'{}' dialog {} / {}: ".format(stageName, dialogCounter, stageDialogAmount), "Please input a valid string.\n").input_string()

				dialogLines.append(dialogInput)
				dialogCounter += 1

			stageDecisionAmount = console.Console("Number of decisions for stage '{}': ".format(stageName), "Please input a numerical value.\n").input_integer()

			decisionCounter = 1
			render.clear_console()
					
			for decisions in range(stageDecisionAmount):
				decisionInput = console.Console("'{}' decision {} / {}: ".format(stageName, decisionCounter, stageDecisionAmount), "Please input a valid string.\n").input_string()

				decisionLines.append(decisionInput)
				decisionCounter += 1

			# enter all info into json file here
			Game(stageName).create_stage()

			for line in dialogLines:
				Game(stageName).create_dialog(line)

			for line in decisionLines:
				Game(stageName).create_decision(line)

			stageCounter += 1

		render.Render().start_screen()

	def edit_game(self, configPath):
		render.clear_console()
		editMessages = config.get_message_list("edit", "messages")
		editDecisions = config.get_message_list("edit", "decisions")

		console.Console().print_list(editMessages)
		console.Console().print_list(editDecisions)

		config.Config(configPath).load_config()
			
		self.loadedConfig = config.Config(doc.File(config.storagePath).get_value("loadedConfig:", config.defaultConfigPath)).get_loaded_config()

		userInput = console.Console("> ", "Please select a valid option.\n").input_list(availableOptions)
		render.clear_console()

		if userInput == "1":
			print("------- Add Stage -------\n\n")
			stageCounter = 1
			stageAmount = console.Console("Number of stages to be added: ", "Please input a numerical value.\n").input_integer()

			for stages in range(stageAmount):
				stageInput = console.Console("Stage {} / {} name: ".format(str(stageCounter), str(stageAmount)), "Please input a valid stage name.\n").input_unique_string("start").lower()

				while not stageInput.isalnum():
					print("Stage names must be alphanumeric strings only.\n")
					stageInput = console.Console("Stage {} / {} name: ".format(str(stageCounter), str(stageAmount)), "Please input a valid stage name.\n").input_unique_string("start").lower()
									
				Game(stageInput).create_stage()
				stageCounter += 1

			self.edit_game(configPath)
			return

		if userInput == "2":
			print("------- Remove Stage -------\n\n")
			configStages = config.Config(configPath).get_json_object()
			console.Console().print_list(configStages)
					
			stageInput = console.Console("Stage name: ", "Please input a valid stage name.\n").input_list(configStages).lower()

			while stageInput == "start":
				print("You can't remove the stage 'start'.\n")
				stageInput = console.Console("Stage name: ", "Please input a valid stage name.\n").input_list(configStages).lower()
							
			Game(stageInput).remove_stage()
			self.edit_game(configPath)
			return

		if userInput == "3":
			print("------- Add Dialog -------\n\n")
			configStages = config.Config(configPath).get_json_object()
			console.Console().print_list(configStages)
					
			stageInput = console.Console("Stage name: ", "Please input a valid stage name.\n").input_list(configStages).lower()
			render.clear_console()
					
			dialogCounter = 1
			dialogAmount = console.Console("Number of dialog lines to add to stage '{}': ".format(stageInput), "Please input a numerical value.\n").input_integer()

			for dialog in range(dialogAmount):
				dialogInput = console.Console("Enter dialog {} / {} for '{}': ".format(dialogCounter, dialogAmount, stageInput), "Please input a valid string.\n").input_string()
				Game(stageInput).create_dialog(dialogInput)
				dialogCounter += 1

			self.edit_game(configPath)
			return

		if userInput == "4":
			print("------- Remove Dialog -------\n\n")
			configStages = config.Config(configPath).get_json_object()
			console.Console().print_list(configStages)
					
			stageInput = console.Console("Stage name: ", "Please input a valid stage name.\n").input_list(configStages).lower()
			render.clear_console()

			dialogList = Game(stageInput).dialog_list()
			console.Console().print_list(dialogList, True)
							
			indexInput = console.Console("Line number to remove ({} to {}): ".format(1, len(dialogList)), "Please input a valid numerical value.\n").input_integer_range(1, len(dialogList))
					
			Game(stageInput).remove_dialog(indexInput - 1)
			self.edit_game(configPath)
			return

		if userInput == "5":
			print("------- Edit Dialog -------\n\n")
			configStages = config.Config(configPath).get_json_object()
			console.Console().print_list(configStages)
					
			stageInput = console.Console("Stage name: ", "Please input a valid stage name.\n").input_list(configStages).lower()
			render.clear_console()

			dialogList = Game(stageInput).dialog_list()
			console.Console().print_list(dialogList, True)

			indexInput = console.Console("Line number to edit ({} to {}): ".format(1, len(dialogList)), "Please input a valid numerical value.\n").input_integer_range(1, len(dialogList))
			render.clear_console()

			print("Currently editing:\n\n" + Game(stageInput).dialog_list()[indexInput - 1] + "\n\n")
			dialogInput = console.Console("Line {} replacement dialog: ".format(indexInput), "Please input a valid string.\n").input_string()

			Game(stageInput).edit_dialog(indexInput - 1, dialogInput)
			self.edit_game(configPath)
			return

		if userInput == "6":
			print("------- Add Decision -------\n\n")
			configStages = config.Config(configPath).get_json_object()
			console.Console().print_list(configStages)

			stageInput = console.Console("Stage name: ", "Please input a valid stage name.\n").input_list(configStages).lower()
			render.clear_console()

			decisionCounter = 1
			decisionAmount = console.Console("Number of decisions to add to stage '{}': ".format(stageInput), "Please input a numerical value.\n").input_integer()

			for decison in range(decisionAmount):
				decisionInput = console.Console("Enter decision {} / {} for '{}': ".format(decisionCounter, decisionAmount, stageInput), "Please input a valid string.\n").input_string()
				Game(stageInput).create_decision(decisionInput)
				decisionCounter += 1

			self.edit_game(configPath)
			return
			
		if userInput == "7":
			print("------- Remove Decision -------\n\n")
			configStages = config.Config(configPath).get_json_object()
			console.Console().print_list(configStages)

			stageInput = console.Console("Stage name: ", "Please input a valid stage name.\n").input_list(configStages).lower()
			render.clear_console()

			decisionList = Game(stageInput).decision_list()
			console.Console().print_list(decisionList, True)
							
			indexInput = console.Console("Line number to remove ({} to {}): ".format(1, len(decisionList)), "Please input a valid numerical value.\n").input_integer_range(1, len(decisionList))
					
			Game(stageInput).remove_decision(indexInput - 1)
			self.edit_game(configPath)
			return
			
		if userInput == "8":
			print("------- Edit Decision -------\n\n")
			configStages = config.Config(configPath).get_json_object()
			console.Console().print_list(configStages)

			stageInput = console.Console("Stage name: ", "Please input a valid stage name.\n").input_list(configStages).lower()
			render.clear_console()

			decisionList = Game(stageInput).decision_list()
			console.Console().print_list(decisionList, True)

			indexInput = console.Console("Line number to edit ({} to {}): ".format(1, len(decisionList)), "Please input a valid numerical value.\n").input_integer_range(1, len(decisionList))
			render.clear_console()

			print("Currently editing:\n\n" + Game(stageInput).decision_list()[indexInput - 1] + "\n\n")
			decisionInput = console.Console("Line {} replacement decision: ".format(indexInput), "Please input a valid string.\n").input_string()

			Game(stageInput).edit_decision(indexInput - 1, decisionInput)
			self.edit_game(configPath)
			return

		if userInput == "exit":
			render.Render().start_screen()
			return