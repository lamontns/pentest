from upc.parser.parser import parser

class selinux(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		key_values = self.slurpfile(filename, {"remove_comments": "^#", "key_values": 1, "remove_blanklines": 1})
		
		for kv in key_values:
			k = kv[0]
			v = kv[1]

			print "[D] selinux: %s=%s" % (k,v)
			if k == "SELINUX" and v != "enforcing":
				self.report.get_by_id("UPC536").add_supporting_data('text_line', [self.kb, "%s=%s" % (k, v)])
				
