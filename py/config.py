from firstStep import FirstStep
from encryption import Encryption
import easygui

# Links
linkPorrum = "http://porrum.informatique.univ-paris-diderot.fr:8080/~etudiant/"
linkMagma = "http://magma.informatique.univ-paris-diderot.fr:2201/~etudiant/"

def getInputAsInt():
	val = 0
	try:
		val=int(raw_input('Choice:'))
	except ValueError:
		print "Not a number !"
	return val

def printValues(theList):
	index = 1
	for item in theList:
		print index, "-", item
		index = index + 1
	del index

def printAndChoose(theList, maxValue):
	choice = 0
	while choice < 1 or choice > maxValue:
		printValues(theList)
		choice = getInputAsInt()
	return choice

# Start Config
br = FirstStep(linkPorrum)
titles, choises = br.getChoices()
numberOfCourses = len(titles)
print "Please introduce the correct answers !"
print numberOfCourses, "courses detected. Please choose yours."
course = printAndChoose(titles, numberOfCourses)
selectedCourse = choises[course - 1].name
br.chooseCourse(selectedCourse)
names = br.getNames()
numberOfNames = len(names)
print numberOfNames, "names detected. Please choose yours."
name = printAndChoose(names, numberOfNames)
selectedName = names[name - 1]
password = ""
while len(password) == 0:
	password = easygui.passwordbox(msg='Password:', title='Encryption message', default='')
passphrase = ""
while len(passphrase) == 0:
	passphrase = easygui.passwordbox(msg='Passphrase:', title='Encryption message', default='')
enc = Encryption(password, passphrase)
fileConfig = open ("marks.cfg", 'w')
fileConfig.write("%s\n"%selectedCourse)
fileConfig.write("%s\n"%selectedName)
fileConfig.write("%s"%enc.encrypt())
print "All data saved !"