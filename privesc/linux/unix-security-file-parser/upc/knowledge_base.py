
class knowledge_base():
    def __init__(self):
        self.data = {}
        self.data["filenames"] = []
        self.data["interface"] = {}
        self.data["user"] = {}
        self.data["group"] = {}
    
    def register_file(self, file):
        self.data["filenames"].append(file)
        
    def add_to_ulist(self, name, value):
        if not name in self.data.keys():
            self.data[name] = []
        self.data[name].append(value)
        self.data[name] = list(set(self.data[name]))
        
    def get_ulist(self, name):
        return self.data[name]
    
    def find_uid_from_name(self, username):
        for u in self.data["user"].keys():
            if username == u:
                return self.data["user"]["uid"]
        return None
    
    def find_gid_from_name(self, groupname):
        return self.data["group"]["gid"]
    
    def find_name_from_uid(self, uid):
        for u in self.data["user"].keys():
            if self.data["user"][u]["uid"] == uid:
                return u
        return None
    
    def find_name_from_gid(self, gid):
        for g in self.data["group"].keys():
            if not g in self.data["group"]:	
                self.data["group"][g] = {}
            if not "gid" in self.data["group"][g]:	
                self.data["group"][g]["gid"] = 12345678
            if self.data["group"][g]["gid"] == gid:
                return g
        return None
    
    def add_user_to_gid(self, gid, user):
        groupname = self.find_name_from_gid(gid)
        self.add_user_to_group(groupname, user)
        
    def add_user_to_group(self, groupname, user):
	if not groupname in self.data["group"]:
		self.data["group"][groupname] = {}
		self.data["group"][groupname]["members"] = []
        m = self.data["group"][groupname]["members"]
        m.append(user)
        self.data["group"][groupname]["members"] = m
        
        
