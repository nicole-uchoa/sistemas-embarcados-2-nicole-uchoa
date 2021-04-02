import socket
import sys

HOST = sys.argv[1] # IP a ser passado por argumento 
PORT = int(sys.argv[2]) # Porta a ser passada por argumento

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
    s.connect((HOST, PORT)) 
    file = open(sys.argv[3], "wb") # Abre o arquivo para escrita e recebe o nome do arquivo por argumento 
    data = s.recv(1024) 
    while data: # Recebe o arquivo em pacotes de tamanho 1024 até ser entregue por completo
        file.write(data) 
        data = s.recv(1024) 

    file.close()
    s.close()
