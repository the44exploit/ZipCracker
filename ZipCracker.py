#!/usr/bin/python3

import pyzipper
from tqdm import tqdm
from colorama import Fore,init
import pyfiglet
import argparse

init(autoreset=True)




def banner():
    banner=pyfiglet.figlet_format("ZipCracker")
    print(banner+Fore.GREEN+"The 44 Exploit\n")


def zipcrack():
    try:
        ZipFile=input("ZipFile: ")
    except:
        print("\n:)")
        exit()
    try:
        Wordlist=input("Wordlist: ")
    except:
        print("\nThanks For Using :)")
        exit()
    try:
        check=pyzipper.ZipFile(ZipFile)
    except:
        print(Fore.RED + "ZipFile Not Found")
        exit()
    try:
        words=len(list(open(Wordlist,"rb")))
        print("Total Passwords To Test: ",words)
    except FileNotFoundError:
        print(Fore.RED + "Wordlist Not Found")
        exit()
        
    with pyzipper.AESZipFile(ZipFile) as zipfile:
        with open(Wordlist,"rb") as wordlist:
            for word in tqdm(wordlist, total=words, unit="Words", leave=False):
                try:
                    zipfile.extractall(pwd=word.strip())
                except:
                    continue
                else:
                    print(Fore.GREEN + "Password Found: ",word.decode().strip())
                    exit()
#comming soon...               
def rarcrack():
    print("coming soon")
    exit()
banner()
parser = argparse.ArgumentParser(description="This is Zip Cracker",usage="./%(prog)s zipcrack",epilog="Example: ./%(prog)s -z")
parser.add_argument("-z","--zipcraker",action="store_true",help="Crack ZipFile")
parser.add_argument("-r","--rarcracker",action="store_true",help="Crack RarFile")

args = parser.parse_args()

if args.zipcraker:
    zipcrack()
if args.rarcracker:
    rarcrack()
    
print("Wordlist Finished")
print("Password Not Found, Try Other Wordlist")
