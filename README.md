# NScanNer

**NScanNer** is a Python-based network vulnerability scanner designed to identify open ports, services, and potential vulnerabilities on target hosts. Built with `nmap` for port scanning and `nvdlib` for querying the National Vulnerability Database (NVD), it offers a user-friendly CLI interface with IP validation and detailed scan reports. Perfect for cybersecurity enthusiasts and ethical hackers learning network security.

## 🌟 Features
- **IP Validation**: Ensures valid IPv4 addresses before scanning.
- **Port Scanning**: Uses `nmap` to detect open ports, services, and operating systems.
- **Vulnerability Analysis**: Queries NVD for known vulnerabilities associated with detected services.
- **Customizable Scans**: Supports user-defined port ranges and scan types (e.g., TCP, UDP).
- **Detailed Reports**: Outputs scan results with timestamps and vulnerability details in a clear format.
- **Error Handling**: Provides user-friendly error messages for invalid inputs or failed scans.

## 🛠️ Technologies Used
- **Python 3.x**: Core programming language.
- **nmap**: For port and service scanning.
- **nvdlib**: For querying NVD’s CVE database.
- **OS & Time Libraries**: For system integration and timestamped reports.

## 📋 Prerequisites
- Python 3.6 or higher
- Nmap installed on your system ([Download Nmap](https://nmap.org/download.html))
- Required Python libraries: `python-nmap`, `nvdlib`

## 🚀 Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Nal19/NScanNer.git
   cd NScanNer
