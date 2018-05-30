from upc.parser.parser import parser
import re

class mount(parser):
	def __init__(self):
		self.issues = []
		
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
		
		lines = self.slurpfile(filename, {"remove_blanklines": 1})
		
		mount_points = []
		
		for line in lines:
			# Output of linux mount command
			m = re.search("^(\S+)\s+on\s+(/\S+)\s+type\s+(\S+)\s+\((\S*)\)", line)
			if m:
				device      = m.group(1)
				mount_point = m.group(2)
				fs_type     = m.group(3)
				options     = m.group(4)
				
				if fs_type == "proc":
					continue
				
				option_used = {"nosuid": 0, "noexec": 0, "nodev": 0, "rw": 0, "ro": 0}
				mount_points.append(mount_point)
				
	#			print "[D] dev=%s, mount_point=%s, fs=%s, opts=%s" % (device, mount_point, fs_type, options)
				
				for option in options.split(","):
					#print "[D] option: %s" % option
					option_used[option] = 1
					
				if not option_used["nosuid"]:
					self.report.get_by_id("UPC537").add_supporting_data('text_line', [self.kb, line])

				if not option_used["noexec"]:
					self.report.get_by_id("UPC538").add_supporting_data('text_line', [self.kb, line])
					
				if not option_used["nodev"]:
					self.report.get_by_id("UPC539").add_supporting_data('text_line', [self.kb, line])
					
				if not option_used["ro"]:
					self.report.get_by_id("UPC540").add_supporting_data('text_line', [self.kb, line])
					
				if fs_type == "vmhgfs":
					self.report.get_by_id("UPC541").add_supporting_data('text_line', [self.kb, line])
					
			if not "/tmp" in mount_points:
				self.report.get_by_id("UPC542").add_supporting_data('text_line', [self.kb, line])
				
# TODO 
# check logs are on separate fs
# check for fat/vfat
# check users can't hardlink to suid progs
# check for nfs file systems