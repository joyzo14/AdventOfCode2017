def calculate(word):
	count = 0
	word=str(word)
	newWord=str(word)
	newWord=newWord+newWord[:int(len(newWord)/2)]
	for i in range(len(str(word))):
		if newWord[i] == newWord[int(len(word)/2)+i]:
			count+=int(newWord[i])
	return count