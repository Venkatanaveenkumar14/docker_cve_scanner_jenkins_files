##  BLUF: Jenkins-Integrated Docker and OSS Vulnerability Scanner

This project implements a **Python-based module** that integrates with **Jenkins pipelines** to **automatically scan Docker images and open-source software (OSS) dependencies** for known vulnerabilities (CVEs) using **Trivy**, a lightweight and efficient security scanner. 

The system parses scan results and generates structured **HTML vulnerability reports** to streamline developer feedback and accelerate remediation efforts.

---

###  Capabilities

- **Docker Image Scanning:**  
  Identifies CVEs in Docker base images and layers.

- **File System / OSS Dependency Scanning:**  
  Detects vulnerable packages from dependency manifests like `requirements.txt`, `package-lock.json`, etc.

- **CI/CD Integration (Jenkins):**  
  Runs automatically during Jenkins pipeline builds to enforce security early in the SDLC.

- **HTML Report Generation:**  
  Converts JSON scan outputs into readable HTML reports for easy developer consumption and audit readiness.

---

###  Outcome

By embedding this scanner into the pipeline:
- **Manual effort is reduced**
- **Developer feedback is real-time**
- **Critical vulnerabilities are surfaced and remediated faster**
- **DevSecOps principles are enforced directly within CI/CD workflows**

This system hardens software delivery pipelines by automating vulnerability detection and promoting proactive remediation during development.
