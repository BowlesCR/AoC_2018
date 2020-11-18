import fileinput
import re
from collections import defaultdict
from datetime import datetime, date


def minuteslist() -> list[int]:
    return [0] * 60


def main():

    sched: dict[tuple[date, int], list[int]] = defaultdict(minuteslist)
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

    sums: dict[int, int] = dict()
    for guard in set([key[1] for key in sched.keys()]):
        sums[guard] = sum([sum(sched[x]) for x in sched.keys() if x[1] == guard])
        # print(f"{guard}, {sums[guard]}")

    sleepyGuard = max(sums, key=sums.get)

    times: list[int] = minuteslist()
    for day in [sched[x] for x in sched if x[1] == sleepyGuard]:
        for i in range(0, 60):
            times[i] += day[i]

    sleepyTime = times.index(max(times))
    # print(sleepyTime)

    print(sleepyGuard * sleepyTime)


if __name__ == "__main__":
    main()
