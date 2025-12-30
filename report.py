def show_report(results_list, net_ip, limit):
    print("\n--- FINAL REPORT ---")
    
    if not results_list:
        print(" No data. Please run 'Scan' first.")
        return

    alive = len(results_list)
    dead = limit - alive
    
    print(f"Network:      {net_ip}.0")
    print(f"Total Hosts:  {limit}")
    print(f"Alive:        {alive}")
    print(f"Dead:         {dead}")
    
    print("\n[ ALIVE HOSTS LIST ]")
    
    results_list.sort()
    
    for num, ip, name, duration in results_list:
        print(f" -> {ip:<15} : {name} | {duration:.0f} ms")