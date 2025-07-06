from typing import Dict, Union

"""
- Level 1: support basic operations GET/SET/DELETE records
- Level 2: support scanning a specific record's fields based on a filter
- Level 3: support TTL configurations on database records
- Level 4: support backup and restore functionality
"""
"""
learning notes:
1. dict.update() a build-in method to update the dictionary with the key-value pairs
2. two dicts comparison can use == operator, why:
    - dictionary is unordered, so equality doesn't depend on the order of the key-value pairs
    - == operator checks if
        - both objects are objects
        - they have the same keys
        - for each key, the values are the same

3. KeyError is a built-in exception in Python that is raised
    when a key is not found in a dictionary.
        try:
            # code that may raise KeyError
        except KeyError:
            # code to handle KeyError
        except Exception as e:
            # code to handle other exceptions
4. if return type is type A or type B, use Union[A, B]
5. pytest.mark.parametrize is a decorator that allows you to run the same test
    with different parameters.
6. super().__init__() is a way to call the constructor of the parent class.
7. how to represent "never expires" in a way that makes comparisons simple and consistent
   expiry = float('inf') if ttl == 0 else timestamp + ttl
"""


class BaseInMemoryKV:
    def __init__(self):
        self.db: Dict[str, Dict[str, str]] = {}

    def set(self, key: str, field_value_pair: Dict[str, str]) -> str:
        if key not in self.db:
            self.db[key] = {}
        self.db[key].update(field_value_pair)
        return ""

    def get(self, key: str, field: str) -> str:
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


class InMemoryKVLevel1(BaseInMemoryKV):
    pass  # Inherits all methods from BaseInMemoryKV


class InMemoryKVLevel2(BaseInMemoryKV):
    def scan(self, key: str, prefix: str) -> Union[Dict[str, str], str]:
        if key not in self.db:
            return ""
        # Find all fields that start with the prefix
        result = {
            field: value
            for field, value in self.db[key].items()
            if field.startswith(prefix)
        }
        if not result:
            return ""
        return result

    # class InMemoryKVLevel3(BaseInMemoryKV):
    """
        Support the timeline of operations and TTL settings for records and fields.
        Each operation from the previous levels now have an alternative version
        with a timestamp parameter to represent the time when the operation occurs.
        Notes:
        - The timeline should always flow forward,
          so timestamps are guaranteed to be strictly increasing as operations as executed.

        - Newly introduced operations should be mixed up with operations defined
          in previous levels, but all prior functionality should still work.

        - `SET_AT<key><field><value><timestamp><ttl>` - inserts `field-value` pair
        or updates the value of the `field` in the record associated with `key`.
        Also sets its time-to-live after the `timestamp` to be `ttl`
        (both are represented as strings).
        The `ttl` is the amount of time that this `field-value` pair should exist in the database,
        meaning it will be available during the interval `[timestamp, timestamp + ttl]` .
        If `ttl = 0` the pair should always be available.
        This operation should return an empty string.

        - `DELETE_AT<key><field><timestamp>` - the same as `DELETE<key><field>` ,
        but with timestamp of the operation specified.
        Returns `"true"` if the field was deleted, and `"false"` otherwise.

        - `GET_AT<key><field><timestamp>` - the same as `GET <key><field>` ,
        but with timestamp of the operation specified.
        - `SCAN_AT<key><prefix><timestamp>` - the same as `SCAN`,
        but with timestamp of the operation specified.
    """
