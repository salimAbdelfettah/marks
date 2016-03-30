import mechanize

class SecondStep():

	def __init__(self, br):
		#print "Get code", br.response().code, "for the second link."
		self.br = br

	def getRequestAndResponseForUsername(self, username):
		if self.br.response().code == 200:
			for link in self.br.links():
				if link.text == username:
					request = self.br.click_link(link)
					response = self.br.follow_link(link)
					return request, response
		return None
