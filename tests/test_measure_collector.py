"""
┌──────────────────────────────────────────────────────────────────────────────┐
│          NOTE: BINNING HAS BEEN REMOVED AS BOTH SLOW AND INACCURATE          │
└──────────────────────────────────────────────────────────────────────────────┘
"""
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
from data_expectations import MeasuresCollector
from rich import traceback

traceback.install()

ds = [
    {"user": "alice", "value": 3},
    {"user": "alice", "value": 4},
    {"user": "alice", "value": 3},
    {"user": "alice", "value": 4},
    {"user": "alice", "value": 5},
    {"user": "alice", "value": 5},
    {"user": "bob", "value": 1},
    {"user": "bob", "value": 2},
    {"user": "bob", "value": 1},
    {"user": "bob", "value": 2},
    {"user": "bob", "value": 1},
    {"user": "charlie", "value": 1},
    {"user": "charlie", "value": 2},
    {"user": "charlie", "value": 1},
    {"user": "dave", "value": 1},
    {"user": "eve", "value": 6},
    {"user": "eve", "value": 7},
    {"user": "finn", "value": 3},
    {"user": "finn", "value": 4},
    {"user": "finn", "value": 3},
    {"user": "finn", "value": 4},
    {"user": "finn", "value": 5},
    {"user": "finn", "value": 5},
    {"user": "finn", "value": 3},
    {"user": "finn", "value": 4},
]


def test_measures():
    m = MeasuresCollector()
    for i in ds:
        m.add(i)

    print(m.collector)

if __name__ == "__main__":
    test_measures()
