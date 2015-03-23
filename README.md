# brutto
Easy brute forcing to whatever you want, Its magic increasing values and direct.


## Implementation 

-   Clone `git clone https://github.com/jofpin/brutto.git`
-   [Download the latest version](https://github.com/jofpin/brutto/archive/master.zip)
-   Install with Python: `python setup.py install`

```python
# So you import the library
from brutto_easy import Brutto
```

## How to use

-   Includes all the letters (A - Z ) in case sensitive.
-   All numbers are reflected in the process ( 0-9 )
-   Also all the symbols and space.

## Settings
-   scope
-   letters
-   numbers
-   symbols
-   space

## Base 
- increase
- direct

### Default settings test with (increase)
```python
# call brutto
test = Brutto()

# Here I implement
for example in test.increase(letters=True, numbers=True, symbols=False, space=False, scope=4):
    print example
```

### Default settings test with (direct)
```python
# call brutto
bruteforce = Brutto()

for example in bruteforce.direct(4):
    print example
```

So you add a custom value to increase letters. scope=(1-5)
```python
# call brutto
test = Brutto()

for example in test.increase(letters=True, scope=5):
    print example
```

With letters and numbers, and increased scope=(1-8 )
```python
# call brutto
test = Brutto()

for example in test.increase(scope=8, letters=True, numbers=True, symbols=False):
    print example
```

-------------

Copyright, 2015 by [Jose Pino](http://twitter.com/jofpin)

-------------
