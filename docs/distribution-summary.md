# Distribution Summary

This document provides a quick overview of all the ways to make `claude-conversation-extractor` available system-wide across different platforms.

## 🚀 Quick Start - Choose Your Platform

### 🍎 macOS
```bash
# Easiest method (recommended)
brew install pipx
pipx install claude-conversation-extractor

# Alternative: Build Homebrew formula
# See docs/distribution.md for details
```

### 🐧 Linux
```bash
# Debian/Ubuntu
sudo apt install python3-pip
pip3 install --user claude-conversation-extractor

# Fedora/RHEL
sudo dnf install python3-pip
pip3 install --user claude-conversation-extractor

# Or use build scripts
./scripts/build-linux.sh
```

### 🪟 Windows
```bash
# Via pip
pip install claude-conversation-extractor

# Or build executable
python scripts/build-windows.py

# Or use package managers (🚧 Coming Soon)
# choco install claude-conversation-extractor
# scoop install claude-conversation-extractor
```

### 🌐 All Platforms (PyPI)
```bash
pip install claude-conversation-extractor
```

## 📦 Distribution Methods

### 1. **PyPI Distribution** ⭐ (Most Universal)
- **Pros**: Works on all platforms, easy to install, automatic updates
- **Cons**: Requires Python, users need pip
- **Best for**: Developers, Python users, cross-platform distribution

**Setup**:
```bash
# Build and upload
python -m build
python -m twine upload dist/*

# Users install with
pip install claude-conversation-extractor
```

### 2. **pipx Installation** ⭐ (macOS/Linux)
- **Pros**: Isolated environment, system-wide access, easy updates
- **Cons**: macOS/Linux only, requires pipx
- **Best for**: macOS users, command-line tool enthusiasts

**Setup**:
```bash
# Users install with
pipx install claude-conversation-extractor
```

### 3. **Homebrew (macOS)** 🚧 **Coming Soon**
- **Pros**: Native macOS experience, easy updates, familiar to users
- **Cons**: Requires formula creation, macOS only, **Not yet implemented**
- **Best for**: macOS users who prefer Homebrew

**Setup**:
```bash
# Create formula and submit to Homebrew (🚧 Coming Soon)
# See homebrew/claude-conversation-extractor.rb template
```

### 4. **Linux Package Managers**
- **Pros**: Native to each distribution, system integration
- **Cons**: Platform-specific, requires package creation
- **Best for**: Linux server deployments, distribution maintainers

**Setup**:
```bash
# Use build scripts
./scripts/build-linux.sh
```

### 5. **Windows Package Managers** 🚧 **Coming Soon**
- **Pros**: Native Windows experience, easy updates
- **Cons**: Requires package creation, Windows only, **Not yet implemented**
- **Best for**: Windows users, enterprise deployment

**Setup**:
```bash
# Create packages for Chocolatey/Scoop (🚧 Coming Soon)
# Or build executable with PyInstaller
python scripts/build-windows.py
```

### 6. **Docker Distribution**
- **Pros**: Consistent environment, no Python installation needed
- **Cons**: Requires Docker, larger download
- **Best for**: Containerized environments, CI/CD

**Setup**:
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install .
ENTRYPOINT ["cce"]
```

## 🎯 Recommended Approach by User Type

### **End Users (Non-Developers)**
- **macOS**: `pipx install claude-conversation-extractor`
- **Linux**: `pip install claude-conversation-extractor`
- **Windows**: `pip install claude-conversation-extractor`

### **System Administrators**
- **Linux**: Use distribution packages (`.deb`, `.rpm`)
- **Windows**: Use pip installation or build executable (Chocolatey/Scoop 🚧 Coming Soon)
- **macOS**: Use pipx or pip installation (Homebrew 🚧 Coming Soon)

### **Developers**
- **All platforms**: `pip install claude-conversation-extractor`
- **Development**: `pip install -e .`

### **Enterprise Deployment**
- **Linux**: Distribution packages or Docker
- **Windows**: MSI installer or Chocolatey
- **macOS**: Homebrew or custom installer

## 🔧 Build Tools & Scripts

### **Automated Builds**
- **Linux**: `./scripts/build-linux.sh` - Creates `.deb`, `.rpm`, Arch packages
- **Windows**: `python scripts/build-windows.py` - Creates executable
- **CI/CD**: GitHub Actions workflow for PyPI releases

### **Manual Builds**
- **PyPI**: `python -m build`
- **Homebrew**: Create formula file
- **Docker**: Build and push to registry

## 📋 Prerequisites for Distribution

### **PyPI**
- Python 3.12+
- `build` and `twine` packages
- PyPI account

### **Homebrew**
- Ruby knowledge
- Homebrew formula creation experience
- GitHub repository

### **Linux Packages**
- Distribution-specific tools (`stdeb`, `rpm-build`)
- Package format knowledge
- Build environment

### **Windows**
- PyInstaller or similar
- Windows development environment
- Package manager accounts (Chocolatey/Scoop)

## 🚀 Getting Started

1. **Choose your primary distribution method** (PyPI recommended)
2. **Set up build environment** and tools
3. **Test installation** on target platforms
4. **Create distribution packages** for additional platforms
5. **Set up CI/CD** for automated releases
6. **Document installation** for each platform

## 📚 Additional Resources

- **Installation Guide**: `installation.md`
- **Distribution Guide**: `distribution.md`
- **Build Scripts**: `scripts/` directory
- **Homebrew Template**: `homebrew/claude-conversation-extractor.rb`
- **CI/CD Workflow**: `.github/workflows/release.yml`

## 🎉 Success Metrics

Your tool is successfully distributed when users can:
- Install it with a single command
- Use it immediately without additional setup
- Access it from any directory on their system
- Update it easily when new versions are released
- Get help and support when needed
