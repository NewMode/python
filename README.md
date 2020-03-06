# newmode-python

[![Build Status](https://secure.travis-ci.org/twilio/twilio-python.png?branch=master)](https://travis-ci.org/twilio/twilio-python)

## Introduction

This project contains the Python API wrapper for New/Mode API.

## Versions

`newmode-python` uses [Semantic Versioning](https://semver.org) for all changes.


### Supported Python Versions

This library has been tested in Python version >= 3.7. Other Python 3.x could be supported.

## Installation

Install from PyPi using [pip](http://www.pip-installer.org/en/latest/), a
package manager for Python.

    pip install newmode

Don't have pip installed? Try installing it, by running this from the command
line:

    $ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

Or, you can [download the source code
(ZIP)](https://github.com/twilio/twilio-python/zipball/master "twilio-python
source code") for `twilio-python`, and then run:

    python setup.py install

You may need to run the above commands with `sudo`.

## Getting Started

Getting started with the New/Mode API couldn't be easier. Create a
`Client` and you're ready to go.

### API Credentials

The `Client` needs your New/Mode credentials. You can either pass these
directly to the constructor (see the code below) or via environment variables.

```python
from Newmode.rest import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
```

Alternately, a `Client` constructor without these parameters will
look for `NEWMODE_API_USER` and `NEWMODE_API_PASSWORD` variables inside the
current environment. API version has a default value of v1.0 so
it's not required to pass this parameter.

We suggest storing your credentials as environment variables. Why? You'll never
have to worry about committing your credentials and accidentally posting them
somewhere public.


```python
from Newmode import Client
client = Client()
```

### Example usage

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)

response = client.getTools()
print(response)
```

### API Functions

#### getTools

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)

response = client.getTools()
print(response)
```

#### getTool

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
tool_id = "XX"

response = client.getTool(tool_id)
print(response)
```

#### lookupTargets

The search parameter could be:

##### Empty

For custom target tools, this will return all targets.

##### Postal Code

For postal code tools, this will return targets matching the postal code.

##### Address

For address tools, this will return targets matching the address.
Format could be:

1) lat::long
2) thoroughfare::locality::administrative_area::country

##### Custom

For csv tools, where search is a valid search term this will return matching targets.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
tool_id = "XX"
search = "XXX"

response = client.lookupTargets(tool_id, search)
print(response)
```


### Getting help

If you need help installing or using the library, please check the [Twilio Support Help Center](https://support.twilio.com) first, and [file a support ticket](https://twilio.com/help/contact) if you don't find an answer to your question.

If you've instead found a bug in the library or would like new features added, go ahead and open issues or pull requests against this repo!

[apidocs]: https://www.twilio.com/docs/api
[twiml]: https://www.twilio.com/docs/api/twiml
[libdocs]: https://twilio.github.io/twilio-python
