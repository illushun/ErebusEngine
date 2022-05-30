import os

import ErebusEngine.util.documents as doc
import ErebusEngine.util.console as console
import ErebusEngine.backend.player as player
import ErebusEngine.backend.engine as engine
import ErebusEngine.config as config

availableOptions = ["1", "2", "3", "4", "exit"]
configFileExtension = ".json"

def clear_console():
	os.system('cls' if os.name in ('nt', 'dos') else 'clear')

class Render:
	def __init__(self):
		pass

	def start_screen(self):
		clear_console()
		startMessages = config.get_message_list("start", "messages")
		startDecisions = config.get_message_list("start", "decisions")

		console.Console().print_list(startMessages)
		console.Console().print_list(startDecisions)

		userInput = console.Console("> ", "Please select a valid option...\n").input_list(availableOptions)

		# start college adventure
		if userInput == "1":
			config.Config(config.defaultConfigFolder + "college_adventure" + configFileExtension).load_config()
			playerObject = player.Player()
			playerObject.set_stage("start")

		# load game
		elif userInput == "2":
			configList = doc.Folder(config.defaultConfigFolder).get_file_list(configFileExtension, False)
			console.Console().print_list(configList)
					
			userInput = console.Console("Load config: ", "Unable to load that config...\n").input_list(configList)
			config.Config(config.defaultConfigFolder + userInput + configFileExtension).load_config()
					
			playerObject = player.Player()
			playerObject.set_stage("start")
			return

		# create game
		elif userInput == "3":
			configList = doc.Folder(config.defaultConfigFolder).get_file_list(configFileExtension, False)
			console.Console().print_list(configList)

			userInput = console.Console("Name your config: ", "Unable to create that config...\n").input_unique_list(configList)			
			engine.Game().game_setup(config.defaultConfigFolder + userInput + configFileExtension)

		# edit game
		elif userInput == "4":
			configList = doc.Folder(config.defaultConfigFolder).get_file_list(configFileExtension, False)
			console.Console().print_list(configList)
					
			userInput = console.Console("Load config: ", "Unable to load that config...\n").input_list(configList)
			engine.Game().edit_game(config.defaultConfigFolder + userInput + configFileExtension)

	def game_text(self, dialogList, decisionList):
		console.Console().print_commands(dialogList, False)
		console.Console("Press 'ENTER' to continue...").input_confirmation()
		clear_console()

		#print("Current stage: " + player.Player().get_current_stage() + "\n\n")
		print("Available Options:\n\n")
		console.Console().print_commands(decisionList)

'''
# pip3 install rich
# doesn't work due to an 'OSError' (Permission denied)
from rich import print
from rich.panel import Panel

# TODO
class Render:
    def __init__(self):
        pass

    def start_screen(self):
        print(Panel("Testing", title="Tester"))
        pass
'''