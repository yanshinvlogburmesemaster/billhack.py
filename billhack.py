import requests 
 import pyfiglet 
 import time 
 import os 
 import random 
 import sys 
  
  
 os.system("clear") 
  
 def mengetik(s): 
     for c in s + '\n': 
         sys.stdout.write(c) 
         sys.stdout.flush() 
         time.sleep(random.random() * 0.2) 
  
  
  
  
  
 mengetik('  11111111111     1111111111    111     111') 
 mengetik('         1111        111        111     111') 
 mengetik('     1111            111        11111111111') 
 mengetik('  1111               111        111     111') 
 mengetik('  11111111111 111    111  111   111     111') 
  
 mengetik('') 
  
 mengetik('Author Page : Zero To Hero Online Class') 
 mengetik('Page cb     : http://m.me/zero.to.hero.238/') 
 mengetik('Telegram Gp : https://t.me/termuxtool0033') 
 mengetik('Telegram GP : https://t.me/+xTO6F0qZs3c1N2Nl') 
  
 mengetik('') 
  
 mengetik('🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊🍊') 
 mengetik('') 
  
 n = int(input("Enter amount for each operator: ")) 
 def bill(x, r1, r2): 
   print("\n"+x+" --> "+"*123*"+str(random.randrange(r1, r2))+"#") 
 [bill("TELENOR or MPT", int("1" * 18), int("9" * 18)) for _ in range(n)] 
 [bill("OOREDOO", int("1" * 16), int("9" * 16)) for _ in range(n)] 
 [bill("MYTEL", int("1" * 13), int("9" * 13)) for _ in range(n)]
