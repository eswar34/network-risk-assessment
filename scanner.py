import subprocess

def run_scan(target):
    subprocess.run(["nmap", "-F", target, "-oN", "scan.txt"], shell=True)

def get_open_ports():
    ports = []

    with open("scan.txt", "r") as file:
        for line in file:
            if "/tcp" in line and "open" in line:
                ports.append(line.strip())

    return ports
