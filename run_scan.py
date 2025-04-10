from scanner.trivy_scanner import scan_docker_image, scan_oss_dependencies
from scanner.report_generator import parse_report, print_summary
from scanner.html_report_generator import generate_html_report

if __name__ == "__main__":
    docker_image = "myscanner:1.0"
    local_path = "."  # Codebase root

    # Scan docker image
    scan_docker_image(docker_image, "docker_scan.json")
    docker_vulns = parse_report("docker_scan.json")
    
    # Scan OSS dependencies
    scan_oss_dependencies(local_path, "dep_scan.json")
    dep_vulns = parse_report("dep_scan.json")

    print("\nDocker Image Vulnerabilities:")
    print_summary(docker_vulns)

    print("\nDependency Vulnerabilities:")
    print_summary(dep_vulns)

# Generate HTML reports
generate_html_report("docker_scan.json", "docker_report.html")
generate_html_report("dep_scan.json", "dependency_report.html")