<p align="center">
  <img alt="Image" src="https://i.imgur.com/XSacNPD.png?2"/>
</p>

# Conditions-PY

Conditions is a Python port of the famous .NET libary [Conditions](https://github.com/ghuntley/conditions) which helps developers write pre- and postcondition validations in a fluent manner. Writing these validations is easy and it improves the readability and maintainability of code.


## Roadmap

Currently this libary is in development with the following items pending:
- Update icon for libary.
- Finish porting of conditions for all Python datatypes.
- Add unit testing.
- Add integration testing.
- Publish to Python package index.


## Supported Platforms

* Python 3+


## Installation (Pending Publish)

Installation is done via PIP:

    pip install conditions-py


## Usage

```python
import conditions-py


def speak(message):
    Condition()\
        .requires(message, 'message')\
        .is_not_null_or_whitespace()
        
    # Do speaking...


def multiple(left, right):
    Condition()\
        .requires(left, 'left')\
        .is_not_null()
    
    Condition()\
        .requires(right, 'right')\
        .is_not_null()\
        .has_length(len(left))
    
    # Do multiplication
```
    
A particular validation is executed immediately when it's method is called, and therefore all checks are executed in the order in which they are written:

## With thanks to

* The icon "<a href="http://thenounproject.com/term/tornado/2706/" target="_blank">Tornado</a>" designed by <a href="http://thenounproject.com/adamwhitcroft/" target="_blank">Adam Whitcroft</a> from The Noun Project.
* <a href="https://github.com/ghuntley">Geoffrey Huntley (ghuntley)</a> who is the original author of "<a href="https://github.com/ghuntley/conditions">Conditions</a>" from which this project was based on.
