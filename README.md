# 🔮 Quantum Unifier - Universal Code Synchronization System

## 🎯 Purpose

**Quantum Unifier** is a powerful code synchronization and unification system designed for **Master SAMI_1978_0126**. It identifies, tracks, and unifies code across multiple devices, GitHub repositories, and network locations using a unique quantum signature.

## ✨ Features

### 🔐 Quantum Authentication
- Verifies master identity using unique quantum signature: `0x4A7D5F9E1C3B8A2D6F4E9C1A7B5D3F8G`
- Secure signature storage in `~/.quantum_sig`
- Environment variable support for automation

### 🌐 GitHub Integration
Automatically syncs all your GitHub repositories:
- **247TaxiDriver/virtualbox** - VirtualBox fork with custom enhancements
- **247TaxiDriver/KhayyamElite-Premium** - Astro-based premium project
- **247TaxiDriver/NLO.QS** - "One 4 all 4 one" quantum system

### 🔍 Multi-Source Scanning
- **Local Files**: Scans home directory, external drives, and system paths
- **Network Devices**: SSH into remote machines to find quantum-marked code
- **GitHub Repos**: Clones and updates all repositories automatically

### 📦 Unified Directory Structure
All code is organized in `~/quantum_unified/`:
```
quantum_unified/
├── local/              # Local files with quantum signature
├── github_repos/       # All GitHub repositories
│   ├── virtualbox/
│   ├── KhayyamElite-Premium/
│   └── NLO.QS/
└── quantum_manifest.json  # Complete metadata of all files
```

### 🔄 Version Control
- Automatic Git initialization in unified directory
- Tracks all changes with timestamps
- Full history of quantum unification events

## 🚀 Installation

### Prerequisites
- Python 3.7+
- Git
- SSH access (for network scanning)
- GitHub Personal Access Token (for repo sync)

### Setup

1. **Clone this repository**:
```bash
git clone https://github.com/247TaxiDriver/virtualbox.git
cd virtualbox
```

2. **Install Python dependencies** (if needed):
```bash
pip3 install requests
```

3. **Set up authentication**:

Option A - Environment variable:
```bash
export QUANTUM_SIG="0x4A7D5F9E1C3B8A2D6F4E9C1A7B5D3F8G"
export GITHUB_TOKEN="your_github_token_here"
```

Option B - Interactive (script will prompt you)

## 📖 Usage

### Basic Usage
```bash
python3 quantum_unifier.py
```

### What Happens?

1. **Authentication**: Enter your quantum signature when prompted
2. **GitHub Token**: Provide your GitHub token (create one at https://github.com/settings/tokens)
3. **Scanning**: The system scans all configured paths
4. **Syncing**: GitHub repos are cloned/updated
5. **Unification**: All code is copied to `~/quantum_unified/`
6. **Version Control**: Changes are committed to local Git repo

### Adding Quantum Signature to Your Code

To mark your code files with the quantum signature, add this comment:

**Python/Bash**:
```python
# QUANTUM_SIGNATURE: 0x4A7D5F9E1C3B8A2D6F4E9C1A7B5D3F8G
```

**JavaScript/C/C++**:
```javascript
// QUANTUM_SIGNATURE: 0x4A7D5F9E1C3B8A2D6F4E9C1A7B5D3F8G
```

**HTML/XML**:
```html
<!-- QUANTUM_SIGNATURE: 0x4A7D5F9E1C3B8A2D6F4E9C1A7B5D3F8G -->
```

## ⚙️ Configuration

### Customize Scan Paths
Edit `SCAN_PATHS` in `quantum_unifier.py`:
```python
SCAN_PATHS = [
    str(Path.home()),  # Home directory
    "/Volumes",        # External drives (macOS)
    "/opt",            # Custom install location
    "/media",          # USB drives (Linux)
]
```

### Add Network Devices
Edit `NETWORK_DEVICES`:
```python
NETWORK_DEVICES = [
    "user@192.168.1.10",
    "user@macbook-pro.local",
]
```

### Add More GitHub Repos
Edit `GITHUB_REPOS`:
```python
GITHUB_REPOS = [
    "247TaxiDriver/virtualbox",
    "247TaxiDriver/KhayyamElite-Premium",
    "247TaxiDriver/NLO.QS",
    "247TaxiDriver/your-new-repo",  # Add here
]
```

## 📊 Manifest File

After unification, `quantum_manifest.json` contains:
```json
{
  "master": "SAMI_1978_0126",
  "signature": "0x4A7D5F9E1C3B8A2D6F4E9C1A7B5D3F8G",
  "unified_at": "2026-02-14T22:00:00",
  "local_files": [...],
  "remote_files": [...],
  "github_repos": [...]
}
```

## 🔒 Security

- **Quantum Signature**: Acts as master authentication
- **Token Storage**: GitHub tokens stored securely in `~/.github_token` (0600 permissions)
- **SSH Keys**: Uses your existing SSH configuration for network devices
- **No Cloud Upload**: All data stays local unless explicitly pushed to GitHub

## 🛠️ Troubleshooting

### "Permission Denied" on Scan
Some system directories require elevated permissions:
```bash
sudo python3 quantum_unifier.py
```

### GitHub Token Issues
Ensure your token has these scopes:
- ✅ `repo` - Full control of repositories
- ✅ `read:user` - Read user profile data

### SSH Connection Failed
Check SSH keys and connectivity:
```bash
ssh -v user@remote-device
```

## 📜 License

This project is part of the VirtualBox fork, which follows the GPL-3.0 license. The Quantum Unifier script is custom code by Master SAMI_1978_0126.

## 🌟 About

**Master**: SAMI_1978_0126  
**Quantum Signature**: 0x4A7D5F9E1C3B8A2D6F4E9C1A7B5D3F8G  
**Contact**:  
- tourasami@gmail.com  
- cryptotaxi247@gmail.com  
- samitouri@msn.com

---

## 🔥 For Brother Sami and companies forever – QOS FOREVER 🔥

This system ensures that all your code, across all devices and platforms, is unified, tracked, and secured under the quantum signature. Your work is protected, organized, and always accessible.

**One codebase. One master. One quantum signature.**

═══════════════════════════════════════════════════════════════