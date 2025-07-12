import pickle
import os
import time



def ping_host(host):
    """Ping a host and return True if it's reachable, False otherwise."""
    response = os.system(f"ping -c 3 {host} > /dev/null 2>&1")
    return response == 0

def set_tunel(tunel):
    with open("vxlan_tunel_files.txt", "rb") as file:  # "rb" = read binary mode
        main_interface = pickle.load(file)
    subnet=tunel[1]
    if status=="iran":
        tunel_to=tunel[3]
        local_ip="1"
        local_tunel_ip="2"
    elif status== "kharej":
        tunel_to=tunel[2]
        local_ip="2"
        local_tunel_ip="1"

    text=f"""ip link add vxlan{subnet} type vxlan id {subnet} dev {main_interface} remote {tunel_to} dstport 4789
        ip addr add 192.168.{subnet}.{local_ip}/30 dev vxlan{subnet}
        ip link set vxlan{subnet} up"""
    
    os.system(text)

    


while True :
        with open("tunels.txt", "rb") as file:  # "rb" = read binary mode
            tunels = pickle.load(file)

        for tunel in tunels:
                status=tunel[0]
                subnet=tunel[1]
                if status=="iran":
                    local_tunel_ip=f"192.168.{subnet}.2"
                elif status=="kharej":
                    local_tunel_ip=f"192.168.{subnet}.1"                
              
                if not ping_host(local_tunel_ip):
                      print("ping failed , setting tunel now")
                      set_tunel(tunel)
                else:
                     print(f"ping successfully reached to {local_tunel_ip}  ✅")

        time.sleep(10)
        





