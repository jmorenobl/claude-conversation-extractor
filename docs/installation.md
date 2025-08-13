# Installation Guide

This guide covers how to install `claude-chat-extractor` on different platforms and make it available system-wide.

## 📦 Installation Methods Status

| Method | Status | Availability |
|--------|--------|--------------|
| **pip** | ✅ **Available Now** | All platforms |
| **pipx** | ✅ **Available Now** | macOS, Linux |
| **Source** | ✅ **Available Now** | All platforms |
| **Homebrew** | 🚧 **Coming Soon** | macOS |
| **Chocolatey** | 🚧 **Coming Soon** | Windows |
| **Scoop** | 🚧 **Coming Soon** | Windows |
| **Docker** | 🚧 **Coming Soon** | All platforms |

**Note**: Package manager installations (Homebrew, Chocolatey, Scoop) are planned for future releases but are not yet implemented. For now, please use pip or pipx installation methods.

## Quick Start

### From PyPI (Recommended)
```bash
pip install claude-chat-extractor
```

### From Source
```bash
git clone https://github.com/yourusername/claude-conversation-extractor
cd claude-conversation-extractor
pip install .
```

## Platform-Specific Installation

### 🐍 Python (All Platforms)

#### Global Installation
```bash
# Install for all users (requires admin/sudo)
sudo pip install claude-chat-extractor

# Install for current user only
pip install --user claude-chat-extractor
```

#### Virtual Environment Installation
```bash
# Create virtual environment
python -m venv claude-env
source claude-env/bin/activate  # On Windows: claude-env\Scripts\activate

# Install in virtual environment
pip install claude-chat-extractor
```

#### Verify Installation
```bash
# Check if commands are available
claude-chat-extractor --help
claude-extract --help
cce --help

# Check version
claude-chat-extractor --version
```

### 🍎 macOS

#### pipx (Recommended)
```bash
# Install pipx if not already installed
brew install pipx

# Install the tool
pipx install claude-chat-extractor
```

#### Homebrew (Alternative) 🚧 **Not Yet Implemented**
```bash
# Install via Homebrew (requires creating a formula first)
# ⚠️  WARNING: This method is not yet implemented
# brew install claude-chat-extractor

# Or if using a custom tap
# brew tap yourusername/tap
# brew install claude-chat-extractor
```

**Note**: Homebrew installation is planned but not yet available. For now, please use pip or pipx installation methods above.

#### Manual Installation
```bash
# Install Python dependencies
brew install python@3.12

# Install the tool
pip3 install claude-chat-extractor
```

#### PATH Configuration
Add to your shell profile (`~/.zshrc`, `~/.bash_profile`):
```bash
export PATH="/usr/local/bin:$HOME/.local/bin:$PATH"
```

### 🐧 Linux

#### Debian/Ubuntu
```bash
# Install system dependencies
sudo apt update
sudo apt install python3-pip python3-venv

# Install the tool
pip3 install --user claude-chat-extractor

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.local/bin:$PATH"
```

#### Fedora/RHEL/CentOS
```bash
# Install system dependencies
sudo dnf install python3-pip python3-setuptools

# Install the tool
pip3 install --user claude-chat-extractor

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.local/bin:$PATH"
```

#### Arch Linux
```bash
# Install from AUR
yay -S claude-chat-extractor

# Or install manually
sudo pacman -S python-pip
pip install --user claude-chat-extractor
```

#### Generic Linux
```bash
# Use the provided build script
./scripts/build-linux.sh

# Follow the instructions in the generated build directory
```

### 🪟 Windows

#### Chocolatey 🚧 **Not Yet Implemented**
```bash
# Install Chocolatey first, then:
# ⚠️  WARNING: This method is not yet implemented
# choco install claude-chat-extractor
```

**Note**: Chocolatey installation is planned but not yet available. For now, please use pip installation method above.

#### Scoop 🚧 **Not Yet Implemented**
```bash
# Install Scoop first, then:
# ⚠️  WARNING: This method is not yet implemented
# scoop install claude-chat-extractor
```

