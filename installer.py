import os
import pickle
import subprocess
import time

CONFIG_FILE = "vxlan_tunel_files.txt"
VXLAN_SETUP_URL = "https://raw.githubusercontent.com/arenavak/vxlan/main/vxlan_setup.py"
PING_URL = "https://raw.githubusercontent.com/arenavak/vxlan/main/ping.py"

def get_main_interface():
    output = os.popen("ip route get 1.1.1.1").read()
    for part in output.split():
        if part == "dev":
            index = output.split().index(part)
            return output.split()[index + 1]
    return None

def save_interface_name(interface_name):
    with open(CONFIG_FILE, "wb") as f:
        pickle.dump(interface_name, f)
    print(f"[✔] Interface '{interface_name}' saved to {CONFIG_FILE}")

def download_files():
    print("[⬇] Downloading vxlan_setup.py and ping.py...")
    time.sleep(1)
    os.system(f"wget -O vxlan_setup.py {VXLAN_SETUP_URL}")
    print("[✔] vxlan_setup.py downloaded.")
    time.sleep(1)
    os.system(f"wget -O ping.py {PING_URL}")
    print("[✔] ping.py downloaded.")
    time.sleep(1)

def add_crontab_entry():
    cron_line = "@reboot python3 " + os.path.abspath("ping.py")
    current_cron = subprocess.getoutput("crontab -l 2>/dev/null")
    if cron_line not in current_cron:
        os.system(f'(crontab -l 2>/dev/null; echo "{cron_line}") | crontab -')
        print("[✔] Crontab entry added.")
    else:
        print("[ℹ] Crontab entry already exists.")

def run_vxlan_setup():
    print("[🚀] Launching vxlan_setup.py...")
    time.sleep(1)
    os.system("sudo python3 vxlan_setup.py")

def main():
    print("🔧 VXLAN Installer Starting...")
    print("Detecting main network interface...")
    time.sleep(1)

    interface = get_main_interface()
    if interface:
        print(f"[✔] Detected main interface: {interface}")
        time.sleep(1)
        print("Saving interface...")
        save_interface_name(interface)
    else:
        print("[✖] Could not detect network interface.")
        return

    print("\nPreparing to download required files...")
    time.sleep(1)
    download_files()

    print("\nSetting up auto-start on reboot...")
    time.sleep(1)
    add_crontab_entry()

    print("\nStarting VXLAN setup interface...")
    time.sleep(1)
    run_vxlan_setup()

if __name__ == "__main__":
    main()
    os.system("rm installer.py")
