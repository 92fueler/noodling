import pytest
from in_memory_kv.v1 import InMemoryKVLevel1, InMemoryKVLevel2


@pytest.mark.parametrize("kv_class", [InMemoryKVLevel1, InMemoryKVLevel2])
def test_inmemory_kv_sequence(kv_class):
    kv = kv_class()

    # SET A B E
    assert kv.set("A", {"B": "E"}) == ""
    assert kv.db == {"A": {"B": "E"}}

    # SET A C F
    assert kv.set("A", {"C": "F"}) == ""
    # order doesn't matter
    expected = {"A": {"B": "E", "C": "F"}}
    assert kv.db == expected

    # SET A B G (B already exists, update the value of B)
    assert kv.set("A", {"B": "G"}) == ""
    assert kv.db == {"A": {"B": "G", "C": "F"}}

    # GET A B
    assert kv.get("A", "B") == "G"

    # GET A D (D is not present)
    assert kv.get("A", "D") == ""

    # DELETE A B
    assert kv.delete("A", "B") == "true"
    assert kv.db == {"A": {"C": "F"}}

    # DELETE A D (not present)
    assert kv.delete("A", "D") == "false"
    assert kv.db == {"A": {"C": "F"}}


def test_inmemory_kv_sequence_2():
    kv = InMemoryKVLevel2()

    kv.set("D", {"EA": "F"})
    kv.set("D", {"EB": "5"})
    kv.set("D", {"ECD": "6"})
    kv.set("D", {"ECDF": "Z"})

    # scan a key with prefix E
    assert kv.scan("D", "E") == {"EA": "F", "EB": "5", "ECD": "6", "ECDF": "Z"}
    assert kv.scan("D", "EC") == {"ECD": "6", "ECDF": "Z"}

    # scan a non-existent key
    assert kv.scan("E", "ECDF") == ""
    assert kv.scan("D", "G") == ""
    # scan all fields
    assert kv.scan("D", "") == {"EA": "F", "EB": "5", "ECD": "6", "ECDF": "Z"}
