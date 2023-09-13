#!/usr/bin/env python3

import sys
from collections import defaultdict

total_file_size = 0
status_code_counts = defaultdict(int)
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.strip().split(" ")
        file_size = int(parts[-1])

        total_file_size += file_size

        status_code = parts[-2]
        status_code_counts[status_code] += 1

        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for code, count in sorted(status_code_counts.items()):
                print(code + ":", count)

except KeyboardInterrupt:
    print("Total file size:", total_file_size)
    for code, count in sorted(status_code_counts.items()):
        print(code + ":", count)
