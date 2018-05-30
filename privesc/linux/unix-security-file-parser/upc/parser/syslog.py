from upc.parser.parser import parser
import re

class syslog(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		key_values = self.slurpfile(filename, {"remove_comments": "^#", "key_values": 1, "remove_blanklines": 1})
		
		remote_server = 0
		for kv in key_values:
			k = kv[0]
			v = kv[1]

			m = re.search("@", k)
			if m:
				remote_server = 1		
			
			m = re.search("@", v)
			if m:
				remote_server = 1
						
		if not remote_server:
			self.report.get_by_id("UPC535").add_supporting_data('hostname', [self.kb])
