from upc.parser.parser import parser

class permissions(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		#fsobjs = self.query_perms(filename, {"matches": ["world_writeable"]})
		
		for f in self.query_perms(filename, {"min_size": 20000000, "matches": ["file", "world_readable"], "notmatches": ["proc"]}):
			self.report.get_by_id("UPC519").add_supporting_data('text_line', [self.kb, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["world_writeable", "directory"], "ignore": ["sticky"], "notmatches": ["proc"]}):
			self.report.get_by_id("UPC513").add_supporting_data('text_line', [self.kb, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["unknown_owner"]}):
			self.report.get_by_id("UPC523").add_supporting_data('text_line', [self.kb, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["unknown_owner"]}):
			self.report.get_by_id("UPC524").add_supporting_data('text_line', [self.kb, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["world_writeable", "file"], "notmatches": ["proc"]}):
			c = self.report.get_by_id("UPC518").count_supporting_data('text_line')
			if c < 200000:
				self.report.get_by_id("UPC518").add_supporting_data('text_line', [self.kb, f.get_line()])
			elif c == 200000:
				self.report.get_by_id("UPC518").add_supporting_data('text_line', [self.kb, "... Only first 200000 listed ..."])

		for f in self.query_perms(filename, {"matches": ["world_writeable", "directory", "sticky"]}):
			self.report.get_by_id("UPC514").add_supporting_data('text_line', [self.kb, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["suid", "file"], "notmatches": ["proc"]}):
			self.report.get_by_id("UPC515").add_supporting_data('text_line', [self.kb, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["sgid", "file"], "notmatches": ["proc"]}):
			self.report.get_by_id("UPC516").add_supporting_data('text_line', [self.kb, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["sgid", "directory"]}):
			self.report.get_by_id("UPC517").add_supporting_data('text_line', [self.kb, f.get_line()])

		for prog in ("perl", "python", "java", "tcl", "ruby"):
			for f in self.query_perms(filename, {"matches": ["file"], "custom_re": ("/%s$" % prog)}):
				self.report.get_by_id("UPC520").add_supporting_data('text_line', [self.kb, f.get_line()])

		for prog in (".rhosts", ".shosts"):
			for f in self.query_perms(filename, {"matches": ["file"], "custom_re": ("/%s$" % prog)}):
				self.report.get_by_id("UPC558").add_supporting_data('text_line', [self.kb, f.get_line()])

		for prog in (".netrc", "id_dsa", "id_rsa"):
			for f in self.query_perms(filename, {"matches": ["file"], "custom_re": ("/%s$" % prog)}):
				self.report.get_by_id("UPC557").add_supporting_data('text_line', [self.kb, f.get_line()])

		for prog in ("g\+\+", "g\+\+\d\d", "g\+\+-\d\.\d", "x86_64-redhat-linux-g\+\+\d\d", "gcc", "javac"):
			for f in self.query_perms(filename, {"matches": ["file"], "custom_re": ("/%s$" % prog)}):
				self.report.get_by_id("UPC521").add_supporting_data('text_line', [self.kb, f.get_line()])

		for f in self.query_perms(filename, {"matches": ["file"], "custom_re": ("/anaconda-ks.cfg$")}):
			self.report.get_by_id("UPC551").add_supporting_data('text_line', [self.kb, f.get_line()])

		for prog in ("tcpdump", "wireshark", "nettl", "snoop", "iptrace"):
			for f in self.query_perms(filename, {"matches": ["file"], "custom_re": ("/%s$" % prog)}):
				self.report.get_by_id("UPC556").add_supporting_data('text_line', [self.kb, f.get_line()])

		# TODO files that probably contains passwords or other useful info

		# world writeable files
		# world writeable directories
		# readable big file
		# writeable home directories