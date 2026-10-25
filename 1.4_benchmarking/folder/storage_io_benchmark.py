"""Task 3: storage read/write benchmark. Run from the repository directory."""
from pathlib import Path
from time import perf_counter
import os

SIZE = 100 * 1024 * 1024  # 100 MiB
CHUNK = 1024 * 1024
file_path = Path('testfile.bin')
results_path = Path('results/io.txt')

start = perf_counter()
try:
    with file_path.open('wb', buffering=0) as output:
        block = bytes(CHUNK)
        for _ in range(SIZE // CHUNK):
            output.write(block)
        os.fsync(output.fileno())
    write_time = perf_counter() - start

    start = perf_counter()
    total_read = 0
    with file_path.open('rb', buffering=0) as source:
        while True:
            block = source.read(CHUNK)
            if not block:
                break
            total_read += len(block)
    read_time = perf_counter() - start

    write_speed = SIZE / (1024 * 1024) / write_time
    read_speed = total_read / (1024 * 1024) / read_time
    text = ("Task 3 — Storage Read/Write Speed\n"
            "Test size: 100 MiB\n"
            f"Write time: {write_time:.4f} seconds\n"
            f"Write speed: {write_speed:.2f} MiB/s\n"
            f"Read time: {read_time:.4f} seconds\n"
            f"Read speed: {read_speed:.2f} MiB/s\n"
            "Note: Read results may include operating-system filesystem caching.\n")
    results_path.parent.mkdir(parents=True, exist_ok=True)
    results_path.write_text(text, encoding='utf-8')
    print(text)
    print(f"Saved to {results_path}")
finally:
    file_path.unlink(missing_ok=True)
