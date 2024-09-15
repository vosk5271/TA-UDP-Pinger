How to Run the Scripts
    Run the Servers: First, you need to run both the udp_pinger_server.py and udp_hb_server.py on separate terminals or machines.
    Run the Clients: Then, run the udp_pinger_client.py and udp_hb_client.py on different terminals.
The Pinger client will send 10 pings to the server and print the round-trip time (RTT) for each ping. The Heartbeat client will send 10 heartbeat messages to the server every 3 seconds, with a 30% chance of skipping some heartbeats (to simulate packet loss).
