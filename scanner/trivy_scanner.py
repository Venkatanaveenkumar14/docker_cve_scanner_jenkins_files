import subprocess
import json

def scan_docker_image(image_name: str, output_file: str = "scan_result.json"):
    cmd = [
        "trivy", "image",
        "--format", "json",
        "--severity", "CRITICAL",
        "--output", output_file,
        image_name
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"[+] Scan completed: {output_file}")
    except subprocess.CalledProcessError:
        print("[-] Trivy scan failed")

def scan_oss_dependencies(path: str, output_file: str = "dependency_scan.json"):
    cmd = [
        "trivy", "fs",
        "--format", "json",
        "--severity", "CRITICAL",
        "--output", output_file,
        path
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"[+] Dependency scan completed: {output_file}")
    except subprocess.CalledProcessError:
        print("[-] Dependency scan failed")