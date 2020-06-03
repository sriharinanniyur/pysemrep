# ner.py - NER functionality.

import socket

METAMAP_PORT = 12345
GNORMPLUS_PORT = 12347

# fetch_aws_ner_data() - accepts a string of bytes and a port as argument, and returns NER data from the AWS server.
def fetch_aws_ner_data(data, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("ec2-18-218-203-118.us-east-2.compute.amazonaws.com", port))
    s.sendall(data)
    server_data = s.recv(4096)
    s.close()
    return str(server_data)

print(fetch_aws_ner_data(open("test.plain", "rb").read(), METAMAP_PORT))
print("")
print(fetch_aws_ner_data(open("test.plain", "rb").read(), GNORMPLUS_PORT))
