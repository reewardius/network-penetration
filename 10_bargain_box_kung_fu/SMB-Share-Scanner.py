 #!/usr/bin/python 2 3 import sys 4 import os 5 from random import randint 6 7 8 def get_ips(start_ip, stop_ip): 9 ips = [] 10 tmp = [] 11 12 for i in start_ip.split(’.’): 13 tmp.append("%02X" % long(i)) 14 15 start_dec = long(’’.join(tmp), 16) 16 tmp = [] 17 18 for i in stop_ip.split(’.’): 19 tmp.append("%02X" % long(i)) 20 21 stop_dec = long(’’.join(tmp), 16) 22
10.7 Login Watcher 157
23 while(start_dec < stop_dec + 1): 24 bytes = [] 25 bytes.append(str(int(start_dec / 16777216))) 26 rem = start_dec % 16777216 27 bytes.append(str(int(rem / 65536))) 28 rem = rem % 65536 29 bytes.append(str(int(rem / 256))) 30 rem = rem % 256 31 bytes.append(str(rem)) 32 ips.append(".".join(bytes)) 33 start_dec += 1 34 35 return ips 36 37 38 def smb_share_scan(ip): 39 os.system("smbclient -q -N -L " + ip) 40 41 if len(sys.argv) < 2: 42 print sys.argv[0] + ": <start_ip-stop_ip>" 43 sys.exit(1) 44 else: 45 if sys.argv[1].find(’-’) > 0: 46 start_ip, stop_ip = sys.argv[1].split("-") 47 ips = get_ips(start_ip, stop_ip) 48 49 while len(ips) > 0: 50 i = randint(0, len(ips) - 1) 51 lookup_ip = str(ips[i]) 52 del ips[i] 53 smb_share_scan(lookup_ip) 54 else: 55 smb_share_scan(sys.argv[1])