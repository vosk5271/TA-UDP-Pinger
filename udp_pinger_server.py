import random
from socket import socket, AF_INET, SOCK_DGRAM

# Create a UDP socket
server_socket = socket(AF_INET, SOCK_DGRAM)

# Bind to IP address and port
server_socket.bind(('10.0.0.2', 12000))

print("UDP Ping Server is ready to receive pings...")

def main():
    ping_count = 0  # Initialize ping count
    
    while True:
        ping_count += 1

        # Generate a random number between 1 and 10 for packet loss simulation
        rand_num = random.randint(1, 10)
        
        # Receive the client packet along with the address
        message, client_address = server_socket.recvfrom(1024)
        message = message.decode()

        # Simulate a 40% packet loss rate
        if rand_num <= 4:
            # Simulate packet loss (do not respond)
            print(f"Packet {ping_count} lost.")
            continue
    
        # Send the received message back to the client
        server_socket.sendto(message.encode(), client_address)
        print(f"Ping {ping_count} responded to {client_address}")

if __name__ == "__main__":
    main()