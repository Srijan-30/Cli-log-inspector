# CLI Log Inspector

Command-line log filtering and inspection tools built in Python and C++.

## Python CLI (`log_inspector.py`)

```bash
python3 log_inspector.py sample.log --level ERROR --summary
python3 log_inspector.py sample.log --search "node-7"
```

## C++ CLI Warmup (`cpp_warmup/line_counter.cpp`)

```bash
g++ -Wall -Wextra -std=c++20 cpp_warmup/line_counter.cpp -o cpp_warmup/line_counter
./cpp_warmup/line_counter sample.log ERROR
```
