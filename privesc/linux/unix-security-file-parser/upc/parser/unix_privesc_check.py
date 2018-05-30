from upc.parser.parser import parser
import re

class unix_privesc_check(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		lines = self.slurpfile(filename, {"remove_comments": "^#", "remove_blanklines": 1, "trim": 1})
		
		for line in lines:
			m = re.search("\[(UPC\d\d\d)\] WARNING: .*", line)
			if m:
				issueno = m.group(1)
				self.report.get_by_id(issueno).add_supporting_data('text_line', [self.kb, line])


