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
2. **Install Dependencies**:
   pip install python-nmap nvdlib
3. **Ensure Nmap is Installed**:
   On Windows: Install Nmap from the official website and add it to your system PATH.
   On Linux/Mac: Install via package manager (e.g., sudo apt install nmap for Ubuntu).

## 🖥️ Usage
1. **Run the scanner**:
   python nscanner.py
2. **Follow the CLI prompts**:
   Enter a target IP address (e.g., 192.168.1.1).
   Specify a port range (e.g., 1-1000) or leave blank for default.
3. **View the results**:
   Port scan results display open ports, services, and OS details.
   Vulnerability scan results list CVEs with severity and descriptions.
   **Example**:
   $ python nscanner.py
   Enter target IP: 192.168.1.1
   Enter port range (e.g., 1-1000): 1-100
   Scan type (TCP/UDP): TCP
   [2025-05-10 10:15:23] Scanning 192.168.1.1...
   [+] Open Port: 80 (http)
   [+] CVE-2023-12345: Medium severity (Apache 2.4.x vulnerability)

## 📝 Example Output
   NScanNer Report - 2025-05-10 10:15:23
   Target: 192.168.1.1
   Port Range: 1-100
   Scan Type: TCP
   [+] Port 80: http (Apache/2.4.29)
   [+] Port 443: https
   Vulnerabilities:
   - CVE-2023-12345: Medium (CVSS: 5.3) - Apache misconfiguration

## 🛡️ Limitations
   Requires root/admin privileges for certain nmap scans (e.g., OS detection).
   NVD queries depend on internet connectivity and API availability.
   Not intended for unauthorized scanning—always obtain permission before scanning networks.

## 🔮 Future Improvements
   Add GUI support for a more accessible interface.
   Implement multithreading for faster scans.
   Integrate additional vulnerability databases (e.g., VulnDB).
   Export reports in JSON or CSV formats.

## 🤝 Contributing
   Contributions are welcome! Feel free to:
      Submit bug reports or feature requests via Issues.
      Fork the repo, make improvements, and submit a pull request.
      Suggested enhancements: better error handling, new scan types, or report formats.

## 📫 Contact
   Author: Nal (@Nal19)
   Email: nalthehcaker@gmail.com
   GitHub: Nal19
