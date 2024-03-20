# https://www.geeksforgeeks.org/socket-programming-python/
# https://stackoverflow.com/questions/2719017/how-to-set-timeout-on-pythons-socket-recv-method
from socket import *
import threading

## A 'real' server should handle multiple clients' requests
#  using coroutines (unlike this demo):
#  https://realpython.com/intro-to-python-threading/

def handle_like_pro(c, addr):
    # Receiving data from the client
    expr = c.recv(0x100).decode()
    print('Expression to evaluate:', expr)
    # Sending an ACK message to the client
    c.send(f'{addr}: {expr} = {eval(expr)}'.encode()) 

    # Closing the connection with the client..
    c.close()

# Creating a server socket
with socket() as s:
    s.settimeout(10.0)
    print('TCP Socket created')
    # Reserving a port
    port = 12345			

    # Binding to the port
    s.bind(('', port))		 
    print(f'... bound to {port}') 

    # Turning the socket into listening mode 
    s.listen(1)	 
    print('and listening...')		 

    # A (tentatively) forever loop
    try:
        while True:
            # Establishing connection with client. 
            print('Waiting...')
            c, addr = s.accept()	 
            # Horses for courses... 
            print(f'Handling a request from: {addr} in a thread')            
            threading.Thread(target = handle_like_pro, 
                             args = (c, addr), 
                             daemon = True).start()
            
    except IOError:
        print('OIOI error!')
    except KeyboardInterrupt:
        print('♪♫Sounds like a wrong key!♫♪')