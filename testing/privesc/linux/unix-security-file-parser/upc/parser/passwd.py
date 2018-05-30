from upc.parser.parser import parser
import re

class passwd(parser):
        def __init__(self):
                self.issues = []
                
        def parse(self, filename, report, kb):
                import magic
                m=magic.Magic()
                n = str(m.from_file(filename))
                if n.count("text") > 0:
                    self.report = report
                    self.kb = kb
                    self.kb.register_file(filename)
                    
                    lines = self.slurpfile(filename, {"remove_blanklines": 1, "trim": 1})
                    
                    for line in lines:
                            fields = line.split(":")
                            user     = fields[0]
                            password = fields[1]
                            uid      = fields[2]
                            gid      = fields[3]
                            gecos    = fields[4]
                            homedir  = fields[5]
                            shell    = fields[6]
                            
                            self.kb.data["user"][user] = {}
                            self.kb.data["user"][user]["passwd_password"] = password
                            self.kb.data["user"][user]["uid"] = uid
                            self.kb.data["user"][user]["gid"] = gid
                            self.kb.data["user"][user]["gecos"] = gecos
                            self.kb.data["user"][user]["homedir"] = homedir
                            self.kb.data["user"][user]["shell"] = shell
                            self.kb.data["user"][user]["is_in_passwd"] = 1
                            
                            self.kb.add_user_to_gid(gid, user)
                                            
                            # Blank password
                            if fields[1] == "":
                                    self.report.get_by_id("UPC507").add_supporting_data('text_line', [self.kb, line])
                                    
                            # Password not shadowed
                            if fields[1] != "x":
                                    self.report.get_by_id("UPC508").add_supporting_data('text_line', [self.kb, line])
                                    
                            # User has shell
                            if fields[6] != "/bin/false" and fields[6] != "/sbin/nologin":
                                    self.report.get_by_id("UPC509").add_supporting_data('text_line', [self.kb, line])
                            
                            m = re.search("^#", user)
                            if m:
                                    self.report.get_by_id("UPC554").add_supporting_data('text_line', [self.kb, line])
                                    
