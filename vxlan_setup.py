import os
import time
import pickle

# tunel structure  : [status],[subnet],[ip iran],[ip kharej],[port]
# status : iran or kharej 
# subnet : 192.168.{subnet},0/30


def clear():
    os.system("clear")

def tunels_printer(tunels):
    for i in tunels:
        print(f"status : {i[0]} , subnet : 192.168.{i[1]}.0/30 , ip Iran : {i[2]} , ip kharej : {i[3]}, port : {i[4]}")

def ping_host(host):
    """Ping a host and return True if it's reachable, False otherwise."""
    response = os.system(f"ping -c 3 {host} > /dev/null 2>&1")
    return response == 0

def ask_tunel(tunels, status):
    tunel = []
    ip_iran = str(input("enter iran ip : "))
    ip_kharej = str(input("enter kharej ip : "))
    port = str(input("enter tunnel port (default 4789 if unsure): "))
    if port == "":
        print("default port has been set port : 4789")
        port = "4789"
    subnet = str(input("enter tunels subnet (ex : for 192.168.100.1 enter 100) : "))
    tunel.append(status)
    tunel.append(subnet)
    tunel.append(ip_iran)
    tunel.append(ip_kharej)
    tunel.append(port)
    tunels.append(tunel)
    with open("tunels.txt", "wb") as file:
        pickle.dump(tunels, file)
    return tunel

def set_tunel(tunel, main_interface):
    subnet = tunel[1]
    port = tunel[4]
    if tunel[0] == "iran":
        tunel_to = tunel[3]
        local_ip = "1"
        local_tunel_ip = "2"
    elif tunel[0] == "kharej":
        tunel_to = tunel[2]
        local_ip = "2"
        local_tunel_ip = "1"

    text = f"""
    ip link add vxlan{subnet} type vxlan id {subnet} dev {main_interface} remote {tunel_to} dstport {port}
    ip addr add 192.168.{subnet}.{local_ip}/30 dev vxlan{subnet}
    ip link set vxlan{subnet} up
    """

    os.system(text)

    while not ping_host(f"192.168.{subnet}.{local_tunel_ip}"):
        print("tunel not set yet waiting for the other server to connect ")
        time.sleep(1)
    print("tunel has been setup successfully ✅")

def clear_tunels(tunels):
    for tunel in tunels:
        text = f"ip link del vxlan{tunel[1]} 2>/dev/null"
        os.system(text)
        print(f"vxlan{tunel[1]} has been deleted")
    tunels.clear()
    with open("tunels.txt", "wb") as file:
        pickle.dump(tunels, file)

def clear_tunel(tunels):
    tunels_printer(tunels)
    tunel = str(input("enter tunels subnet to be deleted\n : "))
    flag = 0
    for i in tunels:
        if i[1] == tunel:
            flag = 1
            text = f"ip link del vxlan{tunel} 2>/dev/null"
            os.system(text)
            tunels.remove(i)
            with open("tunels.txt", "wb") as file:
                pickle.dump(tunels, file)

    if flag == 0:
        print("theres no such a tunel !!!")



tunels = []

try:
    with open("tunels.txt", "rb") as file:
        tunels = pickle.load(file)
except:
    with open("tunels.txt", "wb") as file:
        pickle.dump(tunels, file)

with open("vxlan_tunel_files.txt", "rb") as file:
    main_interface = pickle.load(file)
main_interface = str(main_interface)

clear()
while True:
    print("\033[1;32m" + """
##################################################
#                                                #
#           VXLAN TUNNEL SETUP SCRIPT FOR LINUX  #
#                                                #
##################################################
""" + "\033[0m")

    menu1 = str(input("welcome to vxlan tunel setup\n\n1)set tunel for iran server\n2)set tunel for kharej server (can add multiple servers)\n3)show All tunels \n4)clear a tunel\n5)exit \n: "))
    if menu1 == "1":
        clear()
        status = "iran"
        tunel = ask_tunel(tunels, status)
        set_tunel(tunel, main_interface)
    elif menu1 == "2":
        clear()
        status = "kharej"
        tunel = ask_tunel(tunels, status)
        set_tunel(tunel, main_interface)
    elif menu1 == "3":
        clear()
        tunels_printer(tunels)
        x = input("press enter ...")
    elif menu1 == "4":
        clear()
        clear_tunel(tunels)
        x = input("press enter ...")
    elif menu1 == "5":
        break
    else:
        print("wrong option please enter 1,2,3")
