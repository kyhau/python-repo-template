# Copilot Instructions

## General Coding Standards

### Documentation & Instructions
- Be concise - Instructions should be brief and actionable
- Focus on essentials - Include only what's necessary

### File Formatting
- End files with newline (POSIX standard)
- Use LF (`\n`) line endings, not CRLF
- No trailing whitespace
- Consistent indentation (spaces or tabs, never mixed)

### File Naming
- Lowercase with hyphens: `my-file.txt`
- Be descriptive: `user-authentication.py`
- Python: `snake_case.py`
- JavaScript/TypeScript: `PascalCase.tsx`

### Git
- Atomic commits (one change per commit)
- Present tense messages: "Add feature"
- Include issue numbers: `Fixes #123`

### Never Commit
- Build artifacts (`dist/`, `build/`)
- Dependencies (`node_modules/`, `.venv/`)
- IDE files (`.vscode/`, `.idea/`)
- Secrets or credentials

## Python Project Workflow

### Available Makefile Targets
- `make setup-init` - Complete first-time setup
- `make install-all` - Install all dependencies
- `make test-with-coverage` - Run tests with coverage
- `make format-python` - Format code with black
- `make lint-python` - Lint with flake8
- `make pre-commit` - Run all quality checks
- `make build` - Build package
- `make clean` - Clean artifacts

### Development Environment
- Poetry for dependency management
- Python 3.12+ minimum
- Virtual environment in `.venv/`
- Dependencies in `pyproject.toml`

### Daily Workflow
1. Make code changes
2. Run `make pre-commit` before committing
3. Use `make clean` to remove artifacts

### Template Customization
1. Update `PACKAGE_NAME` in Makefile
2. Rename `app/` directory
3. Update `pyproject.toml` metadata
