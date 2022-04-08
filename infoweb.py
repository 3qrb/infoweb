import requests,socket,json
G , R = "\033[1;32m" , "\033[1;31m"
print(R+"""
           
  ██▓ ███▄    █  ▒ ████▒ ▒█████       █     █░ ▓█████ ▄▄▄▄   
▒▓██▒ ██ ▀█   █ ▒▓██    ▒██▒  ██▒    ▓█░ █ ░█░ ▓█   ▀▓█████▄      
▒▒██▒▓██  ▀█ ██▒░▒████  ▒██░  ██▒    ▒█░ █ ░█  ▒███  ▒██▒ ▄██
░░██░▓██▒  ▐▌██▒░░▓█▒   ▒██   ██░    ░█░ █ ░█  ▒▓█  ▄▒██░█▀     >>code by ahmed<<
░░██░▒██░   ▓██░ ░▒█░   ░ ████▓▒░    ░░██▒██▓ ▒░▒████░▓█  ▀█▓
 ░▓  ░ ▒░   ▒ ▒   ▒ ░   ░ ▒░▒░▒░     ░ ▓░▒ ▒  ░░░ ▒░ ░▒▓███▀▒
░ ▒ ░░ ░░   ░ ▒░  ░       ░ ▒ ▒░       ▒ ░ ░  ░ ░ ░  ▒░▒   ░ 
░ ▒ ░   ░   ░ ░   ░ ░   ░ ░ ░ ▒        ░   ░      ░   ░    ░ 
  ░           ░             ░ ░          ░    ░   ░   ░      

""")
web = input("Website : ");print('')
print("="*40+"|")
print("")
def wepsite():
    ip = socket.gethostbyname(web)
    url_info_ip = f"http://ipwhois.app/json/{ip}"
    response = requests.get(url_info_ip).json()
    print(G+"Website ip information :");print("")
    print(json.dumps(response,indent=4))
    print("")
    print("-"*40);print("")
    print("HTTP headers :");print("")
    url_head = f"https://api.hackertarget.com/httpheaders/?q={web}"
    print(requests.get(url_head).text)
    print('')
    print("-"*40);print("")
    print("Page Links : ");print("")
    url_page = f"https://api.hackertarget.com/pagelinks/?q={web}"
    print(requests.get(url_page).text)
    print('')
    print("-"*40);print("")
    print("Find shared DNS :");print("")
    url_find = f"https://api.hackertarget.com/findshareddns/?q={web}"
    print(requests.get(url_find).text)
    print('')
    print("-"*40);print("")
wepsite()