#!/usr/bin/python 2 3 import lightblue 4 from signal import signal, SIGALRM, alarm 5 import sys 6 7 channel_status = 0 8 got_timeout = False 9 timeout = 2 10 11 12 def sig_alrm_handler(signum, frame): 13 global got_timeout 14 got_timeout = True 15 16 17 signal(SIGALRM, sig_alrm_handler) 18 19 if len(sys.argv) < 2: 20 print "Usage: " + sys.argv[0] + " <addr>" 21 sys.exit(0) 22 23 for channel in range(1, 31): 24 sock = lightblue.socket() 25 got_timeout = False 26 channel_status = 0 27 28 try: 29 alarm(timeout) 30 sock.connect((sys.argv[1], channel)) 31 alarm(0) 32 sock.close() 33 channel_status = 1 34 except IOError: 35 pass 36 37 if got_timeout == True:
142 9 Feeling Bluetooth on the Tooth
38 print "Channel " + str(channel) + " filtered" 39 got_timeout = False 40 elif channel_status == 0: 41 print "Channel " + str(channel) + " closed" 42 elif channel_status == 1: 43 print "Channel " + str(channel) + " open" 