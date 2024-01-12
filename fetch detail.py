import psutil
import platform
import speedtest
import socket
import wmi
from screeninfo import get_monitors


def get_installed_software():
    installed_software = [program.name for program in psutil.process_iter(['pid', 'name'])]
    return installed_software

def get_internet_speed():
    try:
        st = speedtest.Speedtest()
        download_speed = st.download()
        upload_speed = st.upload()
        return download_speed, upload_speed
    except Exception as e:
        return f"Error measuring internet speed: {e}"


def get_screen_resolution():
    try:
        from win32api import GetSystemMetrics
        width = GetSystemMetrics(0)
        height = GetSystemMetrics(1)
        return f"{width}x{height}"
    except ImportError:
        return "Unable to get screen resolution on non-Windows systems"

def get_cpu_info():
    cpu_info = platform.processor()
    return cpu_info

def get_cpu_cores_threads():
    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)
    return cores, threads

def get_gpu_info():
    try:
        w = wmi.WMI()
        gpu_info = w.Win32_VideoController()[0].Name
        return gpu_info
    except Exception as e:
        return f"Unable to get GPU information: {e}"

def get_ram_size():
    ram_size = psutil.virtual_memory().total / (1024**3)
    return round(ram_size, 2)

def get_screen_size():
    monitors = get_monitors()
    
    if monitors:
        primary_monitor = monitors[0]
        width, height = primary_monitor.width, primary_monitor.height
        return f"{width}x{height} pixels"
    else:
        return "Screen size information not available."


import uuid

def get_mac_address():
    mac_address = ':'.join(['{:02x}'.format((int(hex(uuid.getnode())[2:][i:i+2], 16)) & 0xff) for i in range(0, 11, 2)])
    return mac_address



def get_public_ip():
    public_ip = socket.gethostbyname(socket.gethostname())
    return public_ip

def get_windows_version():
    windows_version = platform.version()
    return windows_version

if __name__ == "__main__":
    print("1. Installed Software:", get_installed_software())
    internet_speed = get_internet_speed()
    print(f"2. Internet Speed: Download - {internet_speed[0]} bps, Upload - {internet_speed[1]} bps")
    print("3. Screen Resolution:", get_screen_resolution())
    print("4. CPU Model:", get_cpu_info())
    cores, threads = get_cpu_cores_threads()
    print(f"5. Number of Cores: {cores}, Number of Threads: {threads}")
    print("6. GPU Model:", get_gpu_info())
    print("7. RAM Size:", get_ram_size(), "GB")
    print("8. Screen Size:", get_screen_size())
    print("9. MAC Address:", get_mac_address())
    print("10. Public IP Address:", get_public_ip())
    print("11. Windows Version:", get_windows_version())
