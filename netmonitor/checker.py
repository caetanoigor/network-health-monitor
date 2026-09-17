import subprocess
import re

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
    except Exception:
        return {
            "online": False,
            "packet_loss": 100.0,
            "avg_rtt": None 
        }

if __name__ == "__main__":
    gateway = get_default_gateway()
    print(f"Gateway Padrão: {gateway}")

    if gateway:
        resultado = ping_host(gateway)
        print("Status Gateway:")
        for valor in resultado:
            if valor == 'avg_rtt':
                print(f'{valor}: {resultado[valor]}ms', end=' ')
            else:
                print(f'{valor}: {resultado[valor]} ; ', end=' ')
        print()
        