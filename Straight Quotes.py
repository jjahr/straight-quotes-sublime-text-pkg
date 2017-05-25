# coding: utf8
"""StraightQuotes plugin module."""

import sublime
import sublime_plugin

class StraightQuotesCommand(sublime_plugin.TextCommand):
	""" Main plugin class  “” ‘’ """
	def run(self, edit):
		
		""" self.view.insert(edit, 0, "Hello, World!") """
		
		for region in self.view.find_all("“"):
			self.view.replace(edit, region, "\"")

		for region in self.view.find_all("”"):
			self.view.replace(edit, region, "\"")
		
		for region in self.view.find_all("‘"):
			self.view.replace(edit, region, "\'")

		for region in self.view.find_all("’"):
			self.view.replace(edit, region, "\'")

		""" 
		Add markers after "// comment" comments, so that we can add back in linebreaks later.
		for region in self.view.find_all(r';.*\/\/.*\n'):
			self.view.insert(edit, region, "jjlinebreak")

		Remove all linebreaks not preceeded with semicolon
		for region in self.view.find_all(r'\n(?<!;\n)'):
			self.view.replace(edit, region, "")

		Add linebreaks where we have "jjlinebreak"
		for region in self.view.find_all("jjlinebreak"):
			self.view.replace(edit, region, "\n")
		"""

