import socket
import threading

def calculator(name,sock):
    while True:
        outputstring=''
        
        while True:
            
            data=sock.recv(1)
            if ((data)== b'\n'):
                break
            outputstring+=data.decode()
         
        try:
            
                    
            a=str(eval(outputstring))
            print(a)
        except Exception as e:
           
            print( 'exception', str(e))
            a=str(e)
           
        if data:
            
            sock.send(str(a).encode())
    
#sock.close()

def main():
    host='127.0.0.1'
    port=5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s=socket.socket()
    s.bind((host,port))
    s.listen(5) 
    
    print ("server started")
    while True:
        c,addr=s.accept()
        print('client connected to ip:<' + str(addr)+'>')
        t=threading.Thread(target=calculator,args=('retrThread',c))
        t.start()
    s.close()

if __name__ == '__main__' :
    main()

    
            
   
