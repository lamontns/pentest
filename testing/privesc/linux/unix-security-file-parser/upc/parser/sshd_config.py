from upc.parser.parser import parser

class sshd_config(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		# It's not correct to treat sshd_config as a list of key-value pairs.  
		# It's close enough for a basic audit, though.
		key_values = self.slurpfile(filename, {"remove_comments": "^#", "key_values": 1, "remove_blanklines": 1})
		
		directives_used = {}
		
		for kv in key_values:
			k = kv[0]
			v = kv[1]
			
			# remember which directives have been used
			directives_used[k] = 1
			
			if k == "Port":
				for port in v.split(","):
					self.kb.add_to_ulist("ssh_ports", port)

			if k == "GatewayPorts" and v == "yes":
				self.report.get_by_id("UPC533").add_supporting_data('hostname', [self.kb])
			
			if k == "AllowAgentForwarding" and v == "yes":
				self.report.get_by_id("UPC534").add_supporting_data('hostname', [self.kb])

			if k == "ListenAddress" and v == "0.0.0.0":
				self.report.get_by_id("UPC527").add_supporting_data('hostname', [self.kb])
				
			if k == "PermitRootLogin" and v == "yes":
				self.report.get_by_id("UPC526").add_supporting_data('hostname', [self.kb])
				
			if k == "PermitTunnel" and v == "yes":				
				self.report.get_by_id("UPC528").add_supporting_data('hostname', [self.kb])
				
			if k == "Protocol" and v != "2":
				self.report.get_by_id("UPC529").add_supporting_data('hostname', [self.kb])
				
			if k == "StrictModes" and v == "no":
				self.report.get_by_id("UPC530").add_supporting_data('hostname', [self.kb])
				
			if k == "UsePrivilegeSeparation" and v == "no":
				self.report.get_by_id("UPC531").add_supporting_data('hostname', [self.kb])
				
			if k == "UsePAM" and v == "no":
				self.report.get_by_id("UPC573").add_supporting_data('hostname', [self.kb])
				
			if k == "PermitEmptyPasswords" and v == "yes":
				self.report.get_by_id("UPC574").add_supporting_data('hostname', [self.kb])
				
			if k == "PermitBlacklistedKeys" and v == "yes":
				self.report.get_by_id("UPC575").add_supporting_data('hostname', [self.kb])
				
			if k == "AcceptEnv":
				self.report.get_by_id("UPC532").add_supporting_data('text_line', [self.kb, "%s %s" % (k, v)])
						
			if k == "PermitUserEnvironment":
				self.report.get_by_id("UPC572").add_supporting_data('text_line', [self.kb, "%s %s" % (k, v)])
						
		if not "Port" in directives_used.keys():
			self.report.get_by_id("UPC501").add_supporting_data('hostname', [self.kb])
		else:
			ports = self.kb.get_ulist("ssh_ports")
			if "22" in ports:
				self.report.get_by_id("UPC501").add_supporting_data('hostname', [self.kb])
				self.add_issue("UPC501")
		
		if not "AllowUsers" in directives_used.keys() and not "AllowGroups" in directives_used.keys():
			self.report.get_by_id("UPC503").add_supporting_data('hostname', [self.kb])
			
		if not "Match" in directives_used.keys():
			self.report.get_by_id("UPC504").add_supporting_data('hostname', [self.kb])
			
		if not "ListenAddress" in directives_used.keys():
			self.report.get_by_id("UPC527").add_supporting_data('hostname', [self.kb])

		if not "PermitRootLogin" in directives_used.keys():
			self.report.get_by_id("UPC526").add_supporting_data('hostname', [self.kb])

		