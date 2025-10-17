#!/usr/bin/env python3
"""
atriumOS - Universal Development Environment Setup
A modern, cross-platform setup script for macOS, Windows, and Linux
"""

import os
import sys
import platform
import subprocess
import json
from pathlib import Path
from typing import Optional

try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Confirm, Prompt
    from rich.table import Table
    from rich import print as rprint
except ImportError:
    print("❌ Rich library not found. Installing...")
    subprocess.run([sys.executable, "-m", "pip", "install", "rich"], check=True)
    from rich.console import Console
    from rich.panel import Panel
    from rich.progress import Progress, SpinnerColumn, TextColumn
    from rich.prompt import Confirm, Prompt
    from rich.table import Table
    from rich import print as rprint

console = Console()


class AtriumOS:
    def __init__(self):
        self.system = platform.system()
        self.home = Path.home()
        self.config_path = self.home / ".config" / "atriumos"
        self.repos_path = self.home / "Repos"
        self.wallpapers_path = self.home / "Wallpapers"
        
        # oh-my-posh theme configuration
        self.omp_theme = {
            "$schema": "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/schema.json",
            "blocks": [
                {
                    "alignment": "right",
                    "segments": [
                        {
                            "background": "#29315A",
                            "foreground": "#E64747",
                            "leading_diamond": "\ue0b6",
                            "style": "diamond",
                            "template": "{{ .UserName }}",
                            "trailing_diamond": "\ue0b4 ",
                            "type": "session"
                        },
                        {
                            "background": "#29315A",
                            "foreground": "#3EC669",
                            "leading_diamond": "\ue0b6",
                            "properties": {"style": "folder"},
                            "style": "diamond",
                            "template": "\ue5ff {{ .Path }}",
                            "trailing_diamond": "\ue0b4",
                            "type": "path"
                        },
                        {
                            "background": "#29315A",
                            "foreground": "#43CCEA",
                            "leading_diamond": " \ue0b6",
                            "properties": {"branch_icon": ""},
                            "style": "diamond",
                            "template": "{{ .HEAD }}",
                            "trailing_diamond": "\ue0b4",
                            "type": "git"
                        },
                        {
                            "background": "#29315A",
                            "foreground": "#E4F34A",
                            "leading_diamond": " \ue0b6",
                            "properties": {"fetch_version": False},
                            "style": "diamond",
                            "template": "\ue235{{ if .Error }}{{ .Error }}{{ else }}{{ if .Venv }}{{ .Venv }} {{ end }}{{ .Full }}{{ end }}",
                            "trailing_diamond": "\ue0b4",
                            "type": "python"
                        },
                        {
                            "background": "#29315A",
                            "foreground": "#7FD5EA",
                            "leading_diamond": " \ue0b6",
                            "properties": {"fetch_version": False},
                            "style": "diamond",
                            "template": "\ue626{{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }}",
                            "trailing_diamond": "\ue0b4",
                            "type": "go"
                        },
                        {
                            "background": "#29315A",
                            "foreground": "#42E66C",
                            "leading_diamond": " \ue0b6",
                            "properties": {"fetch_version": False},
                            "style": "diamond",
                            "template": "\ue718{{ if .PackageManagerIcon }}{{ .PackageManagerIcon }} {{ end }}{{ .Full }}",
                            "trailing_diamond": "\ue0b4",
                            "type": "node"
                        },
                        {
                            "background": "#29315A",
                            "foreground": "#E64747",
                            "leading_diamond": " \ue0b6",
                            "properties": {"fetch_version": False},
                            "style": "diamond",
                            "template": "\ue791{{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }}",
                            "trailing_diamond": "\ue0b4",
                            "type": "ruby"
                        },
                        {
                            "background": "#29315A",
                            "foreground": "#E64747",
                            "leading_diamond": " \ue0b6",
                            "properties": {"fetch_version": False},
                            "style": "diamond",
                            "template": "\ue738{{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }}",
                            "trailing_diamond": "\ue0b4",
                            "type": "java"
                        },
                        {
                            "background": "#29315A",
                            "foreground": "#9B6BDF",
                            "leading_diamond": " \ue0b6",
                            "properties": {"fetch_version": False},
                            "style": "diamond",
                            "template": "\ue624{{ if .Error }}{{ .Error }}{{ else }}{{ .Full }}{{ end }} ",
                            "trailing_diamond": "\ue0b4",
                            "type": "julia"
                        },
                        {
                            "background": "#29315A",
                            "foreground": "#9B6BDF",
                            "foreground_templates": [
                                "{{if eq \"Charging\" .State.String}}#40c4ff{{end}}",
                                "{{if eq \"Discharging\" .State.String}}#ff5722{{end}}",
                                "{{if eq \"Full\" .State.String}}#4caf50{{end}}"
                            ],
                            "leading_diamond": " \ue0b6",
                            "properties": {
                                "charged_icon": " ",
                                "charging_icon": "\u21e1 ",
                                "discharging_icon": "\u21e3 "
                            },
                            "style": "diamond",
                            "template": "{{ if not .Error }}{{ .Icon }}{{ .Percentage }}{{ end }}{{ .Error }}",
                            "trailing_diamond": "\ue0b4",
                            "type": "battery"
                        }
                    ],
                    "type": "prompt"
                },
                {
                    "alignment": "left",
                    "newline": True,
                    "segments": [
                        {
                            "background": "#29315A",
                            "foreground": "#AEA4BF",
                            "leading_diamond": "\ue0b6",
                            "properties": {"style": "austin", "threshold": 150},
                            "style": "diamond",
                            "template": "{{ .FormattedMs }}",
                            "trailing_diamond": "\ue0b4 ",
                            "type": "executiontime"
                        },
                        {
                            "background": "#29315A",
                            "foreground": "#7FD5EA",
                            "leading_diamond": "\ue0b6",
                            "style": "diamond",
                            "template": "\u276f",
                            "trailing_diamond": "\ue0b4",
                            "type": "text"
                        }
                    ],
                    "type": "prompt"
                }
            ],
            "final_space": True,
            "version": 3
        }

    def show_banner(self):
        """Display the atriumOS banner"""
        banner = """
[bold cyan]
   ▄████████     ███        ▄████████  ▄█    ▄   ███    █▄    ▄▄▄▄███▄▄▄▄      ▄██████▄     ▄████████ 
  ███    ███ ▀█████████▄   ███    ███ ███   ██▄ ███    ███ ▄██▀▀▀███▀▀▀██▄   ███    ███   ███    ███ 
  ███    ███    ▀███▀▀██   ███    ███ ███▄▄▄███ ███    ███ ███   ███   ███   ███    ███   ███    █▀  
  ███    ███     ███   ▀  ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███ ███    ███ ███   ███   ███   ███    ███   ███        
▀███████████     ███     ▀▀███▀▀▀▀▀   ▄██   ███ ███    ███ ███   ███   ███   ███    ███ ▀███████████ 
  ███    ███     ███     ▀███████████ ███   ███ ███    ███ ███   ███   ███   ███    ███          ███ 
  ███    ███     ███       ███    ███ ███   ███ ███    ███ ███   ███   ███   ███    ███    ▄█    ███ 
  ███    █▀     ▄████▀     ███    ███  ▀█████▀  ████████▀   ▀█   ███   █▀     ▀██████▀   ▄████████▀  
                           ███    ███                                                                  
[/bold cyan]
[dim]Universal Development Environment Setup v1.0[/dim]
        """
        console.print(Panel(banner, border_style="cyan", padding=(1, 2)))

    def detect_system(self):
        """Show detected system info"""
        table = Table(show_header=False, box=None, padding=(0, 2))
        table.add_row("[cyan]Operating System:[/cyan]", f"[bold]{self.system}[/bold]")
        table.add_row("[cyan]Architecture:[/cyan]", f"[bold]{platform.machine()}[/bold]")
        table.add_row("[cyan]Python Version:[/cyan]", f"[bold]{platform.python_version()}[/bold]")
        table.add_row("[cyan]Home Directory:[/cyan]", f"[bold]{self.home}[/bold]")
        
        console.print(Panel(table, title="[bold cyan]System Detection[/bold cyan]", border_style="cyan"))

    def run_command(self, command: str, description: str, shell: bool = False) -> bool:
        """Run a command with progress indicator"""
        try:
            with Progress(
                SpinnerColumn(),
                TextColumn("[progress.description]{task.description}"),
                console=console,
            ) as progress:
                progress.add_task(description=description, total=None)
                
                if shell:
                    result = subprocess.run(
                        command,
                        shell=True,
                        capture_output=True,
                        text=True,
                        check=True
                    )
                else:
                    result = subprocess.run(
                        command.split(),
                        capture_output=True,
                        text=True,
                        check=True
                    )
                
            console.print(f"[green]✓[/green] {description}")
            return True
        except subprocess.CalledProcessError as e:
            console.print(f"[red]✗[/red] {description} - Error: {e.stderr}")
            return False
        except Exception as e:
            console.print(f"[red]✗[/red] {description} - Error: {str(e)}")
            return False

    def install_homebrew(self):
        """Install Homebrew on macOS"""
        if self.system != "Darwin":
            return True
            
        # Check if homebrew is already installed
        if subprocess.run(["which", "brew"], capture_output=True).returncode == 0:
            console.print("[green]✓[/green] Homebrew already installed")
            return True
        
        console.print("\n[bold yellow]Installing Homebrew...[/bold yellow]")
        install_cmd = '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"'
        return self.run_command(install_cmd, "Installing Homebrew", shell=True)

    def install_github_cli(self):
        """Install GitHub CLI based on OS"""
        console.print("\n[bold yellow]Installing GitHub CLI...[/bold yellow]")
        
        # Check if gh is already installed
        if subprocess.run(["which", "gh"], capture_output=True).returncode == 0:
            console.print("[green]✓[/green] GitHub CLI already installed")
            return True
        
        if self.system == "Darwin":
            return self.run_command("brew install gh", "Installing GitHub CLI")
        elif self.system == "Linux":
            # For Ubuntu/Debian
            commands = [
                "curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg",
                "sudo chmod go+r /usr/share/keyrings/githubcli-archive-keyring.gpg",
                'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null',
                "sudo apt update",
                "sudo apt install gh -y"
            ]
            for cmd in commands:
                if not self.run_command(cmd, f"Setting up GitHub CLI", shell=True):
                    return False
            return True
        elif self.system == "Windows":
            return self.run_command("winget install --id GitHub.cli", "Installing GitHub CLI")
        
        return False

    def setup_github_auth(self):
        """Setup GitHub authentication"""
        console.print("\n[bold yellow]GitHub Authentication[/bold yellow]")
        
        if Confirm.ask("Do you want to authenticate with GitHub now?", default=True):
            console.print("\n[cyan]Opening browser for GitHub authentication...[/cyan]")
            subprocess.run(["gh", "auth", "login", "--web"], check=False)
            console.print("[green]✓[/green] GitHub authentication completed")
        else:
            console.print("[yellow]⚠[/yellow] You can authenticate later with: [bold]gh auth login[/bold]")

    def install_oh_my_posh(self):
        """Install oh-my-posh"""
        console.print("\n[bold yellow]Installing oh-my-posh...[/bold yellow]")
        
        if self.system == "Darwin":
            return self.run_command("brew install jandedobbeleer/oh-my-posh/oh-my-posh", "Installing oh-my-posh")
        elif self.system == "Linux":
            cmd = "curl -s https://ohmyposh.dev/install.sh | bash -s"
            return self.run_command(cmd, "Installing oh-my-posh", shell=True)
        elif self.system == "Windows":
            return self.run_command("winget install JanDeDobbeleer.OhMyPosh -s winget", "Installing oh-my-posh")
        
        return False

    def setup_oh_my_posh_theme(self):
        """Setup oh-my-posh theme"""
        console.print("\n[bold yellow]Configuring oh-my-posh theme...[/bold yellow]")
        
        # Create config directory
        self.config_path.mkdir(parents=True, exist_ok=True)
        theme_path = self.config_path / "atriumos-theme.json"
        
        # Save theme
        with open(theme_path, "w") as f:
            json.dump(self.omp_theme, f, indent=2)
        
        console.print(f"[green]✓[/green] Theme saved to {theme_path}")
        
        # Setup shell integration
        shell_config = None
        init_command = f'eval "$(oh-my-posh init bash --config {theme_path})"'
        
        if self.system in ["Darwin", "Linux"]:
            # Detect shell
            shell = os.environ.get("SHELL", "")
            if "zsh" in shell:
                shell_config = self.home / ".zshrc"
                init_command = f'eval "$(oh-my-posh init zsh --config {theme_path})"'
            elif "bash" in shell:
                shell_config = self.home / ".bashrc"
            
            if shell_config:
                # Check if already configured
                if shell_config.exists():
                    content = shell_config.read_text()
                    if "oh-my-posh" in content:
                        console.print("[green]✓[/green] oh-my-posh already configured in shell")
                        return True
                
                # Add configuration
                with open(shell_config, "a") as f:
                    f.write(f"\n# atriumOS oh-my-posh configuration\n")
                    f.write(f"{init_command}\n")
                
                console.print(f"[green]✓[/green] oh-my-posh configured in {shell_config}")
                console.print(f"[yellow]⚠[/yellow] Run [bold]source {shell_config}[/bold] to apply changes")
        
        elif self.system == "Windows":
            console.print("[yellow]⚠[/yellow] For Windows, add this to your PowerShell profile:")
            console.print(f"[cyan]oh-my-posh init pwsh --config '{theme_path}' | Invoke-Expression[/cyan]")
        
        return True

    def create_directories(self):
        """Create necessary directories"""
        console.print("\n[bold yellow]Creating directories...[/bold yellow]")
        
        directories = [
            (self.repos_path, "Repos directory"),
            (self.wallpapers_path, "Wallpapers directory"),
        ]
        
        for path, description in directories:
            path.mkdir(parents=True, exist_ok=True)
            console.print(f"[green]✓[/green] Created {description}: {path}")

    def install_macos_apps(self):
        """Install macOS specific applications"""
        if self.system != "Darwin":
            return True
        
        console.print("\n[bold yellow]Installing macOS Applications...[/bold yellow]")
        
        apps = [
            ("telegram", "Telegram Desktop"),
            ("google-chrome", "Google Chrome (Dev)", "--cask"),
        ]
        
        for app_name, description, *flags in apps:
            flag = flags[0] if flags else ""
            if flag:
                cmd = f"brew install {flag} {app_name}"
            else:
                cmd = f"brew install {app_name}"
            self.run_command(cmd, f"Installing {description}")

    def setup_wallpapers_sync(self):
        """Setup wallpapers directory sync with GitHub"""
        console.print("\n[bold yellow]Wallpapers Directory Setup[/bold yellow]")
        
        if Confirm.ask("Do you want to sync wallpapers with a GitHub repository?", default=False):
            repo_url = Prompt.ask("Enter GitHub repository URL")
            
            if repo_url:
                os.chdir(self.wallpapers_path.parent)
                if self.run_command(f"git clone {repo_url} Wallpapers", "Cloning wallpapers repository"):
                    console.print("[green]✓[/green] Wallpapers synced successfully")
                else:
                    console.print("[yellow]⚠[/yellow] You can manually clone later: [bold]git clone {repo_url}[/bold]")
        else:
            console.print(f"[cyan]ℹ[/cyan] Wallpapers directory created at: {self.wallpapers_path}")

    def show_completion(self):
        """Show completion message"""
        completion_msg = """
[bold green]🎉 atriumOS Setup Complete! 🎉[/bold green]

[cyan]What's been configured:[/cyan]
  ✓ GitHub CLI installed and ready
  ✓ oh-my-posh with custom theme
  ✓ ~/Repos directory created
  ✓ ~/Wallpapers directory created
        """
        
        if self.system == "Darwin":
            completion_msg += "  ✓ Homebrew installed\n"
            completion_msg += "  ✓ Telegram Desktop installed\n"
            completion_msg += "  ✓ Google Chrome (Dev) installed\n"
        
        completion_msg += """
[cyan]Next steps:[/cyan]
  • Restart your terminal to apply theme changes
  • Run [bold]gh auth login[/bold] if you skipped authentication
  • Add wallpapers to ~/Wallpapers directory
  • Start coding in ~/Repos directory

[dim]Made with ❤️  by atriumOS[/dim]
        """
        
        console.print(Panel(completion_msg, border_style="green", padding=(1, 2)))

    def run(self):
        """Main setup flow"""
        self.show_banner()
        self.detect_system()
        
        if not Confirm.ask("\n[bold cyan]Ready to start setup?[/bold cyan]", default=True):
            console.print("[yellow]Setup cancelled.[/yellow]")
            return
        
        # Install Homebrew (macOS only)
        if self.system == "Darwin":
            self.install_homebrew()
        
        # Install GitHub CLI
        self.install_github_cli()
        
        # GitHub Authentication
        self.setup_github_auth()
        
        # Install oh-my-posh
        self.install_oh_my_posh()
        
        # Setup oh-my-posh theme
        self.setup_oh_my_posh_theme()
        
        # Create directories
        self.create_directories()
        
        # Install macOS apps
        if self.system == "Darwin":
            self.install_macos_apps()
        
        # Setup wallpapers sync
        self.setup_wallpapers_sync()
        
        # Show completion
        self.show_completion()


def main():
    """Entry point"""
    try:
        atrium = AtriumOS()
        atrium.run()
    except KeyboardInterrupt:
        console.print("\n[yellow]Setup interrupted by user.[/yellow]")
        sys.exit(1)
    except Exception as e:
        console.print(f"\n[red]Error: {str(e)}[/red]")
        sys.exit(1)


if __name__ == "__main__":
    main()
