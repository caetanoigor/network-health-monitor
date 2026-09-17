import subprocess
import re
import socket

def get_default_gateway():
    try:
        result = subprocess.run(
            ['ip', 'route', 'show', 'default'],
            capture_output=True,
            text=True,
            check=True
        )	
        
        match = re.search(r"default via ([0-9]+(?:\.[0-9]+){3})", result.stdout)
        if match:
            return match.group(1)
        return None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None

def ping_host(host, count=3, timeout=2):
    try:
        cmd = ["ping", "-c", str(count), "-W", str(timeout), host]
        result = subprocess.run(cmd, capture_output=True, text=True)

        loss_match = re.search(r"(\d+)% packet loss", result.stdout)
        packet_loss = float(loss_match.group(1)) if loss_match else 100.0

        rtt_match = re.search(r"rtt min/avg/max/mdev = [\d\.]+/([\d\.]+)/", result.stdout)
        avg_rtt = float(rtt_match.group(1)) if rtt_match else None

        return {
            "online": result.returncode == 0,
            "packet_loss": packet_loss,
            "avg_rtt": avg_rtt
        }
    except (subprocess.SubprocessError, OSError):
        return {
            "online": False,
            "packet_loss": 100.0,
            "avg_rtt": None 
        }

def check_dns(host="google.com"):
    try:
        socket.setdefaulttimeout(3)
        ip_founded = socket.gethostbyname(host)
        return {
            "resolved" : True,
            "ip" : ip_founded
        }
    
    except (socket.gaierror, socket.timeout):
        return {
            "resolved" : False,
            "ip" : None 
        } 

if __name__ == "__main__":
    gateway = get_default_gateway()
    print(f"Default Gateway: {gateway}")
    print(" ")

    if gateway:
        result_gateway = ping_host(gateway)
        rtt = f"{result_gateway['avg_rtt']}ms" if result_gateway['avg_rtt'] is not None else "N/A"
        print(f"Gateway Status: online={result_gateway['online']} ; loss={result_gateway['packet_loss']}% ; avg_rtt={rtt}\n")

    result_dns = check_dns()
    print(f"DNS Resolution: resolved={result_dns['resolved']} ; ip={result_dns['ip']}") 
