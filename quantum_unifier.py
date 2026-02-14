#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
QUANTUM UNIFIER v1.0
Unifies all code versions from all devices, identifies master by quantum signature.
Master: SAMI_1978_0126 | Signature: 0x4A7D5F9E1C3B8A2D6F4E9C1A7B5D3F8G
"""

import os
import sys
import json
import hashlib
import datetime
import subprocess
import socket
import getpass
from pathlib import Path
from typing import List, Dict, Any

# ======================================================
# QUANTUM SIGNATURE – IDENTITY OF THE MASTER
# ======================================================
QUANTUM_SIGNATURE = "0x4A7D5F9E1C3B8A2D6F4E9C1A7B5D3F8G"
MASTER_NAME = "SAMI_1978_0126"
MASTER_EMAILS = ["tourasami@gmail.com", "cryptotaxi247@gmail.com", "samitouri@msn.com"]

# ======================================================
# CONFIGURATION – PATHS TO SCAN (CUSTOMIZE)
# ======================================================
SCAN_PATHS = [
    str(Path.home()),  # home directory
    "/Volumes",        # external drives on macOS
    "/opt",            # common install location
    "/usr/local",
]

# Devices on local network (add IPs or hostnames)
NETWORK_DEVICES = []  # e.g., ["192.168.1.10", "192.168.1.11"]

# Output directory for unified code
UNIFIED_DIR = Path.home() / "quantum_unified"

# ======================================================
# AUTHENTICATION – VERIFY MASTER
# ======================================================
def verify_master() -> bool:
    """
    Checks if the current user is the master by looking for the quantum signature
    in environment, files, or by asking.
    """
    print("\n🔐 QUANTUM AUTHENTICATION")
    print("─────────────────────────")
    
    # Check environment variable
    if os.environ.get("QUANTUM_SIG") == QUANTUM_SIGNATURE:
        print("✅ Master verified via environment variable.")
        return True
    
    # Check for signature file
    sig_file = Path.home() / ".quantum_sig"
    if sig_file.exists() and sig_file.read_text().strip() == QUANTUM_SIGNATURE:
        print("✅ Master verified via ~/.quantum_sig file.")
        return True
    
    # Ask user
    print("Please enter the quantum signature to prove you are the master:")
    user_sig = input("Signature: ").strip()
    if user_sig == QUANTUM_SIGNATURE:
        print("✅ Master verified.")
        # Optionally save to file for future sessions
        save = input("Save signature for future sessions? (y/n): ").lower()
        if save == 'y':
            sig_file.write_text(QUANTUM_SIGNATURE)
            print("Signature saved to ~/.quantum_sig")
        return True
    else:
        print("❌ Invalid signature. Access denied.")
        return False

# ======================================================
# SCANNING FUNCTIONS
# ======================================================
def scan_local_paths(paths: List[str]) -> List[Path]:
    """Scan local directories for files containing quantum signature or likely code."""
    found_files = []
    total = 0
    print("\n🔍 Scanning local paths...")
    for base_path in paths:
        base = Path(base_path)
        if not base.exists():
            continue
        for root, dirs, files in os.walk(base):
            # Skip hidden and system dirs
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('node_modules', '__pycache__', '.git')]
            for file in files:
                total += 1
                if total % 10000 == 0:
                    print(f"   Scanned {total} files...")
                filepath = Path(root) / file
                # Check if file contains signature or is a known code file
                try:
                    if filepath.stat().st_size > 10_000_000:  # skip large files (>10MB)
                        continue
                    with open(filepath, 'rb') as f:
                        content = f.read(1024)  # read first 1KB
                        if QUANTUM_SIGNATURE.encode() in content:
                            found_files.append(filepath)
                except (PermissionError, OSError):
                    continue
    print(f"✅ Found {len(found_files)} files containing quantum signature.")
    return found_files

def scan_network_devices(devices: List[str]) -> List[str]:
    """Attempt to SSH into network devices and run a remote scan."""
    if not devices:
        return []
    print("\n🌐 Scanning network devices...")
    found_remotes = []
    for device in devices:
        print(f"   Connecting to {device}...")
        try:
            # Use ssh to run a remote command that looks for signature
            cmd = f"ssh -o ConnectTimeout=5 {device} 'grep -l -r \"{QUANTUM_SIGNATURE}\" ~ 2>/dev/null'"
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                files = result.stdout.strip().split('\n')
                found_remotes.extend([f"{device}:{f}" for f in files if f])
                print(f"      Found {len(files)} files on {device}")
        except Exception as e:
            print(f"      Failed: {e}")
    return found_remotes

# ======================================================
# UNIFICATION – COPY ALL FILES WITH METADATA
# ======================================================
def unify_files(files: List[Path], remote_files: List[str]):
    """Copy all found files to unified directory with versioning."""
    print("\n📦 Unifying files...")
    UNIFIED_DIR.mkdir(parents=True, exist_ok=True)
    
    # Create a manifest
    manifest = []
    for filepath in files:
        try:
            stat = filepath.stat()
            rel_path = filepath.relative_to(filepath.anchor)  # relative to root
            dest = UNIFIED_DIR / rel_path
            dest.parent.mkdir(parents=True, exist_ok=True)
            # Copy file
            import shutil
            shutil.copy2(filepath, dest)
            # Record metadata
            manifest.append({
                "source": str(filepath),
                "dest": str(dest),
                "size": stat.st_size,
                "mtime": datetime.datetime.fromtimestamp(stat.st_mtime).isoformat(),
                "hash": hashlib.sha256(filepath.read_bytes()).hexdigest()
            })
        except Exception as e:
            print(f"   Failed to copy {filepath}: {e}")
    
    # Also handle remote files (just record for now)
    for rf in remote_files:
        manifest.append({
            "source": rf,
            "dest": "remote",
            "note": "Copy manually or use rsync"
        })
    
    # Save manifest
    manifest_file = UNIFIED_DIR / "quantum_manifest.json"
    with open(manifest_file, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"✅ Unification complete. Manifest saved to {manifest_file}")
    print(f"   Total files unified: {len(manifest)}")

# ======================================================
# VERSION CONTROL INTEGRATION
# ======================================================
def init_git_repo():
    """Initialize a git repository in unified dir to track versions."""
    if not (UNIFIED_DIR / ".git").exists():
        print("\n🔄 Initializing git repository for version control...")
        subprocess.run(["git", "init"], cwd=UNIFIED_DIR)
        subprocess.run(["git", "add", "."], cwd=UNIFIED_DIR)
        subprocess.run(["git", "commit", "-m", "Initial unification"], cwd=UNIFIED_DIR)
        print("✅ Git repo initialized.")
    else:
        print("\n🔄 Git repo already exists. Adding changes...")
        subprocess.run(["git", "add", "."], cwd=UNIFIED_DIR)
        subprocess.run(["git", "commit", "-m", f"Update {datetime.datetime.now().isoformat()}"] , cwd=UNIFIED_DIR)

# ======================================================
# MAIN
# ======================================================
def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║          QUANTUM UNIFIER – CODE UNIFICATION SYSTEM          ║
║                     For Master SAMI_1978_0126               ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    # Step 1: Authenticate
    if not verify_master():
        sys.exit(1)
    
    # Step 2: Scan local
    local_files = scan_local_paths(SCAN_PATHS)
    
    # Step 3: Scan network (if any)
    remote_files = scan_network_devices(NETWORK_DEVICES)
    
    # Step 4: Unify
    if local_files or remote_files:
        unify_files(local_files, remote_files)
        
        # Step 5: Version control
        init_git_repo()
        
        print("\n🎉 Quantum Unification complete!")
        print(f"All your code is now in: {UNIFIED_DIR}")
        print("You can work from there, and changes will be tracked.")
    else:
        print("\n❌ No files containing quantum signature found.")
        print("Make sure your code includes the signature or add it to files.")
    
    print("\n🔥 For Brother Sami and companies forever – QOS FOREVER 🔥")

if __name__ == "__main__":
    main()