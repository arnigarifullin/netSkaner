from scan import start_scan
from report import show_report

main_results = []
main_net = ""
main_limit = 0

while True:
    print("\n NETWORK SCANNER PRO")
    print("1. Scan Network")
    print("2. Show Report")
    print("3. Exit")
    
    choice = input("Choice: ")
    
    if choice == "1":
        main_results, main_net, main_limit = start_scan()
    elif choice == "2":
        show_report(main_results, main_net, main_limit)
    elif choice == "3":
        print("Goodbye!")
        break 
    else:
        print("Invalid choice.")
