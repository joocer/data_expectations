"""
┌──────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘
"""
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
from data_expectations.measures.internals.bloom_filter import BloomFilter
from rich import traceback

traceback.install()


def test_bf():

    size = 500
    fp = 0.05

    bf = BloomFilter(size, fp)
    for i in range(size):
        if not i in (231, 325, 364, 464, 469):
            assert bf.add(f"{i}"), i

    # test all of the added items are found
    for i in range(size):
        assert f"{i}" in bf, f"test_bf - find {i}"

    # test that some items are not found
    collector = []
    for i in range(size):
        if f"{i + size}" in bf:
            collector.append(i + size)

    assert len(collector) <= (
        size * fp * 2
    ), f"test_bf {len(collector)} {(size * fp * 2)}"


if __name__ == "__main__":  # pragma: no cover
    test_bf()

    print("okay")
