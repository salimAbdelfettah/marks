import mechanize
import cookielib
import re

class FirstStep():
	searchCoursesStr = "&nbsp;.*?<"
	searchNamesStr = "\">.*?</a>"

	def __init__(self, link):
		self.link = link
		# Browser
		br = mechanize.Browser()
		# Cookie Jar
		cj = cookielib.LWPCookieJar()
		br.set_cookiejar(cj)
		# Browser options
		br.set_handle_robots(False)
		br.set_handle_redirect(True)
		br.set_handle_refresh(False)
		br.set_handle_equiv(True)
		br.set_handle_referer(True)
		br.addheaders = [('User-agent', 'Firefox')]
		# Open link
		response = br.open(self.link)
		control = None
		#print "Get code", response.code, "for the first link."
		if response.code == 200:
			html = response.get_data().replace("<p/>", "").replace("<p />", "").replace("<hr/>", "")
			response = mechanize.make_response(html, [("Content-Type", "text/html")], self.link, 200, "OK")
			br.set_response(response)
			#print "Tags removed for forms detection."
			# Select the first (index zero) form
			br.select_form(nr=0)
			control = br.form.find_control("idCursus")
		self.br = br
		self.control = control

	def getChoices(self):
		br, control = self.br, self.control
		if control != None:
			textPage = br.response().read()
			courses = re.findall(FirstStep.searchCoursesStr, textPage)
			theCourses = []
			for course in courses:
				course = course.split("<")[0]
				course = course.split(";")[1]
				theCourses.append(course)
				del course
			return theCourses, control.items
		return None, None

	def chooseCourse(self, selected):
		br = self.br
		br.form.set_value([selected], name='idCursus')
		br.submit()
		return self.br

	def getNames(self):
		text = self.br.response().read()
		names = re.findall(FirstStep.searchNamesStr, text)
		theNames = []
		for name in names:
			if len(name) <= 30:
				name = name.split(">")[1]
				name = name.split("<")[0]
				theNames.append(name)
		return theNames