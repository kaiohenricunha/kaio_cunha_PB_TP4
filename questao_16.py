import socket

def udp_client(host='127.0.0.1', port=5000):
    """
    Conecta a um servidor UDP na porta especificada, envia uma mensagem
    e exibe a resposta recebida (esperada "ack").
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Mensagem a ser enviada ao servidor UDP
    message = "Olá, servidor UDP!"
    client_socket.sendto(message.encode('utf-8'), (host, port))
    print(f"Enviada mensagem: {message}")
    
    # Recebe a resposta do servidor (até 1024 bytes)
    ack, server_addr = client_socket.recvfrom(1024)
    print(f"Resposta recebida do servidor {server_addr}: {ack.decode('utf-8')}")
    
    client_socket.close()

if __name__ == "__main__":
    udp_client()
