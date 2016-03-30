import mechanize


class ThirdStep():

	def __init__(self, browser, request, response):
		#print "Get code", response.code, "for the third link."
		browser.open(request)
		self.br = browser

	def enterPassword(self, password):
		br = self.br
		br.select_form(nr=0)
		br.form['pwd'] = password
		br.submit()