import os
import time
import pickle



def clear():
    os.system("clear")




tunels=[]


try:
    with open("tunels.txt", "rb") as file:  # "rb" = read binary mode
        tunels = pickle.load(file)
except:
    with open("tunels.txt", "wb") as file:  # "wb" = write binary mode
        pickle.dump(tunels, file)
    with open("tunels.txt", "wb") as file:  # "wb" = write binary mode
        pickle.dump(tunels, file)



def ping_host(host):
    """Ping a host and return True if it's reachable, False otherwise."""
    response = os.system(f"ping -c 3 {host} > /dev/null 2>&1")
    return response == 0


def ask_tunel(tunels,status):
    tunel=[]
    ip_iran=str(input("enter iran ip : "))
    ip_kharej=str(input("enter kharej ip : "))
    subnet=str(input("enter enter tunels subnet (ex : for 192.168.100.1 enter 100) : "))
    tunel.append(status)
    tunel.append(subnet)
    tunel.append(ip_iran)
    tunel.append(ip_kharej)
    tunels.append(tunel)
    with open("tunels.txt", "wb") as file:  # "wb" = write binary mode
        pickle.dump(tunels, file)
    

    return tunel




def set_tunel(tunel):
    subnet=tunel[1]
    if status=="iran":
        tunel_to=tunel[3]
        local_ip="1"
        local_tunel_ip="2"
    elif status== "kharej":
        tunel_to=tunel[2]
        local_ip="2"
        local_tunel_ip="1"

    text=f"""ip link add vxlan{subnet} type vxlan id {subnet} dev ens3 remote {tunel_to} dstport 4789
        ip addr add 192.168.{subnet}.{local_ip}/30 dev vxlan{subnet}
        ip link set vxlan{subnet} up"""
    
    os.system(text)

    while not ping_host(f"192.168.{subnet}.{local_tunel_ip}"):
        print("tunel not set yet waiting for the other server to connect ")
        time.sleep(1)
    print("tunel has been setup successfully ✅")






def clear_tunels(tunels):
    for tunel in tunels:
        text=f"ip link del vxlan{tunel[1]} 2>/dev/null"
        os.system(text)
        print(f"vxlan{tunel[1]} has been deleted")
    tunels.clear()
    with open("tunels.txt", "wb") as file:  # "wb" = write binary mode
        pickle.dump(tunels, file)




clear()
while True:
    menu1 =str(input("welcome to vxlan tunel setup\n\n1)set tunel for iran server\n2)set tunel for kharej server (can add multiple servers)\n3)clear All tunels \n: "))
    if menu1=="1":
        status="iran"
        tunel=ask_tunel(tunels,status)
        set_tunel(tunel)
    elif menu1=="2":
        status="kharej"
        tunel=ask_tunel(tunels,status)
        set_tunel(tunel)
    elif menu1=="3":
        clear_tunels(tunels)
    else:
        print("wrong option please eneter 1,2,3")



