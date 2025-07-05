from hit_counter.v2 import HitCounter


def test_hit_counter():
    hit_counter = HitCounter()
    hit_counter.hit(1)
    hit_counter.hit(2)
    hit_counter.hit(3)
    hit_counter.hit(3)
    hit_counter.hit(3)
    assert hit_counter.getHits(4) == 5
    assert hit_counter.getHits(300) == 5

    hit_counter.hit(301)
    assert hit_counter.getHits(301) == 5
    assert hit_counter.getHits(303) == 4
    assert hit_counter.getHits(304) == 1
