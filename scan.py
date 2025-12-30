import subprocess
import concurrent.futures
import time
from utils import get_os_platform, get_hostname

def ping_ip(ip):
    start_time = time.perf_counter()
    try:

        flag = get_os_platform() 
        
        result = subprocess.run(
            ["ping", flag, "1", ip],
            capture_output=True,
            text=True,
            timeout=0.5
        )
        end_time = time.perf_counter()
        duration = (end_time - start_time) * 1000

        if result.returncode == 0:
            return True, duration
        else:
            return False, 0
    except:
        return False, 0

def start_scan():
    network_ip = input("Enter network : ")
    try:
        range_limit = int(input("Enter range (: "))
    except:
        print("Error: number needed")
        return [], "", 0 

    results = []
    print(f"\n Scanning {network_ip}.1 to {network_ip}.{range_limit} ...")

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_ip = {}
        
        for i in range(1, range_limit + 1):
            ip = f"{network_ip}.{i}"
            future = executor.submit(ping_ip, ip)    
            future_to_ip[future] = ip
        
        for future in concurrent.futures.as_completed(future_to_ip):
            ip = future_to_ip[future]
            is_alive, duration = future.result()
            
            if is_alive:
                name = get_hostname(ip)
                print(f"[+] {ip:<15} | {name} | {duration:.0f} ms")
                
                last_num = int(ip.split('.')[-1])
  
                results.append((last_num, ip, name, duration))

    print("\n Scan Complete!")
    

    return results, network_ip, range_limit