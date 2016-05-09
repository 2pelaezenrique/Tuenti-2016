class Tables:
	def __init__(self, diners):
	    self.__diners = diners

	def resolve(self):
		# If there are no diners, then no tables
		if(self.__diners <=0):
			return 0
		#If there are only 4 diners or less, only one table is needed
		if(self.__diners <= 4):
			return 1
		else:
			#For each extra pair you need to add a table. 
			if(self.__diners % 2 == 0):
				extraPeople = self.__diners -4
				return int(extraPeople/2 + 1)
			else:
				extraPeople = self.__diners -3
				return int(extraPeople/2 + 1)

if __name__ == "__main__":
	f = open('testInput.sdx', 'r')
	lines = [line.replace('\n', '') for line in f]
	for diners in range(0, int(lines[0])):
		print ("Case #%d: %s" % (diners+1 , Tables(int(lines[diners + 1])).resolve()))