import socket

def tcp_server(host='127.0.0.1', port=5000):
    """
    Cria um servidor TCP que escuta em uma porta específica.
    Ao aceitar uma conexão, o servidor envia uma mensagem de boas-vindas.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Servidor TCP escutando em {host}:{port}")
    
    while True:
        conn, addr = server_socket.accept()
        print("Conexão estabelecida com:", addr)
        data = conn.recv(1024)
        print("Mensagem recebida do cliente:", data.decode('utf-8'))
        welcome_message = "Bem-vindo ao servidor TCP!"
        conn.send(welcome_message.encode('utf-8'))
        conn.close()

if __name__ == "__main__":
    tcp_server()
