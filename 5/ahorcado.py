from pymongo import MongoClient
import time
import re
import getpass
import telnetlib

class Ahorcado:
	def addWordToDB(self, word, db):
		addWord = db.words.insert_one({"word": word})
		print(word)

	def sayLetter(self, preWord, pastLetters):
		client = MongoClient()
		db = client.ahorcado
		regx = re.compile("^" + preWord + "$", re.IGNORECASE)
		allWords = db.words.find({"word": regx})
		letterCounter = {}
		for document in allWords:
			#print(document["word"] + " : "+ str(len(document["word"])))
			lettersInWord = list(set(list(document["word"])))
			for letter in lettersInWord:
				if not letter in pastLetters:
					letterCounter[letter] = letterCounter.get(letter, 1)
					letterCounter[letter] += 1
		
		mostRepeatedLetter = ""
		timesRepeated = 0
		for letter, repetitions in letterCounter.items():
			if repetitions > timesRepeated:
				mostRepeatedLetter = letter
				timesRepeated = repetitions
		
		return mostRepeatedLetter

if __name__ == "__main__":
	#updateDB = input("Update DB (y/n) :")
	updating = False
	while(updating):
		if (updateDB == "y"):
			f = open('words.txt', 'r')
			words = [line.replace('\n', '') for line in f]
			client = MongoClient()
			client.drop_database("ahorcado")
			print("Base de datos borrada")
			db = client.ahorcado
			print("seleccionada base de datos")
			for word in words:
				Ahorcado().addWordToDB(word,db)
			f.close()
			updating = False
		elif(updateDB == "n"):
			updating = False
		else:
			updateDB = input("Only 'n' and 'y' characters are accepted. Update DB? (y/n) :")
	playing = True
	
	HOST = "52.49.91.111"
	PORT = "9988"
	tn = telnetlib.Telnet(HOST, PORT)
	time.sleep(1)
	tn.write(("a\n").encode('ascii'))
	time.sleep(1)


	letters = ""
	screen = b""
	while (playing):
		
		try:
			if(tn.eof):
				raise
			screenArray =screen.decode("ascii").split("\n")
			for line in screenArray:
					print(line)
			
		except:
			#import pdb
			#pdb.set_trace()
			screenArray =screen.decode("ascii").split("\n")
			for line in screenArray:
					print(line)
			playing = False
		else:
			screen = tn.read_very_eager()
			screenArray =screen.decode("ascii").split("\n")
			if (not len(screenArray) - 3 < 0):
				screenNecesary = screenArray[len(screenArray) - 3]
			else:
				for line in screenArray:
					print(line)
				tn.write((nextLetter+"\n").encode('ascii'))
				time.sleep(0.1)
				letters = ""
				continue

			preWord = screenNecesary.replace("_", ".").replace(" ", "")
			print(preWord)

			if (not "." in preWord):
				for line in screenArray:
					print(line)
				tn.write((nextLetter+"\n").encode('ascii'))
				time.sleep(0.1)
				letters = ""
			else:
				if (len(letters) != 0):
					preWord = preWord.replace("." , "[^" + letters + "]")
				nextLetter = Ahorcado().sayLetter(preWord, letters)
				letters += nextLetter
				#print(letters)

				tn.write((nextLetter+"\n").encode('ascii'))
				time.sleep(0.1)
				
