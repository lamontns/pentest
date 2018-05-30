from upc.parser.parser import parser
import re

class ifconfig(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		lines = self.slurpfile(filename, {})
		
		current_interface = None
		
		for line in lines:
			m = re.search("^(\S+)\s+Link\s+encap:(\S+)", line)
			if m:
				current_interface = m.group(1)
				interface_type = m.group(2)
				kb.data["interface"][current_interface] = {}
				kb.data["interface"][current_interface]["interface_type"] = interface_type
			
			m = re.search("inet addr:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+.*Mask:(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
			if m:
				ip = m.group(1)
				netmask = m.group(2)
				kb.data["interface"][current_interface]["ipv4_address"] = ip
				kb.data["interface"][current_interface]["ipv4_netmask"] = netmask
				
			# IPv6 Enabled
			m = re.search("inet6\s+addr:\s*([\da-fA-F:]+)/(\d+)\s+Scope:(\S+)", line)
			if m:
				ip = m.group(1)
				netmask = m.group(2)
				scope = m.group(3)
				kb.data["interface"][current_interface]["ipv6_address"] = ip
				kb.data["interface"][current_interface]["ipv6_netmask"] = netmask
				kb.data["interface"][current_interface]["ipv6_scope"] = scope
				self.report.get_by_id("UPC522").add_supporting_data('text_line', [self.kb, "%s: %s" % (current_interface, line)])
				
