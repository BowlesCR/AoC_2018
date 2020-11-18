import fileinput
import re
from collections import defaultdict
from datetime import datetime, date


def minutelist() -> list[int]:
    return [0] * 60


def main():

    sched: dict[tuple[date, int], list[int]] = defaultdict(minutelist)
    guard: int
    asleep: datetime

    for line in sorted(fileinput.input()):
        match = re.match(
            r"^\[(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2})] \w+ #?(?P<keyword>#?\w+)(?: \w+ \w+){0,1}$",
            line,
        )
        ts = datetime.fromisoformat(match.group("timestamp"))

        if match.group("keyword") == "up":
            for i in range(asleep.minute, ts.minute):
                sched[(ts.date(), guard)][i] = 1
        elif match.group("keyword") == "asleep":
            asleep = ts
        else:
            guard = int(match.group("keyword"))

        # print(f"{match.group('keyword')} {ts}")

    freq: dict[int, list[int]] = defaultdict(minutelist)
    for guard in set([key[1] for key in sched.keys()]):
        for day in [sched[x] for x in sched if x[1] == guard]:
            for i in range(0, 60):
                freq[guard][i] += day[i]

    sleepyGuard: int
    sleepyMinute: int
    sleepyFreq: int = 0

    for guard in freq.keys():
        mx = max(freq[guard])
        if mx > sleepyFreq:
            sleepyGuard = guard
            sleepyFreq = mx
            sleepyMinute = freq[guard].index(mx)

    print(sleepyGuard * sleepyMinute)


if __name__ == "__main__":
    main()
