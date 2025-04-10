# Docker and OSS CVE Scanner for Jenkins Pipelines

This project provides a Python-based module to automate the scanning of Docker images and open-source software (OSS) dependencies inside Jenkins CI/CD pipelines. It identifies and reports **CRITICAL CVEs**, enabling faster remediation by developers.

---

##  Features

- Scans Docker images for security vulnerabilities using **Trivy**
- Detects CRITICAL CVEs in local file system (OSS dependencies)
- Generates JSON reports and **professional HTML reports**
- Integrates directly with Jenkins pipelines via a provided `Jenkinsfile`
- Helps reduce remediation time by surfacing only high-risk issues

---

##  Project Structure

```
docker_cve_scanner/
├── scanner/
│   ├── trivy_scanner.py            # Trivy-based scanner for Docker and filesystem
│   ├── report_generator.py         # Parses Trivy JSON and summarizes CRITICAL CVEs
│   ├── html_report_generator.py    # Generates HTML vulnerability reports
│
├── jenkins/
│   └── Jenkinsfile                 # Jenkins pipeline definition
│
├── requirements.txt               # Python dependencies
├── run_scan.py                    # Main script to execute scanning and reporting
└── README.md
```

---

##  Prerequisites

- Python 3.x
- [Trivy](https://github.com/aquasecurity/trivy)
- Git and Jenkins (for pipeline automation)

Install Python dependencies:
```bash
pip install -r requirements.txt
```

Ensure Trivy is installed:
```bash
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin
```

---

##  How to Use

### 1. Update `run_scan.py`

Replace placeholders:
```python
docker_image = "your-image:latest"         # Replace with the image you want to scan
local_path = "."                            # Path to your codebase (for OSS scan)
```

### 2. Run the Scanner

```bash
python run_scan.py
```

### 3. Output Files

- `docker_scan.json` – Raw scan of Docker image
- `dep_scan.json` – Raw scan of OSS dependencies
- `docker_report.html` – HTML summary of Docker CVEs
- `dependency_report.html` – HTML summary of OSS CVEs

---

##  Jenkins Integration

The provided `Jenkinsfile` installs Trivy, sets up the Python environment, and runs the scan:

```groovy
pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Venkatanaveenkumar14/docker_cve_scanner_jenkins_files.git'
            }
        }

        stage('Install Trivy') {
            steps {
                sh 'curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin'
            }
        }

        stage('Run Security Scan') {
            steps {
                sh 'python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt'
                sh 'python run_scan.py'
            }
        }
    }
}
```

---

##  Purpose

This module is built for CI/CD pipelines to:
- Automate detection of CRITICAL vulnerabilities
- Reduce remediation time by notifying developers early
- Maintain secure Docker images and OSS libraries in production

---

##  Notes

- The HTML reports are designed to be viewed in a browser or stored as Jenkins build artifacts.
- Only CRITICAL severity issues are considered for focused remediation.

---

##  Status

- [x] Docker scan via Trivy
- [x] OSS dependency scan via Trivy filesystem scan
- [x] JSON and HTML reporting
- [x] Jenkins automation ready
