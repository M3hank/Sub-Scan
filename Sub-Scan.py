import requests #Module to Request Website
import argparse #Module to Parse Arguments
import threading #Module for multi-threading


#Creating a Parser
parser = argparse.ArgumentParser()


#Adding Arguments
parser.add_argument('-d','--domain',help='domain',required=True)
parser.add_argument('-w','--wordlist',help='wordlist',required=True)
parser.add_argument('-t','--threads',help='Multi-Threading',default = 10)
args = parser.parse_args()

#Fancy Banner Font Name:- Bloody
print("\033[1;36m ██████  █    ██  ▄▄▄▄          ██████ ▄████▄   ▄▄▄      ███▄    █ \033[0;0m")
print("\033[1;36m▒██    ▒  ██  ▓██▒▓█████▄      ▒██    ▒▒██▀ ▀█  ▒████▄    ██ ▀█   █ \033[0;0m")
print("\033[1;36m░ ▓██▄   ▓██  ▒██░▒██▒ ▄██     ░ ▓██▄  ▒▓█    ▄ ▒██  ▀█▄ ▓██  ▀█ ██▒\033[0;0m")
print("\033[1;36m  ▒   ██▒▓▓█  ░██░▒██░█▀         ▒   ██▒▓▓▄ ▄██▒░██▄▄▄▄██▓██▒  ▐▌██▒\033[0;0m")
print("\033[1;36m▒██████▒▒▒▒█████▓ ░▓█  ▀█▓     ▒██████▒▒ ▓███▀ ░ ▓█   ▓██▒██░   ▓██░\033[0;0m")
print("\033[1;36m▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▓███▀▒     ▒ ▒▓▒ ▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒░   ▒ ▒ \033[0;0m")
print("\033[1;36m░ ░▒  ░ ░░░▒░ ░ ░ ▒░▒   ░      ░ ░▒  ░ ░ ░  ▒     ▒   ▒▒ ░ ░░   ░ ▒░\033[0;0m")
print("\033[1;36m ░  ░  ░   ░░░ ░ ░  ░    ░      ░  ░  ░ ░          ░   ▒     ░   ░ ░ \033[0;0m")
print("\033[1;36m      ░     ░      ░                 ░ ░ ░            ░  ░        ░ \033[0;0m")
print("\033[1;36m                                                                       Github:- m3hank         \033[0;0m")


#defining global variables.
wordlist = args.wordlist
domain = args.domain
threads = args.threads


# Check If The Domain is Available.
def subdomain(subdomain):
    try:
        url = f"http://{subdomain}.{domain}"
        r = requests.head(url)
        if r.status_code == 200 or 301:
            print(f"\033[0;32m Subdomain Found --> {subdomain}.{domain} {r.status_code}")
            with open("output.txt", "a") as f:
                f.write(f"{subdomain}.{domain} \n")
        else: 
         print(f"\033[0;31m Subdomain Found --> {subdomain}.{domain} {r.status_code}")
    except:
        print(f"\033[0;31m {subdomain}.{domain} ")


# Function to Use Thread.
def threader():
    while True:
        worker = q.get()
        subdomain(worker)
        q.task_done()


# Function to Use multiple threads.
def main():
    q = queue.Queue()
    for x in range(int(threads)):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()
    with open(wordlist, "r") as f:
        for line in f:
            q.put(line.strip())
    q.join()


#Function to use default threads.
def default_threads():
    with open(wordlist, "r") as f:
        for line in f:
            subdomain(line.strip())


#Main function.
if __name__ == "__main__":
    default_threads()
