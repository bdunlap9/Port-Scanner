import socket
import argparse
import nmap


class AdvancedPortScanner:
    def __init__(self, target_ip, start_port, end_port):
        self.target_ip = target_ip
        self.start_port = start_port
        self.end_port = end_port

    def scan_ports(self):
        open_ports = []

        for port in range(self.start_port, self.end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target_ip, port))
            if result == 0:
                open_ports.append(port)
            sock.close()

        return open_ports

    def detect_services(self, open_ports):
        nm = nmap.PortScanner()
        services = {}

        for port in open_ports:
            try:
                result = nm.scan(self.target_ip, str(port))
                service = result['scan'][self.target_ip]['tcp'][port]['name']
                services[port] = service
            except KeyError:
                services[port] = 'unknown'

        return services


def main():
    parser = argparse.ArgumentParser(description="Advanced Port Scanner with Service Detection")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("start_port", type=int, help="Start port number")
    parser.add_argument("end_port", type=int, help="End port number")
    args = parser.parse_args()

    target_ip = args.target_ip
    start_port = args.start_port
    end_port = args.end_port

    print(f"Scanning target: {target_ip}")

    scanner = AdvancedPortScanner(target_ip, start_port, end_port)
    open_ports = scanner.scan_ports()
    services = scanner.detect_services(open_ports)

    print("\nOpen Ports and Services:")
    for port, service in services.items():
        print(f"{port}: {service}")


if __name__ == "__main__":
    main()
