from collections import Counter
import re

class WordsRepeated:
	def __init__(self, firstWord, lastWord):
		self.__firstWordIndex = firstWord - 1
		self.__lastWordIndex = lastWord - 1
		self.__totalWords = 1 + lastWord - firstWord;
	def resolve(self):
		f = open('corpus.txt', 'r')
		allWords = f.read().split(" ")

		if(len(allWords) != self.__totalWords):
			for trash in range(self.__firstWordIndex):
				allWords.pop(0)
		if(len(allWords) != self.__totalWords):
			for trash in range(len(allWords) - self.__totalWords):
				allWords.pop()
		slectedText = " ".join(allWords)
		reg = re.compile('\S{1,}')
		mostCommonWords = Counter(ma.group() for ma in reg.finditer(slectedText)).most_common(3)
		return mostCommonWords


if __name__ == "__main__":
	cases = open('testInput.sdx', 'r')
	lines = [line.replace('\n', '') for line in cases]
	for case in range(0, int(lines[0])):
		solution = WordsRepeated(int(lines[case + 1].split(" ")[0]), int(lines[case + 1].split(" ")[1])).resolve()
		print ("Case #%d: %s" % (case+1 , solution[0][0] + " " + str(solution[0][1])+","+ solution[1][0] + " " + str(solution[1][1])+","+ solution[2][0] + " " + str(solution[2][1])))