#!/bin/bash

REPORT_DIR="sample_reports"
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S")
REPORT_FILE="$REPORT_DIR/report_$TIMESTAMP.txt"

mkdir -p "$REPORT_DIR"

echo "Running apt update..."
apt update >/dev/null 2>&1

echo "Linux Patch Audit Report" > "$REPORT_FILE"
echo "========================================" >> "$REPORT_FILE"
echo "Generated: $(date)" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"

echo "All Upgradable Packages" >> "$REPORT_FILE"
echo "----------------------------------------" >> "$REPORT_FILE"
apt list --upgradable 2>/dev/null >> "$REPORT_FILE"

echo "" >> "$REPORT_FILE"
echo "Security-Relevant Packages" >> "$REPORT_FILE"
echo "----------------------------------------" >> "$REPORT_FILE"
apt list --upgradable 2>/dev/null | grep -Ei "openssl|ssh|kernel|linux-image|curl|sudo|gnutls|systemd" >> "$REPORT_FILE"

echo "Report saved to $REPORT_FILE"
