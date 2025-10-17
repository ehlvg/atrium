# atriumOS

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)

**Universal Development Environment Setup** - A modern, cross-platform setup script that configures your development environment in minutes.

```
   ▄████████     ███        ▄████████  ▄█    ▄   ███    █▄    ▄▄▄▄███▄▄▄▄      ▄██████▄     ▄████████
  ███    ███ ▀█████████▄   ███    ███ ███   ██▄ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███
  ███    ███    ▀███▀▀██   ███    ███ ███▄▄▄███ ███    ███ ███   ███   ███   ███    ███   ███    █▀
  ███    ███     ███   ▀  ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███ ███    ███ ███   ███   ███   ███    ███   ███
▀███████████     ███     ▀▀███▀▀▀▀▀   ▄██   ███ ███    ███ ███   ███   ███   ███    ███ ▀███████████
  ███    ███     ███     ▀███████████ ███   ███ ███    ███ ███   ███   ███   ███    ███          ███
  ███    ███     ███       ███    ███ ███   ███ ███    ███ ███   ███   ███   ███    ███    ▄█    ███
  ███    █▀     ▄████▀     ███    ███  ▀█████▀  ████████▀   ▀█   ███   █▀     ▀██████▀   ▄████████▀
                           ███    ███
```

## Features

- **Cross-Platform Support**: Works seamlessly on macOS, Linux, and Windows
- **GitHub CLI Integration**: Automated installation and authentication setup
- **Beautiful Terminal**: Custom oh-my-posh theme with language detection
- **Directory Structure**: Organizes your workspace with standard directories
- **Interactive Setup**: User-friendly prompts guide you through the process
- **Rich UI**: Modern terminal interface with progress indicators and colors

## What Gets Installed

### All Platforms
- GitHub CLI (gh)
- oh-my-posh with custom theme
- Directory structure (`~/Repos`, `~/Wallpapers`)

### macOS Specific
- Homebrew package manager
- Telegram Desktop
- Google Chrome (Dev)

### Theme Features
The custom oh-my-posh theme displays:
- Username and current path
- Git branch information
- Programming language versions (Python, Node, Go, Ruby, Java, Julia)
- Battery status
- Command execution time

## Installation

### Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/atriumos.git
cd atriumos

# Run the setup script
python3 atriumos.py
```

### One-Line Install

```bash
curl -fsSL https://raw.githubusercontent.com/yourusername/atriumos/main/atriumos.py | python3
```

### Prerequisites

- Python 3.7 or higher
- Internet connection
- Administrator/sudo access (for package installations)

## Usage

1. **Run the script**:
   ```bash
   python3 atriumos.py
   ```

2. **Follow the prompts**:
   - Confirm system detection
   - Authenticate with GitHub (optional)
   - Setup wallpaper sync (optional)

3. **Restart your terminal** to apply theme changes

4. **Start coding!**

## What's Configured

After running atriumOS, you'll have:

```
$HOME/
├── .config/
│   └── atriumos/
│       └── atriumos-theme.json    # oh-my-posh theme
├── Repos/                          # Your code repositories
└── Wallpapers/                     # Your wallpaper collection
```

## Command Reference

### Post-Installation Commands

```bash
# Authenticate with GitHub (if skipped)
gh auth login

# Apply shell configuration
source ~/.zshrc   # or ~/.bashrc

# Clone a repository
cd ~/Repos
gh repo clone username/repository

# Customize theme
nano ~/.config/atriumos/atriumos-theme.json
```

## Screenshots

### System Detection
The script automatically detects your operating system, architecture, and Python version.

### Installation Progress
Real-time progress indicators show what's being installed with spinners and status messages.

### Completion Summary
A comprehensive summary shows everything that was configured and next steps.

## Customization

### Modify the Theme

Edit the oh-my-posh theme at `~/.config/atriumos/atriumos-theme.json`:

```json
{
  "$schema": "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/schema.json",
  "blocks": [
    // Customize segments here
  ]
}
```

### Add More Applications (macOS)

Edit the `install_macos_apps()` method in `atriumos.py`:

```python
apps = [
    ("telegram", "Telegram Desktop"),
    ("google-chrome", "Google Chrome (Dev)", "--cask"),
    ("your-app", "Your Application Name", "--cask"),  # Add here
]
```

## Platform-Specific Notes

### macOS
- Homebrew will be installed automatically
- You may need to enter your password for sudo operations
- Xcode Command Line Tools may be required

### Linux
- Tested on Ubuntu/Debian distributions
- Some commands may require sudo password
- Package manager variations may need adjustments

### Windows
- Requires Windows Package Manager (winget)
- PowerShell may need to run as Administrator
- Theme configuration is manual for PowerShell

## Troubleshooting

### Python Rich Library Not Found
The script will automatically install it, but you can manually install:
```bash
pip install rich
```

### GitHub CLI Authentication Fails
Manually authenticate:
```bash
gh auth login --web
```

### oh-my-posh Theme Not Applied
Source your shell configuration:
```bash
# For zsh
source ~/.zshrc

# For bash
source ~/.bashrc
```

### Homebrew Installation Fails (macOS)
Install manually:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

## Contributing

Contributions are welcome! Please check out our [CONTRIBUTING.md](CONTRIBUTING.md) guide.

### Ways to Contribute
- Report bugs and request features
- Improve documentation
- Add support for more package managers
- Create additional themes
- Submit pull requests

## Roadmap

- [ ] Package manager auto-detection for Linux
- [ ] Dotfiles sync integration
- [ ] Plugin system for custom installers
- [ ] Configuration profiles (minimal, full, custom)
- [ ] Docker and container tool setup
- [ ] IDE configuration templates
- [ ] Cloud CLI tools (AWS, Azure, GCP)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- [oh-my-posh](https://ohmyposh.dev/) - Amazing prompt theme engine
- [Rich](https://rich.readthedocs.io/) - Beautiful terminal formatting
- [GitHub CLI](https://cli.github.com/) - GitHub on the command line
- The open-source community

## Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/atriumos/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/atriumos/discussions)
- **Documentation**: [Wiki](https://github.com/yourusername/atriumos/wiki)

---

<div align="center">
  <strong>Made with ❤️ by the atriumOS team</strong>
  <br>
  <sub>Star this repo if you find it useful!</sub>
</div>
