import argparse
import concurrent.futures
import os
import requests
from urllib.parse import urlsplit


# Fancy Banner
print("""\033[1;36m ██████  █    ██  ▄▄▄▄          ██████ ▄████▄   ▄▄▄      ███▄    █
▒██    ▒  ██  ▓██▒▓█████▄      ▒██    ▒▒██▀ ▀█  ▒████▄    ██ ▀█   █
░ ▓██▄   ▓██  ▒██░▒██▒ ▄██     ░ ▓██▄  ▒▓█    ▄ ▒██  ▀█▄ ▓██  ▀█ ██▒
  ▒   ██▒▓▓█  ░██░▒██░█▀         ▒   ██▒▓▓▄ ▄██▒░██▄▄▄▄██▓██▒  ▐▌██▒
▒██████▒▒▒▒█████▓ ░▓█  ▀█▓     ▒██████▒▒ ▓███▀ ░ ▓█   ▓██▒██░   ▓██░
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▓███▀▒     ▒ ▒▓▒ ▒ ░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒░   ▒ ▒ \033[0;0m""")
print("")




# Creating a Parser
parser = argparse.ArgumentParser()

# Adding Arguments
parser.add_argument('-d', '--domain', help='domain', required=True)
parser.add_argument('-w', '--wordlist', help='wordlist', required=True)
parser.add_argument('-t', '--threads', help='Multi-Threading', default=20, type=int)
parser.add_argument('-o', '--output', help='output file', default=None)
args = parser.parse_args()

# Defining global variables.
wordlist = args.wordlist
domain = args.domain
threads = args.threads
output_file = args.output

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

printed_subdomains = set()

def sub_brute(url, Session, printed_subdomains):
    try:
        response = Session.get(url, headers=headers, allow_redirects=True)
        final = response.url
        netloc = urlsplit(final).netloc
        status = response.status_code
        if netloc not in printed_subdomains and domain in netloc:
            printed_subdomains.add(netloc)
            if status == 200:
                print(f'\033[1;32m[+] >> {netloc}   status-code:[{status}]')
            else:
                print(f'\033[1;31m[-] {netloc} {status}')
            if output_file:
                with open(output_file, 'a') as f_out:
                    f_out.write(f'{netloc}\n')
    except:
        pass

def main():
    if not os.path.isfile(wordlist):
        print(f"Unable to read {wordlist}, Please provide a valid wordlist.")
        return
    Session = requests.Session()
    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        with open(wordlist, 'r') as f:
            for line in f:
                subdomain = f'{line.strip()}.{domain}'
                url = f'https://{subdomain}'
                future = executor.submit(sub_brute, url, Session, printed_subdomains)

if __name__ == '__main__':
    main()
