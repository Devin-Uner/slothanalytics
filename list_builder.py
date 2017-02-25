# file = open("symptoms.txt", "r")
# symptoms = []
# skip = False
# for line in file:
# 	if("$" in line):
# 		skip = True
# 	else:
# 		if(skip == False):
# 			if(line.replace("\n", "") not in symptoms):
# 				symptoms += [line.replace("\n", "")]
# 		else:
# 			skip = False

# print symptoms
# print len(symptoms)

# generates the dictionary
file = open("symptoms.txt", "r")
dictionary = {}
allText = ""
for line in file:
	if(len(line) > 3 or "$" in line):
		allText += line
file.close()
allText = allText.split("$")
for thing in allText:
	if(len(thing) > 2):
		# print thing.split("\n")
		dictionary[thing.split("\n")[1]] = thing.split("\n")[2:]

diseases = dictionary.keys()
# print diseases
symptoms = list()
for symptomList in dictionary.values():
	symptoms = list(set(symptoms) | set(symptomList))
print symptoms


tesing1 = dictionary["Heart attacks"]
def matchAandSymptoms(input1):
	result = [0] * len(symptoms)
	for i in range(len(symptoms)):
		# print symptoms[i]
		if(symptoms[i] in input1): 
			result[i] = 1
		else:
			result[i] = 0
	return result

def matchBandDiseases(input2):
	result = [0] * len(diseases)
	for i in range(len(diseases)):
		if(diseases[i] == input2): 
			result[i] = 1
		else:
			result[i] = 0
	return result

def printArray(inputList):
	print "[",
	for i in range(len(inputList)-1):
		print str(inputList[i]) + ",",
	print str(inputList[-1])+"]"

# printArray(matchAandSymptoms(tesing1))
# print ""
printArray(matchBandDiseases("Heart attacks"))

for disease in diseases:
	print disease
	printArray(matchBandDiseases(disease))
	printArray(matchAandSymptoms(dictionary[disease]))
	# print "-------------------"