**Note**: Scoop installation is planned but not yet available. For now, please use pip installation method above.

#### Manual Installation
```bash
# Install Python from python.org
# Then install the tool
pip install claude-chat-extractor
```

#### Build Executable
```bash
# Use the provided build script
python scripts/build-windows.py

# Follow the instructions in the generated installer directory
```

#### PATH Configuration
1. Copy the executable to a directory (e.g., `C:\Tools\`)
2. Add that directory to your PATH environment variable
3. Restart command prompt

### 🐳 Docker

#### Pull and Run
```bash
# Pull the image
docker pull yourusername/claude-chat-extractor

# Run the tool
docker run --rm -v $(pwd):/work yourusername/claude-chat-extractor extract -u <uuid> -i /work/input.json
```

#### Build Locally
```bash
# Build the image
docker build -t claude-chat-extractor .

# Run the tool
docker run --rm -v $(pwd):/work claude-chat-extractor --help
```

## Development Installation

### Editable Install
```bash
# Clone the repository
git clone https://github.com/yourusername/claude-conversation-extractor
cd claude-conversation-extractor

# Install in editable mode
pip install -e .

# Install development dependencies
pip install -e ".[dev]"
```

### From Source
```bash
# Clone and install
git clone https://github.com/yourusername/claude-conversation-extractor
cd claude-conversation-extractor
python setup.py install
```

## Verification and Testing

### Test Commands
```bash
# Test help command
cce --help

# Test version
cce --version

# Test list command (if you have a sample file)
cce list -i sample.json
```

### Check Installation Location
```bash
# Find where the tool is installed
which cce
which claude-chat-extractor

# Check Python package location
python -c "import claude_conversation_extractor; print(claude_conversation_extractor.__file__)"
```

## Troubleshooting

### Common Issues

#### Command Not Found
```bash
# Check if the tool is installed
pip list | grep claude-chat-extractor

# Check PATH
echo $PATH

# Reinstall if needed
pip uninstall claude-chat-extractor
pip install claude-chat-extractor
```

#### Permission Errors
```bash
# Use user installation
pip install --user claude-chat-extractor

# Or use virtual environment
python -m venv claude-env
source claude-env/bin/activate
pip install claude-chat-extractor
```

#### Python Version Issues
```bash
# Check Python version
python --version
python3 --version

# Ensure Python 3.12+ is available
python3.12 --version
```

#### Dependency Issues
```bash
# Upgrade pip
pip install --upgrade pip

# Install with specific Python version
python3.12 -m pip install claude-chat-extractor
```

### Platform-Specific Issues

#### macOS
- Ensure Homebrew is up to date: `brew update`
- Check Python installation: `brew list python@3.12`

#### Linux
- Install system packages: `sudo apt install python3-dev` (Ubuntu/Debian)
- Use virtual environment to avoid permission issues

#### Windows
- Ensure Python is in PATH
- Use PowerShell or Command Prompt as Administrator if needed
- Check Windows Defender isn't blocking the executable

## Uninstallation

### Remove the Tool
```bash
# Uninstall via pip
pip uninstall claude-chat-extractor

# Or if installed via package manager (when available)
# Homebrew: brew uninstall claude-chat-extractor (🚧 Coming Soon)
# apt: sudo apt remove claude-chat-extractor
# dnf: sudo dnf remove claude-chat-extractor
```

### Clean Up
```bash
# Remove configuration files (if any)
rm -rf ~/.config/claude-chat-extractor

# Remove from PATH (edit shell profile files)
# Remove the export PATH line you added
```

## Next Steps

After successful installation:

1. **Read the Usage Guide**: See `usage.md` for detailed usage examples
2. **Check Requirements**: Ensure you have the required input format
3. **Test with Sample Data**: Try the tool with a small export file first
4. **Explore Features**: Use `cce --help` to see all available options

## Support

If you encounter issues:

1. Check this troubleshooting section
2. Review the [GitHub Issues](https://github.com/yourusername/claude-conversation-extractor/issues)
3. Create a new issue with details about your system and error messages
4. Check the [Requirements](requirements.md) for system compatibility
