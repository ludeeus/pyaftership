# pyaftership

[![codecov](https://codecov.io/gh/ludeeus/pyaftership/branch/main/graph/badge.svg)](https://codecov.io/gh/ludeeus/pyaftership)
![python version](https://img.shields.io/badge/Python-3.7=><=3.9-blue.svg)
[![PyPI](https://img.shields.io/pypi/v/pyaftership)](https://pypi.org/project/pyaftership)
![Actions](https://github.com/ludeeus/pyaftership/workflows/Actions/badge.svg?branch=main)

_Async Python wrapper for the AfterShip API_

## Installation

```bash
python3 -m pip install pyaftership
```

## Example usage

Here is an example of what you can do, more examples can be found in the `tests` directory.

```python
import asyncio
import aiohttp
from pyaftership import AfterShip

API_KEY = 'XXXXXXXX0000000000XXXXXXXX0000000XXXXX000'


async def example():
    """Get trackings."""
    async with aiohttp.ClientSession() as session:
        aftership = AfterShip(API_KEY, session)
        trackings = await aftership.trackings.list_trackings()
        print("Pending trackings:", trackings["trackings"])

asyncio.get_event_loop().run_until_complete(example())
```

## Contribute

**All** contributions are welcome!

1. Fork the repository
2. Clone the repository locally and open the devcontainer or use GitHub codespaces
3. Do your changes
4. Lint the files with `make black`
5. Ensure all tests passes with `make test`
6. Ensure 100% coverage with `make coverage`
7. Commit your work, and push it to GitHub
8. Create a PR against the `main` branch