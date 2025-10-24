# tcp-client-server
Simple TCP client-server system that utilizes the Python socket library in which the server acts as a (simple) calculator to act on two numbers sent to it by the client.

The server performs the Operation Code (OC) requested on the two integer numbers it receives from the sender and returns the result. The format of the returned result is “status-code numeric-result”. 

OC can be one of +,-,*, and /, both numbers should be integer numbers. If the request is valid, the operation is performed and a status code of 200 and the result are returned. If the request is not valid, the following error status codes with a result of -1 are sent:
• Invalid OC (i.e., not +, -, *, or /) with an error status code of 620.
• Invalid operands with an error status code of 630 (Operands not integer numbers or attempted division by zero.)

The server responds to CTRL+C to stop.

## To run:

1. Clone the repo: git clone 
  
2. Start the server:
   
```bash
python3 TCP_Server.py
```
You should get the following message: 

> The server is ready to receive

2. Start the client:

```bash
python3 TCP_Client.py testFile.txt
```
The test file should contain 7 lines of operations in the following format: OC num1 num2. There is a test file in the repo that you can use and/or edit.

Eg:

```
+ 2 10
- 100 20
* 25 -3
% 200 3
- 2.5 15
/ 65 4
+ 0 12
```
3. Output:

```
Input request: + 2 10
The result is: 12


Input request: - 100 20
The result is: 80


Input request: * 25 -3
The result is: -75


Input request: % 200 3
Error 620: Invalid OC


Input request: - 2.5 15
Error 630: Invalid Operands


Input request: / 65 4
The result is: 16.25


Input request: + 0 12
The result is: 12

```
