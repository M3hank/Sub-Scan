## Sub-Scan

Sub-Scan is A Multi-Threaded Script Written In Python, It Discovers Subdomains From A Site Using A Wordlist That Is Supplied to It.


## Installation

```
git clone https://github.com/M3hank/Sub-Scan.git
```
```
sudo pip install -r requirements.txt
```
## Requirements

Sub-Scan Requires Following Modules
`argparse`
`threading`
`requests`
`queue`


## Usage

```
python3 Sub-Scan.py -d [domain name] -w [wordlist]  -t [Number of Threads]
```

## Available Arguments

```
Options         descrption

-d               Domain Name 

-w               Wordlist To Use for Enumeration

-t               Multi-Threading

-h               Help
```


## Authors

- [@M3hank](https://www.github.com/M3hank)


## Wordlist Credits

- [Seclists](https://www.github.com/danielmiessler/SecLists)

## Contributing

Contributions are always welcome!
