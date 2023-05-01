import argparse, nmap, asyncio

class AdvancedPortScanner:
    def __init__(self, target_ip, start_port, end_port):
        self.target_ip = target_ip
        self.start_port = start_port
        self.end_port = end_port

    async def scan_port(self, port):
        open_port = None
        conn = asyncio.open_connection(self.target_ip, port)
        _, writer = await asyncio.wait_for(conn, timeout=1, return_when=asyncio.FIRST_COMPLETED)
        
        if writer:
            open_port = port
            writer.close()
            await writer.wait_closed()
        return open_port

    async def scan_ports(self):
        open_ports = []
        port_scan_tasks = [self.scan_port(port) for port in range(self.start_port, self.end_port + 1)]

        for task in asyncio.as_completed(port_scan_tasks):
            try:
                open_port = await task
                if open_port is not None:
                    open_ports.append(open_port)
            except:
                pass

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

async def main():
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
    open_ports = await scanner.scan_ports()
    services = scanner.detect_services(open_ports)

    print("\nOpen Ports and Services:")
    for port, service in services.items():
        print(f"{port}: {service}")

if __name__ == "__main__":
    asyncio.run(main())
