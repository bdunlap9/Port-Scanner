# Advanced Port Scanner with Service Detection

This repository contains an advanced port scanner with service detection implemented in Python using `asyncio` and `nmap`. The port scanner concurrently scans a range of ports on a target IP address, and then detects the services running on the open ports.

## Requirements

To run the script, you need Python 3.7+ and the `python-nmap` library. You can install the library using pip:

```
pip install python-nmap
```

## Usage

1. Clone the repository:

```
git clone https://github.com/bdunlap9/Port-Scanner.git
```

2. Change the working directory:

```
cd Port-Scanner
```

3. Run the script:

```
python port_scanner.py <target_ip> <start_port> <end_port>
```

Replace `<target_ip>` with the target IP address, `<start_port>` with the start port number, and `<end_port>` with the end port number.

For example:

```
python port_scanner.py 192.168.1.1 1 65535
```

This command will scan the target IP address `192.168.1.1` for open ports in the range of 1 to 65535, and then it will detect the services running on the open ports.

## Example Output

The output will display the open ports and their corresponding services:

```
Scanning target: 192.168.1.1

Open Ports and Services:
80: http
443: https
22: ssh
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
