from socket import *
def operate(oc, num1, num2):
    if oc == '+':
        return num1 + num2
    elif oc == '-':
        return num1 - num2
    elif oc == '*':
        return num1 * num2
    elif oc == '/':
        if num2 == 0:
            return -1 
        return num1 / num2
    else:
        return -1
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
print("The server is ready to receive requests")

try:
    while True:
        connectionSocket, addr = serverSocket.accept()
        print(f"Accepted connection from client {addr[0]}:{addr[1]}")
        while True: 
            statusCode = 0
            data = connectionSocket.recv(1024).decode()
            if len(data) == 0:
                break
            try:
                oc, num1, num2 = data.split()
                oc = oc.strip()
                num1 = int(num1)
                num2 = int(num2)
                result = operate(oc, num1, num2)
                
                if result == -1:
                    response = "620 -1"
                    statusCode = "620" 
                else:
                    response = f"200 {result}"
                    statusCode = "200"
            except (ValueError, ZeroDivisionError):
                response = "630 -1"
                statusCode = "630"
            finally:
                connectionSocket.send(response.encode())
                print(f"{data} -> {statusCode} {result}")
        connectionSocket.close()        
except KeyboardInterrupt:
    print("Server stopped.")
    serverSocket.close()
