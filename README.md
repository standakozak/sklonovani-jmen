# sklonovani-jmen
Module for using the API of www.sklonovani-jmen.cz in Python. This API is used for inflecting names in Czech grammar.
To get your API key for using this module, sign up at https://www.sklonovani-jmen.cz/registrace.

## Getting started
To install this module, run
`pip install sklonovani_jmen` in the command line.
## API request
```
from sklonovani_jmen.main import Client 
client = Client(YOUR_KEY) 
client.request("Adelaida")
```
You can find information about other arguments for this method at https://www.sklonovani-jmen.cz/dokumentace or with `help(Client.request)`. \
(Note that hyphens in argument names are replaced with underscores.)
## Account information
```
client.account_info(2)  # Returns information about your remaining credit
```
### PyPI page
https://pypi.org/project/sklonovani-jmen/
