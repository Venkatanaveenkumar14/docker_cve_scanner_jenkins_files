import json

def parse_report(report_path: str):
    with open(report_path, "r") as f:
        data = json.load(f)
    
    critical_vulns = []

    for target in data.get("Results", []):
        for vuln in target.get("Vulnerabilities", []):
            critical_vulns.append({
                "Target": target["Target"],
                "PkgName": vuln.get("PkgName"),
                "VulnerabilityID": vuln.get("VulnerabilityID"),
                "Severity": vuln.get("Severity"),
                "InstalledVersion": vuln.get("InstalledVersion"),
                "FixedVersion": vuln.get("FixedVersion"),
                "Description": vuln.get("Description", "")[:100]
            })
    return critical_vulns

def print_summary(vulns):
    print(f"\n[!] Found {len(vulns)} CRITICAL vulnerabilities.")
    for v in vulns:
        print(f"- {v['Target']} | {v['PkgName']} | {v['VulnerabilityID']} | {v['InstalledVersion']} -> {v['FixedVersion']}")