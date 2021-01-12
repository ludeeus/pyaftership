"""Common helpers for tests."""
import json
import os

API_KEY = "XXXXXXXX0000000000XXXXXXXX0000000XXXXX000"


def load_fixture(filename, asjson=False):
    """Load a fixture."""
    filename = f"{filename}.json" if "." not in filename else filename
    path = os.path.join(os.path.dirname(__file__), "fixtures", filename)
    with open(path, encoding="utf-8") as fptr:
        if asjson:
            return json.loads(fptr.read())
        return fptr.read()
