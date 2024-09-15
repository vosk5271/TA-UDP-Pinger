from socket import socket, AF_INET, SOCK_DGRAM, timeout
import time

# Create a UDP socket
client_socket = socket(AF_INET, SOCK_DGRAM)

# Set a timeout of 1 second for the socket
client_socket.settimeout(1)

# Server's IP address and port
server_address = ('10.0.0.2', 12000)

# Variables to store RTT statistics
min_rtt = float('inf')
max_rtt = float('-inf')
total_rtt = 0
packet_loss_count = 0

for i in range(1, 11):
    start_time = time.time()
    message = f"Ping {i}"

    try:
        # Send the ping message to the server
        client_socket.sendto(message.encode(), server_address)

        # Receive the server's response
        response, _ = client_socket.recvfrom(1024)

        # Calculate round-trip time (RTT)
        rtt = (time.time() - start_time) * 1000  # Convert to milliseconds
        total_rtt += rtt

        # Track min, max RTT
        min_rtt = min(min_rtt, rtt)
        max_rtt = max(max_rtt, rtt)

        print(f"Ping {i}: rtt = {round(rtt, 3)} ms")

    except timeout:
        print(f"Ping {i}: Request timed out")
        packet_loss_count += 1

# Print summary of RTT and packet loss
if 10 - packet_loss_count > 0:
    avg_rtt = total_rtt / (10 - packet_loss_count)
else:
    avg_rtt = 0

print("\nSummary values:")
print(f"min_rtt = {round(min_rtt, 3)} ms")
print(f"max_rtt = {round(max_rtt, 3)} ms")
print(f"avg_rtt = {round(avg_rtt, 3)} ms")
print(f"Packet loss: {packet_loss_count / 10 * 100}%")
