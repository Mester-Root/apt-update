import os,sys,time
try:
    os.system("clear")
except:
    pass
time.sleep(1)
print ("\n\033[36m[*]\033[35m START UPDATE \033[31m[ubuntu]  ...\n")
time.sleep(1)
n = 'deb http://a.docker-registry.ir/ubuntu/ xenial main restricted universe multiverse'
n1 = 'deb-src http://a.docker-registry.ir/ubuntu/ xenial main restricted universe multiverse'
n2 = 'deb http://a.docker-registry.ir/ubuntu/ xenial-updates main restricted universe multiverse'
n3 = 'deb-src http://a.docker-registry.ir/ubuntu/ xenial-updates main restricted universe multiverse'
n4 = 'deb http://a.docker-registry.ir/ubuntu/ xenial-backports main restricted universe multiverse'
n5 = 'deb-src http://a.docker-registry.ir/ubuntu/ xenial-backports main restricted universe multiverse'
n6 = 'deb http://a.docker-registry.ir/ubuntu/ xenial-security main restricted universe multiverse'
n7 = 'deb-src http://a.docker-registry.ir/ubuntu/ xenial-security main restricted universe multiverse'
system = os.system("whoami")
if "u0" in system:
    def ok():
        os.system(f"echo {n} > /etc/apt/sources.list")
        os.system(f"echo {n1} > /etc/apt/sources.list")
        os.system(f"echo {n2} > /etc/apt/sources.list")
        os.system(f"echo {n3} > /etc/apt/sources.list")
        os.system(f"echo {n4} > /etc/apt/sources.list")
        os.system(f"echo {n5} > /etc/apt/sources.list")
        os.system(f"echo {n6} > /etc/apt/sources.list")
        os.system(f"echo {n7} > /etc/apt/sources.list")
    try:
        ok()
    except:
        time.sleep(1)
        print ("\n\033[31m[!] sorry my friend system not shell\n")
        time.sleep(1)
        sys.exit()
if system == "root":
    def yes():
        os.system(f"sudo echo {n} > /etc/apt/sources.list")
        os.system(f"sudo echo {n1} > /etc/apt/sources.list")
        os.system(f"sudo echo {n2} > /etc/apt/sources.list")
        os.system(f"sudo echo {n3} > /etc/apt/sources.list")
        os.system(f"sudo echo {n4} > /etc/apt/sources.list")
        os.system(f"sudo echo {n5} > /etc/apt/sources.list")
        os.system(f"sudo echo {n6} > /etc/apt/sources.list")
        os.system(f"sudo echo {n7} > /etc/apt/sources.list")
    try:
        yes()
    except:
        time.sleep(1)
        print ("\n\033[31m[!] sorry my friend system not shell\n")
        time.sleep(1)
        sys.exit()
#------
os.system("chmod 777 *")
os.system("apt update")
time.sleep(1)
print ("\n\033[36m[*] \033[35mapt updated")
