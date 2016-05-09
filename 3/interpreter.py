class Interpreter: 
	def __init__(self):
		self.__scaffold = {1: self.setMethod, 2: self.setCase, 3:self.setAction}
		self.dictionary = {}
		self.tests = {}
	def createDictionary(self, instructions):
		# status = [nameOfMethod, case]
		status = [0,0]
		lineAtTests= False
		for instruction in instructions:
			indentation = (len(instruction) - len(instruction.lstrip(' ')))/2
			instruction = instruction.lstrip(' ')
			if(instruction == "tapes:"):
				lineAtTests= True
				continue
			if(indentation == 0):
				continue
			if(lineAtTests):
				self.setTest(instruction)
				continue
			status = self.__scaffold[indentation](instruction , status)
	
	def setMethod(self, instruction, status):
		nameOfMethod = instruction.replace(":", "")
		self.dictionary[nameOfMethod] = {}
		status[0] = nameOfMethod
		return status
	
	def setCase(self, instruction, status):
		case = instruction.replace(":", "").replace("'","")
		self.dictionary[status[0]][case] = {}
		status[1] = case
		return status
	
	def setAction(self, instruction, status):
		action = instruction.split(":")
		action[0] = action[0].lstrip(" ")
		action[1] = action[1].lstrip(" ").replace("'","")
		self.dictionary[status[0]][status[1]][action[0]] = action[1]
		return status	
	def setTest(self, instruction):
		test = instruction.split(":")
		numberOfTest = test[0].replace(" ", "")
		sentence = test[1].replace("'","").replace(" ", "")
		self.tests[numberOfTest] = sentence

	def calculateResultOf(self, code):
		result = list(code)
		method = "start"
		position = 0
		while (method != "end"):
			if(position < 0):
				result = [" "] + result
				position += 1
			if(position == len(result)):
				result.append(" ")
			letter = result[position]
			if ("write" in self.dictionary[method][letter]):
				result[position] = self.dictionary[method][letter]["write"]
			
			if ("move" in self.dictionary[method][letter]):
				if (self.dictionary[method][letter]["move"] == "right"):
					position+= 1
				else:
					position-= 1
			if ("state" in self.dictionary[method][letter]):
				method = self.dictionary[method][letter]["state"]
			
			
		return "".join(result)

	def resolve(self, instructions):
		self.createDictionary(instructions)
		file = open('output', 'w+')
		for key , value in sorted(self.tests.items()):
			if(key != "1"):
				file.write("\n")
			file.write("Tape #%d: %s" % (int(key), self.calculateResultOf(value)))
		file.close()
if __name__ == "__main__":
	program = open('testInput.sdx', 'r')
	instructions = [line.replace('\n', '') for line in program]
	Interpreter().resolve(instructions)
	program.close()