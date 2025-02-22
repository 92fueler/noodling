# Low Level Data Structures

This project contains multiple subprojects implementing various low-level data structures and algorithms.

## Project Structure
- `web_crawler/`: Web crawler implementation
- `lru_cache/`: LRU Cache implementation with various approaches
  - `basic_lru_cache.py`: Basic implementation using double linked list
  - `singleton_lru_cache.py`: Thread-safe singleton implementation
  - `tests/`: Test suite for both implementations

## Development Setup

This project uses `uv` for Python package management. Make sure you have `uv` installed.

### Installing Dependencies

For web_crawler subproject:
```bash
uv pip install -e ".[web_crawler]"
```

For lru_cache subproject:
```bash
uv pip install -e ".[lru_cache]"
```

### Running Tests

For web_crawler:
```bash
uv run pytest web_crawler/tests
```

For lru_cache:
```bash
# Run all tests
cd lru_cache && uv run pytest tests/

# Run specific tests
cd lru_cache && uv run pytest tests/test_basic_lru_cache.py
cd lru_cache && uv run pytest tests/test_singleton_lru_cache.py

# Or from project root
uv run pytest lru_cache/tests/
uv run pytest lru_cache/tests/test_basic_lru_cache.py
uv run pytest lru_cache/tests/test_singleton_lru_cache.py
```

### Running Linting

For web_crawler:
```bash
uv run ruff check web_crawler
```

For lru_cache:
```bash
uv run ruff check lru_cache
```