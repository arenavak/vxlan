🛰️ VXLAN Tunnel Setup & Monitor
This project helps you automate VXLAN tunnel creation and monitoring between an Iranian server and foreign servers (like Armenia, France, Germany). It uses Python to set up VXLAN interfaces and ensure persistent connectivity using ping checks and auto-repair logic.

📦 Installation
Clone or download the required scripts directly:


wget https://raw.githubusercontent.com/arenavak/vxlan/main/vxlan_setup.py
wget https://raw.githubusercontent.com/arenavak/vxlan/main/ping.py
⚙️ Setup
Run the setup script to configure VXLAN connections:


sudo python3 vxlan_setup.py
You will be asked:

Whether the server is Iran or Kharej (foreign)

The network interface name (e.g., ens3)

Remote IPs of the other servers

This script saves your configuration for use by the monitor script.

🔁 Auto-Restart on Reboot
To make sure VXLAN tunnels are checked and re-established on reboot, add ping.py to crontab:


(crontab -l 2>/dev/null; echo "@reboot /usr/bin/python3 /full/path/to/ping.py") | crontab -
Replace /full/path/to/ping.py with the actual path on your system.

▶️ Run Monitor Script Manually
You can also manually run the monitor script:


sudo python3 ping.py
It will continuously ping your VXLAN peers and reinitialize any tunnel that goes down.

