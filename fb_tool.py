#!/usr/bin/env python3
import os
import time
import random

print("2:20 PM | 12.5KB/s >...")
print("\nAuthor : Shridhar G")
print("Mobile : 9506176464")
print("GitHub : https://github.com/shrikld")
print("\n=================================")

while True:
    print("[1] Facebook Poll voting")
    print("[2] Posts videos stories like voting")
    print("[3] Facebook reels like voting") 
    print("[4] Comment like voting")
    print("[5] Facebook ids, pages follow")
    print("[6] Comment voting")
    print("[7] Comment rc speed voting")
    print("[8] Groups join")
    print("[9] Create pages")
    print("[10] Auto activate pages")
    print("\nSelect: ", end="")
    
    choice = input()
    if choice in ['q', 'exit']:
        break
        
    print("\n🔐 Login Required")
    email = input("Facebook Email: ")
    pwd = input("Facebook Password: ")
    
    if email and pwd:
        print("✅ Login Successful! Processing...")
        time.sleep(2)
    else:
    
    input("\nPress Enter to continue...")
    os.system('clear')
