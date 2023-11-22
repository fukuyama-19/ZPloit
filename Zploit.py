from colorama import Fore
import requests
from bs4 import BeautifulSoup
import os
import socket
import urllib

os.system ("cls")

banner = """
                   d8b           d8,        
                   88P          `8P    d8P  
                  d88               d888888P
d88888P ?88,.d88b,888   d8888b   88b  ?88'  
   d8P' `?88'  ?88?88  d8P' ?88  88P  88P   
 d8P'     88b  d8P 88b 88b  d88 d88   88b   
d88888P'  888888P'  88b`?8888P'd88'   `?8b  
          88P'                              
         d88    ZPLOIT - Information Gathering              
         ?8P                                
"""

Text = """
1. Header Response Information
2. Port Scanner
3. Admin Finder
4. Wordpress Plugin Finder
5. Click Jacking Detection
6. Exit
"""

def main ():
    os.system ("cls")
    print (Fore.RED + banner)
    print (Fore.GREEN + Text)
    print (Fore.WHITE + "Create BY Exploit-181 | Facebook Page : @exploit-181")
    print ('\n')
    print (Fore.YELLOW + " ___WindowsApplication")
    print ("|__")
    choosen = input (Fore.WHITE + "   Choose => ")

    if (choosen == "1"):
        url = input("Enter Url Address => ")
        req = requests.get (url).headers
        print(Fore.RED, req)
        os.system ("pause")
        main()
    elif (choosen == "2"):
        ipaddress = input("Enter IP Address => ")
        print (Fore.YELLOW + "[!] Please Wait...")
        for port in range(1, 6500):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            connect = sock.connect_ex((ipaddress, port))
            if (connect == 0):
                print(Fore.GREEN + "[*] Port Open From "+ipaddress+":"+str(port))
            sock.close()
        os.system ('pause')
        main()
    elif (choosen == "3"):
        files = open ("admin_path.txt", "r").readlines()
        val = 0
        url = input ("Enter Url [https://example.com] => ")
        print (Fore.YELLOW + "[!] Please Wait...")
        for i in range(len(files)):
            try:
                req = urllib.request.urlopen(url+"/"+files[i])
                print (Fore.GREEN + "[*] Url Found : "+url+"/"+files[i])
            except:
                pass
        os.system ("pause")
        main ()
    elif (choosen == "4"):
        url = input("Enter Url [https://example.com/login.php] => ")
        lst = open("wp_plugin.txt", "r").readlines()
        try:
            for lstt in range(len(lst)):
                urllib.request.urlopen(url+lst[lstt])
                print (Fore.GREEN + "[*] Plugin Found => " + url + lst[lstt])
        except:
            for lstt in range(len(lst)):
                print (Fore.RED + "[*] Trying To Get The File")
        os.system ('pause')
        main()
    elif (choosen == "5"):
        path = "X-Frame-Options"
        url = input ("Enter Url [https://www.example.com] => ")
        req = requests.get (url).headers
        if (path in req.keys()):
            print (Fore.RED + "[+] Not Found Clickjacking Vulnerability "+ Fore.WHITE+" => "+url+path)
        else:
            print (Fore.GREEN + "[*] Missing Clickjacking => "+url+" => "+path)
        os.system ("pause")
        main()
    elif (choosen == "6"):
        pass
        

main()