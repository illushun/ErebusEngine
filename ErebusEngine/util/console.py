from time import sleep

class Console:
	def __init__(self, outputText = "", errorMessage = ""):
		self.outputText = outputText
		self.errorMessage = errorMessage

	def print(self):
		print(self.outputText)
		return

	def print_list(self, list, numberedList = False):
		lineCounter = 1
		for line in list:
			if numberedList:
				print("{}. {}".format(lineCounter, line))
				lineCounter += 1
			else:
				print(line)
		return

	def contains_list_item(self, list):
		return any(item in self.outputText for item in list)

	def contains_item(self, item):
		return self.outputText.__contains__(item)

	def print_commands(self, list, numberedList = True):
		lineCounter = 1
		for line in list:
			if line.__contains__("$LOAD"):
				start = line.index('$')
				end = line.index('$', start + 1)
				substring = line[start + 1 : end]
				line = line.replace("${}$".format(substring), "")

			if line.__contains__("#SLEEP"):
				line = line.replace("#SLEEP", "")
				sleep(1)
                
			if numberedList:
				if line.__contains__("#NO_NUMBER"):
					print(line.replace("#NO_NUMBER", ""))
				else:
					print("{}. {}".format(lineCounter, line))
			else:
				print(line)

			lineCounter +=1
		return

	def input_confirmation(self):
		input(self.outputText)
		return

	def input_string(self):
		userInput = input(self.outputText)
		while self.length_less(userInput, 1):
			if self.length_more(self.errorMessage, 0):
				print(self.errorMessage)
				
			userInput = input(self.outputText)
		return str(userInput)

	def input_unique_string(self, compare):
		userInput = self.input_string()
		while userInput == compare:
			if self.length_more(self.errorMessage, 0):
				print(self.errorMessage)
				
			userInput = self.input_string()
		return str(userInput)

	def input_integer(self):
		userInput = input(self.outputText)
		while self.length_less(userInput, 1) or not userInput.isdigit():
			if self.length_more(self.errorMessage, 0):
				print(self.errorMessage)
				
			userInput = input(self.outputText)
		return int(userInput)

	def input_integer_range(self, minValue, maxValue):
		userInput = self.input_integer()
		while userInput < minValue or userInput > maxValue:
			if self.length_more(self.errorMessage, 0):
				print(self.errorMessage)
				
			userInput = self.input_integer()
		return int(userInput)

	def input_list(self, list):
		userInput = input(self.outputText)
		while self.length_less(userInput, 1) or not self.check_in_list(userInput, list):
			if self.length_more(self.errorMessage, 0):
				print(self.errorMessage)
				
			userInput = input(self.outputText)
		return userInput

	def input_unique_list(self, list):
		userInput = self.input_string()
		while self.check_in_list(userInput, list):
			if self.length_more(self.errorMessage, 0):
				print(self.errorMessage)
				
			userInput = self.input_string()
		return userInput

	def length_less(self, input, value):
		return len(input) < value

	def length_more(self, input, value):
		return len(input) > value

	def check_in_list(self, input, list):
		return input in list

	'''
	def init_user_input_integer_list(self, outputText, list, lowestValue, highestValue):
		userInput = input(outputText)
		while len(userInput) <= 0 or not userInput.isdigit():
			userInput = input(outputText)
		while int(userInput) < (lowestValue - 1) or int(userInput) > (highestValue - 1):
			userInput = input(outputText)
		return userInput
	'''