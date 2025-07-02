from in_memory_kv.v1 import InMemoryKVLevel1


def test_inmemory_kv_sequence():
    kv = InMemoryKVLevel1()

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
