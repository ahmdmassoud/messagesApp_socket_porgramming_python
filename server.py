import socket
from threading import Thread
def incoming_connections():
    while True:
      client, client_address = server.accept()
      print("%s:%s has connected." % client_address)
      client.send(bytes("Please write your name to start using the app", "utf8"))
      clients_list.append(client)
      Thread(target=handel_client_inputs, args=(clients_list,client,)).start()



def handel_client_inputs(clients_list,client):  
    name = client.recv(1024).decode("utf8")
    client.send(bytes('Welcome ','utf8')+bytes(name,'utf8')) 

    active_users[name] = client
    while True:
        msg = client.recv(1024).decode("utf8")
        to , message  = msg.split(',')
        if to == "*":
            broadcast(name,message,client)
        else:    
            active_users[to].send(bytes(name,'utf8')+bytes(':',"utf8")+bytes(message, "utf8"))
            client.send(bytes('Me:','utf8')+bytes(message,'utf8')) 


def broadcast(name, msg,client):  
    for cl in clients_list:
        if cl == client:
           client.send(bytes('Me:','utf8')+bytes(msg,'utf8')) 
        else:    
            cl.send(bytes(name,'utf8')+bytes(':',"utf8")+bytes(msg, "utf8"))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 1233
server.bind((host,port))
server.listen(5)
print("the server is listening on port {} and waiting for connections".format(port))
clients_list = []
active_users={}

ACCEPT_THREAD = Thread(target=incoming_connections)
ACCEPT_THREAD.start()
ACCEPT_THREAD.join()
SERVER.close()
