import re

class fsobj():
    def __init__(self):
        self.attrs = {}
        self.line = None
        pass
        
    def parse_from_find_line(self, line):
        self.line = line;
        # 70012   16 -rw-r--r--   1 u       g           16109 Jan 10 14:19 /some/file
        # 1230    0 brw-r-----   1 root     disk              Aug 10 11:51 /dev/ram1
        # m = re.search("\s*\d+\s+\d+\s+..........\s+\d+\s+\S+\s+\S+\s+(?:\d+\s+)?\S+\s+\S+\s+\S+\s+/.*\s*", line)
 
        m = re.search("\s*(\d+)\s+(\d+)\s+(.)(.)(.)(.)(.)(.)(.)(.)(.)(.)\s+(\d+)\s+(\S+)\s+(\S+)\s+(?:(\d+)\s+)?(\S+\s+\S+\s+\S+)\s+(/.*)\s*", self.line)
        if (m):
            return 1
         
        else:
            print "WARNING: fsobj failed to parse: %s" %line
            
            return 0
            
    def get_attr(self, k):
        # The big regex + storeage is expensive.  Only do it if we have to.
        if not k in self.attrs.keys():
            m = re.search("\s*(\d+)\s+(\d+)\s+(.)(.)(.)(.)(.)(.)(.)(.)(.)(.)\s+(\d+)\s+(\S+)\s+(\S+)\s+(?:(\d+)\s+)?(\S+\s+\S+\s+\S+)\s+(/.*)\s*", self.line)
        
            if (m):
                #print "Matched: %s" % line
                self.attrs["inode"] = m.group(1)
                self.attrs["unknown1"] = m.group(2)
                self.attrs["type"] = m.group(3)
                self.attrs["user_read"] = m.group(4)
                self.attrs["user_write"] = m.group(5)
                self.attrs["user_exec"] = m.group(6)
                self.attrs["group_read"] = m.group(7)
                self.attrs["group_write"] = m.group(8)
                self.attrs["group_exec"] = m.group(9)
                self.attrs["world_read"] = m.group(10)
                self.attrs["world_write"] = m.group(11)
                self.attrs["world_exec"] = m.group(12)
                self.attrs["unknown2"] = m.group(13)
                self.attrs["owner"] = m.group(14)
                self.attrs["group"] = m.group(15)
                self.attrs["size"] = m.group(16)
                self.attrs["date"] = m.group(17)
                self.attrs["path"] = m.group(18)
                
        return self.attrs[k]
    
    def get_line(self):
        return self.line