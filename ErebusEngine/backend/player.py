import json

import ErebusEngine.display.render as render
import ErebusEngine.backend.engine as engine

decisionInputMessage = "I think i'll go with...: "
decisionNotNumberMessage = "\nCan you not see the available decisions?!...\n"
decisionOutOfRangeMessage = "\nThere isn't that many decisions to choose from...\n"

class Player:
    previousStages = []
    currentStage = "start"
	
    def __init__(self):
        pass

    def get_current_stage(self):
        return self.currentStage
	
    def set_stage(self, stage):
			  # if list has over 3 items, remove first item as we don't need so much history
        if len(self.previousStages) > 3:
            self.previousStages.pop(0)

			  # if list already contains duplicate, remove it
        if self.previousStages.__contains__(stage):
            self.previousStages.remove(stage)
					
        self.previousStages.append(stage)
        self.currentStage = stage
			
        render.clear_console()
        getStage = engine.Game(stage)
        stageDialog = getStage.dialog_list()
        stageDecisions = getStage.decision_list()

        render.Render().game_text(stageDialog, stageDecisions)
        self.decision_input()

    def previous_stage(self):
        currentStageIndex = self.previousStages.index(self.currentStage)

        if currentStageIndex == 0:
            self.set_stage(self.currentStage)
        else:
            self.set_stage(self.previousStages[currentStageIndex - 1])

    def decision_input(self):
        getStage = engine.Game(self.currentStage)
        userInput = input(decisionInputMessage)

        while not userInput.isdigit():
            if userInput == "back":
                self.previous_stage()
                return

            if userInput == "exit":
                return

            print(decisionNotNumberMessage)
            userInput = input(decisionInputMessage)

        while int(userInput) < 1 or int(userInput) > len(getStage.decision_list()):
            print(decisionOutOfRangeMessage)
            userInput = input(decisionInputMessage)

        chosenDecision = getStage.decision_list()[int(userInput) - 1]
			
        if chosenDecision.__contains__("$LOAD"):
            start = chosenDecision.index('$')
            end = chosenDecision.index('$', start + 1)
            substring = chosenDecision[start + 1 : end]

            loadPage = substring.split('_')[1].lower()
            self.set_stage(loadPage)

        #print("You have selected: 'decision " + userInput + "'")
        