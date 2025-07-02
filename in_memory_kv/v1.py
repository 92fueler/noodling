from typing import Dict

"""
- support basic operations GET/SET/DELETE records
- support scanning a specific record's fields based on a filter
- support TTL configurations on database records
- support backup and restore functionality
"""
"""
learning notes:
1. dict.update() a build-in method to update the dictionary with the key-value pairs
2. two dicts comparison can use == operator, why:
    - dictionary is unordered, so equality doesn't depend on the order of the key-value pairs
    - == checks if
        - both objects are objects
        - they have the same keys
        - for each key, the values are the same

3. KeyError is a built-in exception in Python that is raised when a key is not found in a dictionary.
        try:
            # code that may raise KeyError
        except KeyError:
            # code to handle KeyError
        except Exception as e:
            # code to handle other exceptions

"""


class InMemoryKVLevel1:
    def __init__(self):
        self.db = {}

    def set(self, key: str, field_value_pair: Dict[str, str]) -> str:
        # if field exists, update the value of the field
        # if field does not exist, add the field to the key
        if key not in self.db:
            self.db[key] = {}
        self.db[key].update(field_value_pair)
        return ""

    def get(self, key: str, field: str) -> Dict[str, str]:
        if key not in self.db:
            print(f"Key {key} not found")
            return ""
        if field not in self.db[key]:
            print(f"Field {field} not found")
            return ""
        return self.db[key][field]

    def delete(self, key: str, field: str) -> str:
        if key not in self.db:
            return "false"
        if field not in self.db[key]:
            return "false"
        del self.db[key][field]
        return "true"
