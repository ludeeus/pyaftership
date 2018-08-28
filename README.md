# pyaftership

_A module to get information pending parcels._

## Notes

This has been tested with python 3.6  
This module uses these external libararies:

- requests

## Install

```bash
pip install pyaftership
```

## Sample usage

```python
from pyaftership import AfterShip

api_key = '9781915b342514bf0dede6e3d058a'
after_ship = AfterShip()

# Get parcel information:
result = after_ship.get_trackings(api_key)

# Print the result:
print(result)

# Add parcel information
result = after_ship.add_tracking(api_key, slug, title, tracking_number)

# Print the result:
print(result)

# Delete parcel information
result = after_ship.delete_tracking(api_key, slug, tracking_number)

# Print the result:
print(result)
```
