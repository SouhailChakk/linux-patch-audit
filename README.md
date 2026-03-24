# Linux Patch Audit

A lightweight patch auditing tool for Ubuntu/Debian systems that checks for pending package updates, highlights security-relevant packages, and generates a simple audit report.

## Features
- Detects pending package upgrades
- Exports results to a timestamped report
- Highlights potentially security-related packages
- Includes both Python and Bash implementations

## Why I Built This
I built this project to practice basic SRE-style infrastructure hygiene tasks such as patch auditing, system maintenance, and repeatable reporting.

## Tech Stack
- Python
- Bash
- apt
- Linux

## How to Run
python3 patch_audit.py
