# Contributing to atriumOS

Thank you for considering contributing to atriumOS! This document outlines the process and guidelines for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected behavior** vs **actual behavior**
- **System information** (OS, Python version, etc.)
- **Relevant logs or screenshots**

**Example:**
```markdown
**Bug:** oh-my-posh theme not applied on zsh

**Steps to reproduce:**
1. Run atriumos.py on macOS
2. Complete setup successfully
3. Restart terminal

**Expected:** Custom theme should be visible
**Actual:** Default prompt appears

**System:** macOS 14.0, Python 3.11, zsh 5.9
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case** - why this would be useful
- **Proposed solution** (if any)
- **Alternative solutions** you've considered

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** following the coding standards below
3. **Test your changes** on multiple platforms if possible
4. **Update documentation** if needed
5. **Write a clear commit message**
6. **Submit a pull request**

## Development Setup

### Prerequisites

- Python 3.7+
- Git
- Virtual environment tool (recommended)

### Setting Up Development Environment

```bash
# Clone your fork
git clone https://github.com/yourusername/atriumos.git
cd atriumos

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install in development mode
pip install -e .
```

### Running Tests

```bash
# Test the script
python3 atriumos.py

# Test on different platforms (if available)
# - macOS
# - Linux (Ubuntu/Debian)
# - Windows
```

## Coding Standards

### Python Style Guide

- Follow [PEP 8](https://pep8.org/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use meaningful variable and function names

### Code Organization

```python
# Good
def install_github_cli(self):
    """Install GitHub CLI based on OS"""
    console.print("\n[bold yellow]Installing GitHub CLI...[/bold yellow]")
    # Implementation...

# Bad
def gh_install(self):
    # No docstring
    print("Installing...")  # Don't use print, use console.print
```

### Documentation

- Add docstrings to all functions and classes
- Update README.md for user-facing changes
- Comment complex logic

### Error Handling

```python
# Good
try:
    result = subprocess.run(command, check=True, capture_output=True)
    console.print(f"[green]✓[/green] {description}")
    return True
except subprocess.CalledProcessError as e:
    console.print(f"[red]✗[/red] {description} - Error: {e.stderr}")
    return False

# Bad
try:
    subprocess.run(command)  # No error handling
except:  # Bare except
    pass  # Silent failure
```

## Platform-Specific Guidelines

### macOS
- Test with both Intel and Apple Silicon if possible
- Ensure Homebrew integration works correctly
- Test with both zsh and bash

### Linux
- Test on at least Ubuntu/Debian
- Consider different package managers (apt, yum, dnf)
- Ensure sudo operations are secure

### Windows
- Test with both PowerShell and Command Prompt
- Ensure winget commands work correctly
- Handle Windows-specific paths properly

## Adding New Features

### Process

1. **Open an issue** first to discuss the feature
2. **Wait for approval** from maintainers
3. **Implement the feature** following the guidelines
4. **Test thoroughly** on all platforms
5. **Submit a pull request**

### Example: Adding a New Application

```python
def install_new_app(self):
    """Install new application"""
    console.print("\n[bold yellow]Installing New App...[/bold yellow]")

    if self.system == "Darwin":
        return self.run_command("brew install app-name", "Installing New App")
    elif self.system == "Linux":
        return self.run_command("sudo apt install app-name -y", "Installing New App")
    elif self.system == "Windows":
        return self.run_command("winget install AppName", "Installing New App")

    return False
```

Then add it to the `run()` method:
```python
def run(self):
    # ... existing code ...

    # Install new app
    self.install_new_app()

    # ... rest of code ...
```

## Commit Message Guidelines

### Format

```
type: brief description

Longer description if needed.

Fixes #123
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
# Good
feat: add support for Fedora package manager
fix: oh-my-posh theme not applying on bash
docs: update installation instructions for Windows

# Bad
update stuff
fix bug
changes
```

## Review Process

1. **Automated checks** must pass (if configured)
2. **Code review** by at least one maintainer
3. **Testing** on multiple platforms (if possible)
4. **Documentation** review
5. **Approval and merge**

## Getting Help

- **GitHub Issues**: For bugs and feature requests
- **GitHub Discussions**: For questions and general discussion
- **Documentation**: Check the [Wiki](https://github.com/yourusername/atriumos/wiki)

## Recognition

Contributors will be recognized in:
- GitHub contributors list
- Release notes for significant contributions
- README acknowledgments section

## License

By contributing to atriumOS, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to atriumOS!
