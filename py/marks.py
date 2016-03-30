from firstStep import FirstStep
from secondStep import SecondStep
from thirdStep import ThirdStep
from fourthStep import FourthStep
from fifthStep import FifthStep
from encryption import Encryption
import time, datetime, easygui

#links
linkPorrum = "http://porrum.informatique.univ-paris-diderot.fr:8080/~etudiant/"
linkMagma = "http://magma.informatique.univ-paris-diderot.fr:2201/~etudiant/"

def checkOnMarks(course, username, password):
	brFS = FirstStep(linkPorrum)
	bOne = brFS.chooseCourse(course)
	brSS = SecondStep(bOne)
	qTwo, rTwo = brSS.getRequestAndResponseForUsername(username)
	brTS = ThirdStep(bOne, qTwo, rTwo)
	brTS.enterPassword(password)
	brFRS = FourthStep(bOne, linkPorrum)
	qFour, rFour = brFRS.accessMarks(username)
	if qFour != None:
		brFFS = FifthStep(bOne, qFour, rFour)
		return brFFS.getMarks()
	return None, None


theFile = open("marks.cfg", 'r')
course = theFile.readline().rstrip('\n')
username = theFile.readline().rstrip('\n')
password = theFile.readline().rstrip('\n')
print "Data loaded."
passphrase = ""
while len(passphrase) == 0:
	passphrase = easygui.passwordbox(msg='Passphrase:', title='Encryption message', default='')
dec = Encryption(password, passphrase)
password = dec.decrypt()
if len(password) == 0:
	print "Wrong passphrase ! Please try again or run 'config' again."
	oldNumberOfMarks, oldMarks = None, None
else:
	oldNumberOfMarks, oldMarks = checkOnMarks(course, username, password)
	print oldNumberOfMarks, "marks detected."
while oldMarks != None:
	time.sleep(3600)
	numberOfMarks, marks = checkOnMarks(course, username, password)
	if numberOfMarks > oldNumberOfMarks:
		print numberOfMarks - oldNumberOfMarks, "new mark(s) detected. Take a look !"
		textMsg = "Hey ! New mark(s) detected ! Take a look !"
		for oldMark, mark in zip (oldMarks, marks):
			if oldMark[1] != mark [1]:
				textMark = mark[0]+" : "+str(mark[1])
				textMsg = textMsg + "\n" + textMark
				print textMark
		easygui.msgbox(textMsg, title=str(numberOfMarks - oldNumberOfMarks)+" new mark(s)")
	else:
		now = datetime.datetime.now()
		print "No new marks. Last check : %d/%d/%d %d:%d:%d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
	oldNumberOfMarks = numberOfMarks
	oldMarks = marks