from upc.parser.parser import parser

class sysctl(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		# It's not correct to treat sysctl_config as a list of key-value pairs.  
		# It's close enough for a basic audit, though.
		key_values = self.slurpfile(filename, {"remove_comments": "^#", "key_values": 1, "remove_blanklines": 1})
		
		
		for kv in key_values:
			k = kv[0]
			v = kv[1]
			
			if k == "kernel.sysrq" and v == "1":
				self.report.get_by_id("UPC559").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])

			if k == "kernel.modules_disabled" and v == "0":
				self.report.get_by_id("UPC560").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
		
			if k == "vm.mmap_min_addr" and v == "0":
				self.report.get_by_id("UPC561").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])

			if k == "kernel.kptr_restrict" and v == "0":
				self.report.get_by_id("UPC562").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])

			if (k == "net.ipv4.ip_forward" and v == "1") or (k == "net.ipv4.conf.all.forwarding" and v == 1):
				self.report.get_by_id("UPC563").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])

			if (k == "net.ipv6.ip_forward" and v == "1") or (k == "net.ipv6.conf.all.forwarding" and v == 1):
				self.report.get_by_id("UPC564").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
				
			if (k == "net.ipv4.conf.all.accept_redirects" == "1"):
				self.report.get_by_id("UPC565").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
				
			if (k == "net.ipv4.icmp_echo_ignore_broadcasts" == "0"):
				self.report.get_by_id("UPC566").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
				
			if (k == "net.ipv4.icmp_ignore_bogus_error_responses" == "0"):				
				self.report.get_by_id("UPC567").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
				
			if (k == "net.ipv4.tcp_syncookies" == "0"):
				self.report.get_by_id("UPC568").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
				
			if (k == "net.ipv4.conf.all.accept_source_route" == "1"):
				self.report.get_by_id("UPC569").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
				
			if (k == "net.ipv4.conf.all.rp_filter" == "0"):
				self.report.get_by_id("UPC570").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
				
			if (k == "net.ipv4.conf.all.secure_redirects" == "1"):
				self.report.get_by_id("UPC571").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
				
			if (k == "kernel.randomize_va_space" == "0"):
				self.report.get_by_id("UPC576").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
				
			if (k == "kernel.randomize_va_space" == "1"):
				self.report.get_by_id("UPC576").add_supporting_data('text_line', [self.kb, "%s = %s" % (k, v)])
				
