from upc.parser.parser import parser
import re

class group(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		lines = self.slurpfile(filename, {"remove_blanklines": 1, "trim": 1})
		
		for line in lines:
			fields = line.split(":")
			group    = fields[0]
			password = fields[1]
			gid      = fields[2]
			members  = fields[3]
			
			self.kb.data["group"][group] = {}
			self.kb.data["group"][group]["group_password"] = password
			self.kb.data["group"][group]["gid"] = gid
			self.kb.data["group"][group]["members"] = []

			for user in members.split(","):
				self.kb.add_user_to_group(group, user)
