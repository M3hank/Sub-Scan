## Sub-Scan

Sub-Scan is A Multi-Threaded Script Written In Python, It Discovers Subdomains From A Site Using A Wordlist That Is Supplied to It.


## Installation
```
git clone https://github.com/M3hank/Sub-Scan.git
```
```
pip3 install -r requirements.txt
```
## Screenshot

![Sub-Scan](https://github.com/M3hank/Sub-Scan/assets/70057473/214593cf-8700-45c5-87ec-e279ef1b703a)

## Requirements

Sub-Scan Requires Following Modules
`argparse`
`requests`
`concurrent.futures`


## Usage

```
python3 Sub-Scan.py -d [domain name] -w [wordlist]  -t [Number of Threads] -o [filename.txt]
```

## Available Arguments

```
Options         descrption

-d               Domain Name 

-w               Wordlist To Use for Enumeration

-t               Multi-Threading

-o               Save Output In A File

-h               Help

```


## Authors

- [@M3hank](https://www.github.com/M3hank)


## Wordlist Credits

- [Seclists](https://www.github.com/danielmiessler/SecLists)

## Contributing

Contributions are always welcome!
