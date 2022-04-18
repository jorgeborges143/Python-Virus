# WARNING!
DO NOT EXECUTE THIS SCRIPT ON YOUR OR ANYBODY ELSE COMPUTER.
I am not responsible for any actions performed by you or anybody while using this script. 
I can only control what I do and I can't control what everybody else does.
This script is fully built in python and tested in virtual environments [win10|win11].

# What is a ransomware?
Ransomware, is a word that derives from joining the words "Ransom"+"Malware".
This kind of virus restricts access to any infected system, normally, the ransomware encrypts all the user's data and sometimes even applications, normally followed by a ransom in cryptocurrencies, claiming this is the only way to restore the information. 
This kind of payments, can make it really hard for authorities to find the author of the crime. 
Since normally payments are made in cryptocurrencies like BTC, LTC, or ETH, the authorities and entities responsible for finding cybercriminals can use the blockchain to follow and trace the stolen cryptocurrencies.
In the case of ransoms in Monero (XMR) the history may become a little bit different. Since monero uses 2 Private Keys instead of 1, it not only gives double privacy to the attacker but also turns it really hard not to say almost impossible to find/trace the stolen cryptocurrencies.
Normally, cryptocurrencies have a private key, this private key is known as your "secret spend key" which all cryptocurrency address has and it is the only way you have to spend the funds of the respective address.
But Monero doesn't stop there, Monero has the "secret spend key" like all other cryptocurrencies, but in order to see your balance or transactions, it will request you for another private key, the "secret view key", this key is the only way you have to access the transactions made from address X to address Y. 
In the Monero blockchain, the sender and receiver information is "hidden", in this case, only the "public view key", this means you can only see the transaction value and transactions sent by the address if you have the "private view key", even so, you can't see who sent the XMR to your wallet address. This is the reason why Monero is considered the cryptocurrency offering more privacy and anonymity to its users.
e.g:
https://localmonero.co/blocks/tx/0ed322657624584a28a2a814208a4a8a7337adf0360861b9460a1aeea4081d8b
https://blockchair.com/en/monero/transaction/0ed322657624584a28a2a814208a4a8a7337adf0360861b9460a1aeea4081d8b

# Friendly Reminder
NEVER pay for a ransomware ransom, remember, sending money to a criminal for him committing his crime is almost like telling him to continue!
Even if your information was really important, always try to reach the authorities and explain your situation, try to remember everything you've done, how have you been contacted or where have you downloaded the file, every step is important in order to understand and mitigate how the virus is spreading across machines or being shared on the internet.
Another reason not to pay a ransom from ransomware is not being sure that after paying for it, the files will be recovered and the criminal will not request more money.

# How does it work?
The script calls read_directory(directory_chosen_by_user) and tries to get the admin rights allowed by the user, while the user doesn't give admin rights, the script keeps asking for them. Once the admin rights were given, the script will search for all files, directories, and subdirectories in the given path and starts doing its job.
The script verifies for each file if its content is a Fernet token or not by executing a urlsafe_b64decode to the file content decoded in "latin-1".
If the content is a Fernet token, the script will proceed and verify is the given decryption key matches with the self.privKey (the private key defined before executing the script compiled or not), if it matches, then it will decrypt the file. 
If the content is not a Fernet token, the script will proceed and encrypt the files using the self.privKey (the private key defined before executing the script compiled or not).

# I'VE EXECUTED ON MY PC
As you have or should have read above, I advise everyone not to do that, even so, I'll not leave a man behind!
DO NOT SEND CRYPTO TO THE ADDRESS REQUESTING FOR 0.001 BTC (It is a random address that is not mine and I'll not request your money in order to solve the situation).
Please send me an e-mail with the subject "URGENT MY PC IS INFECTED!", so it catches my attention.
Please try to remember your private key (if changed on code before execution), and PLEASE DO NOT CHANGE ANY CODE (if it still exists on the pc and hasn't got encrypted too).
