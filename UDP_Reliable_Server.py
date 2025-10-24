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
    
serverName = '127.0.0.1'
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind((serverName, serverPort))
print("The server is ready to receive")

try:
    while True:
        message, clientAddress = serverSocket.recvfrom(2048) 
        data = message.decode()
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
            serverSocket.sendto(response.encode(), clientAddress)
            print(f"{data} -> {statusCode} {result}")
except KeyboardInterrupt:
    print("Server stopped.")
    serverSocket.close()



