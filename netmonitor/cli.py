import argparse
from netmonitor.checker import get_default_gateway, ping_host, check_dns

def main():
    args = parse_args()
        
    print("=" * 54)
    print("                NETWORK HEALTH MONITOR")
    print("=" * 54)
        
    #Default Gateway
    gateway = get_default_gateway()
    if gateway:
        print(f"[*] Default Gateway: {gateway}")
        gateway_result = ping_host(gateway, count=args.count)
        status = "OK" if gateway_result["online"] else "FAILED"
        rtt = f"{gateway_result['avg_rtt']}ms" if gateway_result["avg_rtt"] is not None else "N/A"
        print(
            f"    Status: {status} | Packet Loss: {gateway_result['packet_loss']}% | Avg RTT: {rtt}\n"
        )
    else:
        print("[!] Default gateway not found.\n")
            
    #DNS     
    print(f"[*] Testing DNS resolution ({args.dns_test})...")
    dns_result = check_dns(args.dns_test)
    
    if dns_result['resolved']:
        print(f"    Status: OK | Resolved IP: {dns_result['ip']}\n")
    else:
        print(f"    Status: FAILED | Error: {dns_result.get('error', 'Unknown')}\n")
            
    #External Connectivity
    print(f"[*] Testing external connectivity ({args.target})...")
    external_result = ping_host(args.target, count=args.count)
    external_status = "OK" if external_result["online"] else "FAILED"
    external_rtt = (
        f"{external_result['avg_rtt']}ms" if external_result["avg_rtt"] is not None else "N/A"
    )
    
    print(
        f"    Status: {external_status} | Packet Loss: {external_result['packet_loss']}% | Avg RTT: {external_rtt}"
    )
        
    print("=" * 54)

def parse_args():
    parser = argparse.ArgumentParser(description='Network Health Monitor - Connectivity Diagnostics')
    
    parser.add_argument('-t', '--target', type=str, default='8.8.8.8', 
                        help='External hostname or IP to test connectivity (default: 8.8.8.8).')
    
    parser.add_argument('-d', '--dns-test', type=str, default='google.com', 
                            help='Domain Name resolution test (default: google.com).')
    
    parser.add_argument('-c', '--count', type=int, default=4, 
                                help='Specify the number of ping packets. (default: 4).')
    
    return parser.parse_args()

if __name__ == '__main__':
    main()