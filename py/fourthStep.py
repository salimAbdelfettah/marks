import mechanize

class FourthStep():

	def __init__(self, br, link):
		#print "Get code", br.response().code, "for the fourth link."
		self.br = br
		self.link = link

	def accessMarks(self, username):
		br = self.br
		answerText = br.response().read()
		if "Erreur d'identification" in answerText:
			print "Connection failed !"
			print "Wrong password for user", username
			print "Please run 'config' again with the correct username and password."
			return None, None
		else:
			#print "Connection success !"
			html = br.response().get_data().replace("<p/>", "")
			response = mechanize.make_response(html, [("Content-Type", "text/html")], self.link, 200, "OK")
			br.set_response(response)
			for link in self.br.links():
				if "voirNotes" in link.url:
					request = self.br.click_link(link)
					response = self.br.follow_link(link)
					return request, response