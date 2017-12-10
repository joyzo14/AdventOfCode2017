def calculate(word):
	count = 0
	word=str(word)
	for i in range(len(word)):
		if word[i-1]==word[i]:
			count+=int(word[i])
	return count