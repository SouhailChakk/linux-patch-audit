# Linux Patch Audit

A lightweight Linux patch auditing tool written in Python and Bash that checks for pending package updates, identifies security-relevant patches, and generates an audit report.  
This project simulates basic system maintenance and patch management tasks typically performed in SRE, SOC, and system administration roles.

---

## Project Overview

Keeping systems updated is a critical security and reliability task. This tool automates the process of:

- Checking for pending updates
- Identifying security-related packages
- Generating a patch audit report
- Providing both Python and Bash implementations

This project demonstrates automation, Linux system management, and basic security auditing practices.

---

## Features

- Detects pending package upgrades
- Highlights security-relevant packages (openssl, ssh, kernel, sudo, etc.)
- Generates timestamped audit reports
- Works on Ubuntu/Debian systems
- Available in both Python and Bash versions

---

## Tech Stack

- Python
- Bash
- Linux (Ubuntu/Debian)
- apt package manager

---

## Project Structure
linux-patch-audit/
│
├── patch_audit.py # Python version of the patch audit tool
├── patch_audit.sh # Bash version of the patch audit tool
├── sample_reports/
│ └── report_example.txt
└── README.md


---

## How to Run

### Python Version
python3 patch_audit.py
