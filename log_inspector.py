import argparse
from collections import Counter
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Inspect log files by severity level, keyword, or summary counts."
    )
    parser.add_argument("logfile", help="Path to the log file")
    parser.add_argument(
        "--level",
        choices=["INFO", "WARN", "ERROR"],
        help="Filter lines by log severity level",
    )
    parser.add_argument(
        "--search",
        help="Case-insensitive keyword to match within lines",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Print total lines scanned and counts per log level",
    )
    return parser.parse_args()


def detect_level(line: str) -> str | None:
    for level in ("INFO", "WARN", "ERROR"):
        if f" {level} " in line or line.startswith(f"{level} "):
            return level
    return None


def process_logs(
    logfile: str,
    level: str | None = None,
    search: str | None = None,
) -> tuple[list[str], Counter[str], int]:
    matches: list[str] = []
    counts: Counter[str] = Counter()
    total_lines = 0
    needle = search.lower() if search else None

    try:
        with open(logfile, encoding="utf-8", errors="replace") as f:
            for raw_line in f:
                total_lines += 1
                line = raw_line.rstrip("\r\n")
                detected = detect_level(line)
                if detected:
                    counts[detected] += 1

                if level and detected != level:
                    continue
                if needle and needle not in line.lower():
                    continue

                matches.append(line)
    except FileNotFoundError:
        print(f"Error: file not found -> {logfile}", file=sys.stderr)
        sys.exit(1)
    except OSError as exc:
        print(f"Error reading '{logfile}': {exc}", file=sys.stderr)
        sys.exit(1)

    return matches, counts, total_lines


def main() -> None:
    args = parse_args()
    matches, counts, total_lines = process_logs(
        logfile=args.logfile,
        level=args.level,
        search=args.search,
    )

    for line in matches:
        print(line)

    if args.summary:
        print("\n--- Summary ---")
        print(f"Total lines: {total_lines}")
        for lvl in ("INFO", "WARN", "ERROR"):
            print(f"{lvl}: {counts[lvl]}")


if __name__ == "__main__":
    main()