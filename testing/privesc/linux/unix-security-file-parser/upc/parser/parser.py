import re
from upc.fsobj import fsobj

class parser:
    def __init__(self):
        pass
    
    def order_files(self):
        pass
    
    def auto_parse(self):
        pass
    
    # opts can contain:
    #   remove_comments: "^#"
    # 
    # returns multiline string
    def slurpfile(self, filename, opts):
        print "[D] opening: %s" % filename
        f = open(filename, 'r')
        lines = f.readlines()
        
        if "remove_comments" in opts.keys():
            newlines = []
            for line in lines:
                if not re.search(opts["remove_comments"], line):
                    newlines.append(line)
                lines = newlines
                
        if "remove_blanklines" in opts.keys() and opts["remove_blanklines"]:
            newlines = []
            for line in lines:
                if not re.search("^\s*$", line):
                    newlines.append(line)
            lines = newlines

        if "trim" in opts.keys() and opts["trim"]:
            newlines = []
            for line in lines:
                newlines.append(line.strip())
            lines = newlines

        if "key_values" in opts.keys() and opts["key_values"]:
            newlines = []
            for line in lines:
                m = re.search("^\s*(\S+?)[\s=]+(.*?)\s*$", line)
                if m:
                    newlines.append([m.group(1), m.group(2)])
            lines = newlines
                         
        return lines
    
    def query_perms(self, filename, opts):
        print "[D] opening: %s" % filename
        f = open(filename, 'r')
        
        # TODO move this somewhere
        regexp = {}
        regexp['world_writeable'] = '\s.[r-][w-][xsS-][r-][w-][xsS-][r-]w[xtT-]\s'
        regexp['world_readable']  = '\s.[r-][w-][xsS-][r-][w-][xsS-]r[w-][xtT-]\s'
        regexp['file']            = '\s-[r-][w-][xsS-][r-][w-][xsS-][r-][w-][xtT-]\s'
        regexp['directory']       = '\sd[r-][w-][xsS-][r-][w-][xsS-][r-][w-][xtT-]\s'
        regexp['sticky']          = '\s.[r-][w-][xsS-][r-][w-][xsS-][r-][w-][tT]\s'
        regexp['suid']            = '\s.[r-][w-][sS][r-][w-][xsS-][r-][w-][xtT-]\s'
        regexp['sgid']            = '\s.[r-][w-][xsS-][r-][w-][sS][r-][w-][xtT-]\s'
        regexp['unknown_owner']   = '\s.[r-][w-][xsS-][r-][w-][xsS-][r-][w-][xtT-]\s+\d+\s+\d+'
        regexp['unknown_group']   = '\s.[r-][w-][xsS-][r-][w-][xsS-][r-][w-][xtT-]\s+\d+\s+\S+\s+\d+'
        regexp['proc']            = '\s/proc/'
                
        eregexp = {}
        eregexp['min_size'] = '\d+\s+\d+\s+..........\s+\d+\s+\S+\s+\S+\s+(\d+)\s+?\S+\s+\S+\s+\S+\s+/'

        allowed_opts = ["matches", "notmatches", "ignore", "min_size", "custom_re"]        
        # This odd-looking construction is apparently quite fast
        # http://effbot.org/zone/readline-performance.htm
        while 1:
            lines = f.readlines(100000)
            if not lines:
                break
            for line in lines:
                # We need this regexp to avoid creating objects unnecessarily
                matched = 1
                
                # TODO check that one "matches" was passed at least
                # TODO check that matches are valid
                for opt in opts.keys():
                    if matched and opt in allowed_opts:
                        if matched and opt == "notmatches":
                            for s in opts['notmatches']:
                                m = re.search(regexp[s], line)
                                if m:
                                    matched = 0
                                    break
                        
                        if matched and opt == "matches":
                            for s in opts['matches']:
                                m = re.search(regexp[s], line)
                                if not m:
                                    matched = 0
                                    break
                        
                        if matched and opt == "ignore":
                            for s in opts['ignore']:
                                m = re.search(regexp[s], line)
                                if m:
                                    matched = 0
                                    break

                        if matched and opt == "min_size":
                            m = re.search(eregexp[opt], line)
                            if m:
                                size = m.group(1)
                                if int(size) < int(opts["min_size"]):
                                    matched = 0
                                    break

                        if matched and opt == "custom_re":
                            #print "[D] Custom"
                            m = re.search(opts[opt], line)
                            if not m:
                                matched = 0
                                break

                # Need further checking for unkown_owner and unknown_group
                if matched:
                    fso = fsobj();
                    r = fso.parse_from_find_line(line)
                    
                    if r:
                        if "unknown_owner" in opts['matches']:
                            if self.kb.find_uid_from_name(fso.get_attr("owner")):
                                matched = 0
                                break
                            
                        if "unknown_group" in opts['matches']:
                            if self.kb.find_gid_from_name(r.fso.get_attr("group")):
                                matched = 0
                                break
                        
                        yield fso
    
    def add_issue(self, title):
        print "[D] Added issue %s" % title
        pass
    