#!/usr/bin/env python3
"""Keep events from the next two weeks and print them sorted by date.

Reads lines `YYYY-MM-DD|title|venue` from stdin.
Usage: cat events.txt | python events_next.py
"""
import datetime as dt
import sys


def main() -> int:
    today = dt.date.today()
    horizon = today + dt.timedelta(days=14)
    events = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            date, title, venue = line.split("|", 2)
            date = dt.date.fromisoformat(date.strip())
        except ValueError:
            print(f"skip bad line: {line}", file=sys.stderr)
            continue
        if today <= date <= horizon:
            events.append((date, title.strip(), venue.strip()))
    events.sort()
    if not events:
        print("no events in the next two weeks")
        return 1
    for date, title, venue in events:
        print(f"{date}  {title} - {venue}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
