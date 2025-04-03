import socket

def udp_server(host='127.0.0.1', port=5000):
    """
    Cria um servidor UDP que escuta em uma porta específica.
    Quando recebe um datagrama, exibe a mensagem e responde com um "ack".
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"Servidor UDP escutando em {host}:{port}")
    
    while True:
        # Recebe datagrama (máximo 1024 bytes) e o endereço do remetente
        data, addr = server_socket.recvfrom(1024)
        print(f"Recebido datagrama de {addr}: {data.decode('utf-8')}")
        
        # Responde com "ack" para o remetente
        ack = "ack"
        server_socket.sendto(ack.encode('utf-8'), addr)
        print(f"Enviado 'ack' para {addr}")

if __name__ == "__main__":
    udp_server()
