# python-repo-template

[![Build and Test](https://github.com/kyhau/python-repo-template/workflows/Build%20and%20Test/badge.svg)](https://github.com/kyhau/python-repo-template/actions/workflows/python-ci.yml)
[![Codecov](https://codecov.io/gh/kyhau/python-repo-template/branch/main/graph/badge.svg)](https://codecov.io/gh/kyhau/python-repo-template)
[![CodeQL](https://github.com/kyhau/python-repo-template/workflows/CodeQL/badge.svg)](https://github.com/kyhau/python-repo-template/actions/workflows/codeql-analysis.yml)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](http://en.wikipedia.org/wiki/MIT_License)

Modern Python project template with Poetry, Makefile workflows, automated testing, linting, and GitHub Actions CI/CD.

**Supports Python 3.11, 3.12, 3.13**

## ✨ What's Included

### 🔧 Development Tools
- **[Poetry](https://python-poetry.org/)** - Modern dependency management
- **[Makefile](Makefile)** - Convenient command shortcuts for common tasks
- **[pytest](https://pytest.org/)** - Testing framework with coverage reporting
- **[black](https://black.readthedocs.io/)** - Code formatting
- **[flake8](https://flake8.pycqa.org/)** - Python code linting
- **[yamllint](https://yamllint.readthedocs.io/)** - YAML file linting

### 🔐 Security & Code Quality
- **[CodeQL](https://codeql.github.com)** - Automated security analysis ([workflow](.github/workflows/codeql-analysis.yml))
- **[Secrets Scan](https://github.com/gitleaks/gitleaks)** - Gitleaks and TruffleHog for detecting hardcoded secrets ([workflow](.github/workflows/secrets-scan.yml))
- **[Snyk](https://snyk.io/)** - Vulnerability scanning ([workflow](.github/workflows/snyk.yml))
- **[Dependabot](https://docs.github.com/en/code-security/dependabot)** - Automated dependency updates ([config](.github/dependabot.yml))

### 🚀 CI/CD
- **[GitHub Actions](https://github.com/features/actions)** - Automated testing and deployment
- **[Codecov](https://codecov.io/)** - Code coverage reporting
- **Stale Issue Management** - Automatically closes inactive issues

## 🚀 Getting Started

### 1. Create Repository from Template

Click **"Use this template"** on GitHub or:

```bash
mkdir new_repo_name
cd new_repo_name
git init
git pull https://github.com/kyhau/python-repo-template
```

### 2. Customize Your Project

Update these files:
- `pyproject.toml` - Package name, version, dependencies
- `Makefile` - Set `PACKAGE_NAME` and `TEST_PATH` variables
- `README.md` - Replace with your project description
- `app/` - Rename to your package name

### 3. Set Up Development Environment

**Quick setup (recommended for first-time setup):**
```bash
make setup-init
```

**Manual setup (if you prefer step-by-step):**
```bash
make setup-venv    # Configure Poetry to use local virtualenv
make install-all   # Install all dependencies
```

## 📋 Development Workflow

### Common Commands

```bash
make setup-init         # First-time setup (configure, lock, install everything)
make help               # Show all available commands
make install-all        # Install all dependencies (main, dev, test)
make test               # Run tests without coverage
make test-with-coverage # Run tests with coverage
make format-python      # Auto-format Python code
make lint-python        # Lint Python code
make lint-yaml          # Lint YAML files
make build              # Build the package
make clean              # Clean build artifacts
```

### Running Tests

```bash
# Run tests with coverage
make test-with-coverage

# Run tests only
make test

# Format and lint code
make format-python
make lint-python
make lint-yaml
```

### Managing Dependencies

```bash
# Update dependencies to latest compatible versions
make update-deps

# Regenerate lock file
make lock
```

## 🏗️ Project Structure

```
python-repo-template/
├── .github/
│   ├── workflows/        # CI/CD workflows
│   └── dependabot.yml    # Dependency updates config
├── app/                  # Your Python package
│   ├── __init__.py
│   └── main.py
├── tests/                # Unit tests
│   └── test_example.py
├── pyproject.toml        # Project metadata and dependencies
├── Makefile              # Build and test commands
└── README.md             # This file
```

## 📦 Building and Releasing

```bash
# Build the package
make build

# The built package will be in dist/
ls dist/
```
