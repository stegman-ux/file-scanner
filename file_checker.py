import os
import colorama
from colorama import Fore
import fade
os.system('pip install colorama')
os.system('pip install fade')
os.system('cls')
welcom ='''
               _                          
 __      _____| | ___ ___  _ __ ___   ___ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \         [*]créator : intrable
  \ V  V /  __/ | (_| (_) | | | | | |  __/         [*]Version : 1.0
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|         
[!]Welcome brother
[!]this tool juste verify keyword , like "webhook" in open source files
'''
welcom = fade.greenblue(welcom)
print(welcom)
print(Fore.CYAN+"Press enter for acces...")
input()
os.system('cls')

ascii_art = '''
   __ _ _             _               _             
  / _(_) | ___    ___| |__   ___  ___| | _____ _ __ 
 | |_| | |/ _ \  / __| '_ \ / _ \/ __| |/ / _ \ '__|
 |  _| | |  __/ | (__| | | |  __/ (__|   <  __/ |   
 |_| |_|_|\___|  \___|_| |_|\___|\___|_|\_\___|_|   
                                                    
 [!]The file must to be in the folder of this tool.
 [!]This tool just checks in open source files
'''
ascii_art = fade.greenblue(ascii_art)
print(ascii_art)
wbho = input(Fore.CYAN+"Enter the name of the file to check  : ")
os.system(f'findstr webhook ./{wbho}')
os.system(f'findstr w3bhook ./{wbho}')
os.system(f'findstr https://canary.discord.com/api/webhooks ./{wbho}')
os.system(f'findstr https://discord.com/api/webhooks ./{wbho}')
os.system(f'findstr https://ptb.discord.com/api/webhooks ./{wbho}')
os.system(f'findstr hook ./{wbho}')
os.system(f'findstr h00k ./{wbho}')
os.system(f'findstr w4bh00k ./{wbho}')
os.system(f'findstr w2bhook ./{wbho}')
os.system(f'findstr h00k ./{wbho}')
os.system(f'findstr cstealer ./{wbho}')
print()
print()
print()
print(Fore.RED+"if you dont view result , its because the file do u want to scan is not a grabber")
input(Fore.RED+"Scan Finish !...")

# simple py script
# coded by intrable
# (im debutant)