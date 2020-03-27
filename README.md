# newmode-python

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
from Newmode import Client

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

Return all existing tools.

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

Return specific tool.

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

Lookup for targets for a given tool.

The search parameter could be:

##### Empty

For custom target tools, this will return all targets.

##### Postal Code

For postal code tools, this will return targets matching the postal code.

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

#### getAction

Return action information for given tool.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
tool_id = "XX"

response = client.getAction(tool_id)
print(response)
```

#### runAction

Run action for given tool.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
tool_id = "XX"

payload = {
	"first_name": "Mark",
	"last_name": "Styles",
	"email_address": "lambic@pm.me",
	"postal_code": "H4E 2Y7",
	"email_subject": "This is my subject",
	"your_letter": "This is my letter"
}

response = client.runAction(tool_id, payload)
print(response)
```

#### getTarget

Get specific target.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
target_id = "XXXXXX"

response = client.getTarget(target_id)
print(response)
```

#### getCampaigns

Get existing campaigns.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)

response = client.getCampaigns()
print(response)
```

#### getCampaign

Get specific campaign.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
campaign_id = "XX"

response = client.getCampaign(campaign_id)
print(response)
```


#### getOrganizations

Get existing organizations.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)

response = client.getOrganizations()
print(response)
```

#### getOrganization

Get specific organization.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
organization_id = "XX"

response = client.getOrganization(organization_id)
print(response)
```

#### getServices

Get existing services.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)

response = client.getServices()
print(response)
```

#### getService

Get specific service.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
service_id = "XX"

response = client.getService(service_id)
print(response)
```

#### getOutreaches

Get existing outreaches for given tool.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
tool_id = "XX"

response = client.getOutreaches(tool_id)
print(response)
```

#### getOutreach

Get specific outreach.

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)
outreach_id = "XX"

response = client.getOutreach(outreach_id)
print(response)
```

### Paging

In order to get results paginated, you need to send params like this:

```python
from Newmode import Client

api_user = "XXXXXXXXXXXXXXXXX"
api_password = "YYYYYYYYYYYYYYYYYY"
api_version = "v1.0"
client = Client(api_user, api_password, api_version)

params = {
	'page[size]': 5,
	'page[number]': 2
}

response = client.getServices(params = params)
print(response)
```

### Publishing new versions

In order to publish new versions to Pypi.org, you need to run:

```
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
```

### Getting help

If you need help installing or using the library, please [contact us](https://www.newmode.net/contact).
