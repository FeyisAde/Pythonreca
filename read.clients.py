client_file = open("clients.txt", 'r')

clientNo = 1

for client in client_file:
    client = client.rstrip('\n')
    print(f"{clientNo}.{client}")
    clientNo += 1

