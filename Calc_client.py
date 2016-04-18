import socket
def main():
    host='127.0.0.1'
    port = 5000
    size=1024
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s=socket.socket()
    s.connect((host,port))
    print('connected to server')

    while True:
        f=input('enter file name:')
        #f0 = open(f, 'r')
        f1=open('new.txt', 'w')
        outputstring=''
        with open(f) as f0:
            for line in f0:
                #print (line)
                s.send((line.strip('\n\r')+'\n').encode()) 
                data = s.recv(1024)
                outputstring+=data.decode()
                
                f1.write(outputstring)
                
                f1.write('\n')
                outputstring=''
        f1.close()
                
        print ('open new file to see outputs')

    s.close() 

if __name__ == '__main__':
    main()
