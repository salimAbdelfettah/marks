from bs4 import BeautifulSoup
import re

class FifthStep():

	COURSE = 1
	RESULT = 2
	MARK = 3
	JURY= 4
	SESSION = 5

	def __init__(self, browser, request, response):
		#print "Get code", response.code, "for the fifth link."
		browser.open(request)
		self.br = browser


	def getMarks(self):
		br = self.br
		text = br.response().read()
		#text = unidecode(text)
		text = re.sub(r'&nbsp;', '', text)
		soup = BeautifulSoup(text.strip(u'\xa0'), "html.parser")
		body = soup.body
		data = body.findAll("td")
		numberOfMarks = 0
		index = 1
		marks = []
		for td in data:
			if td.a == None:
				text = td.string
			else:
				text = td.a.string
			if index == FifthStep.COURSE:
				courseName = text
			elif index == FifthStep.MARK:
				if text == None:
					marks.append((courseName, 0.))
				else:
					marks.append((courseName, float(text)))
					numberOfMarks = numberOfMarks + 1
			elif index == FifthStep.SESSION:
				index = 0
			index = index + 1
		return numberOfMarks, marks