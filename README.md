
# 🛰️ VXLAN Tunnel Setup & Monitor

This project automates the creation and monitoring of **VXLAN tunnels** between an Iranian server and foreign servers . It ensures persistent connectivity using Python scripts that create VXLAN interfaces and automatically repair them if the connection drops.

---

## 📦 Download Installer

To get started, download the installer script:

```bash
wget https://raw.githubusercontent.com/arenavak/vxlan/main/installer.py
```

Once downloaded, run the installer:

```bash
sudo python3 installer.py
```

---

## ⚙️ Main Menu

After installation, if you want to access the main menu, run the following command:

```bash
python3 vxlan_setup.py
```

This will allow you to configure your VXLAN connections, including:
- Whether this is an **Iran** or **Kharej (foreign)** server
- The name of your network interface (e.g., `ens3`)
- The IP addresses of the peer servers

Your settings will be saved and used by the monitor script.

---

## 🌟 Advantages

- Automatically detects your active network interface and configures the tunnel on it
- Lets you view all currently active VXLAN tunnels
- Easily clear/remove any existing tunnel from the system
- **Most importantly:** Every 10 seconds, it pings the peer server through the tunnel. If the connection fails, **both sides automatically reset the tunnel**, ensuring a reliable and self-healing link

---



## 🛠️ Requirements

- Python 3
- `ip` and `ping` commands (usually available by default on most Linux distros)
- Root/sudo access

---

## 💸 Donations Welcome

If you'd like to support the project, feel free to donate:

**TRON / USDT (TRC-20):**

```
TFXSXuRAkNRNEKtWCNSXKjTWQQ2kTQy2Yu
```

Thanks for your support!

---
```

