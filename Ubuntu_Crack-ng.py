import os
print ("Ubuntu_Crack-ng---- by grimreaper567123")
print(".")
print("aircrack-ng automatic toolkit for ubuntu")
print(".")
print(".")
print(".")
print(".")
print ("run as sudo")
print(".")
print(".")
print("restart to access other commands")
print(".")
print("ctrl + c to exit")
print(".")
print ("set card to monitor (1)")
print ("stop monitoring mode (2)")
print ("scan wifi (run by itself) (3)")

choice = input()
if choice == "1":
	os.system("sudo airmon-ng start wlp3s0")
elif choice == "2":
	os.system("sudo airmon-ng stop wlp3s0mon")
elif choice == "3":
	os.system("sudo airmon-ng start wlp3s0")
	os.system("sudo airodump-ng wlp3s0mon")
