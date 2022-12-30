import argparse
import concurrent.futures
import requests


# Fancy Banner
print("\033[1;36m ██████  █    ██  ▄▄▄▄          ██████ ▄████▄   ▄▄▄      ███▄    █ \033[0;0m")
print("\033[1;36m▒██    ▒  ██  ▓██▒▓█████▄      ▒██    ▒▒██▀ ▀█  ▒████▄    ██ ▀█   █ \033[0;0m")
print("\033[1;36m░ ▓██▄   ▓██  ▒██░▒██▒ ▄██     ░ ▓██▄  ▒▓█    ▄ ▒██  ▀█▄ ▓██  ▀█ ██▒\033[0;0m")
print("\033[1;36m  ▒   ██▒▓▓█  ░██░▒██░█▀         ▒   ██▒▓▓▄ ▄██▒░██▄▄▄▄██▓██▒  ▐▌██▒\033[0;0m")
print("\033[1;36m▒██████▒▒▒▒█████▓ ░▓█  ▀█▓     ▒██████▒▒ ▓███▀ ░ ▓█   ▓██▒██░   ▓██░\033[0;0m")
print("\033[1;36m▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▓███▀▒     ▒ ▒▓▒ ▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒░   ▒ ▒ \033[0;0m")
print("")

# Creating a Parser
parser = argparse.ArgumentParser()

# Adding Arguments
parser.add_argument('-d', '--domain', help='domain', required=True)
parser.add_argument('-w', '--wordlist', help='wordlist', required=True)
parser.add_argument('-t', '--threads', help='Multi-Threading', default=20, type=int)
parser.add_argument('-o', '--output', help='output file', default=None)
parser.add_argument('-m', '--max-subdomains', help='maximum number of subdomains to check in the Wordlist', default=None, type=int)
args = parser.parse_args()

# Defining global variables.
wordlist = args.wordlist
domain = args.domain
threads = args.threads
output_file = args.output
max_subdomains = args.max_subdomains

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def sub_brute(subdomain):
    try:
        url = f'http://{subdomain}'
        response = requests.head(url,headers=headers,allow_redirects = True)
        status = response.status_code
        if status == 200:
            print(f'\033[1;32m [+] >> {subdomain}   status-code:[{status}]\033[00m')
            if output_file:
                with open(output_file, 'a') as f:
                    f.write(f'{subdomain}\n')
        elif status == 301:
            print(f'\033[1;33m [+] >> {subdomain}   status-code:[{status}]\033[00m)')
        elif status == 404:
            print(f'\033[1;31m [+] >> {subdomain} status-code:{status}\033[00m')
    except Exception as e:
        pass

def main():
    with open(wordlist, 'r') as f:
        subdomains = [f'{line.strip()}.{domain}' for line in f]
        if max_subdomains:
            subdomains = subdomains[:max_subdomains]
        with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
            for subdomain in subdomains:
                executor.submit(sub_brute, subdomain)

if __name__ == '__main__':
    main()
