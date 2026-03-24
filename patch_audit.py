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


def run_command(command: list[str]) -> tuple[bool, str]:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return False, (e.stdout + "\n" + e.stderr).strip()
    except FileNotFoundError:
        return False, f"Command not found: {' '.join(command)}"


def detect_os() -> str:
    return platform.platform()


def get_upgradable_packages() -> list[str]:
    ok, _ = run_command(["apt", "update"])
    if not ok:
        return ["ERROR: Failed to run apt update"]

    ok, output = run_command(["apt", "list", "--upgradable"])
    if not ok:
        return ["ERROR: Failed to list upgradable packages"]

    lines = [line.strip() for line in output.splitlines() if line.strip()]
    if len(lines) <= 1:
        return []

    return lines[1:]


def highlight_security_packages(packages: list[str]) -> list[str]:
    flagged = []
    for pkg in packages:
        lower_pkg = pkg.lower()
        if any(keyword in lower_pkg for keyword in SECURITY_KEYWORDS):
            flagged.append(pkg)
    return flagged


def write_report(packages: list[str], flagged: list[str]) -> Path:
    report_dir = Path("sample_reports")
    report_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_path = report_dir / f"patch_report_{timestamp}.txt"

    with report_path.open("w", encoding="utf-8") as f:
        f.write("Linux Patch Audit Report\n")
        f.write("=" * 40 + "\n")
        f.write(f"Generated: {datetime.now()}\n")
        f.write(f"System: {detect_os()}\n")
        f.write(f"Pending updates: {len(packages)}\n\n")

        f.write("All Upgradable Packages\n")
        f.write("-" * 40 + "\n")
        if packages:
            for pkg in packages:
                f.write(pkg + "\n")
        else:
            f.write("No pending updates found.\n")

        f.write("\nSecurity-Relevant Packages\n")
        f.write("-" * 40 + "\n")
        if flagged:
            for pkg in flagged:
                f.write(pkg + "\n")
        else:
            f.write("No obvious security-relevant packages flagged.\n")

    return report_path


def main() -> None:
    print("Running Linux patch audit...\n")
    packages = get_upgradable_packages()

    if packages and packages[0].startswith("ERROR:"):
        print(packages[0])
        return

    flagged = highlight_security_packages(packages)
    report_path = write_report(packages, flagged)

    print(f"System: {detect_os()}")
    print(f"Pending updates found: {len(packages)}")
    print(f"Security-relevant packages flagged: {len(flagged)}")
    print(f"Report saved to: {report_path}")


if __name__ == "__main__":
    main()
