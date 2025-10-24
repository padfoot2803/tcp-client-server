from socket import *
import sys
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) 
serverAddress = (serverName, serverPort)
if len(sys.argv) != 2:
    print("Usage: python UDP_Reliable_Client.py <input_file>")
    exit()

filename = sys.argv[1]
try:
    file = open(filename, 'r')
    for line in file:
        currentProblem = line.strip()
        clientSocket.sendto(currentProblem.encode(), serverAddress)

        data, serverAddress = clientSocket.recvfrom(2048)
        response = data.decode()
        statusCode, result = response.split()

        print(currentProblem)
        if statusCode == "200":
            print(f"The result is: {result}")
        elif statusCode == "620":
            print(f"Error {statusCode}: Invalid OC")
        else:
            print(f"Error {statusCode}: Invalid Operands")
    file.close()

    clientSocket.close()        
except Exception as e:
        print(f"An error occurred:{e}")

