from in_memory_kv.v1 import InMemoryKVLevel1


def test_inmemory_kv_sequence():
    kv = InMemoryKVLevel1()

    # 1. SET A B E
    assert kv.set("A", {"B": "E"}) == ""
    assert kv.db == {"A": {"B": "E"}}

    # 2. SET A C F
    assert kv.set("A", {"C": "F"}) == ""
    # order doesn't matter
    expected = {"A": {"B": "E", "C": "F"}}
    assert kv.db == expected

    # 3. SET A B G (B already exists, update the value of B)
    assert kv.set("A", {"B": "G"}) == ""
    assert kv.db == {"A": {"B": "G", "C": "F"}}

    # 3. GET A B
    assert kv.get("A", "B") == "G"

    # 4. GET A D (D is not present)
    assert kv.get("A", "D") == ""

    # 5. DELETE A B
    assert kv.delete("A", "B") == "true"
    assert kv.db == {"A": {"C": "F"}}

    # 6. DELETE A D (not present)
    assert kv.delete("A", "D") == "false"
    assert kv.db == {"A": {"C": "F"}}
