from upc.parser.parser import parser
import re

class sudoers(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		lines = self.slurpfile(filename, {"remove_comments": "^#", "remove_blanklines": 1, "trim": 1})
		
		for line in lines:
			if re.search("^\S+\s.*NOPASSWD:", line):
				self.report.get_by_id("UPC502").add_supporting_data('text_line', [self.kb, line])
				
			if re.search("^\S+\s*ALL\s*=\s*\(\s*ALL\s*\)\s*ALL", line):
				self.report.get_by_id("UPC505").add_supporting_data('text_line', [self.kb, line])
				
			if re.search("=.*\bchown\b", line):
				self.report.get_by_id("UPC506").add_supporting_data('text_line', [self.kb, line])

