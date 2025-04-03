import socket

def tcp_client(host='127.0.0.1', port=12345):
    """
    Conecta a um servidor TCP na porta especificada, envia uma mensagem
    e exibe a resposta recebida do servidor.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    # Mensagem que será enviada ao servidor
    message = "Olá, servidor! Aqui é o cliente."
    client_socket.send(message.encode('utf-8'))
    
    # Recebe a resposta do servidor
    response = client_socket.recv(1024)
    print("Resposta do servidor:", response.decode('utf-8'))
    
    client_socket.close()

if __name__ == "__main__":
    tcp_client()
