from upc.parser.parser import parser
import re

class netstat(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		lines = self.slurpfile(filename, {"remove_blanklines": 1})
		
		
		list_ports_tcp = []
		list_ports_udp = []
		
		for line in lines:
			# Output of AIX netstat -na:
			# tcp4       0      0  *.23             *.*                 LISTEN
			# tcp6       0      0  ::1.23           *.*                 LISTEN
			# tcp        0      0  *.23             *.*                 LISTEN
			# udp4       0      0  *.*              *.* 
			# udp6       0      0  *.111            *.*
			# udp        0      0  *.111            *.*
			m = re.search("^\s*(tcp|tcp4|tcp6|udp|udp4|udp6)\s+(\d+)\s+(\d+)\s+(\S+)\.([^\s\.]+)\s+(\S+)\.([^\s\.]+)(?:\s+(\S+))?\s*$", line)
			if m:
				proto        = m.group(1)
				recvq        = m.group(2)
				sendq        = m.group(3)
				localip      = m.group(4)
				localport    = m.group(5)
				remoteip     = m.group(6)
				remoteport   = m.group(7)
				state        = m.group(8)
			
				if (state and state == "LISTEN") or (localport != "*" and proto[0] == "u"):
					
					if localip != "127.0.0.1" and localip != "::1":
						# Unnecessary services
						if localport in ["7", "9", "11", "13", "15", "17", "19", "37", "79"]:
							self.report.get_by_id("UPC577").add_supporting_data('text_line', [self.kb, line])
						
						# Insecure/plaintext protocols
						if localport in ["21", "23", "512", "513", "514"]:
							self.report.get_by_id("UPC578").add_supporting_data('text_line', [self.kb, line])
					
			# Output of Linux netstat -na:
			# tcp        0      0 0.0.0.0:10              0.0.0.0:*               LISTEN
			# tcp6       0      0 :::22                   :::*                    LISTEN
			# udp        0      0 0.0.0.0:68              0.0.0.0:*
			# udp6       0      0 :::123                  :::*
			m = re.search("^\s*(tcp|tcp6|udp|udp6)\s+(\d+)\s+(\d+)\s+(\S+):([^\s:]+)\s+(\S+):([^\s:]+)(?:\s+(\S+))?\s*$", line)
			if m:
				proto        = m.group(1)
				recvq        = m.group(2)
				sendq        = m.group(3)
				localip      = m.group(4)
				localport    = m.group(5)
				remoteip     = m.group(6)
				remoteport   = m.group(7)
				state        = m.group(8)
			
				if (state and state == "LISTEN") or (localport != "*" and proto[0] == "u"):
					
					if localip != "127.0.0.1" and localip != "::1":
						# Unnecessary services
						if localport in ["7", "9", "11", "13", "15", "17", "19", "37", "79"]:
							self.report.get_by_id("UPC577").add_supporting_data('text_line', [self.kb, line])
						
						# Insecure/plaintext protocols
						if localport in ["21", "23", "512", "513", "514"]:
							self.report.get_by_id("UPC578").add_supporting_data('text_line', [self.kb, line])
					
