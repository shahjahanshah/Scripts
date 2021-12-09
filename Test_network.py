## importing socket module
import socket


ips = ['10.219.214.63', '10.219.214.28']
ports = [22, 22]

for ip, port in zip(ips, ports):
   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   result = sock.connect_ex((ip, port))
   print(" ",result)
   sock.close()
   assert result == 0