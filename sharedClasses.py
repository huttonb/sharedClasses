def main():
#	text = input('filename 1:')
#	text1 = input('filename 2:')
	
	
#	socFile = open(text, "r")
#	issuesFile = open(text1, "r")

	fuckBackSlash = "\\"
	print(fuckBackSlash)
	className1 = "F:"+ fuckBackSlash + input("Input first File Name : ") + ".txt"
	className2 = "F:" + fuckBackSlash + input("Input second File Name: ") + ".txt"
	socFile = ("F:\social.txt")
	issuesFile = ("F:\issues.txt")
	firstClasses = formatClassesFile(className1, True)
	secondClasses = formatClassesFile(className2, True)
	
	
	
	findCommonClasses(className1, className2, firstClasses, secondClasses)

	
def formatClassesFile(fileName, display):
	tempFile = open(fileName, "r")
	classesString = tempFile.read()
	classesString = classesString.replace("*","")
	classesList = classesString.split(' or ')
	dep = ""
		# goes through and adds the depName to the class number
	for x in range(0, len(classesList) - 1):
		if classesList[x].islower() or classesList[x].isupper():
			tokens = classesList[x].split(' ')
			dep = tokens[0]
		else:
			classesList[x] = dep + " " + classesList[x]
	
	if display:
		print("\nPrinting file name: " + fileName + "\n")
		for classNum in classesList:
			print(classNum)
		
		
	return classesList
	
	
	
def findCommonClasses(fileNameOne, fileNameTwo, classListOne, classListTwo):
	combinedClasses = list()
	for classNumOne in classListOne:
		for classNumTwo in classListTwo:
			if classNumOne == classNumTwo:
				combinedClasses.append([classNumOne])
				
				
	fuckBackSlash = "\\"			
	newCombinedFile = "F:" + fuckBackSlash + input("What would you like to call this new list?") + ".txt"
	
	t = open(newCombinedFile, 'w')
	f = open('combinedClasses.txt', 'w')
	f.write('\n \n **************************************************')
	f.write('\n Combined Classes of: ' + fileNameOne + ' and of: ' + fileNameTwo + " are: \n")
	for classNum in combinedClasses:
	
		tempString1 = ""
		tempString1 = classNum
		f.write("%s\n" % tempString1)
		t.write("%s\n" % tempString1)
	
	

main()


	
