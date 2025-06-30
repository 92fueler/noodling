# Noodling

Practice interview questions in stealth.

## Quick Start

### Bootstrap the Project

Set up the development environment with one command:

```bash
./script/bootstrap
```

This script will:
- Check for Python 3.10+ and uv installation
- Install all dependencies
- Set up the project in development mode
- Show you available commands

### Code Quality

Use the lint script for formatting and linting:

```bash
# Format and lint everything
./script/lint

# Only format code
./script/lint --format

# Only check for issues
./script/lint --lint

# Auto-fix issues
./script/lint --fix

# Target specific package
./script/lint lru_cache
./script/lint --fix web_crawler
```


## Development Setup

This project uses `uv` for Python package management.

### Prerequisites

- Python 3.10 or higher
- uv package manager
