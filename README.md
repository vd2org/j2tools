# j2tools
Useful tools for jinja2

## Install

```bash
pip install j2tools
```

## Testing

_coming soon_

## YamlLoader

YamlLoader is a template loader for jinja2 template framework.
It loads templates from yaml-files. Useful when you need to
store many small templates in one file.

#### Example:

```yaml
# templates.yaml
home:
  welcome: |
    Welcome, {{username}}!
  goodbye: |
    Goodbye, {{username}}!
```

```python
# main.py
from jinja2 import Environment
from j2tools import YamlLoader

jinja = Environment(loader=YamlLoader('templates.yaml'))

username = 'John Doe'
template1 = jinja.get_template('home/welcome')
rendered1 = template1.render(username=username)
print(rendered1) # Welcome, John Doe!

template2 = jinja.get_template('home/goodbye')
rendered2 = template2.render(username=username)
print(rendered2) # Goodbye, John Doe!
``` 

## t_factory

t_facotory is a small tool which helps prefixed templates easily.

See examples below.

#### Example:

```yaml
# templates_en.yaml
home:
  welcome: |
    Welcome, {{username}}!
  goodbye: |
    Goodbye, {{username}}!
```

```yaml
# templates_ru.yaml
home:
  welcome: |
    Привет, {{username}}!
  goodbye: |
    Пока, {{username}}!
```

```python
# main.py
from jinja2 import Environment, PrefixLoader
from j2tools import YamlLoader
from j2tools import t_factory

loader = PrefixLoader({
                       'en': YamlLoader('templates_en.yaml'),
                       'ru': YamlLoader('templates_ru.yaml'),})
  
jinja = Environment(loader=loader)
get_t = t_factory(jinja)

def print_templates(t, username):
    rendered1 = t('home/welcome', username=username)
    print(rendered1) 
    
    rendered2 = t('home/goodbye', username=username)
    print(rendered2) 
    
print_templates(get_t('en'), 'John Doe')
# Expected output:
# Welcome, John Doe!
# Goodbye, John Doe!

print_templates(get_t('ru'), 'Иван')
# Expected output:
# Привет, Иван!
# Пока, Иван!
``` 

## plural

`plural` is jinja2 filter function for easy text pluralization.

#### Example:

```yaml
# templates.yaml
info:
  users: |
    System have {{users}} active {{users|plural('en','user','users')}}.
```

```python
# main.py
from jinja2 import Environment
from j2tools import YamlLoader
from j2tools import plural

jinja = Environment(loader=YamlLoader('templates.yaml'))
jinja.filters['plural'] = plural

template1 = jinja.get_template('info/users')
rendered1 = template1.render(users=1)
print(rendered1) # System have 1 active user.
rendered2 = template1.render(users=23)
print(rendered2) # System have 23 active users.
``` 

## elapsed and remaining

Calculates and formats elapsed time to string like this:
`25d 4h 3m 35s`. Can be used as jinja2 filter.

#### Example:

```yaml
# templates.yaml
info:
  uptime: |
    System uptime: {{started|elapsed(show_seconds=True)}}.
  newyear: |
    To next year remaining {{newyear|remaining}}!
```

```python
# main.py
from jinja2 import Environment
from j2tools import YamlLoader
from j2tools import elapsed, remaining
import datetime

jinja = Environment(loader=YamlLoader('templates.yaml'))
jinja.filters['elapsed'] = elapsed
jinja.filters['remaining'] = remaining

started = datetime.datetime.now()
newyear = datetime.datetime(2020, 1, 1, 0, 0, 0)

username = 'John Doe'
template1 = jinja.get_template('info/uptime')
rendered1 = template1.render(started=started)
print(rendered1) # System uptime: 25d 4h 3m 35s.

template2 = jinja.get_template('info/newyear')
rendered2 = template2.render(newyear=newyear)
print(rendered2) # To next year remaining 295d 10h 13m 10s!
``` 

## uchar

Simple jinja2 function to insert unicode characters
by unicode names. Very useful for inserting emoji.

#### Example:

```yaml
# templates.yaml
home:
  welcome: |
    Welcome, {{username}} {{UN('THUMBS UP SIGN')}}!
```

```python
# main.py
from jinja2 import Environment
from j2tools import YamlLoader
from j2tools import uchar

jinja = Environment(loader=YamlLoader('templates.yaml'))
jinja.globals['UN'] = uchar

template1 = jinja.get_template('info/users')
rendered1 = template1.render(username='John Doe')
print(rendered1) # Welcome, John Doe 👍!
``` 

