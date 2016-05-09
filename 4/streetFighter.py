class Combos: 
	combos = {	1 : ["L" , "LD" , "D", "RD", "R","P"],
				2 : ["D" , "RD", "R", "P"],
				3 : ["R", "D", "RD", "P"],
				4 : ["D", "LD", "L" ,"K"],
				5 : ["R", "RD", "D","LD","L", "K"]}

	def __init__(self):
		self.position = {	1: 0,
							2: 0,
							3: 0,
							4: 0,
							5: 0}
	
	def updateCombo(self, n, move):
		actualStep = self.combos[n][self.position[n]]
		if (move == actualStep):
			self.continueCombo(n)
		else:
			lastPosition = self.position[n]
			self.resetCombo(n)
			if (lastPosition != 0):
				self.updateCombo(n,move)
		if (self.position[n] == len(self.combos[n])):
			self.resetCombo(n)
			
	def checkIfComboFilsAtEnd(self, n, nextMove):
		#It is necessary to update the combos before calling this method
		itFails = False
		nextStepOfCombo = self.combos[n][self.position[n]]
		comboBeforeLastMove = self.position[n]==len(self.combos[n]) - 1
		if(comboBeforeLastMove and nextStepOfCombo != nextMove):
			itFails = True
		elif(comboBeforeLastMove):
			self.resetCombo(n)
		return itFails

	def continueCombo(self, n):
		self.position[n]	+= 1

	def resetCombo(self, n):
		self.position[n]	= 0	
	
	def countFailsAtSession(self, session):
		i = 0
		numberOfFails = 0
		for move in session:
			someComboFails = False
			for n in range(1,6):
				self.updateCombo(n, move)
				nextMove = ""
				if(i != len(session) - 1):
					nextMove = session[i+1]
				else:
					nextMove = "None"
				
				if (self.checkIfComboFilsAtEnd(n, nextMove)):
					someComboFails = True
				
			if (someComboFails):
				numberOfFails += 1
					
			i += 1
		return numberOfFails
if __name__ == "__main__":
	history = open('submitInput.sdx', 'r')
	output = open("output", "w+")
	trainingSessions = [line.replace('\n', '') for line in history]
	for case in range(0,int(trainingSessions[0])):
		session = trainingSessions[case+1].split("-")
		if(case != 0):
			output.write("\n")
		output.write("Case #%d: %s" % (case + 1, Combos().countFailsAtSession(session)))
	history.close()
	output.close()

