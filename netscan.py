import os
print ("Nikto scan is automatically running on port 80")
ip = raw_input("Enter Target IP: ")
boxname = raw_input("Enter Box Name: ")
os.system("mkdir ~/Documents/%s" % boxname)
os.system("/opt/masscan/bin/./masscan -p0-65535 %s -n -e tun0 --rate 10000 -oL masscan" % ip) # -e tun0 for all boxes through vpn
os.system("mv masscan ~/Documents/%s/masscan" % boxname)
os.system("nmap -sC -sV %s -oN nmap" % ip )
os.system("mv nmap ~/Documents/%s/nmap" % boxname)
os.system("nikto -h %s --output nikto.txt" % ip)
os.system("mv nikto.txt ~/Documents/%s/nikto.txt" % boxname) 
print ("                        ")
print ("                             ")
print ("                              ")
print ("                             ")
print ("                              ")

print ("-----Scan Completed-----")
print ("                             ")
print ("                              ")
print ("                              ")

