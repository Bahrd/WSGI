# https://www.geeksforgeeks.org/socket-programming-python/
# https://stackoverflow.com/questions/2719017/how-to-set-timeout-on-pythons-socket-recv-method
from socket	import *
from sys import stdin

# Create a socket object 
with socket() as s:
    s.settimeout(1.0)
    try:
        # Reserving a port
        port = 12345			

        # Connecting to the server
        s.connect(('127.0.0.1', port))
        expr = stdin.read().strip().encode() # Cf. down under...
        s.send(expr)
        
        # Receiving data from the server
        # and decoding to get the string.
        result = s.recv(0x100).decode()
        print(f'{result}')
        
        # close the connection (once and for all)
        s.close()
    except:
        print('Connection problem!')
# echo '1 * 2 - 3 + 4 / 5' | & pyth_path client.py
