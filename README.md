

---

# 🛰️ VXLAN Tunnel Setup & Monitor

This project automates the creation and monitoring of **VXLAN tunnels** between an Iranian server and foreign servers. It ensures persistent connectivity using Python scripts that create VXLAN interfaces and automatically repair them if the connection drops.

---

## 🌐 What Is This Tunnel?

This script sets up a **VXLAN (Virtual Extensible LAN)** tunnel between two servers—typically one in **Iran** and one **abroad**. A VXLAN tunnel acts like a virtual network cable that links two machines on different networks, as if they were side by side on the same LAN.

* It adds a **virtual network interface** to your system (e.g., `vxlan100`).
* You choose a **subnet number** (like `100`, `101`, etc.).
* The **VXLAN ID** will be exactly the same as the subnet number you enter.
* The tunnel assigns:

  * **Iran Server**: `192.168.<your_subnet>.1`
  * **Foreign Server**: `192.168.<your_subnet>.2`
* This allows you to **ping each server from the other** using local IPs across a secure VXLAN tunnel.
* You can create **up to 256 separate tunnels**, each with its own VXLAN ID and subnet, ideal for managing multiple services in parallel.

This setup is **perfect for X-UI / 3X-UI** installations, allowing internal API calls or management ports to connect securely without exposing services publicly.

---

## 📦 Download Installer

To get started, download the installer script:

```bash
wget https://raw.githubusercontent.com/arenavak/vxlan/main/installer.py
```

Then run the installer:

```bash
sudo python3 installer.py
```

---

## ⚙️ Main Menu

After installation, run the configuration menu with:

```bash
python3 vxlan_setup.py
```

From there you can:

* Select whether this is an **Iran** or **Foreign (Kharej)** server
* Enter the IP address of the **peer server**
* Choose a **VXLAN port** (optional — default is 4789)
* Choose a **subnet number**, which also becomes your **VXLAN ID**

> 🛑 **Note:** You can now set a custom VXLAN port.
> The default port is `4789`, but it's **recommended to use ports above `10000` and below `65535`** to avoid conflicts and improve compatibility with firewalls.

---

## 🔄 Auto-Monitoring

* Every **10 seconds**, the `ping.py` script checks the tunnel's health.
* If the tunnel goes down, it **automatically resets the VXLAN connection** on that specific pair.
* This ensures high availability and automatic healing of your tunnel.

---

## 🌟 Advantages

* Automatically detects your main network interface
* Fully automated setup—no manual configuration
* Create and maintain **multiple VXLAN tunnels**
* Automatically repairs tunnels on disconnection
* Easily view or remove active tunnels
* **Secure internal networking** for services like X-UI / 3X-UI

---

## 🛠️ Requirements

* Python 3
* `ip` and `ping` commands (default in most Linux distros)
* Root/sudo access

---

## 💸 Donations Welcome

If you'd like to support the project, feel free to donate:

**TRON / USDT (TRC-20):**

```
TFXSXuRAkNRNEKtWCNSXKjTWQQ2kTQy2Yu
```

Thank you for your support! ❤️

---

