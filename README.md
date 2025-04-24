# 🛰️ VXLAN Tunnel Setup & Monitor

This project automates the creation and monitoring of **VXLAN tunnels** between an Iranian server and foreign servers (such as Armenia, France, and Germany). It ensures persistent connectivity using Python scripts that create VXLAN interfaces and automatically repair them if the connection drops.

---

## 📦 Download Scripts

Use the following commands to download the necessary scripts:

```bash
wget https://raw.githubusercontent.com/arenavak/vxlan/main/vxlan_setup.py
wget https://raw.githubusercontent.com/arenavak/vxlan/main/ping.py
```

---

## ⚙️ Initial Setup

Run the setup script to configure your VXLAN connections:

```bash
sudo python3 vxlan_setup.py
```

You will be asked:
- Whether this is an **Iran** or **Kharej (foreign)** server
- The name of your network interface (e.g., `ens3`)
- The IP addresses of the peer servers

This will save your settings for use by the monitor script.

---

## 🔁 Run on Boot (Auto-Reconnect)

To make sure `ping.py` runs automatically on system reboot, add it to your crontab with:

```bash
(crontab -l 2>/dev/null; echo "@reboot /usr/bin/python3 /full/path/to/ping.py") | crontab -
```

> Replace `/full/path/to/ping.py` with the **actual full path** of the script.

---

## ▶️ Run the Monitor Script Manually

You can also manually launch the tunnel monitor anytime:

```bash
sudo python3 ping.py
```

This script pings all VXLAN peers and will automatically restart any tunnel that goes down.

---

## 🛠️ Requirements

- Python 3
- `ip` and `ping` commands (usually available by default on most Linux distros)
- Root/sudo access

---

