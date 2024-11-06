import nmap
import nvdlib

#Get IP Address
def host_ip():
        target = input("Enter the IP address to be scanned: ")
        attempt = 1
        while attempt <= 3:
                if valid_ip(target):
                        return target
                        break
                else:
                        target = input("IP address is invalid. Enter correct address(Example: 192.162.1.1): ")
                        attempt+=1
        if attempt < 3:
                return 0
		
#Validate IP address
def valid_ip(t_ip):
    parts = t_ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        try:
            number = int(part)
            if number < 0 or number > 255:
                return False
        except ValueError:
            return False
    return True
    
#Scan
def scan_host(ip_addr):
        scan = nmap.PortScanner()
        scan.scan(ip_addr)
        service = []
        ports = []
        status = ''
        n=0
        try:
                scan[ip_addr].state()
        except KeyError:
                status = 'down'
        else:
                for host in scan.all_hosts():
                        print('Host: {}'.format(host))
                        print('State: {}'.format(scan[host].state()))
                        print('Protocol: {}'.format(scan[host].all_protocols()))
                        for proto in scan[host].all_protocols():
                                print('No - Port - Service')
                                for port in scan[host][proto]:
                                        n=n+1
                                        print('{}  - Port:{} - {}'.format(n, port, scan[host][proto][port]['name']))
                                        s = scan[host][proto][port]['name']
                                        service.append(s)
                                        ports.append(port)
                status = scan[host].state()
        finally:
                return status, service, ports

#Initiating scan
def init_vulb_scan(service, ports):
        cont = True
        l = len(service)
        print("Number of Services found: ", l)
        option = int(input("Select the service to be scanned for vulnerability(Enter number between 1 - {}): ".format(l)))
        attempt = 1
        while cont:
                if option <= l and option != 0:
                        index = option-1
                        key1 = service[index]
                        key2 = str(ports[index])
                        print("Vulnerability Scanning is in process for the service {} on port {}".format(key1,key2))
                        vulb_scan(key1, key2)
                        c = input("Do you want to scan another service(Y/N): ")
                        if c == 'Y' or c == 'y' or c == 'Yes' or c == 'yes':
                                option = int(input("Select Service: "))
                                cont = True
                        else:
                                cont = False
                elif attempt <= 3:
                        option = int(input('Select number between 1 - {}: '.format(l)))
                        cont = True
                        attempt = attempt + 1
                else:
                        print("Attempts Exceeded! Vulnerability Scan Terminated!!")
                        cont = False


#Vulnerability Scanning
def vulb_scan(key1, key2):
        try:
                key = key1+' '+key2
                result = nvdlib.searchCVE(keywordSearch=key, limit = 5)
        except:
                print("Check Internet Connection")
        else:
                if result == []:
                        print("No vulnerabilities Found")
                else:
                        print("!!Vulnerability Found!!")
                        for r in result:
                                vulb_rep(r)
        return 0
        
	
#Report
def vulb_rep(result):
        
        print("------------------------------------------------------")
        print("ID - ", result.id)
        print("Published - ", result.published)
        print("Descriptions - ", result.descriptions[0].value)
        print("Score - ", result.score)
        print("URL - ", result.url)
        print("------------------------------------------------------")
        return 0


t = host_ip() #function to get ip address
if t != 0:
        print("Scanning Host ", t)
        status, service, ports = scan_host(t)
        if service == [] and status == 'down':
                print("Host is down! Try Again.")
        elif service == [] and status == 'up':
                print("Scan Blocked")
        else:
                init_vulb_scan(service, ports)
else:
        print("Invalid! Scan cancelled.")
