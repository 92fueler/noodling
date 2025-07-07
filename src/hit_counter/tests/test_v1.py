import pytest
from src.hit_counter.v1 import HitCounter, HitCounterV2


@pytest.mark.parametrize("hit_counter_class", [HitCounter, HitCounterV2])
def test_hit_counter(hit_counter_class):
    hit_counter = hit_counter_class()
    hit_counter.hit(1)
    hit_counter.hit(2)
    hit_counter.hit(3)
    assert hit_counter.getHits(4) == 3
    assert hit_counter.getHits(300) == 3
    assert hit_counter.getHits(301) == 2
    assert hit_counter.getHits(302) == 1
