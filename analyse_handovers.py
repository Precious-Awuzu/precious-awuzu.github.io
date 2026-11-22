"""Run: python analyse_handovers.py support-cases.csv"""
import csv
import sys
from collections import defaultdict


def summarise(path):
    groups = defaultdict(list)
    with open(path, newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            band = min(int(row["handovers"]), 2)
            groups[band].append(int(row["repeat_contact_within_7_days"]))
    for band, outcomes in sorted(groups.items()):
        repeats = sum(outcomes)
        print(f"{band}{'+' if band == 2 else ''} handovers: "
              f"{repeats}/{len(outcomes)} repeated ({repeats / len(outcomes):.0%})")


if __name__ == "__main__":
    summarise(sys.argv[1])
