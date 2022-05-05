#Ymani Nesmith M3A
#PEX 2

import hashlib
import re 

print("CyS 431 PEX2 - Hash Collider - by Cadet Ymani Nesmith")
print("\n")        

print("Starting Task 1. . .")
print("\n")        

print("Running hash collision for file: samplefile.txt")

collisions = 0

words = open("words.txt", "r")
wordList = words.readlines()
words.close()

md5_hash = hashlib.md5()
tinyhash = open("samplefile.txt","rb")
content = tinyhash.read()
tinyhash.close()
#
# digest = hashlib.md5(content).hexdigest()
md5_hash.update(content)
digest = md5_hash.hexdigest()

print("Full MD5 digest is: ",digest)
tiny = digest [:5]
print("TinyHash digest is: ",tiny)

index = 0
while collisions < 5:
    
    content = content+ wordList[index % len(wordList)].strip().encode()
    index = index + 1
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
#     digest = hashlib.md5(content).hexdigest()
    if digest [:5] == tiny:
        collisions = collisions + 1
        print("Found TinyHash collision #" + str(collisions) + " after trying " + str(index) + " words. ")
        file = open("collision #" + str(collisions) + ".txt", "wb")
        file.write(content)
        print("Collision saved as file: collision#" + str(collisions) + ".txt")
        file.close()
        
# print("\n")        
# print("Starting Task 2. . . ")
# print("\n")        
# 
# print("Running hash collision for file: contract.txt")
# 
# md5_hash = hashlib.md5()
# contract = open("contract.txt", "rb")
# # reader = open("contract.txt","r")
# inside = contract.read()
# contract.close()
# 
# # print(str(inside))
# 
# md5_hash.update(inside)
# digest = md5_hash.hexdigest()
# print("Full MD5 digest is: ",digest)
# money = digest [:5]
# print("TinyHash digest is: ",money)
# 
# regex = r"\$([0-9,]*)" # Regex pattern to locate dollar amount
# dollar_val = re.search(regex, str(inside)).group(0).replace("$", "")
# # Find and store dollar amount
# # print(dollar_val)
# 
# inside = inside[:len(inside)- len(dollar_val)] # removing original dollar amount
# # print(inside)
# for counter in range(0, int(dollar_val)):
#     
#     new_contract = inside + bytes(str(counter), 'ASCII')
# #     print(new_contract)
#     digest = hashlib.md5(new_contract).hexdigest()
# #     md5_hash.update(new_contract)
# #     digest = md5_hash.hexdigest()
#     if digest [:5] == money :
#         print("Found TinyHash collision using this number: " + str(counter))
#         file = open("newcontract.txt", "wb")
#         file.write(new_contract)
#         print("New contract saved to file: newcontract.txt")
#         file.close()
#         break
# 
# 
#         
