from socket import *
import sys

serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName, serverPort))
if len(sys.argv) != 2:
    print("Usage: python3 TCP_Client.py <input_file>")
    exit()
filename = sys.argv[1]

try:
    file = open(filename, 'r')
    for line in file:
        currentProblem = line.strip()
        clientSocket.send(currentProblem.encode())
        print(f"Input request: {currentProblem}")
        response = clientSocket.recv(1024).decode()
        statusCode, result = response.split()

        if statusCode == "200":
            print(f"The result is: {result}")
        elif statusCode == "620":
            print(f"Error {statusCode}: Invalid OC")
        else:
            print(f"Error {statusCode}: Invalid Operands")
        print('\n')    
                   
    file.close() 
    clientSocket.close()    
except Exception as e:
    print(f"An error occurred: {e}")
