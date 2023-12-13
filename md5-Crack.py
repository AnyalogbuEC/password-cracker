#importing the library for hash
import hashlib
#setting flag to 0
flag = 0
#taking the hash file to compare
pass_hash = input("Enter md5 hash:  ")
#taking the file that contains the password
wordlist = input("Filename:  ")
#trying to open the password file
try:
	pass_file = open(wordlist, "r")
except:
	print("file not found")
	quit()
#creating the hash to compared
for word in pass_file :
	enc_wrd = word.encode('utf-8')
	digest = hashlib.md5(enc_wrd.strip()).hexdigest()
	#prints out password with its hash
	print(word +"==>" + digest)
#comparing the digest with the hash
	if digest == pass_hash :
		#tells that the password has be found
		print("*" * 60)
		print("\t\t password found :-)")
		#print the password
		print("\t\t password is  " + word)
		print("*" * 60)
		#setting the flag to anything not 0
		flag =1
		break
#taking of the case of  password not found
if flag ==0 :
	print("#" * 60)
	print("\n\n password/passphrase not in the list\n\n")
	print("#" * 60)