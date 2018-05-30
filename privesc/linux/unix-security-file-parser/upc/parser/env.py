from upc.parser.parser import parser
import re

class env(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		lines = self.slurpfile(filename, {"remove_comments": "^#", "remove_blanklines": 1, "trim": 1})
		
		tmoutset = 0
		
		for line in lines:
			if re.search("^TMOUT=\d+", line):
				tmoutset = 1
				
		if not tmoutset:
			self.report.get_by_id("UPC579").add_supporting_data('text_line', [self.kb, ""])
				
