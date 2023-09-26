#!/usr/bin/python3
import requests
import sys
from colorama import Fore
import time

# Função para exibir o banner
def exibir_banner():
    return (Fore.YELLOW + '''

|  \/  |  / \  |  _ \|  ___|_ _| \ | |  _ \| ____|  _ \ 
| |\/| | / _ \ | |_) | |_   | ||  \| | | | |  _| | |_) |
| |  | |/ ___ \|  __/|  _|  | || |\  | |_| | |___|  _ < 
|_|  |_/_/   \_\_|   |_|   |___|_| \_|____/|_____|_| \_\
                                                        


                Bug Bounty

''')

def main():
    print(exibir_banner())

    if len(sys.argv) < 2:
        print('Modo de uso: python3 fuzz_deep.py https://exemplo.com')
        sys.exit(1)

    url = sys.argv[1]
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(Fore.GREEN+"")
            print(f"200:~/fuzzdeep$ {url}")
        else:
            print(Fore.RED+"")
            print(f"{response.status_code}:~/fuzzdeep$ {url}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer solicitação HTTP: {e}")
        sys.exit(1)

    # Abrir e processar o arquivo 'wordlists.txt'
    with open('wordlists.txt', 'r') as file:
        for line in file:
            line = line.strip('\n')
            fullurl = f"{url}{line}"
            try:
                response = requests.get(fullurl)
                if response.status_code == 200:
                    print(f"200:~/fuzzdeep$ {fullurl}")
                else:
                    print(f"{response.status_code}:~/fuzzdeep$ {fullurl}")
            except requests.exceptions.RequestException as e:
                print(f"Erro ao fazer solicitação HTTP: {e}")

if __name__ == "__main__":
    main()
