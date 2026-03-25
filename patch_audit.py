import subprocess
import platform
from datetime import datetime
from pathlib import Path

SECURITY_KEYWORDS = [
    "openssl",
    "ssh",
    "kernel",
    "linux-image",
    "curl",
    "sudo",
    "gnutls",
    "systemd",
]


def run_command(command):
    """Run a shell command and return output."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, e.stderr.strip()


def detect_os():
    """Detect operating system."""
    return platform.platform()


def get_upgradable_packages():
    """Get list of upgradable packages."""
    print("Updating package list...")
    ok, _ = run_command(["apt", "update"])
    if not ok:
        return []

    ok, output = run_command(["apt", "list", "--upgradable"])
    if not ok:
        return []

    lines = output.splitlines()
    if len(lines) <= 1:
        return []

    return lines[1:]


def highlight_security_packages(packages):
    """Filter security-related packages."""
    flagged = []
    for pkg in packages:
        if any(keyword in pkg.lower() for keyword in SECURITY_KEYWORDS):
            flagged.append(pkg)
    return flagged


def write_report(packages, flagged):
    """Write audit report to file."""
    report_dir = Path("sample_reports")
    report_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = report_dir / f"patch_report_{timestamp}.txt"

    with open(report_path, "w") as f:
        f.write("Linux Patch Audit Report\n")
        f.write("=" * 40 + "\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write(f"System: {detect_os()}\n")
        f.write(f"Pending updates: {len(packages)}\n\n")

        f.write("All Upgradable Packages\n")
        f.write("-" * 40 + "\n")
        for pkg in packages:
            f.write(pkg + "\n")

        f.write("\nSecurity-Relevant Packages\n")
        f.write("-" * 40 + "\n")
        for pkg in flagged:
            f.write(pkg + "\n")

    return report_path


def main():
    print("Running Linux Patch Audit...\n")

    packages = get_upgradable_packages()
    flagged = highlight_security_packages(packages)
    report = write_report(packages, flagged)

    print("Audit Complete")
    print("System:", detect_os())
    print("Pending updates:", len(packages))
    print("Security packages:", len(flagged))
    print("Report saved to:", report)


if __name__ == "__main__":
    main()
