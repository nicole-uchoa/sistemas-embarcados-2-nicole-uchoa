import sys
import socketserver

FILE = sys.argv[2] # Arquivo para enviar

file = open(FILE, "rb") # Abre o arquivo para leitura de bytes
bFile = file.read() # Le o arquivo para variavel em memoria
file.close()


class Handler(socketserver.BaseRequestHandler): # Classe para tratar as requisições
    def handle(self):
        self.request.sendall(bFile) # Envia o arquivo para o cliente


HOST = "0.0.0.0" # Host para aceitar requisições de qualquer IP
PORT = int(sys.argv[1]) # Porta passada por argumento
with socketserver.TCPServer((HOST, PORT), Handler) as server: # Inicia o servidor
    server.serve_forever()
