import pyfiglet
import sys
import socket
from datetime import datetime

# Creating an ASCII banner for the port scanner
ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Defining a target for scanning
if len(sys.argv) == 2:
    # Translating the hostname to IPv4
    target = socket.gethostbyname(sys.argv[1])
else:
    # Display error message if the argument count is incorrect
    print("Invalid amount of Argument")

# Print the scanning target and start time
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:
    # Scanning all ports in the range 1 to 65,535
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # Attempt to connect to the port
        result = s.connect_ex((target, port))
        if result == 0:
            # Print the open port
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    # Handle the Ctrl+C (keyboard interrupt) gracefully
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    # Handle errors in resolving the hostname
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    # Handle errors in socket connection
    print("\ Server not responding !!!!")
    sys.exit()
