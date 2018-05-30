# Not a class, just a bunch of constants

version = None

# Used to store a data structure representing the issues we've found
# We use this to generate the report
issues = {}

issue_template = {
    # 
    # These issues correspond ot issues from unix-privesc-check.  UPC000-UPC499 reserved for this.
    #                  
    'UPC001': {
       'title': "UPC001: Files and Directories writeable by other users",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC002': {
       'title': "UPC002: Group-writeable Files or Directories",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC003': {
       'title': "UPC003: World-writeable Files or Directories (but sticky bit set)",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC004': {
       'title': "UPC004: World-writeable Files or Directories",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC005': {
       'title': "UPC005: Files readable by other users",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC006': {
       'title': "UPC006: Files readable by other groups",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC007': {
       'title': "UPC007: Files world-readable",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC008': {
       'title': "UPC008: /etc/passwd allows external authentcation",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC009': {
       'title': "UPC009: NIS is used for authentication on this system",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC010': {
       'title': "UPC010: LDAP is used for authentication on this system",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC011': {
       'title': "UPC011: NIS is used for authentication on this system",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC012': {
       'title': "UPC012: LDAP is used for authentication on this system",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC013': {
       'title': "UPC013: There seem to be some password hashes in /etc/passwd",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC014': {
       'title': "UPC014: The following accounts have no password:",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC015': {
       'title': "UPC015: User doesn't have a password",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC016': {
       'title': "UPC016: User doesn't have a password",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC017': {
       'title': "UPC017: Sudo is configured - Manually check nothing unsafe is allowed",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC018': {
       'title': "UPC018: Some users can use sudo without a password",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC019': {
       'title': "UPC019: Postgres trust configured in pg_hba.conf",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC020': {
       'title': "UPC020: Can connect to local postgres database as \\",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC021': {
       'title': "UPC021: Can connect to local postgres database as \\",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC022': {
       'title': "UPC022: This system is an NFS client.  Check for nosuid and nodev options.",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC023': {
       'title': "UPC023: SetUID shell script may be vulnerable to race attacks",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC024': {
       'title': "UPC024: Cleartext subversion passsword file",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC025': {
       'title': "UPC025: Encrypted private SSH key found",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC026': {
       'title': "UPC026: Unencrypted private SSH key found",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC027': {
       'title': "UPC027: Public SSH Key found",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC028': {
       'title': "UPC028: SSH agents running",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC029': {
       'title': "UPC029: SSH Agent has keys loaded",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC030': {
       'title': "UPC030: GPG agents running",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC031': {
       'title': "UPC031: No NX",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC032': {
       'title': "UPC032: No NX logging",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC033': {
       'title': "UPC033: Auditing not enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC034': {
       'title': "UPC034: No NX",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC035': {
       'title': "UPC035: NX set to logging only",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC036': {
       'title': "UPC036: No ASLR",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC037': {
       'title': "UPC037: Conservative ASLR",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC038': {
       'title': "UPC038: mmap allows map to 0",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC039': {
       'title': "UPC039: SELinux does not enforce",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC040': {
       'title': "UPC040: NX not enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC041': {
       'title': "UPC041: SSP not enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC042': {
       'title': "UPC042: SSP not enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                  
                  
    # 
    # Other issues start here
    #                  
    'UPC501': {
       'title': "Default SSH Port",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'writable_progs': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC502': {
       'title': "Some Users Do Not Require a Password To Use Sudo",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC503': {
       'title': "SSH Users Not Whitelisted",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC504': {
       'title': "SSH Match Rules Not Used",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'TODO': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC505': {
       'title': "Sudo Allow Some Users To Execute Any Command",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC506': {
       'title': "Sudo Allows The Use of Potentially Dangerous Commands",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'TODO': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC507': {
       'title': "User has blank password in /etc/passwd",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC508': {
       'title': "User has unshadowed password in /etc/passwd",
       'description': '''TODO.  Note that this can be a false-positive on AIX where * and ! safe values to have in /etc/passwd.''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC509': {
       'title': "User has shell defined in /etc/passwd",
       'description': '''TODO.  NB: On AIX and Linux a empty shell field means the default shell (/usr/bin/sh and /bin/sh respectively).''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC510': {
       'title': "User has blank password in /etc/shadow",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC511': {
       'title': "Account uses unknown hashing algorithm in /etc/shadow",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC512': {
       'title': "Multiple hashing algorithms used in /etc/shadow",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                  
    'UPC513': {
       'title': "World Writeable Directory (sticky bit not set)",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC514': {
       'title': "World Writeable Directory (sticky bit set)",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC515': {
       'title': "SUID Program",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC516': {
       'title': "SGID Program",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC517': {
       'title': "SGID Directory",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC518': {
       'title': "World Writeable File",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC519': {
       'title': "World Readable Big File",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                  
    'UPC520': {
       'title': "Scripting Language Installed",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC521': {
       'title': "Compiler Installed",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC522': {
       'title': "IPv6 Enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC523': {
       'title': "Filesystem Entries With Unknown Owner",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC524': {
       'title': "Filesystem Entries With Unknown Group",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC525': {
       'title': "IPv6 Enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC533': {
       'title': "SSH Allows GatewayPorts",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
            
    'UPC534': {
       'title': "SSH Allows AllowAgentForwarding",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },              
    'UPC526': {
       'title': "SSH Allows PermitRootLogin",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                
    'UPC528': {
       'title': "SSH Allows PermitTunnel",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                
    'UPC529': {
       'title': "SSH Allows Protocol Version 1",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                
    'UPC530': {
       'title': "SSH Does Not Mandate StrictModes",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                
    'UPC531': {
       'title': "SSH Does Not Use UsePrivilegeSeparation",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                
    'UPC532': {
       'title': "SSH Allows AcceptEnv",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
                                    
    'UPC527': {
       'title': "SSH Service Binds To All Interfaces (ListenAddress)",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },

    'UPC526': {
       'title': "SSH Allows Root Logins (PermitRootLogin)",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC535': {
       'title': "Syslog Does Not Log To Remote Server",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC536': {
       'title': "SELinux Not Enforcing",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC537': {
       'title': "File system mounted without nosuid option",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC538': {
       'title': "File system mounted without noexec option",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC539': {
       'title': "File system mounted without nodev option",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC540': {
       'title': "File system mounted without ro option",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC541': {
       'title': "Mounted Filesystem Does Not Support File Permissions",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC542': {
       'title': "/tmp Not On Separate File System",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC550': {
       'title': "SNMP Daemon Invokes External Commands Via 'pass'",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC549': {
       'title': "SNMP Daemon Invokes External Commands Via 'exec'",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC548': {
       'title': "SNMP Daemon Allows Write Access",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC547': {
       'title': "SNMP Daemon Allows Access To Large View",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC546': {
       'title': "",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC545': {
       'title': "SNMP Daemon Allows Insecure Protocol Version",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC544': {
       'title': "SNMP Daemon Uses Default Community String",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC543': {
       'title': "SNMP Daemon Does Not Restrict Source IP Address",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC551': {
       'title': "Anaconda Configuration File Found",
       'description': '''File may contain root password hash.''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC552': {
       'title': "/etc/shadow Contains Entries That Are Missing From /etc/passwd",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC553': {
       'title': "/etc/passwd Contains Entries That Are Missing From /etc/shadow",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC554': {
       'title': "Attempt To Use Comments in /etc/passwd",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC555': {
       'title': "Attempt To Use Comments in /etc/shadow",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC556': {
       'title': "Network Sniffing Tools Installed",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC557': {
       'title': "File Found That May Contain Cleartext Passwords Or Keys",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC558': {
       'title': "Files Found That May Contain ACLs For Access From Network",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC559': {
       'title': "SysRq Key Enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC560': {
       'title': "Kernel Module Loading Is Enabled",
       'description': '''TODO''',
       'recommendation': '''Set to 0 at boot time to prevent loading of malicious modules or unloading of required modules.''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC561': {
       'title': "Processes Allowed to Map to Virtual Address 0",
       'description': '''TODO''',
       'recommendation': '''4096 or other non-zero value.  http://wiki.debian.org/mmap_min_addr''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC562': {
       'title': "Kernel Memory Addresses Are Not Hidden",
       'description': '''Knowledge of kernel addresses may help to exploit certain classes of vulnerability.''',
       'recommendation': '''Set to 1''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC563': {
       'title': "IP Forwarding Enabled (IPv4)",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC564': {
       'title': "IP Forwarding Enabled (IPv6)",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },

    'UPC565': {
       'title': "Host Accepts Redirects",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC566': {
       'title': "Host Does Not Ignore ICMP Broadcasts",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC567': {
       'title': "Host Does Not Ignore Bogus Error Messages",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC568': {
       'title': "TCP SYN Cookies Not Used To Mitigate DoS Attacks",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC569': {
       'title': "Host Accepts Source Routed Packets",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC570': {
       'title': "Reverse Path Filtering Not Used to Drop Spoofed Packets",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC571': {
       'title': "Host Accepts 'Secure' Redirects",
       'description': '''Host will accept ICMP redirects from its default gateway - which can be spoofed''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC572': {
       'title': "SSH Daemon has PermitUserEnvironment option Enabled",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC573': {
       'title': "SSH Daemon not configured to use PAM",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC574': {
       'title': "SSH Daemon Allows Use of Empty Passwords",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC575': {
       'title': "SSH Daemon Allows Blacklisted SSH Keys To Be Used",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC575': {
       'title': "Virtual Address Space Randomisation Disabled",
       'description': '''TODO''',
       'recommendation': '''Set to 2''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC576': {
       'title': "Virtual Address Space Randomisation Set Conservatively",
       'description': '''TODO''',
       'recommendation': '''Set to 2''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC577': {
       'title': "Unnecessary Network Services Listening on Network Interface",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC578': {
       'title': "Insecure Network Services Listening on Network Interface",
       'description': '''TODO''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },
    'UPC579': {
       'title': "No Idle Timeout Set On Shell",
       'description': '''The shell used for the audit did not have the TMOUT environment variable set''',
       'recommendation': '''TODO''',
       'supporting_data': {
          'text_line': {
             'section': "description",
             'preamble': "TODO:",
          },
       }
    },

}


