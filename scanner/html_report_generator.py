import json
from datetime import datetime

def generate_html_report(json_path: str, html_output_path: str):
    with open(json_path, "r") as f:
        data = json.load(f)

    report_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Security Vulnerability Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f7f7f7;
            color: #333;
            padding: 20px;
        }}
        h1 {{
            color: #c0392b;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}
        th, td {{
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #e74c3c;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h1>Security Vulnerability Report</h1>
    <p><strong>Scan Date:</strong> {report_time}</p>
    <table>
        <thead>
            <tr>
                <th>Target</th>
                <th>Package</th>
                <th>Vuln ID</th>
                <th>Severity</th>
                <th>Installed</th>
                <th>Fixed</th>
                <th>Description</th>
            </tr>
        </thead>
        <tbody>
    """

    for target in data.get("Results", []):
        for vuln in target.get("Vulnerabilities", []):
            html += f"""
            <tr>
                <td>{target.get("Target")}</td>
                <td>{vuln.get("PkgName")}</td>
                <td>{vuln.get("VulnerabilityID")}</td>
                <td>{vuln.get("Severity")}</td>
                <td>{vuln.get("InstalledVersion")}</td>
                <td>{vuln.get("FixedVersion") or "N/A"}</td>
                <td>{vuln.get("Description", "")[:120]}...</td>
            </tr>
            """

    html += """
        </tbody>
    </table>
</body>
</html>
"""

    with open(html_output_path, "w") as f:
        f.write(html)

    print(f"[+] HTML report generated: {html_output_path}")