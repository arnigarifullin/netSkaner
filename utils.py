import socket
import platform

def get_os_platform():
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    return param

def get_hostname(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"
