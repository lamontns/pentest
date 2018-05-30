from upc.parser.parser import parser
import re

class snmpd(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		lines = self.slurpfile(filename, {"remove_comments": "^#", "remove_blanklines": 1})
		
		for line in lines:
			m = re.search("^com2sec\s+(\S+)\s+(\S+)\s+(\S+)", line)
			if m:
				sec_name  = m.group(1)
				source    = m.group(2)
				community = m.group(3)
				
				if source == "default":
					self.report.get_by_id("UPC543").add_supporting_data('text_line', [self.kb, line])
					
				if community == "public" or community == "private":
					self.report.get_by_id("UPC544").add_supporting_data('text_line', [self.kb, line])
					
			m = re.search("^group\s+(\S+)\s+(\S+)\s+(\S+)", line)
			if m:
				group_name     = m.group(1)
				security_model = m.group(2)
				secuirty_name  = m.group(3)
				
				if security_model == "v1":
					self.report.get_by_id("UPC545").add_supporting_data('text_line', [self.kb, line])
							
			m = re.search("^view\s+(\S+)\s+included\s+(\S+)", line)
			if m:
				view_name = m.group(1)
				subtree   = m.group(2)
					
				# 1.3.6.1.2.1 - SNMP MIB-2
				# 1.3.6.1.2 - IETF Management
				# 1.3.6.1 - OID assignments from 1.3.6.1 - Internet
				# 1.3.6 - US Department of Defense
				# 1.3 - ISO Identified Organization
				# 1 - ISO assigned OIDs	
				if subtree == ".1.3.6.1.2.1" or subtree == ".1.3.6.1.2" or subtree == ".1.3.6.1" or subtree == ".1.3.6" or subtree == ".1.3" or subtree == ".1":
					self.report.get_by_id("UPC547").add_supporting_data('text_line', [self.kb, line])
					
			m = re.search("^access\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)", line)
			if m:
				group_name     = m.group(1)
				context        = m.group(2)
				security_model = m.group(3)
				security_level = m.group(4)
				prefix         = m.group(5)
				read           = m.group(6)
				write          = m.group(7)
				notify         = m.group(8)
				
				if write != "none":
					self.report.get_by_id("UPC548").add_supporting_data('text_line', [self.kb, line])
							
			m = re.search("^exec\s+(.*?)", line)
			if m:
				command = m.group(1)
				
				# snmp executes something.  Check it's safe.
				self.report.get_by_id("UPC549").add_supporting_data('text_line', [self.kb, line])
							
			m = re.search("^pass\s+(\S+)\s+(.*?)", line)
			if m:
				mib     = m.group(1)
				command = m.group(2)
				
				# snmp executes something.  Check it's safe.
				self.report.get_by_id("UPC550").add_supporting_data('text_line', [self.kb, line])
						