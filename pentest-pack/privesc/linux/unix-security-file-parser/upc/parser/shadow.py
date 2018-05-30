from upc.parser.parser import parser
import re

class shadow(parser):
	def __init__(self):
		self.issues = []
	
	def detect_format(self, filename):
		is_linux = 1
		is_aix = 1
		
		lines = self.slurpfile(filename, {"remove_blanklines": 1, "trim": 1})
		for line in lines:
			fields = line.split(":")
			if not len(fields) == 9:
				is_linux = 0
				break
		
		if is_linux:
			return "linux"
		
		# TODO
		#f = open(filename, 'r')
		#s = f.read()
		#fields = s.split()
		#pass
	
	def parse(self, filename, report, kb):
		self.report = report
		self.kb = kb
		self.kb.register_file(filename)
	
		lines = self.slurpfile(filename, {"remove_blanklines": 1, "trim": 1})
		
		crypt_std_des_used = 0
		crypt_ext_des_used = 0
		md5_hash_used = 0
		blowfish2_used = 0
		blowfish2a_used = 0
		sha256_used = 0
		sha512_used = 0
				
		for line in lines:
			fields = line.split(":")
			
			if len(fields) <= 8:
				continue
			user             = fields[0]
			password         = fields[1]
			password_changed = fields[2]
			min_age          = fields[3]
			max_age          = fields[4]
			warn_days        = fields[5]
			grace_period     = fields[6]
			expiry_date      = fields[7]
			reserved         = fields[8]
			
			if not user in self.kb.data["user"].keys():
				self.kb.data["user"][user] = {}
			self.kb.data["user"][user]["shadow_password"] = password
			self.kb.data["user"][user]["password_changed"] = password_changed
			self.kb.data["user"][user]["min_age"] = min_age
			self.kb.data["user"][user]["max_age"] = max_age
			self.kb.data["user"][user]["warn_days"] = warn_days
			self.kb.data["user"][user]["grace_period"] = grace_period
			self.kb.data["user"][user]["expiry_date"] = expiry_date
			self.kb.data["user"][user]["reserved"] = reserved
			self.kb.data["user"][user]["is_in_shadow"] = 1
			
			# Blank password
			if fields[1] == "":
				self.report.get_by_id("UPC510").add_supporting_data('text_line', [self.kb, line])
				
			# Record which hash types are used
			elif re.search("^[\./0-9A-Za-z]{9}$", fields[1]):
				crypt_std_des_used = 1
				
			elif re.search("^_", fields[1]):
				crypt_ext_des_used = 1
				
			elif re.search("^\$1\$", fields[1]):
				md5_hash_used = 1
				
			elif re.search("^\$2\$", fields[1]):
				blowfish2_used = 1
				
			elif re.search("^\$2a\$", fields[1]):
				blowfish2a_used = 1
				
			elif re.search("^\$5\$", fields[1]):
				sha256_used = 1
				
			elif re.search("^\$6\$", fields[1]):
				sha512_used = 1
				
			elif fields[1] != "!" and fields[1] != "*":
				self.report.get_by_id("UPC511").add_supporting_data('text_line', [self.kb, line])
				
			m = re.search("^#", user)
			if m:
				self.report.get_by_id("UPC555").add_supporting_data('text_line', [self.kb, line])

				
		# Mixture of hashes used
		if crypt_std_des_used + crypt_ext_des_used + md5_hash_used + blowfish2_used + blowfish2a_used + sha256_used + sha512_used > 1:
			self.report.get_by_id("UPC512").add_supporting_data('none', [self.kb])

		for user in self.kb.data["user"].keys():
			if "is_in_passwd" in self.kb.data["user"][user] and self.kb.data["user"][user]["is_in_passwd"] == 1:
				if not "is_in_shadow" in self.kb.data["user"][user].keys():
					self.report.get_by_id("UPC553").add_supporting_data('text_line', [self.kb, user])
					
			if "is_in_shadow" in self.kb.data["user"][user] and self.kb.data["user"][user]["is_in_shadow"] == 1:
				if not "is_in_passwd" in self.kb.data["user"][user].keys():
					self.report.get_by_id("UPC552").add_supporting_data('text_line', [self.kb, user])

		
