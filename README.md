# WeDontMake

![Django CI](https://github.com/sergeibershadsky/wedontmake/workflows/Django%20CI/badge.svg)
### Installation

Copy .env file and add github and django variables:
```bash
cp .env.example .env
```

generate django secret key and copy it to *SECRET_KEY* environment variable:
```python
from django.core.management.utils import get_random_secret_key
get_random_secret_key()
```

Got to GitHub Dev Settings https://github.com/settings/developers and create a new app there to obtain ClientId and 
secret for github environment settings

### Running

```bash
docker-compose build
docker-compose up
```

